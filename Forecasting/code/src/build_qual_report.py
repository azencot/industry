"""Qualitative bakeoff review: overlays, horizon profiles, ranks, intermittent cards."""

from __future__ import annotations

import base64
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .evaluate import seasonal_naive_scale
from .load_panel import CODE_ROOT, load_cutoff, load_meta, load_panel

REPORTS = CODE_ROOT / "reports"
QUAL = REPORTS / "qual"
FIGS = QUAL / "figures"

FORECAST_FILES = {
    "seasonal_naive": "forecasts_seasonal_naive.csv",
    "ets": "forecasts_ets.csv",
    "lightgbm": "forecasts_lightgbm.csv",
    "chronos_bolt_small": "forecasts_chronos_bolt_small.csv",
}

COLORS = {
    "seasonal_naive": "#7f7f7f",
    "ets": "#1f77b4",
    "lightgbm": "#2ca02c",
    "chronos_bolt_small": "#d62728",
    "actual": "#111111",
}

EXPECTED = {
    "smooth_seasonal": "SN ≈ ETS",
    "mean_step": "ETS / LightGBM",
    "promo_driven": "LightGBM",
    "intermittent": "messy; Chronos competitive",
    "cold_start": "Chronos relative (LGBM may win if promo-parent)",
}

REGIME_CHAMPION = {
    "smooth_seasonal": "seasonal_naive",
    "mean_step": "ets",
    "promo_driven": "lightgbm",
    "intermittent": "chronos_bolt_small",
    "cold_start": "chronos_bolt_small",
}


def load_all_forecasts() -> pd.DataFrame:
    parts = []
    for model, fname in FORECAST_FILES.items():
        path = REPORTS / fname
        if not path.exists():
            raise FileNotFoundError(f"Missing {path}; run `python -m src.run_compare` first")
        df = pd.read_csv(path)
        df["ds"] = pd.to_datetime(df["ds"]).dt.normalize()
        df["model"] = model
        parts.append(df)
    return pd.concat(parts, ignore_index=True)


def per_series_mase(panel: pd.DataFrame, forecasts: pd.DataFrame) -> pd.DataFrame:
    test = panel.loc[~panel["in_train"], ["series_id", "ds", "y", "regime"]]
    train = panel.loc[panel["in_train"], ["series_id", "y"]]
    merged = test.merge(forecasts, on=["series_id", "ds"], how="inner")
    rows = []
    for (sid, model), g in merged.groupby(["series_id", "model"]):
        ty = train.loc[train["series_id"] == sid, "y"].to_numpy()
        scale = seasonal_naive_scale(ty)
        mae = float(np.mean(np.abs(g["y"].to_numpy() - g["yhat"].to_numpy())))
        rows.append(
            {
                "series_id": sid,
                "model": model,
                "regime": g["regime"].iloc[0],
                "mase": mae / scale,
                "mae": mae,
            }
        )
    return pd.DataFrame(rows)


def select_series(series_mase: pd.DataFrame, meta: pd.DataFrame) -> list[dict]:
    """Per regime: first id, best/worst under expected champion, plus extras."""
    picks: list[dict] = []
    seen: set[tuple[str, str]] = set()

    def add(regime: str, sid: str, reason: str) -> None:
        key = (regime, sid)
        if key in seen:
            return
        seen.add(key)
        picks.append({"regime": regime, "series_id": sid, "reason": reason})

    for regime in EXPECTED:
        sub = series_mase.loc[series_mase["regime"] == regime]
        ids = sorted(sub["series_id"].unique())
        if not ids:
            continue
        add(regime, ids[0], "first_id")
        champ = REGIME_CHAMPION[regime]
        c = sub.loc[sub["model"] == champ]
        if not c.empty:
            best = c.loc[c["mase"].idxmin()]
            worst = c.loc[c["mase"].idxmax()]
            add(regime, str(best["series_id"]), f"best_mase_under_{champ}")
            add(regime, str(worst["series_id"]), f"worst_mase_under_{champ}")

    # Prefer a mean_step with known shift and a promo with horizon promos
    for _, m in meta.loc[meta["regime"] == "mean_step"].iterrows():
        if m.get("shift_date") and str(m["shift_date"]) not in ("", "nan"):
            add("mean_step", str(m["series_id"]), "has_shift_date")
            break
    return picks


def plot_overlay(
    panel: pd.DataFrame,
    forecasts: pd.DataFrame,
    meta_row: pd.Series,
    sid: str,
    cutoff: pd.Timestamp,
    out_path: Path,
    history_days: int = 90,
) -> None:
    g = panel.loc[panel["series_id"] == sid].sort_values("ds")
    train = g.loc[g["in_train"]]
    test = g.loc[~g["in_train"]]
    # show last history_days of train for long series
    if len(train) > history_days:
        train_plot = train.iloc[-history_days:]
    else:
        train_plot = train

    fig, axes = plt.subplots(2, 1, figsize=(11, 5.5), sharex=False, gridspec_kw={"height_ratios": [3, 1.2]})
    ax, axr = axes

    ax.plot(train_plot["ds"], train_plot["y"], color=COLORS["actual"], lw=1.2, label="actual (train)")
    ax.plot(test["ds"], test["y"], color=COLORS["actual"], lw=1.6, label="actual (test)")
    ax.axvline(cutoff, color="#666", ls="--", lw=1, label="cutoff")

    if meta_row.get("regime") == "mean_step" and meta_row.get("shift_date") and str(meta_row["shift_date"]) not in ("", "nan"):
        ax.axvline(pd.Timestamp(meta_row["shift_date"]), color="#548235", ls=":", lw=1.4, label="shift_date")

    if g["promo"].sum() > 0:
        promo = g.loc[g["promo"] == 1]
        ax.scatter(promo["ds"], promo["y"], s=22, c="#e2a03f", zorder=4, label="promo=1")

    for model in FORECAST_FILES:
        fc = forecasts.loc[(forecasts["series_id"] == sid) & (forecasts["model"] == model)]
        ax.plot(fc["ds"], fc["yhat"], lw=1.3, color=COLORS[model], label=model)

    ax.set_title(f"{sid}  ·  {meta_row.get('regime', '')}")
    ax.set_ylabel("y")
    ax.legend(loc="upper left", fontsize=7, ncol=3)

    # residual on test vs lightgbm and seasonal_naive for readability
    for model in ("seasonal_naive", "lightgbm", "chronos_bolt_small"):
        fc = forecasts.loc[(forecasts["series_id"] == sid) & (forecasts["model"] == model)]
        mrg = test[["ds", "y"]].merge(fc[["ds", "yhat"]], on="ds")
        axr.plot(mrg["ds"], mrg["y"] - mrg["yhat"], color=COLORS[model], lw=1.0, label=model)
    axr.axhline(0, color="#999", lw=0.8)
    axr.set_ylabel("residual")
    axr.legend(loc="upper left", fontsize=7, ncol=3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


def horizon_mae(panel: pd.DataFrame, forecasts: pd.DataFrame) -> pd.DataFrame:
    test = panel.loc[~panel["in_train"], ["series_id", "ds", "y"]].copy()
    # horizon index within each series
    test["h"] = test.groupby("series_id").cumcount() + 1
    merged = test.merge(forecasts, on=["series_id", "ds"])
    merged["ae"] = (merged["y"] - merged["yhat"]).abs()
    return merged.groupby(["model", "h"], as_index=False)["ae"].mean().rename(columns={"ae": "mae"})


def plot_horizon(hprof: pd.DataFrame, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(9, 3.5))
    for model, g in hprof.groupby("model"):
        ax.plot(g["h"], g["mae"], marker="o", ms=3, color=COLORS[model], label=model)
    ax.set_xlabel("horizon step h")
    ax.set_ylabel("MAE (pooled)")
    ax.set_title("Error by forecast horizon")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


def intermittent_table(panel: pd.DataFrame, forecasts: pd.DataFrame) -> pd.DataFrame:
    test = panel.loc[(~panel["in_train"]) & (panel["regime"] == "intermittent")]
    rows = []
    for model in FORECAST_FILES:
        fc = forecasts.loc[forecasts["model"] == model]
        m = test.merge(fc, on=["series_id", "ds"])
        y = m["y"].to_numpy()
        yhat = m["yhat"].to_numpy()
        zero_y = y == 0
        spike = y > 0
        pred_zero = yhat < 0.5
        rows.append(
            {
                "model": model,
                "both_zero_rate": float(np.mean(pred_zero & zero_y)),
                "missed_spike_rate": float(np.mean(pred_zero[spike])) if spike.any() else float("nan"),
                "mean_pred_on_zero": float(np.mean(yhat[zero_y])) if zero_y.any() else float("nan"),
                "mae": float(np.mean(np.abs(y - yhat))),
            }
        )
    return pd.DataFrame(rows)


def rank_table(metrics_csv: Path) -> pd.DataFrame:
    m = pd.read_csv(metrics_csv)
    reg = m.loc[m["scope"] == "regime"].copy()
    reg["rank"] = reg.groupby("regime")["mase"].rank(method="min")
    return reg.pivot(index="regime", columns="model", values="rank")


def img_b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def build() -> None:
    QUAL.mkdir(parents=True, exist_ok=True)
    FIGS.mkdir(parents=True, exist_ok=True)

    panel = load_panel()
    meta = load_meta().set_index("series_id")
    cutoff_info = load_cutoff()
    cutoff = pd.Timestamp(cutoff_info["cutoff"])
    forecasts = load_all_forecasts()
    series_mase = per_series_mase(panel, forecasts)
    series_mase.to_csv(QUAL / "series_mase.csv", index=False)

    picks = select_series(series_mase, meta.reset_index())
    pd.DataFrame(picks).to_csv(QUAL / "selected_series.csv", index=False)

    fig_recs = []
    for p in picks:
        sid = p["series_id"]
        mrow = meta.loc[sid] if sid in meta.index else pd.Series({"regime": p["regime"]})
        fname = f"{p['regime']}__{sid}.png"
        out = FIGS / fname
        plot_overlay(panel, forecasts, mrow, sid, cutoff, out)
        # mase by model for caption
        sm = series_mase.loc[series_mase["series_id"] == sid].set_index("model")["mase"].to_dict()
        fig_recs.append({**p, "path": out, "rel": f"figures/{fname}", "mase_by_model": sm})

    hprof = horizon_mae(panel, forecasts)
    hprof.to_csv(QUAL / "horizon_mae.csv", index=False)
    plot_horizon(hprof, FIGS / "horizon_mae.png")

    inter = intermittent_table(panel, forecasts)
    inter.to_csv(QUAL / "intermittent_hit_miss.csv", index=False)

    ranks = rank_table(REPORTS / "metrics.csv")
    ranks.to_csv(QUAL / "rank_by_regime.csv")

    # --- HTML ---
    rank_html = ranks.round(0).astype("Int64").to_html()
    inter_html = inter.round(3).to_html(index=False)
    sections = []
    for rec in fig_recs:
        mase_str = ", ".join(f"{k}={v:.2f}" for k, v in sorted(rec["mase_by_model"].items()))
        sections.append(
            f"""
<section>
  <h3>{rec['regime']} — <code>{rec['series_id']}</code></h3>
  <p><strong>Why selected:</strong> {rec['reason']} · expected: {EXPECTED.get(rec['regime'], '?')}<br>
  <strong>Series MASE:</strong> {mase_str}</p>
  <img alt="{rec['series_id']}" src="data:image/png;base64,{img_b64(rec['path'])}"/>
</section>
"""
        )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Bakeoff qualitative review</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
         max-width: 1000px; margin: 2rem auto; padding: 0 1rem; color: #1a1a1a; line-height: 1.45; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 0.9rem; margin: 1rem 0; }}
  th, td {{ border: 1px solid #ccc; padding: 0.35rem 0.5rem; text-align: left; }}
  img {{ max-width: 100%; height: auto; border: 1px solid #ddd; }}
  code {{ background: #f4f4f4; padding: 0.1rem 0.3rem; }}
  ul.checklist {{ list-style: none; padding-left: 0; }}
  .meta {{ color: #444; }}
</style>
</head>
<body>
<h1>Bakeoff qualitative review</h1>
<p class="meta">Cutoff <code>{cutoff_info['cutoff']}</code> · H={cutoff_info['horizon']} ·
reuses <code>reports/forecasts_*.csv</code> (no retrain).</p>

<h2>Manual checklist</h2>
<ul class="checklist">
  <li>☐ Promo spikes: LightGBM tracks; univariate miss or smear</li>
  <li>☐ Mean step: SN stays wrong after break; ETS/LGBM adapt better</li>
  <li>☐ Intermittent: Chronos vs SN on zeros/spikes (see table)</li>
  <li>☐ Cold start: short history visible; who over/under-reacts</li>
  <li>☐ Horizon: who degrades after h≈14</li>
</ul>

<h2>Regime × model MASE rank (1 = best)</h2>
{rank_html}
<p class="meta">From <code>metrics.csv</code> regime scope.</p>

<h2>Error by horizon</h2>
<img alt="horizon mae" src="data:image/png;base64,{img_b64(FIGS / 'horizon_mae.png')}"/>

<h2>Intermittent hit / miss</h2>
<p><code>both_zero_rate</code>: share of days with y=0 and yhat&lt;0.5 ·
<code>missed_spike_rate</code>: among y&gt;0, share with yhat&lt;0.5 ·
<code>mean_pred_on_zero</code>: average prediction on true zeros.</p>
{inter_html}

<h2>Case overlays</h2>
{''.join(sections)}

<p class="meta">Regenerate: <code>python -m src.build_qual_report</code></p>
</body>
</html>
"""
    (QUAL / "QUAL.html").write_text(html)

    # brief markdown index
    md = [
        "# Qualitative bakeoff review",
        "",
        "Open [`QUAL.html`](QUAL.html) in a browser (primary).",
        "",
        f"- Selected series: `{len(picks)}`",
        "- Artifacts: `series_mase.csv`, `horizon_mae.csv`, `intermittent_hit_miss.csv`, `rank_by_regime.csv`, `figures/`",
        "",
    ]
    (QUAL / "QUAL.md").write_text("\n".join(md) + "\n")
    print(f"Wrote {QUAL / 'QUAL.html'} ({len(fig_recs)} overlays)")


if __name__ == "__main__":
    build()
