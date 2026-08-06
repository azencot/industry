# Forecasting synthetic panel (Phase 1)

Seeded multi-regime daily panel for method tradeoff demos (SN / ETS / LightGBM / Chronos-Bolt later).

## Regimes

| Regime | What you should see | Later expected winner |
|--------|---------------------|------------------------|
| `smooth_seasonal` | Stable weekly seasonality | Seasonal Naive / ETS |
| `mean_step` | Permanent jump in series **mean** at `shift_date` | ETS / LightGBM |
| `promo_driven` | Spikes when `promo=1` (known in horizon too) | LightGBM |
| `intermittent` | Sparse integer demand, many zeros | Metric drama; Chronos vs local |
| `cold_start` | Only 30–60 train days | Chronos-Bolt |

## Layout

- `schemas/panel.md` — column dictionary
- `scripts/generate_panel.py` — write `generated/`
- `scripts/verify_gold.py` — DGP invariant checks (exit 1 on fail)
- `scripts/build_review_report.py` — `review/REVIEW.html` + `REVIEW.md` + figures
- `generated/` — panel + meta + cutoff
- `review/` — human sign-off (open **REVIEW.html** in a browser)

## Setup + regenerate

Requires Python ≥3.10 (3.11 recommended). From this folder:

```bash
cd Forecasting/data
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/generate_panel.py
python scripts/verify_gold.py
python scripts/build_review_report.py
open review/REVIEW.html   # or double-click
```

Same seed → same panel. Sign off the HTML checklist before building `Forecasting/code/` models.
