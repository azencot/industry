---
name: ml-deep-dive
description: >-
  Practice ML/LLM technical answers for Amazon FinTech interviews: 3-minute
  spoken responses and follow-up Q&A. Use when the user invokes /ml-deep-dive
  or prepares generative AI, eval, RAG, or production ML talking points.
---

# ML deep dive (FinTech)

## When to use

Technical portion of PS1 for Senior Applied Scientist, FinTelligence. Align with [`AGENTS.md`](../../AGENTS.md) ML frame and [`Amazon_FinTech/INDEX.md`](../../Amazon_FinTech/INDEX.md) role summary.

## Workflow

1. **Pick topic** — user chooses or rotate:
   - End-to-end LLM system you shipped
   - Eval framework that gates model releases
   - Low-label / weak supervision / synthetic data
   - RAG vs fine-tuning vs continual pre-training (finance docs)
   - Tiered inference / model routing / cost at scale
   - Agents for finance workflows (guardrails, audit, abstention)
   - Document IE / NER for payments or cash application
   - Failure in production and how you debugged it
2. **Prompt user** — "You have 3 minutes. Go." (or draft from their project notes if they provide bullets).
3. **Score** (brief):
   - [ ] Clear problem + **your** role
   - [ ] Architecture/data/model/eval/deploy mentioned
   - [ ] **Metrics** and tradeoffs
   - [ ] FinTech angle: precision, compliance, scale
   - [ ] Not over-indexed on research without shipping
4. **Follow-ups** — ask 2–3 interviewer probes, e.g.:
   - "How do you know it's safe to reduce human review?"
   - "What would you measure in shadow mode?"
   - "When would synthetic data hurt you?"
5. **Full reference answer** — ~90s spoken bullets (not gaps-only); user learns by comparing, not reconstructing.
6. **Optional retake** — user re-answers once; score delta only.
7. **Persist** — run `/debrief` → `Amazon_FinTech/debrief/` (and `mocks/` if treated as a drill).

Day 2 reference answers: [`2026-06-21_day2-ml-depth.md`](../../Amazon_FinTech/debrief/2026-06-21_day2-ml-depth.md).

## Default answer skeleton

```
Problem & stakes (finance, scale, compliance)
→ Data & constraints (messy, regulated, limited labels)
→ Approach (model, routing, human loop)
→ Eval & gating (offline + online, regression detection)
→ Result (metrics, adoption, cost)
→ Lesson / what you'd do next
```

## Reference reading (interviewer-aligned)

- [Continual pre-training for financial LLMs](https://aws.amazon.com/blogs/machine-learning/efficient-continual-pre-training-llms-for-financial-domains/)
- [ECG-QALM synthetic NER data](https://www.amazon.science/publications/ecg-qalm-entity-controlled-synthetic-text-generation-using-contextual-q-a-for-ner)

## Do not

- Give textbook-only answers with no production or eval detail
- Recommend expensive frontier-only stacks without frugality tradeoffs
