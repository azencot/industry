---
name: timed-code
description: >-
  Simulate Amazon PS1 live coding: one medium LeetCode problem, 25 minutes,
  narrated approach. Use when the user invokes /timed-code or asks for timed
  coding interview practice in the industry repo.
---

# Timed code (PS1 simulation)

## When to use

Amazon Applied Scientist phone screen live coding. Problems from [`code/`](../../code/) or PS1-priority patterns in root [`INDEX.md`](../../INDEX.md).

**Interview mode:** `code/` is in [`.cursorignore`](../../.cursorignore) and [`.vscode/settings.json`](../../.vscode/settings.json) disables Cursor Tab + inline/Python suggestions for all `.py` files in this repo. Paste your solution in chat for review after the drill (agent won't index `code/` during the timer).

## Workflow

1. **Select problem**
   - User picks, or choose from PS1-priority pattern not recently logged in INDEX timed table.
   - Prefer canonical file (no `_practice` suffix) unless user wants a re-attempt on scratch version.
2. **State rules** — 25 min; restate → clarify → approach + O() → example → code → test; **narrate invariants**.
3. **Clarifying questions** — ask user (or answer yourself if solo drill): empty input, duplicates, ties, constraints.
4. **Timed phase** — user codes; coach only if stuck >3 min or user asks.
5. **Review**
   - Correctness (edge cases)
   - Time/space complexity stated?
   - Interview narration quality
6. **Log** — append row to timed table in [`INDEX.md`](../../INDEX.md):

   `| YYYY-MM-DD | filename | minutes | pass/fail | notes |`

7. **Optional** — if full simulation, run `/debrief` → `Amazon_FinTech/mocks/YYYY-MM-DD_timed-code.md` + summary in `Amazon_FinTech/debrief/`.

## Problem file convention (timed drills)

- **Path:** `code/YYYY-MM-DD_{leetcode#}_{slug}_practice.py`
- **Header:** full problem statement, examples, constraints, LeetCode link
- **Body:** `class Solution(object):` — user fills in; agent does **not** hint unless asked mid-drill
- **Tests:** small `if __name__ == "__main__"` block at bottom

## Problem selection (default rotation)

Rotate across: hash map, sliding window, BFS/DFS, heap, intervals, binary search, trie, linked list.

## Communication prompts (coach user to say aloud)

- "I'm using a hash map because lookups need to be O(1)..."
- "This pointer marks the start of a valid window because..."
- "Time O(n), space O(k) for the counter."

## Do not

- Jump straight to code without approach sign-off
- Pick hard problems unlikely in PS1 (hard DP, obscure graph) unless user requests
