# Debrief — 2026-06-26 — JD drill: LLM system choices (RAG/FT/CPT/routing)

## Session

- **Type:** mock (JD technical, ml-deep-dive style) — evening drill
- **Duration:** ~20 min
- **Prior context:** [`2026-06-26_coding-and-jd-technical.md`](2026-06-26_coding-and-jd-technical.md) (JD track Q1/Q2); same-day LP mock

## Conclusions

JD technical drill on RAG vs fine-tuning vs continual pre-training vs routing, then human-corrections follow-ups. Started ~70%, ended ~85% after corrections.

### Two corrections that must stick (got these backwards first)
- **RAG is the default when labels are limited** (ground on docs/records without training) — NOT continual pre-training. First answer had this inverted.
- **Fine-tuning shapes task behavior, not broad domain knowledge.** Best domain *language/style* = CPT; best *grounding* = RAG; best *behavior/format* = FT.

### Memorize sentence
> RAG grounds facts, fine-tuning shapes behavior, continual pre-training teaches broad domain language, and routing manages cost-risk tradeoffs.

### Human corrections (Q-follow-up) — strong instinct, fix the order
- First answer jumped straight to RLHF/GRPO. **Fix:** corrections become a **data/eval asset first** — failure taxonomy (retrieval / extraction / reasoning / policy / ambiguity) → regression tests + slice metrics → fix the failing component → only *then* preference optimization.
- Memorize: *Human corrections should first become regression tests and a failure taxonomy; only some become training signal.*

### Preference vs factual feedback — landed ~85%
- Good: separated factual error vs format/preference; lighter interventions first (ICL/schema → short FT only if consistent + enough data).
- **Fix:** don't rely only on LLM-as-judge for finance facts → evidence-backed adjudication (source records, deterministic checks, human audit on high severity). Distinguish per-user vs global preference before retraining.
- Memorize: *Factual corrections go into regression and safety gates; preference corrections go into prompts, schemas, or workflow personalization.*

## Recurring theme (3rd time today)
Strong on **modeling/RL mechanisms**, under-weights **production/eval-first framing**. Same pattern as A/B drill (precision-as-primary) — instinct is research-first; interview wants eval-gate-first. Lead with eval/data/guardrails, then the model technique.

## Decisions / artifacts updated
- [x] prep-plan.md — Fri 26 evening drill logged
- [x] This debrief + mock log [`mocks/2026-06-26_jd-llm-system-choices.md`](../../Amazon_FinTech/mocks/2026-06-26_jd-llm-system-choices.md)
- [x] INDEX.md debrief + mock rows

## Open questions
- Q3 agent-failure (from afternoon JD mock) still unanswered.

## Next session (one prompt for session B)
> Read `@Files .cursor/skills/debrief/2026-06-26_llm-system-choices-drill.md`. Resume JD track: answer the unanswered agent-failure Q3, then parallelism/scaling. Practice leading every answer with eval/data/guardrails before the model technique.
