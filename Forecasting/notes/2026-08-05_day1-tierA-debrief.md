# Debrief — Forecasting Day 1 Tier A (2026-08-05)

**Track:** Forecasting (general industry practice — not SCOT)  
**Duration:** ~2h deep-dives + Q&A (SN → ETS → LightGBM primer → Chronos)  
**Artifacts:** [`method-decision-table.md`](method-decision-table.md) · [`2026-08-05_day1-competition-themes.md`](2026-08-05_day1-competition-themes.md) · [`2026-08-05_tierA-deep-dives.md`](2026-08-05_tierA-deep-dives.md)

---

## Covered

- Seasonal naive: product vs baseline; hierarchy/reconciliation; stockout lookback; exogenous drivers
- ETS: level/trend/season equations; AutoETS (grid + AICc); when beats / loses to naive
- LightGBM: tabular framing; boosting from zero (tree → GBM → XGBoost vs LightGBM); split search / histograms; toy boosting round
- Chronos vs Chronos-Bolt: quantize+AR vs patch+direct; vs LightGBM decision
- M4/M5 themes + decision table drafted earlier same day

## What went well

- Asked clarifying questions until concepts stuck (exogenous, reconciliation, stockout copy, who sets tree splits)
- Chronos self-check landed clean on first try (cost + promo/events; Bolt when thin features / zero-shot)
- SN product-vs-baseline self-check essentially correct after one sharpen

## Corrections (lock these)

| Miss | Fix |
|------|-----|
| ETS beats SN when “error non-zero”; SN wins on “jumps” | ETS wins by **smoothing** stable level/trend/season; SN wins when season is ultra-stable or history too short for AutoETS — **jumps hurt both** |
| LGBM vs Chronos: “fast/interpretable/standard”; reject if corpus too large | Decision axis = **features vs zero-shot**. LGBM when trusted covariates + panel; reject when thin features / cold-start / leakage — **large tables favor LGBM**, not reject it |
| Chronos “expensive” | Mostly Chronos-**1** AR sampling + naive full-catalog serve; Bolt cheaper but still often loses to LGBM when features are rich |

## Still open (Day 1)

- [ ] Seasonal naive pipeline on a chosen dataset (M5 / Favorita / Electricity)
- [ ] Optional Tier B one-liner skim
- [ ] One clean spoken retake: LightGBM vs Chronos (without notes)
- [ ] TimesFM: only table one-liner so far — enough until Day 5

## Next session

1. Finish Day 1 pipeline: pick dataset + seasonal naive baseline under `Forecasting/pipeline/`  
2. Or start Day 2 features + LightGBM implementation  

**Handoff prompt:**

```
@Forecasting/prep-plan.md @Forecasting/notes/2026-08-05_day1-tierA-debrief.md @Forecasting/notes/2026-08-05_tierA-deep-dives.md
Continue Forecasting prep: Day 1 remaining = seasonal naive pipeline (+ optional LGBM vs Chronos retake), then Day 2.
```
