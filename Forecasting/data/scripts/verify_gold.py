#!/usr/bin/env python3
"""Gold invariant checks for the synthetic forecasting panel."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generated"

REGIMES = [
    "smooth_seasonal",
    "mean_step",
    "promo_driven",
    "intermittent",
    "cold_start",
]

# Tunable gates — fail loud if DGP drift breaks interview demos
THRESHOLDS = {
    "min_series_per_regime": 8,
    "smooth_acf7_min": 0.35,
    "smooth_zero_rate_max": 0.05,
    "mean_step_min_delta": 25.0,
    "promo_lift_min": 1.4,
    "promo_rate_min": 0.05,
    "promo_rate_max": 0.35,
    "intermittent_zero_min": 0.55,
    "intermittent_zero_max": 0.90,
    "intermittent_max_y": 40,
    "cold_train_min": 30,
    "cold_train_max": 60,
    "horizon": 28,
}


def lag_acf(y: np.ndarray, lag: int) -> float:
    y = np.asarray(y, dtype=float)
    if len(y) <= lag + 2:
        return float("nan")
    y0 = y[:-lag]
    y1 = y[lag:]
    if np.std(y0) < 1e-8 or np.std(y1) < 1e-8:
        return 0.0
    return float(np.corrcoef(y0, y1)[0, 1])


def check(name: str, ok: bool, detail: str, rows: list[dict]) -> None:
    rows.append({"check": name, "pass": bool(ok), "detail": detail})
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}: {detail}")


def verify() -> int:
    panel_path = GEN / "panel.parquet"
    meta_path = GEN / "series_meta.csv"
    cutoff_path = GEN / "cutoff.json"
    if not panel_path.exists() or not meta_path.exists() or not cutoff_path.exists():
        print("Missing generated artifacts. Run generate_panel.py first.", file=sys.stderr)
        return 1

    panel = pd.read_parquet(panel_path)
    meta = pd.read_csv(meta_path)
    cutoff_info = json.loads(cutoff_path.read_text())
    cutoff = pd.Timestamp(cutoff_info["cutoff"])
    horizon = int(cutoff_info["horizon"])
    rows: list[dict] = []

    # --- integrity ---
    check(
        "unique_series_ds",
        not panel.duplicated(["series_id", "ds"]).any(),
        f"dupes={int(panel.duplicated(['series_id', 'ds']).sum())}",
        rows,
    )
    check(
        "cutoff_json_matches_column",
        (panel["in_train"] == (pd.to_datetime(panel["ds"]) <= cutoff)).all(),
        f"cutoff={cutoff.date()}",
        rows,
    )
    check(
        "horizon_matches_config",
        horizon == THRESHOLDS["horizon"] and cutoff_info.get("horizon") == horizon,
        f"horizon={horizon}",
        rows,
    )

    for regime in REGIMES:
        n_series = meta.loc[meta["regime"] == regime, "series_id"].nunique()
        check(
            f"regime_count::{regime}",
            n_series >= THRESHOLDS["min_series_per_regime"],
            f"n_series={n_series}",
            rows,
        )

    # no calendar gaps
    gap_fails = []
    for sid, g in panel.groupby("series_id"):
        ds = pd.to_datetime(g["ds"]).sort_values().reset_index(drop=True)
        expected = pd.Series(pd.date_range(ds.iloc[0], ds.iloc[-1], freq="D"))
        if len(ds) != len(expected) or not np.array_equal(ds.to_numpy(), expected.to_numpy()):
            gap_fails.append(sid)
    check("no_daily_gaps", len(gap_fails) == 0, f"gap_series={gap_fails[:5]}", rows)

    # post-cutoff rows exist
    post = panel.loc[~panel["in_train"]].groupby("series_id").size()
    check(
        "post_cutoff_horizon_rows",
        (post == horizon).all() and len(post) == meta["series_id"].nunique(),
        f"min={int(post.min()) if len(post) else -1} max={int(post.max()) if len(post) else -1}",
        rows,
    )

    # leakage: non-promo regimes have promo==0 (cold_start may have promo if parent=promo)
    non_promo_regimes = ["smooth_seasonal", "mean_step", "intermittent"]
    for regime in non_promo_regimes:
        sub = panel.loc[panel["regime"] == regime]
        check(
            f"promo_zero::{regime}",
            (sub["promo"] == 0).all(),
            f"promo_sum={int(sub['promo'].sum())}",
            rows,
        )

    # --- per-regime ---
    # smooth
    smooth_ids = meta.loc[meta["regime"] == "smooth_seasonal", "series_id"]
    acfs = []
    zero_rates = []
    for sid in smooth_ids:
        y = panel.loc[(panel["series_id"] == sid) & panel["in_train"], "y"].to_numpy()
        acfs.append(lag_acf(y, 7))
        zero_rates.append(float(np.mean(y == 0)))
    check(
        "smooth_seasonal::acf7",
        float(np.nanmean(acfs)) >= THRESHOLDS["smooth_acf7_min"],
        f"mean_acf7={float(np.nanmean(acfs)):.3f}",
        rows,
    )
    check(
        "smooth_seasonal::zero_rate",
        float(np.max(zero_rates)) <= THRESHOLDS["smooth_zero_rate_max"],
        f"max_zero_rate={float(np.max(zero_rates)):.3f}",
        rows,
    )

    # mean_step
    step_ok = True
    step_details = []
    for _, m in meta.loc[meta["regime"] == "mean_step"].iterrows():
        if not m["shift_date"] or pd.isna(m["shift_date"]):
            step_ok = False
            step_details.append(f"{m['series_id']}:missing_shift_date")
            continue
        shift = pd.Timestamp(m["shift_date"])
        g = panel.loc[panel["series_id"] == m["series_id"]].copy()
        g["ds"] = pd.to_datetime(g["ds"])
        before = g.loc[g["ds"] < shift, "y"].mean()
        after = g.loc[(g["ds"] >= shift) & g["in_train"], "y"].mean()
        delta = float(after - before)
        if delta < THRESHOLDS["mean_step_min_delta"]:
            step_ok = False
            step_details.append(f"{m['series_id']}:delta={delta:.1f}")
        if not (g["ds"].min() < shift < cutoff):
            step_ok = False
            step_details.append(f"{m['series_id']}:shift_out_of_range")
    check(
        "mean_step::mean_jump",
        step_ok,
        "all_ok" if step_ok else "; ".join(step_details[:5]),
        rows,
    )

    # promo
    promo_ok = True
    promo_details = []
    for sid in meta.loc[meta["regime"] == "promo_driven", "series_id"]:
        g = panel.loc[panel["series_id"] == sid]
        rate = float(g["promo"].mean())
        if not (THRESHOLDS["promo_rate_min"] <= rate <= THRESHOLDS["promo_rate_max"]):
            promo_ok = False
            promo_details.append(f"{sid}:rate={rate:.3f}")
        y1 = g.loc[g["promo"] == 1, "y"].mean()
        y0 = g.loc[g["promo"] == 0, "y"].mean()
        lift = float(y1 / y0) if y0 > 0 else 0.0
        if lift < THRESHOLDS["promo_lift_min"]:
            promo_ok = False
            promo_details.append(f"{sid}:lift={lift:.2f}")
        # known-future promo in horizon
        if g.loc[~g["in_train"], "promo"].sum() == 0:
            promo_ok = False
            promo_details.append(f"{sid}:no_horizon_promo")
    check(
        "promo_driven::lift_and_rate",
        promo_ok,
        "all_ok" if promo_ok else "; ".join(promo_details[:5]),
        rows,
    )

    # intermittent
    int_ok = True
    int_details = []
    for sid in meta.loc[meta["regime"] == "intermittent", "series_id"]:
        y = panel.loc[panel["series_id"] == sid, "y"].to_numpy()
        if not np.allclose(y, np.round(y)):
            int_ok = False
            int_details.append(f"{sid}:non_integer")
        zr = float(np.mean(y == 0))
        if not (THRESHOLDS["intermittent_zero_min"] <= zr <= THRESHOLDS["intermittent_zero_max"]):
            int_ok = False
            int_details.append(f"{sid}:zero_rate={zr:.3f}")
        if float(np.max(y)) > THRESHOLDS["intermittent_max_y"]:
            int_ok = False
            int_details.append(f"{sid}:max_y={float(np.max(y)):.0f}")
    check(
        "intermittent::discrete_sparse",
        int_ok,
        "all_ok" if int_ok else "; ".join(int_details[:5]),
        rows,
    )

    # cold_start
    cold_ok = True
    cold_details = []
    for _, m in meta.loc[meta["regime"] == "cold_start"].iterrows():
        ntr = int(m["n_train_days"])
        if not (THRESHOLDS["cold_train_min"] <= ntr <= THRESHOLDS["cold_train_max"]):
            cold_ok = False
            cold_details.append(f"{m['series_id']}:n_train={ntr}")
        n_post = int((~panel.loc[panel["series_id"] == m["series_id"], "in_train"]).sum())
        if n_post != horizon:
            cold_ok = False
            cold_details.append(f"{m['series_id']}:post={n_post}")
    check(
        "cold_start::train_length",
        cold_ok,
        "all_ok" if cold_ok else "; ".join(cold_details[:5]),
        rows,
    )

    summary = pd.DataFrame(rows)
    n_fail = int((~summary["pass"]).sum())
    print(f"\n{len(summary) - n_fail}/{len(summary)} checks passed; {n_fail} failed")
    summary.to_csv(GEN / "gold_checks.csv", index=False)
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(verify())
