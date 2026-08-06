"""Run SN / ETS / LightGBM / Chronos-Bolt bakeoff on signed-off panel."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Callable

import pandas as pd

from .evaluate import score_forecasts
from .load_panel import CODE_ROOT, load_cutoff, load_panel

REPORTS = CODE_ROOT / "reports"
CHRONOS_MODEL_ID = "amazon/chronos-bolt-small"

EXPECTED = {
    "smooth_seasonal": "SN ≈ ETS",
    "mean_step": "ETS / LightGBM",
    "promo_driven": "LightGBM",
    "intermittent": "messy (use WAPE/MASE)",
    "cold_start": "Chronos-Bolt relative",
}


def _get_runner(key: str) -> tuple[str, Callable]:
    if key == "sn":
        from .models.seasonal_naive import forecast_seasonal_naive

        return "seasonal_naive", forecast_seasonal_naive
    if key == "ets":
        from .models.ets import forecast_ets

        return "ets", forecast_ets
    if key == "lgbm":
        from .models.lightgbm_model import forecast_lightgbm

        return "lightgbm", forecast_lightgbm
    if key == "chronos":
        from .models.chronos_bolt import forecast_chronos_bolt

        return "chronos_bolt_small", forecast_chronos_bolt
    raise SystemExit(f"Unknown model {key}; choose sn,ets,lgbm,chronos")


def parse_models(spec: str) -> list[str]:
    allowed = {"sn", "ets", "lgbm", "chronos"}
    keys = [k.strip().lower() for k in spec.split(",") if k.strip()]
    bad = [k for k in keys if k not in allowed]
    if bad:
        raise SystemExit(f"Unknown models {bad}; choose from {sorted(allowed)}")
    return keys


def write_regime_report(metrics: pd.DataFrame, timings: dict[str, float], path: Path) -> None:
    lines = [
        "# Bakeoff metrics by regime",
        "",
        f"Chronos checkpoint: `{CHRONOS_MODEL_ID}` (zero-shot).",
        "",
        "## Timings (seconds)",
        "",
        "| Model | Wall time |",
        "|-------|-----------|",
    ]
    for name, sec in timings.items():
        lines.append(f"| `{name}` | {sec:.2f} |")
    lines += ["", "## Overall", ""]
    overall = metrics.loc[metrics["scope"] == "overall"].sort_values("mase")
    lines += [
        "| Model | MAE | RMSE | WAPE | MASE | n |",
        "|-------|-----|------|------|------|---|",
    ]
    for _, r in overall.iterrows():
        lines.append(
            f"| `{r['model']}` | {r['mae']:.3f} | {r['rmse']:.3f} | {r['wape']:.3f} | {r['mase']:.3f} | {int(r['n'])} |"
        )

    lines += ["", "## By regime", ""]
    for regime in sorted(metrics.loc[metrics["scope"] == "regime", "regime"].unique()):
        sub = metrics.loc[(metrics["scope"] == "regime") & (metrics["regime"] == regime)].sort_values(
            "mase"
        )
        lines += [
            f"### `{regime}` — expected: {EXPECTED.get(regime, '?')}",
            "",
            "| Model | MAE | RMSE | WAPE | MASE |",
            "|-------|-----|------|------|------|",
        ]
        for _, r in sub.iterrows():
            lines.append(
                f"| `{r['model']}` | {r['mae']:.3f} | {r['rmse']:.3f} | {r['wape']:.3f} | {r['mase']:.3f} |"
            )
        winner = sub.iloc[0]["model"] if len(sub) else "?"
        lines += ["", f"Lowest MASE: **`{winner}`**", ""]

    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Forecasting method bakeoff")
    parser.add_argument(
        "--models",
        default="sn,ets,lgbm,chronos",
        help="Comma list: sn,ets,lgbm,chronos",
    )
    args = parser.parse_args()
    keys = parse_models(args.models)

    cutoff = load_cutoff()
    horizon = int(cutoff["horizon"])
    panel = load_panel()
    print(f"Loaded panel {panel.shape[0]} rows; cutoff={cutoff['cutoff']} H={horizon}")

    REPORTS.mkdir(parents=True, exist_ok=True)
    metric_parts: list[pd.DataFrame] = []
    timings: dict[str, float] = {}

    for key in keys:
        name, fn = _get_runner(key)
        print(f"Running {name}...")
        fcst, elapsed = fn(panel, horizon)
        timings[name] = elapsed
        print(f"  done in {elapsed:.2f}s; {len(fcst)} forecast rows")
        metric_parts.append(score_forecasts(fcst, panel, name))
        fcst.to_csv(REPORTS / f"forecasts_{name}.csv", index=False)

    metrics = pd.concat(metric_parts, ignore_index=True)
    metrics.to_csv(REPORTS / "metrics.csv", index=False)
    write_regime_report(metrics, timings, REPORTS / "metrics_by_regime.md")
    print(f"Wrote {REPORTS / 'metrics.csv'}")
    print(f"Wrote {REPORTS / 'metrics_by_regime.md'}")
    print(metrics.loc[metrics["scope"] == "overall"].to_string(index=False))


if __name__ == "__main__":
    main()
