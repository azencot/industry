---
name: debrief
description: >-
  Write post-mock or post-interview debriefs and close the loop: update mocks,
  stories, INDEX, and AGENTS.md from session feedback. Use when the user invokes
  /debrief or finishes a prep session and wants learnings persisted.
---

# Debrief (close the loop)

## When to use

After mock interview, timed code drill, real interview, or any substantial prep session.

## Workflow

1. **Gather** — ask briefly (or infer from session):
   - Session type, duration, what was covered
   - What went well / what broke
   - Any recurring corrections ("still wrong", "forgot to mention X")
2. **Write mock log** — create or append `Amazon_FinTech/mocks/YYYY-MM-DD_{type}.md` using template in [`Amazon_FinTech/mocks/README.md`](../../Amazon_FinTech/mocks/README.md).
3. **Update indexes**
   - Add row to mock table in [`Amazon_FinTech/INDEX.md`](../../Amazon_FinTech/INDEX.md)
   - Update timed log in root [`INDEX.md`](../../INDEX.md) if coding
   - Mark LP ready in [`Amazon_FinTech/stories/README.md`](../../Amazon_FinTech/stories/README.md) if story improved
4. **Promote corrections** — if something failed twice or is broadly useful:

   | If correction is about… | Update |
   |-------------------------|--------|
   | Session behavior / conventions | [`AGENTS.md`](../../AGENTS.md) |
   | Workflow steps | relevant `.cursor/skills/*/SKILL.md` |
   | Story content | `Amazon_FinTech/stories/*.md` |
   | Problem-specific note | root `INDEX.md` pattern table |

5. **Next session** — one concrete action item (single focus).

## Output

Confirm files touched:

```
Debrief saved: Amazon_FinTech/mocks/YYYY-MM-DD_{type}.md
Updated: [list paths]
Next session: [one item]
```

## Principles (from compounding prep)

- Facts live in repo files; preferences live in AGENTS.md and skills
- Corrections in session → transcript → debrief → config update
- Do not leave learnings only in chat
