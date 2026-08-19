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

**Numbers:** [`vlm_multimodal_project.md`](vlm_multimodal_project.md) — synced to TSLMTSEXAM **`grpo`** (2026-08-10). **8B dual** is the TSExam/TSRBench ceiling; **27B** wins ChatTS cat; **9B** is Stage C + vLLM.

**Stack:** Python 3.11 · PyTorch · Transformers · PEFT/LoRA · TRL (GRPO) · Accelerate/DeepSpeed · vLLM (9B dual plugin) · HuggingFace · Slurm DDP

### Elevator pitch (30s)

Built an end-to-end research stack for fine-tuning and evaluating multimodal LLMs on time-series reasoning. Core idea: two complementary visual encodings — matplotlib chart (native Qwen ViT) and delay-embedding (DINOv3) — fused into one LLM. Dual tower is **measured** (delay-only collapses ChatTS numerical; native ViT cannot learn delay). Official-protocol SOTA or on par on TSExam, ChatTS, and TSRBench; TSRBench still behind proprietary. 100+ YAML sweeps on Slurm/DDP; 8B remains the north-star ceiling.

### Problem & approach

**Goal:** Teach general-purpose VLMs to reason over univariate/multivariate time series — not just classify UCR shapes, but answer exam-style questions, forecast, explain temporal relations, and generate structured captions.

**Key insight:** A single rendering loses information. Charts preserve amplitude/trend semantics; delay embeddings capture topological structure. Dual-tower architecture routes chart → visual (frozen native ViT) and delay image → visual_dino (DINOv3 + trainable merger), both projected into LLM token space.

**Two-stage curriculum:**

| Stage | What trains | Purpose |
|-------|-------------|---------|
| **A** | DINO backbone (LoRA) + alignment merger on alignment/caption data — no LLM updates | Learn *how to see* a series |
| **B** | Merge Stage A weights; add LM LoRA (+ optional DINO LoRA); fine-tune on task data; merger often frozen | Learn *how to answer* about it |
| **C** | C-RS (SFT on gold TR traces) then C-RL2 (GRPO). Letter-GRPO on saturated SFT was a no-op. | Upweight good traces; 9B TSExam 0.9316 |

Decouples vision from language reasoning; caption priors transfer to downstream QA.

### Technical scope (personal ownership)

| Area | What I built / operated |
|------|-------------------------|
| **Model integration** | Patched Qwen3-VL-8B and Qwen3.5 0.8B / 9B / 27B (122B infra only); DinoVisionTower; dual-stream collator; adapter merge A→B; vLLM 9B dual plugin (100/100 HF parity gate) |
| **Training** | PyTorch DDP, LoRA/PEFT, stratified samplers, YAML-config-first (162+ configs) |
| **Data pipeline** | Unified loaders: TSExam, TSExam-numeric, caption, ChatTS, ICL-UCR, CaTS, TSRBench, TR-v2 |
| **Eval harness** | Official TSExam HF / ChatTS / TSRBench n=4125; parse-miss ≠ accuracy; thinking/EOS bugs caught |
| **RL / advanced** | C-RS gold traces → C-RL2 GRPO; early letter-GRPO did not beat SFT; pilot harness for mix screens |
| **Infra** | Slurm, QTSX_ARTIFACT_ROOT, DeepSpeed ZeRO-3 (122B), NCCL tuning |

### Benchmarks & headline results

Full table: [`vlm_multimodal_project.md`](vlm_multimodal_project.md). Official protocols. **8B dual** unless noted.

| Benchmark | Best | Vs published |
|-----------|------|----------------|
| TSExam HF (n=746) | **0.926** Stage B; **0.9316** 9B after C-RS | — |
| TSRBench overall (n=4125) | **0.4565** no-ICL 4ep; TR-v2 8B **44.7** | Qwen3-VL-32B 44.9 · GPT-5 T+V 55.6 |
| ChatTS official | 8B numerical **matches 14B paper** (0.787); **27B cat 0.92 / 0.90** | ChatTS-14B A 0.889/0.788, B 0.862/0.787 |
| TSExam-numeric medAE | **0.14** (0.8B unified3) | — |

**Do not** lead with 9B/27B as better on TSRBench (~0.41–0.43). **Do not** treat TimeOmni 49.4 as overall (that is EP; overall 36.7).

### Negative result (show rigor)

Subset-mix experiments for temporal-relation and reasoning buckets **regressed vs control** → stopped additive buckets; revisiting data generation instead of stacking more training mixes.

Stage B **over-reasoning** on complex TSRBench tasks (domain-specific, multi-hop alongside basic TS ops) — diagnosed via task-level audit, not fixed by stacking more training buckets.

### Recent work (Jun 2025 — Anchor C material)

1. **Caption scarcity (Stage A):** Generated synthetic TS↔text alignment data from TSExam + ChatTS (LLaVA-style) when real captions insufficient.
2. **Synthetic too basic:** Added CaTS (~16K samples) to Stage A → strong perception eval (next-token prediction + TSExam perception slices).
3. **Stage B reasoning gaps:** Audited TSRBench task taxonomy; identified **missing operations** (val extraction, segmentation, multi-hop primitives). Extended TSExam to cover these ops rather than adding data buckets blindly.

**Stage C:** C-RS on gold TR traces then C-RL2. Letter-GRPO on saturated SFT was a no-op. 9B TSExam 0.9316; TSRBench barely moved.

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
- **Multi-scale validation** — 0.8B to choose; **8B is still TSExam/TSRBench ceiling**; 9B/27B for ChatTS + serving; 122B is infra, not a result

---

## JD alignment summary

| FinTelligence pillar | Evidence | Strength |
|----------------------|----------|----------|
| End-to-end ML systems | VLM stack: data → train → eval → infra | **Strong** |
| Eval gating / regression detection | Tiered eval, pilot noise floors, parse-miss logging | **Very strong** — sharpest differentiator |
| Tiered models / cost tradeoffs | 0.8B near 8B on TSExam; 8B still north-star; 27B wins ChatTS; 122B FT not a win | **Strong** |
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
| 0.8B near 8B on TSExam; 8B still north-star; 27B wins ChatTS | SLM / mid-size routing when quality holds; cost at product scale |
| Negative TR bucket mixes | Don't cargo-cult data — same discipline before shipping to finance users |

### Production bridge (20s — not yet built, but show thinking)

> Shadow eval before promote; confidence/abstention when parse-miss spikes; slice regressions by task group; human review queue for low-confidence outputs; user corrections → golden-set refresh → gated retrain.

---

## Interview delivery guide

### Recommended structure (5–7 min ML deep-dive)

1. **Problem (30s):** VLMs fail on temporal/structured reasoning; need exam-grade QA
2. **Insight (30s):** Dual encodings; decouple vision alignment from language reasoning
3. **System (60s):** Dual towers, A/B/C recipe, YAML sweeps, vLLM 9B parity; **8B is TSExam/TSRBench ceiling**
4. **Win (30s):** Official protocol — TSExam **0.926**, TSRBench **~45.6%** (open on par, closed ahead), ChatTS numerical **matches 14B paper**; 27B wins ChatTS cat
5. **Honest limit (30s):** TR saturates; letter-GRPO no-op; don’t mix 9B/27B as if they beat 8B on TSRBench
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

**Industry collaboration:** Google, NVIDIA, **Bosch Center for AI (Haifa)** — three papers (see below). Google/NVIDIA still TBD.

### Bosch Center for AI (Haifa) — name these

Collab is **BCAI Haifa**, not RTC-NA Sunnyvale. Do not imply you already work on Shabnam’s SoundSee team. Do say you already publish with Bosch AI.

| Paper | Venue | Bosch coauthors (public) | Why it maps |
|-------|-------|--------------------------|-------------|
| **Synth-FAR** — synthetic frequency + AR data for TS forecasting / FM pipelines | TMLR 2026 | Michal Moshkovitz, Orly Avner, **Dotan Di Castro** (+ Liran Nochumsohn, you) | JD preferred: synthetic data, frequency, TSFM data pipelines. Earlier line: Freq-Synth. |
| **LDDBM** — general **modality translation** via contrastive + predictive latent diffusion bridge | NeurIPS 2025 | Nimrod Berman, Omkar Joglekar, Eitan Kosman, **Dotan Di Castro** | **Best fit for Shabnam:** arbitrary sensor/vision modality pairs, not a forecast head. |
| **Reviving Life on the Edge** — joint score-based graph generation with rich edge attributes; traffic-scene graphs | TMLR 2025 (you recalled 2024) | Nimrod Berman, Eitan Kosman, **Dotan Di Castro** | ADAS-adjacent generative; don’t oversell as an ADAS product. |

**Spoken (15–20s, why Bosch / “have you worked with Bosch?”):**

> I’ve collaborated with Bosch Center for AI on three papers: synthetic frequency-driven time series for foundation-model data pipelines, a general modality-translation diffusion bridge, and graph generation for traffic scenes. I want to do that class of work inside RTC — multimodal sensors plus vision, with product transfer.

If probed on contribution: IC verbs for what **you** decided/built; Bosch scientists were collaborators, not your reports. Don’t invent implementation you didn’t own.

---

## Gaps & open items

- [ ] **STAR stories** — triage done: ImagenTime + SKD keep (reframe); compute story retire; Customer Obsession gap remains
- [x] **Three anchors + cheat sheet** — [`anchor-cheat-sheet.md`](../anchor-cheat-sheet.md)
- [ ] **Hands-on ledger** — explicit list of personal vs delegated work across 2020–present
- [x] **Industry collab specifics** — Bosch BCAI Haifa: Synth-FAR, LDDBM, edge-graph TMLR (see above). Google/NVIDIA still TBD.
- [ ] **Motivation narrative** — why this IC role now (counter "will miss running a lab")
- [ ] **Prior loop details** — which role/stories triggered "too managerial"
- [x] **2-min pitch** — [`elevator-pitch.md`](../elevator-pitch.md)
- [ ] **Production story** — any internal tools, real (non-benchmark) eval, serving constraints

---

## Quick reference — numbers to remember

| Metric | Value |
|--------|-------|
| **North-star model** | Qwen3-VL-**8B** dual |
| TSExam HF | **0.926** (8B full-B); **0.9316** (9B C-RS) |
| TSRBench overall | **0.4565** (8B no-ICL 4ep); TR-v2 8B **44.7** |
| ChatTS | 8B num **= 14B paper**; **27B cat 0.92 / 0.90** |
| TSExam-numeric medAE | 0.14 |
| Caption attr-recovery | 0.72 macro |
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
