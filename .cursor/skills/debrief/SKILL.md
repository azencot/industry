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

**Amazon SCOT session debriefs** live under **[`Amazon_SCOT/notes/`](../../Amazon_SCOT/notes/)** (`YYYY-MM-DD_{topic}.md`) — relationship/contribution track; not a FinTech PS1 machine unless it becomes a formal loop.

**Forecasting track session debriefs** live under **[`Forecasting/notes/`](../../Forecasting/notes/)** (`YYYY-MM-DD_{topic}.md`) — general industry forecasting practice; not SCOT. Company call prep/debriefs → **[`Forecasting/interviews/`](../../Forecasting/interviews/)**.

**GenAI track session debriefs** live under **[`GenAI/notes/`](../../GenAI/notes/)** (`YYYY-MM-DD_{topic}.md`) — generative AI / LLM roles; not forecasting. Company call prep/debriefs → **[`GenAI/interviews/`](../../GenAI/interviews/)**.

**General reusable references** about Omri or project background live under **`.cursor/skills/debrief/`** so every future agent can load them independent of interview track.

| File type | Path pattern | Example |
|-----------|--------------|---------|
| Amazon FinTech session debrief | `Amazon_FinTech/debrief/YYYY-MM-DD_{topic}.md` | `2026-06-24_prep-strategy.md` |
| Amazon SCOT session debrief | `Amazon_SCOT/notes/YYYY-MM-DD_{topic}.md` | `2026-08-01_scot-scaffold.md` |
| Forecasting session debrief | `Forecasting/notes/YYYY-MM-DD_{topic}.md` | `2026-08-05_day1-tierA-debrief.md` |
| Forecasting company call prep/debrief | `Forecasting/interviews/{company}/YYYY-MM-DD_*.md` | `Forecasting/interviews/the-trade-desk/2026-08-12_recruiter-prep.md` |
| GenAI session debrief | `GenAI/notes/YYYY-MM-DD_{topic}.md` | `2026-08-12_rag-eval-debrief.md` |
| GenAI company call prep/debrief | `GenAI/interviews/{company}/YYYY-MM-DD_*.md` | `GenAI/interviews/acme/2026-08-12_prep.md` |
| General profile/project reference | `.cursor/skills/debrief/{name}_{topic}.md` | `omri_azencot_experience.md`, `vlm_multimodal_project.md` |

Template: [`Amazon_FinTech/debrief/README.md`](../../Amazon_FinTech/debrief/README.md).

**Mock drills** (timed-code, full-mock, mock-lp, ml-deep-dive as simulation): *also* write `Amazon_FinTech/mocks/YYYY-MM-DD_{type}.md` using [`Amazon_FinTech/mocks/README.md`](../../Amazon_FinTech/mocks/README.md).

## Workflow

1. **Gather** — ask briefly (or infer from session):
   - Session type, duration, what was covered
   - What went well / what broke
   - Any recurring corrections ("still wrong", "forgot to mention X")
2. **Write debrief** — FinTech session notes → **`Amazon_FinTech/debrief/`**. SCOT session notes → **`Amazon_SCOT/notes/`**. Forecasting session notes → **`Forecasting/notes/`**. GenAI session notes → **`GenAI/notes/`** (company calls → **`GenAI/interviews/`**). General background about Omri or a project → **`.cursor/skills/debrief/`**.
3. **Update indexes**
   - FinTech: add row to debrief table in [`Amazon_FinTech/INDEX.md`](../../Amazon_FinTech/INDEX.md); mock table / timed log / stories README as applicable
   - SCOT: add timeline or key-files pointer in [`Amazon_SCOT/INDEX.md`](../../Amazon_SCOT/INDEX.md)
   - Forecasting: add session log row in [`Forecasting/INDEX.md`](../../Forecasting/INDEX.md); company table in [`Forecasting/interviews/INDEX.md`](../../Forecasting/interviews/INDEX.md) if applicable; update [`Forecasting/prep-plan.md`](../../Forecasting/prep-plan.md) checkboxes
   - GenAI: add session log row in [`GenAI/INDEX.md`](../../GenAI/INDEX.md); company table in [`GenAI/interviews/INDEX.md`](../../GenAI/interviews/INDEX.md) if applicable
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
  — or Amazon_SCOT/notes/YYYY-MM-DD_{topic}.md for SCOT track
  — or Forecasting/notes/YYYY-MM-DD_{topic}.md for Forecasting track
  — or GenAI/notes/YYYY-MM-DD_{topic}.md (or GenAI/interviews/...) for GenAI track
[Mock log: Amazon_FinTech/mocks/YYYY-MM-DD_{type}.md — if applicable]
Updated: [list paths]
Next session: [one item + @Files prompt]
```

## Principles (from compounding prep)

- Facts live in repo files; preferences live in AGENTS.md and skills
- **Amazon FinTech session debriefs → `Amazon_FinTech/debrief/`**
- **Amazon SCOT session debriefs → `Amazon_SCOT/notes/`**
- **Forecasting session debriefs → `Forecasting/notes/`** (company calls → **`Forecasting/interviews/`**)
- **GenAI session debriefs → `GenAI/notes/`** (company calls → `GenAI/interviews/`)
- **General profile/project references → `.cursor/skills/debrief/`**
- Corrections in session → debrief file → config update
- Do not leave learnings only in chat; session B should `@Files` the debrief
