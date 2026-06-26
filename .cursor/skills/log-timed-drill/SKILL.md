---
name: log-timed-drill
description: >-
  Log a completed timed-code drill result to the root INDEX.md timed table and
  the Amazon_FinTech/prep-plan.md daily checklist. Use after a /timed-code
  attempt is reviewed, or when the user asks to log/record a coding drill result.
---

# Log timed drill

Record a finished `/timed-code` attempt in **two** places. Keep one source of truth: the timed table lives **only** in root [`INDEX.md`](../../INDEX.md), not `Amazon_FinTech/INDEX.md`.

## Inputs (gather or infer)

- **Date** (`YYYY-MM-DD`), **filename** (in `code/`), **minutes**, **pass/fail**
- **Notes:** pattern, key invariant, bug(s) hit, over/under 25 min
- If minutes unknown, estimate from drill timestamps and **flag the estimate** to the user.

## Steps

1. **Append a row** to the "Timed attempt log" table in root [`INDEX.md`](../../INDEX.md):

   `| YYYY-MM-DD | \`filename.py\` | ~min | pass/fail | pattern; invariant; bug(s); over/under 25 min |`

2. **Update** [`Amazon_FinTech/prep-plan.md`](../../Amazon_FinTech/prep-plan.md) for the current day:
   - Mark the timed-medium checkbox progress (e.g. `**1/2:** <file> (pattern, ~min, pass)`); only `[x]` when the day's target count is met.
   - Strike the covered pattern in the patterns line (e.g. `~~heap~~`).

3. **Reading `code/`:** it is in `.cursorignore`, so file tools are blocked. Read/run drill files via Shell with `required_permissions: ["all"]`.

4. **Optional** — full-simulation drill also gets `/debrief` → `Amazon_FinTech/mocks/YYYY-MM-DD_timed-code.md`.

## Row example

```
| 2026-06-26 | `2026-06-26_347_top_k_frequent_elements_practice.py` | ~15 | pass | heap / top-K; size-k min-heap on `(freq,num)`; bug: return drained `h` not `heappop(h)`; under 25 min |
```

## Do not

- Do not create a timed table in `Amazon_FinTech/INDEX.md` — root `INDEX.md` is canonical.
- Do not invent minutes; estimate and flag if unknown.
