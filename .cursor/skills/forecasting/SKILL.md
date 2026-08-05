---
name: forecasting
description: >-
  Practice industry forecasting system design and tradeoff answers for
  senior/principal applied scientist roles. Use when the user invokes
  /forecasting or practices production forecasting, LightGBM vs Chronos,
  eval metrics, or mock principal-scientist forecasting questions.
---

# Forecasting (industry practice)

## When to use

General forecasting-role prep — **not** Amazon SCOT relationship work (`Amazon_SCOT/`). Plan: [`Forecasting/prep-plan.md`](../../Forecasting/prep-plan.md). Profile: [`omri_azencot_experience.md`](../debrief/omri_azencot_experience.md).

## Positioning

User has deep research TS / generative / FM expertise. Push **production judgment**: scale, cost, latency, maintainability, eval, cold start, intermittent demand. Do **not** quiz classical ARIMA derivations. Do **not** default to SCOT contribution pitch unless asked.

## Workflow

1. **Pick mode** — user chooses or rotate:
   - **Landscape** — method use/reject (naive, ETS, LightGBM, Chronos, …)
   - **Eval** — MAPE/WAPE/MASE/CRPS; intermittent demand; when metrics lie
   - **Production** — pipeline, drift, retrain, monitoring, 5M req/day
   - **Tradeoff** — LightGBM vs Chronos; why stats still win; FM everywhere?
   - **System design** — 500K SKUs / inventory / millions of series
   - **Debug** — MAPE doubled; cold start; holiday shift
2. **Prompt** — “You have 3–5 minutes. Go.” Prefer spoken; accept typed if practicing alone.
3. **Score** (brief):
   - [ ] Restates problem + constraints (scale, cost, latency, data quality)
   - [ ] Baseline first (naive / ETS) before fancy models
   - [ ] Clear **decision** (what they’d ship and why)
   - [ ] Eval aligned to business (not vanity MAPE)
   - [ ] Failure modes + monitoring
   - [ ] IC voice (“I”), no roadmap laundry list
4. **Follow-ups** — 2–3 probes, e.g.:
   - “Why not Chronos on every series?”
   - “How do you handle intermittent SKUs?”
   - “What kills this in production in 90 days?”
   - “How would you A/B against the current champion?”
5. **Reference skeleton** — give a tight 90s–3 min outline after they answer (not a paper).
6. **Optional retake** — one retry; score delta only.
7. **Persist** — save corrections to `Forecasting/notes/YYYY-MM-DD_<topic>.md`; update [`prep-plan.md`](../../Forecasting/prep-plan.md) checkboxes if mid-week. Session debriefs for this track also live under `Forecasting/notes/` (not FinTech/SCOT folders).

## Default answer skeleton

```
Problem & business stake
→ Data shape (volume, hierarchy, intermittency, covariates)
→ Baseline + simple strong model
→ When you’d escalate (boosting / DL / FM)
→ Eval + uncertainty
→ Production (retrain, monitor, cost)
→ Kill / rollback criteria
```

## Question bank (Day 7)

- Design a forecasting system for Amazon-scale inventory
- How would you forecast millions of time series?
- New products / cold start
- Holidays that change every year
- Why not Chronos everywhere?
- Why is LightGBM still competitive?
- How do you forecast uncertainty?
- How do you detect concept drift?
- Convince leadership to migrate to a foundation model (or argue against)
- How would you measure business impact?
- 500K retail SKUs — build the system
- LightGBM vs Chronos — when each?
- Why are statistical models still competitive?
- Evaluate intermittent demand
- Productionize a forecasting model
- MAPE suddenly doubled — debug

## Anti-patterns to interrupt

- Jumping to FMs without a baseline
- MAPE as default for intermittent / sparse demand
- “We’d use the latest paper” with no cost/latency story
- Research tour without a ship decision
- Confusing this track with SCOT contribution / Boris pitch
