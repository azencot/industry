---
name: debrief
description: >-
  Write post-session debriefs and close the loop: save conclusions to
  .cursor/skills/debrief/, update mocks/stories/INDEX, and AGENTS.md. Use when
  the user invokes /debrief or finishes a prep session and wants learnings persisted.
---

# Debrief (close the loop)

## When to use

After mock interview, timed code drill, real interview, exploration session, or any substantial prep work.

## Where debrief files live

**Always** write debrief files under **`.cursor/skills/debrief/`** (this directory). Do not use `Amazon_FinTech/debrief/` or other paths.

| File type | Path pattern | Example |
|-----------|--------------|---------|
| Per-session debrief | `.cursor/skills/debrief/YYYY-MM-DD_{topic}.md` | `2026-06-24_prep-strategy.md` |
| Long-lived reference | `.cursor/skills/debrief/{name}_{topic}.md` | `omri_azencot_experience.md` |

Template: [`README.md`](README.md) in this folder.

**Mock drills** (timed-code, full-mock, mock-lp, ml-deep-dive as simulation): *also* write `Amazon_FinTech/mocks/YYYY-MM-DD_{type}.md` using [`Amazon_FinTech/mocks/README.md`](../../Amazon_FinTech/mocks/README.md).

## Workflow

1. **Gather** — ask briefly (or infer from session):
   - Session type, duration, what was covered
   - What went well / what broke
   - Any recurring corrections ("still wrong", "forgot to mention X")
2. **Write debrief** — create file in **this directory** (`.cursor/skills/debrief/`).
3. **Update indexes**
   - Add row to debrief table in [`Amazon_FinTech/INDEX.md`](../../Amazon_FinTech/INDEX.md)
   - Add row to mock table if a drill log was created
   - Update timed log in root [`INDEX.md`](../../INDEX.md) if coding
   - Mark LP ready in [`Amazon_FinTech/stories/README.md`](../../Amazon_FinTech/stories/README.md) if story improved
4. **Promote corrections** — if something failed twice or is broadly useful:

   | If correction is about… | Update |
   |-------------------------|--------|
   | Session behavior / conventions | [`AGENTS.md`](../../AGENTS.md) |
   | Workflow steps | relevant `.cursor/skills/*/SKILL.md` |
   | Story content | `Amazon_FinTech/stories/*.md` |
   | Experience / pitch framing | `.cursor/skills/debrief/omri_azencot_experience.md` |
   | Problem-specific note | root `INDEX.md` pattern table |

5. **Next session** — one concrete action item + suggested `@Files` handoff prompt for session B.

## Output

Confirm files touched:

```
Debrief saved: .cursor/skills/debrief/YYYY-MM-DD_{topic}.md
[Mock log: Amazon_FinTech/mocks/YYYY-MM-DD_{type}.md — if applicable]
Updated: [list paths]
Next session: [one item + @Files prompt]
```

## Principles (from compounding prep)

- Facts live in repo files; preferences live in AGENTS.md and skills
- **All debrief files → `.cursor/skills/debrief/`**
- Corrections in session → debrief file → config update
- Do not leave learnings only in chat; session B should `@Files` the debrief
