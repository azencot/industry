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
3. **Ask question** — use a realistic Amazon prompt, e.g.:
   - "Tell me about a time you dove deep to find the root cause of a problem."
   - "Describe a situation where you disagreed with an engineer or PM."
   - "Tell me about delivering results under a tight deadline with imperfect data."
4. **User answers** (or user asks you to draft from their bullets).
5. **Critique** using checklist:
   - [ ] STAR structure clear
   - [ ] Says **"I"**, not "we" — individual actions explicit
   - [ ] At least one **metric** or concrete outcome
   - [ ] Shows tradeoff or mistake, not perfection
   - [ ] Ends with **lesson learned**
   - [ ] Fits **FinTech / ML production** context when possible
6. **Iterate** — one revision pass; tighten to ~90 seconds spoken.
7. **Persist** — save or update `Amazon_FinTech/stories/{lp-slug}_{title}.md`; mark LP ready in `stories/README.md` table.

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
