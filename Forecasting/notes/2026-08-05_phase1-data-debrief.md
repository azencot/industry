# Debrief — Forecasting Phase 1 synthetic data (2026-08-05)

**Track:** Forecasting (general industry practice — not SCOT)  
**Duration:** design + implement + manual HTML review  
**Artifacts:** [`../data/`](../data/) · [`../data/review/REVIEW.html`](../data/review/REVIEW.html) · gold `generated/gold_checks.csv`

---

## Covered

- Chose synthetic multi-regime panel over raw M5/Favorita/Electricity for day-1 tradeoff demos
- Five regimes: `smooth_seasonal`, `mean_step` (mean structural break — not ETS “level”), `promo_driven`, `intermittent`, `cold_start`
- Generator + gold invariant checks + REVIEW.html/md with exemplar plots
- Manual browser review signed off; optional spot-checks (promo in horizon, shift before cutoff, cold x-axis) discussed

## What went well

- Regimes map cleanly to later expected winners (SN/ETS, ETS/LGBM, LGBM, metric drama, Chronos-Bolt)
- Gold 19/19 after fixing false-positive gap check on cold-start (Series vs DatetimeIndex `.equals`)
- HTML review with inline figures is the right sign-off surface

## Corrections / terminology

| Miss | Fix |
|------|-----|
| “Level shift” | Prefer **`mean_step`** — permanent jump in series mean; related to ETS level only as the *state that adapts*, not the DGP name |
| “No train/test split” non-goal | Means no rolling CV machinery; **cutoff + `in_train` is the split** |
| Code under skill vs track | Hands-on lives under **`Forecasting/data/`** (and later `Forecasting/code/`), not `.cursor/skills/` |

## Still open

- [ ] `Forecasting/code/`: seasonal naive → ETS → LightGBM → Chronos-Bolt on this panel
- [ ] Segment metrics by regime (prove the expected winners)
- [ ] Optional later: tiny real discrete retail slice for credibility

## Next session

1. Scaffold `Forecasting/code/` and run **seasonal naive** on `data/generated/panel.parquet`  
2. Report MAE/RMSE/WAPE/MASE overall + by regime  

**Handoff prompt:** `@Forecasting/notes/2026-08-05_phase1-data-debrief.md` `@Forecasting/data/README.md` `@Forecasting/prep-plan.md` — implement SN baseline under `Forecasting/code/` reading the signed-off panel.
