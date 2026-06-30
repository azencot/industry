# Debrief — 2026-06-30 — PS1 final sprint (interview day)

## Session

- Type: pre-interview 5-hour sprint + bonus systems drill
- Duration: ~6 h (09:18–15:07), interview at 21:00
- Prior context: recruiter confirmed format change — Science Depth 20 / Coding 20 / **Ownership** LP 20 (was Deliver Results)

## Conclusions

- **Science depth (~75 min):** full VLM walkthrough strong; lead with multimodal/VLM, keep diffusion as theory reserve. Recurring fixes locked: add **one FinTech bridge sentence**; self-bound headline as **best among open/non-proprietary**; synthetic risk = **distribution shift even with correct labels**; numerical reasoning valid only for **visually recoverable** quantities; partial TSRBench = **screening gate** not winner; ablation needs **token-budget control**.
- **Coding (~40 min):** 3 mediums (`322` DP memo, `3` sliding window, `57` insert interval). Pattern of the day = **right approach, tail-end slip** (every miss was a typo/invariant error in the last lines). Habit to hold: **dry-run last 5 lines**; `while left <= right`; state invariant + O() before coding.
- **Ownership (~30 min):** TR-synthetic-kill story sharpened. Lead with **ownership moment (promotion criteria)**, not benchmark context. Kill line: **TR 26.9→21.9 (−5.0)**, still kill despite avg +1.8 / AR-IR ~+7. Phrasings: "killed that **data path**", "**distribution shift**", gates "**block promotion, not learning**", "I would **not start by generating more data**". Story file updated (90s version + follow-ups).
- **Integration mock (~30 min):** science / coding / Ownership openers all ~85–90%.
- **Bonus systems drill (~40 min):** exposed gaps at the engineering layer Karan probes — batch/accum, LR+sweep, sampler bug, adapter chain, eval decode, optimizer/throughput. Grounded answers from repo configs now in cheat sheet. **8B batch corrected**: effective global 64 = early 2×4 or later 1×8 ×8 GPUs (mostly 8× A100 historically; RTX Pro 6000 recent).

## Decisions / artifacts updated

- [x] prep-plan.md — 5-hour sprint logged per block + interview-day crib + systems-drill weak-spot list
- [x] stories/ownership_killed-tr-synthetic.md — opener, 90s version, follow-ups
- [x] vlm-technical-cheat-sheet.md — new "Training / Systems Engineering" section + 2 Karan pull-thread rows
- [x] code/ — 3 new practice files (322, 3, 57)
- [ ] omri_azencot_experience.md — no change
- [ ] AGENTS.md — no change

## Open questions

- Peak GPU memory per stage not logged in repo; exact peft version unknown; chart token count (~114) is processor-dependent — state as caveats if pressed.

## Next session (one prompt for session B)

> Read this file. PS1 happened 30 Jun 21:00 (Karan). Run `/debrief` on the real interview: what was asked in each block (science/coding/Ownership), what landed, what to fix for the next loop.
