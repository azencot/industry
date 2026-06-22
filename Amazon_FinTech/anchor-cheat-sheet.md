# PS1 anchor cheat sheet — VLM time-series reasoning

**One project, three angles.** Read before PS1 intro / ML deep-dive / LP follow-ups.  
Full context: [`.cursor/skills/debrief/vlm_multimodal_project.md`](../.cursor/skills/debrief/vlm_multimodal_project.md)

North star: [TSRBench](https://tsrbench.github.io/) · Control: allcap-a5b3 (TSExam 0.854, TSRBench 0.339, TR 28.7%)

---

## Anchor A — Production ML/LLM system

| | |
|---|---|
| **Problem** | General VLMs can't do exam-grade time-series reasoning (MCQ, numbers, temporal relations). |
| **Insight** | Raw TS tokens are inefficient; dual visual encodings (chart + delay embedding) fused into one LLM. |
| **What I built** | Patched Qwen3-VL-8B & Qwen3.5-0.8B forwards; DinoVisionTower; dual-stream collator + M-RoPE tags; two-stage curriculum (Stage A: vision alignment, Stage B: LM LoRA); YAML-config sweeps (162 configs); DDP on 8× GPU via Slurm. |
| **Metrics** | TSExam HF **0.890** (0.8B) vs **0.901** (8B); caption attr-recovery **0.72** macro. |
| **JD map** | End-to-end ML systems; tiered models (0.8B ≈ 8B on TSExam); multimodal finance docs analogy. |
| **Honest limit** | TSRBench overall still gap vs frontier (~0.45 8B vs proprietary trillion-scale). |
| **Lesson** | Decouple *how to see* (Stage A) from *how to answer* (Stage B) — same pattern as domain alignment → task FT on finance docs. |
| **LPs** | Invent & Simplify, Deliver Results, Ownership |

**90s spoken:** Goal → dual encoding → two-stage curriculum → I built stack (patch, collator, sweeps) → 0.89 on 0.8B near 8B ceiling.

---

## Anchor B — Eval / monitoring / gating

| | |
|---|---|
| **Problem** | Full TSRBench runs are expensive; headline accuracy hides slice regressions and parse failures. |
| **Insight** | Treat eval like a release gate — cheap sanity before north star; track parse-miss separately from accuracy. |
| **What I built** | Tiered eval (loss → TSExam subset → TSRBench subset → full); per-task/per-group accuracy; parse-miss logging; pilot harness (~15 min, TSExam ±0.3 pp noise floor); HF + local dataset parity checks. |
| **Metrics** | TSRBench overall **0.454** (8B best); killed TR bucket mixes that regressed vs control (TR ~29%). |
| **JD map** | Eval frameworks that **gate** model changes; slice metrics by task group (→ doc type / entity type in FinTech). |
| **Honest limit** | TR reasoning still hard (~29%); additive data buckets made it worse, not better. |
| **Lesson** | More training mix ≠ better when task distribution shifts — stop and fix data generation. |
| **LPs** | Ownership, Earn Trust, Dive Deep, Have Backbone |

**90s spoken:** I owned eval harness → tiered gates → found TR mixes regressed → killed them → would shadow-eval + slice metrics before ship in production.

---

## Anchor C — Ambiguity / Dive Deep (data + task diagnosis)

| | |
|---|---|
| **Problem** | Stage A lacked captions; Stage B over-reasoned on complex TSRBench tasks (domain-specific, multi-hop). |
| **Insight** | Gaps were *missing operations* in training/eval coverage, not just insufficient data volume. |
| **What I built** | (1) Synthetic TS↔text alignment from TSExam + ChatTS for Stage A; (2) added CaTS ~16K for richer captions; (3) task-level TSRBench audit → extended TSExam with missing ops (val extraction, segmentation, multi-hop primitives). |
| **Metrics** | Stage A: strong next-token + TSExam perception after CaTS; Stage B reasoning still in progress (TSRBench 0.339 control → probing caption-transfer). |
| **JD map** | Low-label / synthetic data (with quality risk); learning from structured corrections; messy domain-specific reasoning. |
| **Honest limit** | Synthetic captions are basic without CaTS; Stage B reasoning not solved yet. |
| **Lesson** | When progress stalls, instrument tasks before adding data — same as debugging a stalled experiment (SKD story). |
| **LPs** | Dive Deep, Learn and Be Curious, Customer Obsession (if framed as "what users/exam actually need") |

**90s spoken:** Caption scarcity → I generated alignment data + added CaTS → Stage A fixed → Stage B still weak on TSRBench reasoning → I audited tasks, found missing ops → extended TSExam instead of stacking buckets.

---

## Quick numbers (memorize)

| Metric | Value |
|--------|-------|
| TSExam HF Q35 / 8B | 0.890 / 0.901 |
| TSRBench overall Q35 / 8B | 0.374 / 0.454 |
| TSRBench TR | ~29% (hard, in progress) |
| TSExam-numeric medAE | 0.14 |
| Caption attr-recovery | 0.72 |
| Configs / scripts | 162 / 125 |
| Pilot detectability | TSExam ±0.3 pp in ~15 min |

---

## FinTech one-liners (bridge any anchor)

| Research | FinTech |
|----------|---------|
| Dual chart + delay encoding | Tables + text + numbers — one view loses information |
| Stage A → B curriculum | Domain alignment → task FT on invoices / remittance |
| Tiered eval + parse-miss | Slice by doc type; schema reliability before accuracy |
| 0.8B ≈ 8B on TSExam | SLM routing when quality holds |
| Killed bad TR mixes | Don't cargo-cult data before shipping to finance users |
| Extended TSExam ops | Cover field extraction / segmentation primitives exams actually test |

---

## Supporting LP stories (not anchors)

| LP | Story | Status |
|----|-------|--------|
| Invent & Simplify | ImagenTime — [`stories/invent-simplify_imagentime.md`](stories/invent-simplify_imagentime.md) | Draft v2 DCC L5 |
| Dive Deep | SKD setup-bug debug **or** Anchor C TSRBench audit | Reframe SKD; Anchor C ready |
| Customer Obsession | **Gap** | Need stakeholder/user story |

---

## If Karan pulls a thread

| Question | Point to |
|----------|----------|
| "Walk me through architecture" | Anchor A — dual tower, Stage A/B |
| "How do you know it's ready to ship?" | Anchor B — tiered eval, parse-miss, negative TR |
| "What failed recently?" | Anchor B (TR mixes) + Anchor C (over-reasoning) |
| "Low labels / synthetic data?" | Anchor C — synthetic align + CaTS + quality caveats |
| "RL?" | GRPO warm-started from SFT, MCQ rewards; Stage C VRT planned |
| "Why Amazon / FinTech?" | Elevator pitch — precision, eval gates, peer scientists at scale |
