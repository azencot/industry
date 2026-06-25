# Mock — 2026-06-24 — timed-code (567)

## Setup

- **Duration:** ~50 min (target 25; debug iterations)
- **Focus:** sliding window / hash map — PS1 medium
- **Problem:** 567 Permutation in String — `code/2026-06-24_567_permutation_in_string_practice.py`

## What went well

- Approach narrated before coding; iterated to correct solution without full hint dump
- Key learning: `for` cannot rewind — `while` + `le` restart for overlap cases
- All tests pass including `adc`/`dcda`, `ab`/`aab`

## What broke

- [x] **Verbal / structure:** initial complexity O(len(s2)×len(s1)) — corrected to O(1) map, O(len(s2)) typical
- [x] **Technical gap:** overlap window restart (`le+1`) — fixed with `while`
- [ ] **Time:** over 25 min — acceptable for learning rep; aim narrated 25 min next medium

## Corrections to promote

| Observation | Update where |
|-------------|--------------|
| `for` vs `while` when adjusting index | debrief + next timed-code rep |
| Worst-case O(n²) with dict.copy resets | mention O(n) fixed-window upgrade if probed |
| Dated `_practice.py` + interview mode | [`timed-code/SKILL.md`](../../.cursor/skills/timed-code/SKILL.md) |

## Next session (one thing)

TMAY IC paragraph read-aloud — close Jun 24 prep-plan.
