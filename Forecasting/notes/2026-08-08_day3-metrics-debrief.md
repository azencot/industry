# Debrief — Day 3 Evaluation / metrics (2026-08-08)

**Track:** Forecasting (general industry practice — not SCOT)  
**Covered:** Point metrics (MAPE/SMAPE + known MAE/RMSE/WAPE/MASE); pinball/CRPS; forced answers; MAPE-doubled spoken; intervals / coverage / calibration / business KPIs  
**Artifacts:** [`metrics-cheat-sheet.md`](metrics-cheat-sheet.md) · [`../prep-plan.md`](../prep-plan.md)

---

## Covered

- MAPE vs SMAPE vs WAPE framing; forced answers scored (RMSE units corrected)
- Spoken “MAPE doubled overnight” — data-first + MAE/demand + slice; playbook locked
- Intervals: nominal \(1-\alpha\), central PI = \(q_{\alpha/2}\)–\(q_{1-\alpha/2}\) (90% → q5–q95; 95% → q2.5–q97.5)
- Coverage vs calibration; fill rate = demand fulfilled (not replenishment)
- Business KPI layer above forecast error

## Corrections / concepts locked

| Topic | Lock |
|-------|------|
| RMSE units | RMSE has **same units as \(y\)**; misleading via outlier amplification, not unit mismatch |
| MAPE / SMAPE | Stakeholder %; fragile on zeros — WAPE preferred for panels |
| WAPE | Portfolio \(\sum\|e\|/\sum\|y\|\); weights big SKUs |
| Intermittent | MAPE/SMAPE break → WAPE and/or MASE (+ pinball/CRPS if inventory) |
| MAPE debug | Metric → pipeline/data → scope → baselines → model; **not MoE overnight** |
| Fleet demand drop | Don’t dismiss — holidays / outages / promo cliffs happen |
| Nominal \(\alpha\) | \(\alpha\) = outside; \(1-\alpha\) = claimed coverage |
| Fill rate | Units shipped (or fulfilled) / demand — not refill speed |

## Still open

- [ ] Day 4 — production checklist + spoken productionize SKU demand
- [ ] Spoken retake: LightGBM vs Chronos using bakeoff regime table
- [ ] Optional: skim Amazon Forecast metrics docs / one Uber-Google metrics writeup (plan said skim only)

## Next session

1. Start **Day 4 — Production forecasting**: write [`production-checklist.md`](production-checklist.md); spoken 3-min productionize a SKU demand model.

**Handoff:** `@Forecasting/notes/2026-08-08_day3-metrics-debrief.md` `@Forecasting/notes/metrics-cheat-sheet.md` `@Forecasting/prep-plan.md`
