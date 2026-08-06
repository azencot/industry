# Forecasting model bakeoff (v1)

Compare **Seasonal Naive**, **ETS**, **LightGBM**, and **Chronos-Bolt (small)** on the signed-off synthetic panel in [`../data/generated/`](../data/generated/).

## Locked choices

| Item | Choice |
|------|--------|
| Seasonal period `m` | **7** (known from DGP / daily weekly seasonality) |
| Chronos | `amazon/chronos-bolt-small` zero-shot (no fine-tune) |
| Metrics | MAE, RMSE, WAPE, MASE (`m=7`) |
| Split | single cutoff from `cutoff.json` |

## Setup

```bash
cd Forecasting/code
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**macOS note:** LightGBM needs OpenMP — `brew install libomp` if import fails on `libomp.dylib`.

Chronos pulls Hugging Face weights on first run. This repo pins `chronos-forecasting==1.4.1` + `torch<2.4` for older macOS PyPI wheels.

## Run

```bash
python -m src.run_compare
python -m src.run_compare --models sn,ets,lgbm
python -m src.run_compare --models chronos
```

Writes `reports/metrics.csv` and `reports/metrics_by_regime.md`.

## Interview one-liner

Naive = no train; ETS = cheap per-series fit; LightGBM = global train on features; Chronos-Bolt = pretrained zero-shot inference.
