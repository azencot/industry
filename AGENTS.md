# AGENTS.md — industry repo onboarding

Hand this to every new AI session working in this repo. Treat it like a day-one doc for a collaborator.

## Purpose

Interview prep workspace for **Amazon FinTech Senior Applied Scientist** (FinTelligence). Not a production app repo — optimize for **recall under pressure**, **articulation** (ML + STAR stories), and **timed coding with narration**.

## Reading order

1. [`INDEX.md`](INDEX.md) — annotated map of the repo
2. [`Amazon_FinTech/INDEX.md`](Amazon_FinTech/INDEX.md) — active role, timeline, interviewer context
3. [`.cursor/skills/debrief/omri_azencot_experience.md`](.cursor/skills/debrief/omri_azencot_experience.md) — experience profile, flagship project, JD alignment, IC framing
4. [`Amazon_FinTech/prep-plan.md`](Amazon_FinTech/prep-plan.md) — weekly plan; check today's focus
5. Latest [`.cursor/skills/debrief/`](.cursor/skills/debrief/) entry when borrowing context from a prior session
6. Latest [`Amazon_FinTech/mocks/`](Amazon_FinTech/mocks/) entry if continuing mock-drill follow-up

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
- Format: **DCC** ([`stories/README.md`](Amazon_FinTech/stories/README.md)) — Title · Outline · Ecosystem · Issue · Objectives · Actions · Results · Learnings; **L6: ~800–900 words / ~6–7 min spoken**; L7 leverage beats where true
- Say **"I"**, not "we" — interviewers probe individual contribution
- Include **metrics** (latency, F1, adoption, dollars, time saved)
- End with **what you learned**
- Priority LPs for this role: Customer Obsession, Ownership, Dive Deep, Deliver Results, Invent and Simplify, Earn Trust, Have Backbone, Learn and Be Curious

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
| `timed-code` | Timed LeetCode simulation |
| `ml-deep-dive` | ML/LLM technical depth practice |
| `debrief` | Post-mock or post-interview write-up |
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
