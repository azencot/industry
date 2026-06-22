---
name: mock-lp
description: >-
  Run Amazon Leadership Principle behavioral drills using STAR format. Use when
  the user practices LP questions, behavioral interview prep, STAR stories, or
  invokes /mock-lp for Amazon FinTech prep.
---

# Mock LP (Leadership Principles)

## When to use

Behavioral prep for Amazon interviews. Default context: [`Amazon_FinTech/stories/`](../../Amazon_FinTech/stories/) and [`AGENTS.md`](../../AGENTS.md).

## Workflow

1. **Pick LP** — user names one, or choose from PS1 priority list in `Amazon_FinTech/stories/README.md`.
2. **Check existing story** — read matching file in `stories/` if present; offer to refine vs draft new.
3. **Use DCC template** — [`Amazon_FinTech/stories/README.md`](../../Amazon_FinTech/stories/README.md): Title · Outline · Ecosystem · Issue · Objectives · Actions · Results · Learnings.
4. **Ask question** — use a realistic Amazon prompt, e.g.:
   - "Tell me about a time you dove deep to find the root cause of a problem."
   - "Describe a situation where you disagreed with an engineer or PM."
   - "Tell me about delivering results under a tight deadline with imperfect data."
5. **User answers** (or user asks you to draft from their bullets).
6. **Critique** using DCC quality bar in [`stories/README.md`](../../Amazon_FinTech/stories/README.md):
   - [ ] **L6 length** — ~800–900 words body, **~6–7 min** spoken (L5 is too thin)
   - [ ] **Alternatives considered** — paths rejected with reason
   - [ ] **Influence** — aligned team/stakeholders with data, not authority
   - [ ] **Ownership** early — role, what *I* owned vs collaborators
   - [ ] **Concrete before** — baseline pain, operational not just technical
   - [ ] **Friction** — ≥1 failed path or tuning struggle
   - [ ] **De-risk loop** — how representation/risk was validated
   - [ ] **Causal results** — which action drove which metric
   - [ ] Says **"I"**; metrics; lesson; plain English for jargon once
   - [ ] No self-labels ("core Invent move"); FinTech bridge optional
7. **Iterate** — one revision pass; tighten **~6–7 min spoken script** (keep 90s backup).
8. **Persist** — save or update `Amazon_FinTech/stories/{lp-slug}_{title}.md` using full DCC sections; mark LP ready in `stories/README.md` table.

## Output format

```markdown
## Question
[LP prompt]

## Your answer (STAR)
...

## Critique
- Strong:
- Fix:

## Revised answer (90 sec)
...

## Saved to
[path]
```

## Do not

- Invent projects the user never described — ask for bullets first
- Write generic "we delivered successfully" stories
