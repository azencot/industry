# Mock — 2026-06-26 — ml-deep-dive (JD: LLM system choices)

## Setup

- Duration: ~20 min
- Focus: RAG vs FT vs CPT vs routing for finance docs; human-corrections follow-ups
- ML topics: retrieval/grounding, fine-tuning, continual pre-training, routing, RLHF/GRPO, preference vs factual feedback

## What went well

- Tiered eval instinct solid (gold → messy real → shadow; primary + guardrails + kill)
- Preference vs factual split (~85%): lighter interventions first (ICL/schema → short FT)
- Recovered well after corrections; ended ~85%

## What broke

- [ ] Technical gap: had RAG/CPT backwards (RAG = default for limited labels, not CPT)
- [ ] Technical gap: said FT gives best domain adaptation (it shapes behavior; CPT = domain language)
- [ ] Framing: jumped to RLHF/GRPO before treating corrections as eval/data asset
- [ ] Recurring: research-first instinct; interview wants eval-gate-first

## Corrections to promote

| Observation | Update where |
|-------------|--------------|
| RAG grounds / FT behavior / CPT domain language / routing cost-risk | debrief (memorize line) |
| Corrections → regression tests + taxonomy first, training signal later | debrief |
| Evidence-backed adjudication, not only LLM-judge, for finance facts | debrief |
| Lead with eval/data/guardrails before model technique | recurring — watch in Fri mock |

## Next session (one thing)

- Resume JD track at agent-failure Q3, then parallelism/scaling; practice eval-first framing.
