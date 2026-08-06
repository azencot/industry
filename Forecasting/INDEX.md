# Forecasting — industry practice track

General prep for **senior / principal applied scientist** roles where forecasting is central (Amazon, Microsoft, Uber, Airbnb, Stripe, etc.). **Not** SCOT relationship prep — that lives in [`Amazon_SCOT/`](../Amazon_SCOT/).

---

## Goal

By end of a focused week, answer industry questions with engineering judgment under real constraints (cost, latency, maintainability, scale, business impact) — not paper recaps.

Target questions:

- “500K retail SKUs — how would you build the forecasting system?”
- “When LightGBM vs Chronos?”
- “Why are statistical models still competitive?”
- “How do you evaluate intermittent demand?”
- “How would you productionize a forecasting model?”
- “MAPE suddenly doubled — how do you debug?”

---

## Key files

| File | What |
|------|------|
| [`prep-plan.md`](prep-plan.md) | 7-day checklist + daily hands-on thread |
| [`notes/`](notes/) | Day summaries, one-pagers, mock answers |
| [`data/`](data/) | Synthetic multi-regime panel + gold checks + [`data/review/REVIEW.html`](data/review/REVIEW.html) |
| [`code/`](code/) | Model bakeoff (later; reads `data/generated/`) |

Skill: **`/forecasting`** — spoken system-design / tradeoff drills.

Shared profile: [`.cursor/skills/debrief/omri_azencot_experience.md`](../.cursor/skills/debrief/omri_azencot_experience.md).

---

## Session log

| Date | Session | Notes |
|------|---------|-------|
| 2026-08-05 | Day 1 Tier A deep-dives | [`notes/2026-08-05_day1-tierA-debrief.md`](notes/2026-08-05_day1-tierA-debrief.md) — SN/ETS/LGBM/Chronos |
| 2026-08-05 | Phase 1 synthetic data (signed off) | [`notes/2026-08-05_phase1-data-debrief.md`](notes/2026-08-05_phase1-data-debrief.md) · [`data/review/REVIEW.html`](data/review/REVIEW.html) — 50 series, gold 19/19 |

---

## Positioning (read once)

You already have deeper research expertise than most industry scientists. **Do not** spend time on classical theory derivations (ARIMA proofs, stationarity lemmas). Gap = what production forecasting teams actually do, how they evaluate, and what tradeoffs they make.

Interview signal at principal level: **why you’d choose A over B under constraints**, not the latest architecture paper.
