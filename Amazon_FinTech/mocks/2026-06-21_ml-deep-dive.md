# Mock — 2026-06-21 — ml-deep-dive

## Setup

- **Duration:** ~60 min
- **Focus:** Day 2 ML/LLM depth — RAG/FT/CPT, eval gating, NER/low labels
- **Topics covered:** Topic 1 (+ blog pushback, invoice/SEC follow-up); Topic 2 (+ amount-precision + shadow follow-ups); Topic 3 (full answer)

## What went well

- Strongest on **Topic 3** — task audit → missing ops → synthetic path maps cleanly to Anchor C
- Correct **no-ship** instinct when compliance-critical slice regresses
- **OCR/parse vs model** separation — production-minded, aligns with Anchor B parse-miss logging
- Engaged with blog quote on CPT — corrected framing to **limited labels + domain corpus**

## What broke

- [x] **Verbal / structure:** Topic 1–2 missing IC voice ("I built"), metrics, FinTech slice vocabulary
- [x] **Technical gap:** CPT trigger conflated with generic "scarce data"; "large data → RAG/FT" overstated; CPT→SFT→RAG overkill for single-field fix
- [ ] **LP story weak:** N/A this drill

## Scores

| Topic | Score | Notes |
|-------|-------|-------|
| RAG/FT/CPT | 70 (after correction) | Two-axis framing landed |
| Eval + corrections | 60 | Needs retake with reference bullets |
| NER/low labels | 78 | Say ECG-QALM by name in PS1 |

## Corrections to promote

| Observation | Update where |
|-------------|--------------|
| User needs full reference answer + optional retake, not gaps-only feedback | `ml-deep-dive/SKILL.md` |
| CPT = limited **labels** + large **unlabeled** corpus | This debrief + blog debrief |
| Block ship on compliance slice; don't CPT for one field | This debrief |
| Interactive practice > passive reading | Session workflow confirmed |

## Next session (one thing)

One **spoken drill** from prep-plan line 19 (*safe deploy* recommended) — 3 min aloud with retake.
