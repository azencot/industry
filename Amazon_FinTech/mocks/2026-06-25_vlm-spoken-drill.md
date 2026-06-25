# Mock — 2026-06-25 — vlm-spoken-drill (Anchor B + C)

## Setup

- **Duration:** ~90 min (interactive Q&A)
- **Focus:** Jun 25 prep-plan — eval gating + task audit
- **Topics:** Tiered eval latencies, parse-miss NR/TSF, TR kill, three regimes, Stage A/C metrics

## What went well

- User corrected pilot-harness conflation — docs now match actual eval ladder
- Strong audit taxonomy and per-task generator examples (TR, NR, Goldstein)
- Verified 0.8B deltas captured in cheat sheet

## What broke

- [x] **Verbal:** Initial eval story missing latencies and per-task promotion
- [x] **Numbers:** Rounded 38→40% before user supplied **0.382→0.405** table
- [ ] **Stage A:** curriculum mechanics (frozen LLM, DINO) one line short

## Corrections to promote

| Observation | Update where |
|-------------|--------------|
| Eval latencies + parse-miss | [`anchor-cheat-sheet.md`](../anchor-cheat-sheet.md) Anchor B |
| Audit + Stage C metrics | Anchor C + [`dive-deep_tsrbench-reasoning-audit.md`](../stories/dive-deep_tsrbench-reasoning-audit.md) |
| Don't cite ±0.3 pp unless user uses it | debrief + vlm project |

## Next session (one thing)

`/timed-code` — hash or BFS.
