# Debrief — Day 1 Part 2 themes + Day 2 features (2026-08-06)

**Track:** Forecasting (general industry practice — not SCOT)  
**Covered:** M4/M5 competition themes (signed off); feature lenses + leakage; spoken “why LightGBM still wins bakeoffs”  
**Artifacts:** [`2026-08-05_day1-competition-themes.md`](2026-08-05_day1-competition-themes.md) · [`2026-08-06_day2-features.md`](2026-08-06_day2-features.md) · [`../prep-plan.md`](../prep-plan.md)

---

## Covered

- Day 1 Part 2 reopened and taught (not quiz-from-scratch): M4 pooling/ensembles; M5 hierarchy, intermittent metrics, related series, features-vs-fancy
- Spoken check: intermittent metrics — MAPE dies on zeros → WAPE/MASE
- Day 2 reframed: **3 lenses** (cutoff/leak, drivers > architecture, label≠feature) instead of memorizing the full covariate laundry list
- Feature note + v1 ship set (lags, calendar, planned promo/price, category/store)
- Spoken 2-min: why LightGBM wins production bakeoffs

## Corrections / concepts locked

| Topic | Lock |
|-------|------|
| Intermittent eval | MAPE undefined/unstable on zeros; lead with **WAPE and/or MASE**, not MASE alone |
| Holidays | Moving holidays → add event calendar; don’t skip holidays because they move |
| Promo leakage | Planned promo at cutoff = fair; **final/realized** promo = leak |
| LGBM spoken | Lead with **covariates + global pooling**, not fast/interpretable; SN/ETS = true baselines; LGBM = production default before FM |
| LGBM inference | Fit once on panel; **score in parallel** — avoid “recursive eval” unless rolling lags step-by-step |
| Features pedagogy | Menu ≠ homework; interview = cutoff discipline + drivers first |

## Still open

- [x] Day 3: metrics cheat sheet + spoken “MAPE doubled overnight” — see [`2026-08-08_day3-metrics-debrief.md`](2026-08-08_day3-metrics-debrief.md)
- [ ] Spoken retake: LightGBM vs Chronos using bakeoff regime table (from bakeoff debrief)
- [ ] Optional Tier B skim

## Next session

1. ~~Day 3~~ → **Day 4 — Production** (see Day 3 debrief handoff).

**Handoff:** `@Forecasting/notes/2026-08-08_day3-metrics-debrief.md` `@Forecasting/notes/metrics-cheat-sheet.md` `@Forecasting/prep-plan.md`
