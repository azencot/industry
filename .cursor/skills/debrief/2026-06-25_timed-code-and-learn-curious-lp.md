# Debrief — 2026-06-25 — timed-code (Islands) + Learn & Be Curious LP

## Session

- **Type:** timed-code drill + LP draft/strategy + spoken-script fill
- **Duration:** ~1 hr (evening, after Anchor B/C session earlier same day)
- **Prior context:** [`2026-06-25_anchor-bc-lp-debrief.md`](2026-06-25_anchor-bc-lp-debrief.md)

## What we did

### 1. timed-code — Number of Islands (200)

- BFS/DFS pattern (sliding window was 24 Jun); ~35 min, **pass**.
- Bugs across 3 iterations: `.length` → `len()`; `== 1` vs `== '1'` (strings); `do_dfs(grid,i,j)` wrong arity (nested fn); pre-marking `visited` in outer loop before recursion; **user caught my missing bounds check** in the "clean" snippet I suggested.
- Final: top-of-DFS bounds + visited/water guard, clean outer loop. All asserts pass.
- File: [`code/2026-06-25_200_number_of_islands_practice.py`](../../code/2026-06-25_200_number_of_islands_practice.py)

### 2. LP strategy — Customer Obsession decision

- User considered drafting Customer Obsession (ImagenTime/Few repo) for story variety (3 VLM LPs feels narrow).
- **Decision: do NOT draft CO.** Technical science screens rarely span CO; repo-usability angle risks sounding like open-source hygiene without adoption metrics. Plan already says stop drafting CO/Earn Trust unless mock surfaces a gap.

### 3. New story — Learn and Be Curious (diffusion)

- User had a ready DOC narrative (learned diffusion w/ students Ilan, Nimrod → 7 papers ICML/ICLR/NeurIPS).
- Drafted into agreed DOC format: [`stories/learn-be-curious_diffusion-mastery.md`](../../Amazon_FinTech/stories/learn-be-curious_diffusion-mastery.md).
- Reframed for IC voice: "I learned/implemented/debugged/rewrote" not "my group succeeded"; trimmed managerial setup (tenure-track, funding/recruitment).
- Filled **~8-min spoken script (~1048 words)** to match other LP files.
- Registered in `stories/README.md` (still ☐ — drafted, not rehearsed).

## Conclusions

- **Story bank now spans 2 projects:** VLM (Ownership, Dive Deep, Deliver Results) + diffusion/ImagenTime (Invent & Simplify, Learn & Be Curious). Good variety hedge against one-project impression.
- **Learn & Be Curious = backup variety story, not PS1 primary.** Lead with VLM technical LPs for Karan.
- **Coding still slow:** 3rd timed medium in a row over 25 min (50, 50, 35). Trend improving but need a one-shot clean pass.

## Recurring corrections to promote

| Observation | Where |
|-------------|-------|
| Suggested DFS snippet without bounds check | self-note: always include bounds in grid DFS template |
| Drafted LP prose without agreed DOC format first | mock-lp already covers; read an existing story before drafting |

## Open / verify

- [ ] Learn & Curious: confirm exact paper count (7) + venues; add one concrete SDE-enabled modeling decision; managerial-voice read-aloud pass.
- [ ] Rehearse Learn & Curious aloud (target ~85%) before marking ready.
- [ ] Coding: land a BFS/DFS or heap medium in one clean pass under 25 min (Thu 26 sprint).

## Next session

> `@Files .cursor/skills/debrief/2026-06-25_timed-code-and-learn-curious-lp.md` — Fri 26 Jun coding sprint #1 (2× timed mediums: heap/intervals/trie/binary search); optionally rehearse Learn & Be Curious aloud once.
