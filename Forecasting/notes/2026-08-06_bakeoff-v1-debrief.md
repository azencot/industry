# Debrief — Forecasting bakeoff v1 + code review (2026-08-06)

**Track:** Forecasting (general industry practice — not SCOT)  
**Covered:** Implement SN/ETS/LightGBM/Chronos-Bolt-small bakeoff; ~30 min code/report review; metric + Chronos point-forecast Q&A  
**Artifacts:** [`../code/`](../code/) · [`../code/reports/metrics_by_regime.md`](../code/reports/metrics_by_regime.md)

---

## Covered

- Bakeoff on signed-off synthetic panel: seasonal naive (`m=7`), AutoETS, global LightGBM (lags + known-future promo/price), Chronos-Bolt `amazon/chronos-bolt-small` zero-shot (median quantile)
- Metrics: MAE, RMSE, WAPE, MASE overall + by regime; wall timings
- Review: contract → evaluate.py → four model files → regime narrative
- Q&A: why MAE/WAPE/MASE are absolute-error based; why Chronos uses median not mean

## Results (lock for interviews)

| Regime | Winner (MASE) | Takeaway |
|--------|---------------|----------|
| overall | LightGBM | Promo mass in panel rewards features |
| `promo_driven` | LightGBM (crush) | Don’t Chronos-everywhere when promo/price is the lever |
| `mean_step` | LightGBM ≥ ETS > SN | Seasonal copy fails after mean break |
| `intermittent` | Chronos | Lead with WAPE/MASE, not MAPE |
| `smooth_seasonal` | Chronos/LGBM edged SN/ETS | Baselines still competitive; not “FM required” |
| `cold_start` | **LightGBM** (nuance) | Half cold series are promo-parent → covariates help; Chronos still beats SN/ETS |

## Corrections / concepts locked

| Topic | Lock |
|-------|------|
| Absolute vs squared metrics | MAE/WAPE/MASE = typical miss / planning lens (L1). RMSE = outlier-sensitive (L2). |
| Chronos point forecast | Bolt is probabilistic; **median (q=0.5)** matches L1 metrics; mean aligns more with RMSE |
| Fit stories | SN no train; ETS per-series fit; LGBM global train; Chronos pretrained inference |
| Ops pins | `chronos-forecasting==1.4.1` + `torch<2.4` on this Mac; LightGBM needs `brew install libomp` |

## Still open

- [ ] Day 2: feature list with leakage notes + spoken “why LGBM wins bakeoffs”
- [ ] Day 3: metrics cheat sheet note (concepts partly locked here)
- [ ] Spoken retake: LightGBM vs Chronos using **this** regime table
- [ ] Optional: tighten cold_start DGP (smooth-only) if we want Chronos to win that segment by construction

## Next session

1. Write ½-page feature/leakage list for the LightGBM pipeline; practice 2-min spoken using promo vs cold_start results.  

**Handoff:** `@Forecasting/notes/2026-08-06_bakeoff-v1-debrief.md` `@Forecasting/code/reports/metrics_by_regime.md` `@Forecasting/prep-plan.md`
