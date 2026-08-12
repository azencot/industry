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
| [`interviews/`](interviews/) | Company / exploratory call prep (Keystone, Trade Desk, …) — not SCOT |
| [`data/`](data/) | Synthetic multi-regime panel + gold checks + [`data/review/REVIEW.html`](data/review/REVIEW.html) |
| [`code/`](code/) | Bakeoff + [`code/reports/metrics_by_regime.md`](code/reports/metrics_by_regime.md) + qual [`code/reports/qual/QUAL.html`](code/reports/qual/QUAL.html) |

Skill: **`/forecasting`** — spoken system-design / tradeoff drills.

Shared profile: [`.cursor/skills/debrief/omri_azencot_experience.md`](../.cursor/skills/debrief/omri_azencot_experience.md).

---

## Session log

| Date | Session | Notes |
|------|---------|-------|
| 2026-08-05 | Day 1 Tier A deep-dives | [`notes/2026-08-05_day1-tierA-debrief.md`](notes/2026-08-05_day1-tierA-debrief.md) — SN/ETS/LGBM/Chronos |
| 2026-08-05 | Phase 1 synthetic data (signed off) | [`notes/2026-08-05_phase1-data-debrief.md`](notes/2026-08-05_phase1-data-debrief.md) · [`data/review/REVIEW.html`](data/review/REVIEW.html) — 50 series, gold 19/19 |
| 2026-08-05 | Bakeoff v1 (SN/ETS/LGBM/Chronos-Bolt) | [`code/`](code/) · [`code/reports/metrics_by_regime.md`](code/reports/metrics_by_regime.md) |
| 2026-08-06 | Bakeoff code review + metrics/Chronos Q&A | [`notes/2026-08-06_bakeoff-v1-debrief.md`](notes/2026-08-06_bakeoff-v1-debrief.md) |
| 2026-08-06 | Day 1 Part 2 themes + Day 2 features | [`notes/2026-08-06_day1-part2-day2-debrief.md`](notes/2026-08-06_day1-part2-day2-debrief.md) · themes · [`notes/2026-08-06_day2-features.md`](notes/2026-08-06_day2-features.md) |
| 2026-08-08 | Day 3 Evaluation / metrics | [`notes/2026-08-08_day3-metrics-debrief.md`](notes/2026-08-08_day3-metrics-debrief.md) · [`notes/metrics-cheat-sheet.md`](notes/metrics-cheat-sheet.md) |
| 2026-08-08 | Keystone.AI call prep (Raunak) | [`interviews/keystone-ai/2026-08-10_raunak-prep.md`](interviews/keystone-ai/2026-08-10_raunak-prep.md) — Mon 2026-08-10; reading done through Raunak interview · [`notes/2026-08-08_keystone-raunak-prep-debrief.md`](notes/2026-08-08_keystone-raunak-prep-debrief.md) |
| 2026-08-09 | Keystone prep close-out | [`notes/2026-08-09_keystone-raunak-prep-debrief.md`](notes/2026-08-09_keystone-raunak-prep-debrief.md) — re-engage framing; FT availability pocket; intro/logistics done; LGBM/MAPE optional |
| 2026-08-10 | Keystone call with Raunak | [`interviews/keystone-ai/2026-08-10_raunak-debrief.md`](interviews/keystone-ai/2026-08-10_raunak-debrief.md) — opportunistic hire; manager + CV; FM/synthetic data; Boris interest |
| 2026-08-12 | TTD Channel Growth recruiter prep | [`interviews/the-trade-desk/2026-08-12_recruiter-prep.md`](interviews/the-trade-desk/2026-08-12_recruiter-prep.md) — Senior AS; forecast / pace / recs on emerging channels |
| 2026-08-12 | TTD recruiter screen (Stephanie) | [`interviews/the-trade-desk/2026-08-12_recruiter-debrief.md`](interviews/the-trade-desk/2026-08-12_recruiter-debrief.md) — cleared; HM **Kennedy**; next = 45 min Python coding; DL is team gap |

---

## Positioning (read once)

You already have deeper research expertise than most industry scientists. **Do not** spend time on classical theory derivations (ARIMA proofs, stationarity lemmas). Gap = what production forecasting teams actually do, how they evaluate, and what tradeoffs they make.

Interview signal at principal level: **why you’d choose A over B under constraints**, not the latest architecture paper.
