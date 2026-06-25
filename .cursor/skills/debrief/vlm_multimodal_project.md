# Time-Series Vision-Language Models — project summary

**Long-lived reference.** Extend this file as the project evolves — new results, problems solved, ablations, interview angles.  
**Interview cheat sheet:** [`Amazon_FinTech/anchor-cheat-sheet.md`](../../Amazon_FinTech/anchor-cheat-sheet.md)  
**Experience profile (broader arc):** [`omri_azencot_experience.md`](omri_azencot_experience.md)

Last updated: 2026-06-21

---

## Overview

**Goal:** Teach general-purpose VLMs to reason over univariate and multivariate time series — not just classify UCR shapes, but answer exam-style questions, forecast, explain temporal relations, and generate structured captions.

**North star benchmark:** [TSRBench](https://tsrbench.github.io/) — multi-task, multi-modal time series reasoning (15 tasks across 4 dimensions: Perception, Reasoning, Prediction, Decision-Making; 4,125 problems from 14 domains including finance). TSRBench evaluates both textual and visual TS representations; text and vision are strongly complementary per the benchmark authors.

**Supporting benchmarks:** TSExam (20K MCQ + 746-item HF eval), TSExam-numeric (11K regression), ChatTS (105K align + 44K SFT), caption data (7.7K), ICL-UCR, CaTS-Bench (~16K), TSRBench JSONL (12-task MCQ north-star subset).

**Intellectual lineage:** ImagenTime (NeurIPS 2024) established that rendering time series as images unlocks vision-model advances; this project extends that insight from *generation* to *reasoning* via VLMs.

---

## Core insight

LLMs do not understand raw time-series values efficiently — feeding numeric tokens is wasteful and weak on structure.

**Dual representation hypothesis:** A single rendering loses information.

| Encoding | Captures | Route |
|----------|----------|-------|
| **Line chart** (matplotlib) | Amplitude, trend, local shape | Frozen native Qwen ViT (`visual`) |
| **Delay-embedding plot** | Topological / dynamical structure | DINOv3 + trainable merger (`visual_dino`) |

Both streams are projected into LLM token space and fused for downstream tasks (MCQ, regression, captioning, open QA).

**Design principle:** Decouple *how to see* a series from *how to answer* about it — enables caption/alignment priors to transfer to downstream QA (same pattern as domain pre-training → task fine-tuning on finance docs).

---

## Architecture

```
Time series input
    ├── line chart ──────────→ Qwen native ViT (frozen) ──→ projector ──┐
    │                                                                    ├──→ LLM (LoRA in Stage B)
    └── delay-embedding image → DINOv3 + merger (LoRA in Stage A) ──→ projector ──┘
```

**Model integration (personal ownership):**

- Patched forwards for **Qwen3-VL-8B** and **Qwen3.5-0.8B (Q35)**
- Custom **DinoVisionTower** for delay-embedding stream
- **Dual-stream collator** with M-RoPE type tags (Q35)
- **Adapter merge/resume** across curriculum stages (Stage A weights → Stage B init)

**Scale strategy:** Validate ideas on **0.8B Q35** first (~15 min pilot runs); compare against **8B ceiling** before committing full sweeps.

---

## Training curriculum

| Stage | What trains | LLM updates? | Purpose |
|-------|-------------|--------------|---------|
| **A** | DINO backbone (LoRA) + alignment merger on caption/align data | **No** | Learn *how to see* a series |
| **B** | Merge Stage A; add LM LoRA (+ optional DINO LoRA); merger often frozen | **Yes** (LM LoRA) | Learn *how to answer* |
| **C** *(in progress)* | GRPO / VRT — gold-based RL on SFT adapters | RL on LoRA | CoT correctness rewards on gold labels |

### Stage A data sources (evolution)

0. **Baseline failure:** instruction-following only (no captions) — **50+ configs**, TSExam stuck at **~61.8%**; zero-shot TS-image perception insufficient.
1. **Synthetic TS↔text alignment:** adapted TSExam + ChatTS generators — compose captions from **per-series gold features** (no LLM; template + randomization).
2. **CaTS** (Rose Yu group): expert-audited domains (traffic, electricity, etc.); LLM trained on **~1.6K** audited seeds → **~16K** caption repo for messy real-world signal.
3. **Stage A mix:** TSExam + ChatTS synthetic captions + CaTS → perception lift → TSExam **~90.5%** on recent 8B stack.

### Stage B data mix

Mostly QA: TSExam MCQ, ChatTS SFT, TSExam-numeric regression, small caption holdout to avoid forgetting.

**Caption-transfer hypothesis (active arc):** Stage A descriptive captions (ChatTS align, CaTS, aligned captions) → Stage B on TSExam/TSRBench. Achieved **0.88 TSExam HF** with caption priors; probing whether linguistic structure helps temporal reasoning on TSRBench (north star still ~0.32–0.34 on 0.8B vs ~0.45 on 8B).

**Control baseline (Jun 2025):** `allcap-a5b3` — TSExam 0.854, TSRBench 0.339, TR 28.7%.

---

## Technical scope — what I built

| Area | Details |
|------|---------|
| **Training** | PyTorch DDP (`torchrun`, 8× RTX Pro 6000); LoRA via PEFT (~43M–few-hundred-M trainable params); stratified multi-task samplers; YAML-config-first sweeps (**162 configs**, **125 scripts**) |
| **Data pipeline** | Unified loaders across TSExam, TSExam-numeric, caption, ChatTS, ICL-UCR, CaTS-Bench, TSRBench JSONL; stratified balancing; leave-one-out ablations (e.g. drop caption bucket → +3 pp TSExam) |
| **Eval harness** | Tiered gates per checkpoint: **loss** (free) → **TSExam** (~35 s) → **176-item TSRBench slice** (~12 s) → **full TSRBench** (~3 min 0.8B / ~5 min 8B, 8-GPU). Per-task/per-group accuracy; **parse-miss** (non–single-letter MCQ output) separate from accuracy — surfaced **NR** / **TSF** format gaps. HF + local parity. |
| **Fast train screen** | Capped subset (~10K, 2 epochs) on Q35 for data-mix screening — distinct from eval gate ladder above |
| **RL** | GRPO on Qwen3-VL-8B (TRL + DeepSpeed); warm-started from SFT adapters; rule-based MCQ correctness rewards |
| **Infra** | Slurm submission; `QTSX_ARTIFACT_ROOT` artifact separation; dual venvs (torch 2.4/8B vs 2.11/Q35); NCCL tuning (P2P disable on heterogeneous nodes); agent/onboarding automation for repeatable train/eval workflows |
| **Reproducibility** | Fixed samplers (post bug-fix), seed control, artifact paths, documented eval protocol fixes (e.g. deductive-reasoning option parsing) |

---

## Experimentation methodology

Amazon-relevant habits embedded in the stack:

1. **Config-first** — one hypothesis per change; fork YAML, not training code; parallel Slurm sweeps
2. **Tiered eval gates** — loss → TSExam → TSRBench slice → full north star (see latencies in eval harness)
3. **Parse-miss ≠ accuracy** — track schema/reliability separately (production analog: doc parsing failures)
4. **Multi-scale validation** — 0.8B first, 8B as ceiling reference
5. **Living experiment index** — ~160 configs documented for reproducibility and handoff

---

## Results

| Benchmark | Task | Best Q35 (0.8B) | Best 8B | Notes |
|-----------|------|-----------------|---------|-------|
| **TSExam HF** | 746-item MCQ (AutonLab) | **0.890** (tsexam-v2 repro) | **0.901** (unified champion) | Tiered eval sanity check |
| **TSRBench reasoning** | Reasoning bracket (0.8B) | **0.245→0.255** (+1.0 pp) | — | vs `stageb-weak11k`; + audit data + Stage C (`reason-stageC-weak11k`) — prelim |
| **TSRBench overall** | 12-task MCQ north star | **0.382→0.405** (+2.3 pp) | 0.374 (capnum-a8b4) | 0.8B audit path prelim; 8B best **0.454** (capnumicl-a8b4) |
| **TSRBench TR** | Temporal-relation reasoning (160 items) | 0.287 (allcap control) | — | Hard problem; in progress |
| **TSExam-numeric** | Regression (medAE) | **0.14** (unified3) | — | Numeric correctness |
| **Caption attr-recovery** | 9-field macro accuracy | **0.72** (caption specialist) | — | Field extraction analog |
| **ChatTS** | Free-text QA (cat/num/reason) | — | ~0.84 cat / 0.76 num | 8B path |

**Headline for intro:** Open **8B** scores **~46% overall on TSRBench** — strongest open-source model at that scale, just below frontier proprietary systems orders of magnitude larger. TSExam ~90% is internal eval discipline, not the external hook.

---

## Negative results (show rigor)

### TR / reasoning bucket mixes regressed

Subset-mix experiments targeting temporal-relation and reasoning buckets **performed worse than control** → stopped additive buckets; pivoted to revisiting **data generation** rather than stacking more training mixes.

**Lesson:** More data buckets ≠ better when task distribution shifts. Same discipline needed before shipping to finance users.

### Stage B over-reasoning on complex TSRBench tasks

TSRBench reasoning tasks are domain-specific and multi-hop — they combine basic TS analysis (value extraction, segmentation) with higher-level inference. Model sometimes over-reasons or fails on primitives.

**Diagnosis (Jun 2025):** Task-level audit revealed **missing operations** in training/eval coverage — not insufficient volume alone. Response: extended TSExam to support identified operations rather than blindly adding data buckets.

---

## Problems solved — detailed log

*Add new entries at the top as work progresses.*

### 2026-06 — TSRBench task audit + Stage C (reasoning bracket)

**Problem:** Blind TR/reasoning mixes regressed TR (−5 pp) — see Ownership kill.

**Action:** Manual audit of all TSRBench reasoning tasks → three regimes (operator depth · domain knowledge defer · format/convention). Rebuilt reasoning synthetic repo; per-task TSExam generators (TR segmentation/ordering, NR value→formula, Goldstein-scale format synthetics, etc.). Adapted Stage B + Stage C (VRT/GRPO on gold CoT).

**Result (0.8B prelim vs `stageb-weak11k`):** TSRBench overall **0.382→0.405 (+2.3 pp)**; reasoning **0.245→0.255 (+1.0 pp)**. 8B WIP.

**Interview angle:** Anchor C — instrument before scaling data.

---

### 2025-06 — Stage B reasoning gaps (TSRBench task audit)

**Problem:** Stage B QA fine-tuning underperformed on TSRBench reasoning slices despite decent TSExam scores. Over-reasoning on complex multi-hop tasks.

**Action:** Spent several days on TSRBench task taxonomy — mapped required primitives (val extraction, segmentation, multi-hop decisions alongside basic TS analysis). Identified operations absent from TSExam training coverage. Extended TSExam to support these operations.

**Status:** In progress — probing whether coverage fix improves TSRBench TR without hurting TSExam transfer.

**Interview angle:** Anchor C (Dive Deep) — instrument tasks before adding data.

---

### 2025-06 — Synthetic captions too basic (CaTS integration)

**Problem:** Synthetic TS↔text alignment from TSExam + ChatTS unlocked Stage A training but captions lacked richness for robust perception.

**Action:** Integrated **CaTS-Bench** (~16K samples) into Stage A mix.

**Result:** Strong Stage A eval on next-token prediction and TSExam perception slices.

**Interview angle:** Synthetic data quality risk — augment with curated real data when synthetic ceiling hits (Karan's ECG-QALM lane).

---

### 2025-06 — Caption data scarcity (synthetic alignment generation)

**Problem:** Real time-series caption data insufficient for Stage A alignment (LLaVA-style TS↔text pairing).

**Action:** Generated synthetic alignment data from TSExam + ChatTS templates/pipelines.

**Result:** Enough volume to train Stage A vision alignment without LLM updates.

**Interview angle:** Low-label regime — synthetic bootstrap with quality caveats.

---

## FinTech bridges

| Research concept | FinTech parallel |
|------------------|------------------|
| Dual chart + delay encoding | Multimodal docs: tables + text + numbers; one view loses information |
| Two-stage curriculum (caption → QA) | Domain alignment → task fine-tuning on invoices, remittance, filings |
| Caption 9-field attr-recovery (0.72) | Entity/field extraction from documents |
| TSExam-numeric medAE 0.14 | Numeric correctness for payment matching |
| Tiered eval + parse-miss tracking | Slice metrics by doc/entity type; schema reliability before accuracy |
| 0.8B near 8B on TSExam (0.890 vs 0.901) | SLM routing when quality holds; cost at transaction scale |
| Negative TR bucket mixes | Don't cargo-cult data before shipping to finance users |
| Extended TSExam ops | Cover extraction/segmentation primitives the benchmark actually tests |
| Synthetic + CaTS caption pipeline | Controlled synthetic text for NER/IE with quality gates |

### Production bridge (not yet built — show thinking)

> Shadow eval before promote; confidence/abstention when parse-miss spikes; slice regressions by task group; human review queue for low-confidence outputs; user corrections → golden-set refresh → gated retrain.

---

## PS1 interview hooks

**One project, three anchors** — see [`anchor-cheat-sheet.md`](../../Amazon_FinTech/anchor-cheat-sheet.md).

| Anchor | Theme | Lead with |
|--------|-------|-----------|
| **A** | Production ML/LLM | Dual-tower, Stage A/B curriculum, DDP stack, 0.890 on 0.8B |
| **B** | Eval / monitoring | Tiered eval, pilot harness, parse-miss, killed TR mixes |
| **C** | Dive Deep / ambiguity | Caption pipeline + TSRBench task audit → extended TSExam |

**5–7 min ML deep-dive order:**

1. Problem (30s): VLMs fail exam-grade TS reasoning
2. Insight (30s): Dual encodings; Stage A decouples vision from language
3. System (60s): What *I* built — patch, collator, YAML sweeps, Slurm DDP
4. Win (30s): TSExam 0.89 on 0.8B *or* TSRBench ~46% open 8B
5. Honest limit (30s): TR mixes regressed; Stage B reasoning gaps
6. FinTech bridge (30s): Multimodal docs, field extraction, eval-gated ship

**Karan resonance:** eval methodology, curriculum/domain adaptation, low-label caption transfer, negative results from bad data mixing — mirrors his [continual pre-training for financial LLMs](https://aws.amazon.com/blogs/machine-learning/efficient-continual-pre-training-llms-for-financial-domains/) and [ECG-QALM synthetic NER](https://www.amazon.science/publications/ecg-qalm-entity-controlled-synthetic-text-generation-using-contextual-q-a-for-ner) work.

**Anti-patterns (prior loop):** Don't lead with "research program" or mentorship — say "I implemented the tiered eval harness" / "I designed the dual-tower stack."

---

## Stack

Python 3.11 · PyTorch 2.4 (8B) / 2.11 (Q35) · Transformers 4.57 / 5.10 · PEFT/LoRA · TRL (GRPO) · Accelerate/DeepSpeed · HuggingFace datasets · Slurm · 8× GPU DDP

---

## Open questions

- [ ] Exact TSRBench leaderboard rank for open 8B before PS1 — verify on [tsrbench.github.io](https://tsrbench.github.io/)
- [ ] Does extended TSExam ops coverage improve TSRBench TR without TSExam regression?
- [ ] Stage C GRPO/VRT — timeline and expected gain on MCQ vs reasoning slices
- [ ] Caption-transfer: does Stage A linguistic structure help TR on TSRBench at 0.8B scale?

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-21 | Initial extended summary — architecture, curriculum, results, Stage A/B problems solved, three anchors |
