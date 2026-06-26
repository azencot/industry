# Omri Azencot — experience & expertise (FinTelligence)

Session debrief compiled 2026-06-21. Canonical reference for resume walkthrough, ML deep-dive, and story framing for **Senior Applied Scientist, FinTelligence** (PS1: Karan Aggarwal, 30 Jun 2026).

Sources: [`CV_Azencot_10399493.pdf`](../CV_Azencot_10399493.pdf), VLM project brief, [Google Scholar](https://scholar.google.com/citations?user=MEGuRmAAAAAJ&hl=en), prep-session analysis.

---

## Identity & positioning

| | |
|---|---|
| **Name** | Omri Azencot |
| **Contact** | aizencot@gmail.com · [github.com/azencot-group](https://github.com/azencot-group) · [omriazencot.com](http://omriazencot.com) |
| **Status** | US Permanent Resident (Green Card) |
| **Education** | Ph.D. CS, Technion (2011–2017); B.Sc. CS & Math, Technion (2005–2010) |
| **Current roles** | PI & Senior Scientist, Ben-Gurion University (2020–); Research Affiliate, ICSI Berkeley (2025–) |
| **Prior** | Assistant Adjunct Professor, UCLA (2017–2020) |
| **Publications** | 40+ in NeurIPS, ICML, ICLR |

### How to position for this role

**Lead with:** hands-on applied scientist — architecture → data → train → eval → scale tradeoffs.

**Counter signal:** PI title reads "managerial." Prior loop feedback: *"too managerial for our needs."* Every answer must include **what I personally built/decided/debugged**, not lab leadership alone.

**One-line identity:**

> End-to-end ML scientist for messy sequential and multimodal data: dual representations, curriculum design, eval gates, and honest negative results — with a research arc evolving toward LLM reasoning systems.

---

## Research arc (2020–present)

Coherent program, not scattered papers. Use as 90-second "what I do now" backbone:

```
Sequential / dynamical modeling (Koopman, forecasting)
    → Time series as images (ImagenTime, delay embeddings)
    → Generative modeling under scarcity & irregular sampling
    → Multimodal LLM reasoning + systematic eval (Qwen VLM stack)
```

### Tier 1 — mention briefly alongside flagship VLM project

| Work | Venue | Why it matters for FinTelligence |
|------|-------|----------------------------------|
| **ImagenTime** — image transforms + diffusion for short/long TS | NeurIPS 2024 | Intellectual predecessor to dual-encoding VLM; +58% / +132% generative gains |
| **Irregular TS** — completion + masking, two-step framework | NeurIPS 2025 | Messy/missing data (finance-relevant); ~70% discriminative gain, ~85% compute reduction |
| **Data-scarce unified modeling** | NeurIPS 2025 | Low-label regime; +55% with 5% data (CV) |
| **One-step diffusion distillation** | NeurIPS 2025 | Efficient inference → SLM / routing narrative |

### Tier 2 — only if prompted

- Koopman VAEs / forecasting lineage (ICLR 2024, ICML 2020) — sequential credibility
- Disentangled multimodal representations (ICLR 2026) — controllable outputs
- Lightweight forecasting (Super-Linear, XCTFormer) — when not to use a VLM

### Skip for "current work" focus

- Geometry / shape correspondence (TOG, SIGGRAPH era)
- JAMA autism video analysis — applied impact, but domain pivot is hard in 30s

---

## Flagship project: Time-Series Vision-Language Models

**Extended summary (build on this):** [`vlm_multimodal_project.md`](vlm_multimodal_project.md)  
**PS1 cheat sheet:** [`anchor-cheat-sheet.md`](../anchor-cheat-sheet.md)

**Stack:** Python 3.11 · PyTorch 2.4 (8B) / 2.11 (Q35) · Transformers · PEFT/LoRA · TRL (GRPO) · Accelerate/DeepSpeed · HuggingFace · Slurm · 8× GPU DDP

### Elevator pitch (30s)

Built an end-to-end research stack for fine-tuning and evaluating multimodal LLMs on time-series reasoning. Core idea: represent each series through two complementary visual encodings — a matplotlib line chart (native Qwen ViT) and a delay-embedding image (DINOv3) — fused into a single LLM for MCQ, regression, captioning, and open QA. Ran 100+ config-driven experiments across two model scales (8B and 0.8B), multiple benchmarks, and a Slurm/DDP cluster, with systematic ablations and a fast pilot harness for dataset screening.

### Problem & approach

**Goal:** Teach general-purpose VLMs to reason over univariate/multivariate time series — not just classify UCR shapes, but answer exam-style questions, forecast, explain temporal relations, and generate structured captions.

**Key insight:** A single rendering loses information. Charts preserve amplitude/trend semantics; delay embeddings capture topological structure. Dual-tower architecture routes chart → visual (frozen native ViT) and delay image → visual_dino (DINOv3 + trainable merger), both projected into LLM token space.

**Two-stage curriculum:**

| Stage | What trains | Purpose |
|-------|-------------|---------|
| **A** | DINO backbone (LoRA) + alignment merger on alignment/caption data — no LLM updates | Learn *how to see* a series |
| **B** | Merge Stage A weights; add LM LoRA (+ optional DINO LoRA); fine-tune on task data; merger often frozen | Learn *how to answer* about it |

Decouples vision from language reasoning; caption priors transfer to downstream QA.

### Technical scope (personal ownership)

| Area | What I built / operated |
|------|-------------------------|
| **Model integration** | Patched Qwen3-VL-8B and Qwen3.5-0.8B forwards; custom DinoVisionTower; dual-stream collator with M-RoPE type tags (Q35); adapter merge/resume across stages |
| **Training** | PyTorch DDP (torchrun, 8× RTX Pro 6000), LoRA via PEFT (~43M–few-hundred-M trainable params), stratified multi-task samplers, YAML-config-first sweeps (162 configs, 125 scripts) |
| **Data pipeline** | Unified loaders for TSExam (20K MCQ), TSExam-numeric (11K regression), caption (7.7K), ChatTS (105K align + 44K SFT), ICL-UCR, CaTS-Bench, TSRBench JSONL |
| **Eval harness** | Tiered eval (loss → TSExam subset → TSRBench subset → full north-star); per-task/per-group accuracy; parse-miss logging; HF + local dataset parity |
| **RL / advanced** | GRPO on Qwen3-VL-8B (TRL + DeepSpeed) with MCQ correctness rewards; pilot harness (~8–15 min Q35 runs) with measured noise floors for dataset ablation |
| **Infra** | Slurm submission, artifact root separation (QTSX_ARTIFACT_ROOT), dual venvs (torch 2.4/8B vs 2.11/Q35), NCCL tuning, agent/onboarding automation |

### Benchmarks & headline results

| Benchmark | Task | Best Q35 (0.8B) | Best 8B (reference) |
|-----------|------|-----------------|---------------------|
| TSExam HF | 746-item MCQ exam | **0.890** (tsexam-v2 repro) | **0.901** (unified champion) |
| TSRBench overall | 12-task MCQ north star | 0.374 (capnum-a8b4) | 0.454 (capnumicl-a8b4) |
| TSRBench TR | Temporal-relation reasoning (160 items) | 0.287 (allcap control) | — |
| TSExam-numeric | Regression (medAE) | **0.14** (unified3) | — |
| Caption attr-recovery | 9-field macro accuracy | **0.72** (caption specialist) | — |
| ChatTS | Free-text QA (cat/num/reason) | — | ~0.84 cat / 0.76 num |

**Caption-transfer hypothesis (current arc):** Stage A on descriptive captions → Stage B on TSExam/TSRBench. Achieved 0.88 TSExam HF with caption priors; probing whether linguistic structure helps temporal reasoning on TSRBench (north star ~0.32–0.34 on 0.8B vs 0.45 on 8B).

**Control baseline (Jun 2025):** allcap-a5b3 — TSExam 0.854, TSRBench 0.339, TR 28.7%.

### Negative result (show rigor)

Subset-mix experiments for temporal-relation and reasoning buckets **regressed vs control** → stopped additive buckets; revisiting data generation instead of stacking more training mixes.

Stage B **over-reasoning** on complex TSRBench tasks (domain-specific, multi-hop alongside basic TS ops) — diagnosed via task-level audit, not fixed by stacking more training buckets.

### Recent work (Jun 2025 — Anchor C material)

1. **Caption scarcity (Stage A):** Generated synthetic TS↔text alignment data from TSExam + ChatTS (LLaVA-style) when real captions insufficient.
2. **Synthetic too basic:** Added CaTS (~16K samples) to Stage A → strong perception eval (next-token prediction + TSExam perception slices).
3. **Stage B reasoning gaps:** Audited TSRBench task taxonomy; identified **missing operations** (val extraction, segmentation, multi-hop primitives). Extended TSExam to cover these ops rather than adding data buckets blindly.

**Planned Stage C:** GRPO / VRT — gold-based RL on SFT adapters (MCQ correctness rewards).

### PS1 three anchors (one project, three angles)

Full detail: [`vlm_multimodal_project.md`](vlm_multimodal_project.md). Cheat sheet: [`anchor-cheat-sheet.md`](../anchor-cheat-sheet.md).

| Anchor | Theme | VLM angle |
|--------|-------|-----------|
| **A** | Production ML/LLM | Dual-tower, two-stage curriculum, DDP training stack |
| **B** | Eval / monitoring | Tiered eval, pilot harness, parse-miss, killed TR mixes |
| **C** | Ambiguity / Dive Deep | Caption pipeline (synthetic + CaTS); TSRBench gap → extended TSExam ops |

**Supporting LP stories (not anchors):** ImagenTime (Invent & Simplify, reframed); SKD debug (Dive Deep, reframed). **Retire PS1:** compute-bottleneck story.

### Experimentation methodology (Amazon-relevant)

- **Config-first** — one hypothesis per change; fork YAML, not training code; parallel Slurm sweeps
- **Pilot harness** — 4-bucket capped subset (~10K samples, 2 epochs); screens datasets in ~15 min; calibrated noise floors (TSExam ±0.3 pp detectable)
- **Tiered eval gates** — cheap TSExam HF sanity before expensive full TSRBench; parse-miss tracked separately from accuracy
- **Reproducibility** — fixed samplers, seed control, artifact paths, documented eval protocol fixes
- **Multi-scale validation** — validate on 0.8B Q35 first; compare against 8B ceiling

---

## JD alignment summary

| FinTelligence pillar | Evidence | Strength |
|----------------------|----------|----------|
| End-to-end ML systems | VLM stack: data → train → eval → infra | **Strong** |
| Eval gating / regression detection | Tiered eval, pilot noise floors, parse-miss logging | **Very strong** — sharpest differentiator |
| Tiered models / cost tradeoffs | Q35 0.8B near 8B on TSExam (0.890 vs 0.901) | **Strong** |
| Data-centric iteration | Caption-transfer, negative TR buckets, leave-one-out ablations | **Very strong** |
| Messy structured data | Irregular TS, multimodal encodings, field-level caption recovery | **Analogous** — bridge explicitly to finance |
| Learning from corrections | GRPO (rule-based MCQ rewards); iterative supervision loops | **Partial** — not production user-feedback yet |
| Agents at scale | Open QA, MCQ reasoning | **Weak** — fine-tuning + eval, not multi-agent |
| Production / compliance trust | Research stack; no serving story yet | **Gap** — address with "how I'd gate deploy" |

---

## FinTech bridges (use in interview)

Explicit translations from time-series research → finance:

| Research concept | FinTech parallel |
|------------------|------------------|
| Dual chart + delay encoding | Multimodal docs: tables + text + numbers; one view loses information |
| Two-stage curriculum (caption → QA) | Domain pre-training / alignment → task fine-tuning on invoices, remittance, filings |
| Caption 9-field attr-recovery (0.72) | Entity/field extraction from documents |
| TSExam-numeric medAE 0.14 | Numeric correctness for payment matching |
| Irregular TS completion + masking | Incomplete records, delayed postings, partial remittance fields |
| Tiered eval + parse-miss tracking | Slice metrics by doc/entity type; schema parsing reliability before accuracy |
| 0.8B near 8B quality | SLM routing when quality holds; cost at transaction scale |
| Negative TR bucket mixes | Don't cargo-cult data — same discipline before shipping to finance users |

### Production bridge (20s — not yet built, but show thinking)

> Shadow eval before promote; confidence/abstention when parse-miss spikes; slice regressions by task group; human review queue for low-confidence outputs; user corrections → golden-set refresh → gated retrain.

---

## Interview delivery guide

### Recommended structure (5–7 min ML deep-dive)

1. **Problem (30s):** VLMs fail on temporal/structured reasoning; need exam-grade QA
2. **Insight (30s):** Dual encodings; decouple vision alignment from language reasoning
3. **System (60s):** Two-stage curriculum, unified pipeline, tiered eval, 0.8B→8B validation
4. **Win (30s):** TSExam **0.890 on 0.8B** vs **0.901 on 8B**
5. **Honest limit (30s):** TR bucket mixes regressed; pivoted to data generation
6. **FinTech bridge (30s):** Same pattern as doc IE — multimodal inputs, field extraction, regression-gated releases

### Karan Aggarwal — likely resonance

Lean hardest on: **eval methodology**, **curriculum/domain adaptation**, **low-label transfer via captions**, **negative results from bad data mixing** — mirrors his continual pre-training and limited-label NLP work.

### Anti-patterns (prior loop lesson)

| Avoid | Do instead |
|-------|------------|
| "I built a research program…" | "I designed the dual-tower stack and ran 160 config sweeps…" |
| "I mentored N students…" | "I implemented the tiered eval harness; I owned gating logic." |
| Grant/roadmap/hiring stories | Retire for PS1 unless tied to a technical fork |
| "We improved SOTA…" | "I chose delay-embedding + chart dual encoding; ablation showed…" |

---

## Core competencies (from CV)

**ML:** Deep learning; LLMs; generative AI; sequential modeling; multimodal learning; diffusion; representation learning

**Systems:** End-to-end pipelines; large-scale training; model eval & validation; experimentation; efficient inference; scalable ML

**Applied research:** Experiment design; ablations; model analysis; algorithm development; data-centric modeling

**Industry collaboration:** Google, NVIDIA, Bosch AI — *details TBD; add hands-on contribution per partner when available*

---

## Gaps & open items

- [ ] **STAR stories** — triage done: ImagenTime + SKD keep (reframe); compute story retire; Customer Obsession gap remains
- [x] **Three anchors + cheat sheet** — [`anchor-cheat-sheet.md`](../anchor-cheat-sheet.md)
- [ ] **Hands-on ledger** — explicit list of personal vs delegated work across 2020–present
- [ ] **Industry collab specifics** — technical contribution per Google/NVIDIA/Bosch
- [ ] **Motivation narrative** — why this IC role now (counter "will miss running a lab")
- [ ] **Prior loop details** — which role/stories triggered "too managerial"
- [x] **2-min pitch** — [`elevator-pitch.md`](../elevator-pitch.md)
- [ ] **Production story** — any internal tools, real (non-benchmark) eval, serving constraints

---

## Quick reference — numbers to remember

| Metric | Value |
|--------|-------|
| TSExam HF (Q35) | 0.890 |
| TSExam HF (8B) | 0.901 |
| TSExam-numeric medAE | 0.14 |
| Caption attr-recovery | 0.72 macro |
| TSRBench overall (Q35 / 8B) | 0.374 / 0.454 |
| TSRBench TR | ~29% (hard problem, in progress) |
| Generative gains (ImagenTime) | +58% short / +132% long |
| Data-scarce improvement | +55% with 5% data |
| Experiment configs | 162 configs, 125 scripts |
| Trainable params (LoRA) | ~43M–few-hundred-M |

---

## Related files

- [`CV_Azencot_10399493.pdf`](../CV_Azencot_10399493.pdf) — application resume
- [`prep-plan.md`](../prep-plan.md) — 7-day schedule
- [`INDEX.md`](../INDEX.md) — role timeline & interviewer context
- [`stories/`](../stories/) — STAR bank (pending IC reframes)
