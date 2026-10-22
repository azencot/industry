# AGENTS.md — industry repo onboarding

Hand this to every new AI session working in this repo. Treat it like a day-one doc for a collaborator.

## Purpose

Industry prep workspace:

- **FinTech (FinTelligence)** — formal interview loop: recall under pressure, LP/STAR articulation, timed coding with narration
- **Forecasting** — general industry forecasting practice for AS roles (production, eval, tradeoffs); **not** SCOT
- **GenAI** — generative AI / LLM role interviews and prep, including multimodal / TSFM research-scientist roles; **not** forecasting-AS loops
- **ScientificML** — scientific ML / physical-AI principal applied scientist roles (simulation, operator learning, industrial time series); **not** forecasting-AS or GenAI loops
- **IndustrialResearch** — industry research-lab conversations (Apple AI Research, Meta research, and similar); **not** product AS loops
- **Talks** — dual-use HTML decks under [`talks/`](talks/) (Bosch cut now; community talks later); not company-loop notes
- **SCOT** — relationship / contribution prep (not a PS1 machine unless it becomes a formal loop)

Not a production app repo.

## Reading order

1. [`INDEX.md`](INDEX.md) — annotated map of the repo
2. Active track INDEX:
   - FinTech → [`Amazon_FinTech/INDEX.md`](Amazon_FinTech/INDEX.md)
   - Forecasting → [`Forecasting/INDEX.md`](Forecasting/INDEX.md) (week plan, notes, `/forecasting` drills)
   - GenAI → [`GenAI/INDEX.md`](GenAI/INDEX.md) (interviews, notes; GenAI roles only)
   - ScientificML → [`ScientificML/INDEX.md`](ScientificML/INDEX.md) (Siemens and similar scientific-ML loops)
   - IndustrialResearch → [`IndustrialResearch/INDEX.md`](IndustrialResearch/INDEX.md) (research-lab intros; Koltun / Ozan lives in [`IndustrialResearch/apple/`](IndustrialResearch/apple/); AIML DMLI / Nick Foti lives in [`IndustrialResearch/apple-dmli/`](IndustrialResearch/apple-dmli/); Meta lives in [`IndustrialResearch/meta/`](IndustrialResearch/meta/))
   - SCOT → [`Amazon_SCOT/INDEX.md`](Amazon_SCOT/INDEX.md) (contacts, collab, contribution pitch, questions)
3. [`.cursor/skills/debrief/omri_azencot_experience.md`](.cursor/skills/debrief/omri_azencot_experience.md) — experience profile, flagship project, IC framing (shared)
4. FinTech only: [`Amazon_FinTech/prep-plan.md`](Amazon_FinTech/prep-plan.md) — weekly plan; check today's focus
5. FinTech only: latest [`Amazon_FinTech/debrief/`](Amazon_FinTech/debrief/) or [`mocks/`](Amazon_FinTech/mocks/) when continuing that track
6. Forecasting only: [`Forecasting/prep-plan.md`](Forecasting/prep-plan.md); notes under [`Forecasting/notes/`](Forecasting/notes/); company prep under [`Forecasting/interviews/`](Forecasting/interviews/) (not GenAI/SCOT)
7. GenAI only: notes under [`GenAI/notes/`](GenAI/notes/); company prep under [`GenAI/interviews/`](GenAI/interviews/) (not under Forecasting)
8. ScientificML only: company prep under [`ScientificML/`](ScientificML/) (Siemens lives in [`ScientificML/Siemens/`](ScientificML/Siemens/); not under GenAI or Forecasting)
9. IndustrialResearch only: company prep under [`IndustrialResearch/`](IndustrialResearch/) (Koltun / Ozan lives in [`IndustrialResearch/apple/`](IndustrialResearch/apple/); AIML DMLI / Nick Foti lives in [`IndustrialResearch/apple-dmli/`](IndustrialResearch/apple-dmli/); Meta research lives in [`IndustrialResearch/meta/`](IndustrialResearch/meta/); not the Health AIML loop under GenAI)
10. SCOT only: [`contribution-plan.md`](Amazon_SCOT/contribution-plan.md) + [`mengfei-notes.md`](Amazon_SCOT/mengfei-notes.md) before Boris/Mengfei calls; session/post-call notes in [`Amazon_SCOT/notes/`](Amazon_SCOT/notes/) (SCOT debriefs live here, not under FinTech/Forecasting/GenAI/ScientificML)

## Behavior

- Be direct; push back if an approach is wrong for interview constraints.
- When unsure, say so — do not guess confidently.
- Keep diffs scoped to the task; no drive-by refactors of unrelated `code/` solutions.
- Prefer updating **existing** index/story/mock files over creating duplicate notes.
- **Never** add Cursor co-author trailers or attribution to git commits.

## Coding conventions (`code/`)

- Language: **Python 3**
- LeetCode style: `class Solution(object):` with problem statement in header comments
- Filenames: `{number}_{slug}.py`; `_practice` suffix = scratch attempt (keep both when learning)
- Live interview process: restate → clarify edge cases → approach + complexity → example → code → test
- Narrate **invariants** while coding (critical for Amazon Live Code)

## Behavioral / LP conventions

- **Positioning:** PI title reads managerial — prior loop feedback was "too managerial." Lead with hands-on IC work (see [`.cursor/skills/debrief/omri_azencot_experience.md`](.cursor/skills/debrief/omri_azencot_experience.md)); avoid grant/mentoring/roadmap stories at PS1
- Format: **DOC** ([`stories/README.md`](Amazon_FinTech/stories/README.md)) — Title · Outline · Ecosystem · Issue · Objectives · Actions · Results · Learnings; **L6: ~700–850 words body / ~8 min descriptive spoken**; apply **DOC AI checklist** in README after draft
- Say **"I"**, not "we" — interviewers probe individual contribution
- Include **metrics** (latency, F1, adoption, dollars, time saved)
- End with **what you learned**
- Priority LPs for this role: Customer Obsession, Ownership, Dive Deep, Deliver Results, Invent and Simplify, Earn Trust, Have Backbone, Learn and Be Curious

## IndustrialResearch interviews

From the 2026-10-20 call with Ozan Sener ([`IndustrialResearch/apple/2026-10-20_ozan-call.md`](IndustrialResearch/apple/2026-10-20_ozan-call.md)):

- A research interview in this loop goes to the **assumption** that makes the method work, and to **how it differs** from the nearby methods.
- Results are for when they are asked. Know the numbers. Do not open with the table for an interviewer working in this style.
- Do not predict the next interviewer from ethnicity. One call is one person. Have the numbers ready because someone else in the loop may want them.

## ML / FinTech talking points (default frame)

When discussing LLM systems for finance:

- Precision is a **compliance requirement**, not a nice-to-have
- Eval frameworks **gate** every model change before ship
- Tradeoffs: RAG vs fine-tuning vs continual pre-training vs routing to SLMs
- Low-label regimes: weak supervision, synthetic data (with privacy/quality risks), human corrections as training signal

## Skills

Load from [`.cursor/skills/`](.cursor/skills/) when the user invokes or the task matches:

| Skill | Trigger |
|-------|---------|
| `mock-lp` | LP / behavioral practice |
| `siemens-mock` | Siemens phone-screen mock; log in `ScientificML/Siemens/mocks.md` |
| `timed-code` | Timed LeetCode simulation |
| `ml-deep-dive` | ML/LLM technical depth practice |
| `follow-up-mock` | 15-min hard follow-up (mid-conversation; Yujie / Chung-Cheng / on-site) |
| `forecasting` | Industry forecasting system design / tradeoff drills |
| `debrief` | Post-mock or post-interview write-up |
| `log-timed-drill` | Logging a finished timed-code result to INDEX + prep-plan |
| `commit-push` | User asks to commit and/or push |

## Git

- Author email (this repo): `aizencot@gmail.com` — must match a verified GitHub email for contribution graph
- Remote: `git@github.com:azencot/industry.git`
- Use skill **`commit-push`** for all agent commits (avoids `--trailer` failures on older git)
- Do **not** update git config
- Push only when the user asks

## After substantial work

Run **`/debrief`** or at minimum:

- Update [`INDEX.md`](INDEX.md) timed log or relevant index entry
- Append mock notes if applicable
- Promote repeated corrections into this file or a skill
