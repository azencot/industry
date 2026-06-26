---
name: debrief
description: >-
  Write post-session debriefs and close the loop: save Amazon FinTech session
  conclusions to Amazon_FinTech/debrief/, keep general profile/project references
  in .cursor/skills/debrief/, update mocks/stories/INDEX, and AGENTS.md. Use
  when the user invokes /debrief or finishes prep work and wants learnings persisted.
---

# Debrief (close the loop)

## When to use

After mock interview, timed code drill, real interview, exploration session, or any substantial prep work.

## Where debrief files live

**Amazon FinTech-specific session debriefs** live under **[`Amazon_FinTech/debrief/`](../../Amazon_FinTech/debrief/)**.

**General reusable references** about Omri or project background live under **`.cursor/skills/debrief/`** so every future agent can load them independent of this interview track.

| File type | Path pattern | Example |
|-----------|--------------|---------|
| Amazon FinTech session debrief | `Amazon_FinTech/debrief/YYYY-MM-DD_{topic}.md` | `2026-06-24_prep-strategy.md` |
| General profile/project reference | `.cursor/skills/debrief/{name}_{topic}.md` | `omri_azencot_experience.md`, `vlm_multimodal_project.md` |

Template: [`Amazon_FinTech/debrief/README.md`](../../Amazon_FinTech/debrief/README.md).

**Mock drills** (timed-code, full-mock, mock-lp, ml-deep-dive as simulation): *also* write `Amazon_FinTech/mocks/YYYY-MM-DD_{type}.md` using [`Amazon_FinTech/mocks/README.md`](../../Amazon_FinTech/mocks/README.md).

## Workflow

1. **Gather** — ask briefly (or infer from session):
   - Session type, duration, what was covered
   - What went well / what broke
   - Any recurring corrections ("still wrong", "forgot to mention X")
2. **Write debrief** — create Amazon FinTech session notes in **`Amazon_FinTech/debrief/`**. If the learning is general background about Omri or a project reference, update **`.cursor/skills/debrief/`** instead.
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
Debrief saved: Amazon_FinTech/debrief/YYYY-MM-DD_{topic}.md
[Mock log: Amazon_FinTech/mocks/YYYY-MM-DD_{type}.md — if applicable]
Updated: [list paths]
Next session: [one item + @Files prompt]
```

## Principles (from compounding prep)

- Facts live in repo files; preferences live in AGENTS.md and skills
- **Amazon FinTech session debriefs → `Amazon_FinTech/debrief/`**
- **General profile/project references → `.cursor/skills/debrief/`**
- Corrections in session → debrief file → config update
- Do not leave learnings only in chat; session B should `@Files` the debrief
