# Deliver Results: Dual-tower VLM — TSExam 0.905, TSRBench 45.2% (3ep)

**Leadership Principle:** Deliver Results  
**Project:** Time-series VLM reasoning stack (Anchor A)  
**Status:** Draft v4 — DCC L6  
**Target length:** ~850 words (body) · ~6–7 min spoken

---

## Title

Shipping time-series reasoning on Qwen3-VL-8B: 0.62 → 0.90 TSExam, 40% → 45% TSRBench

## Outline

As project lead I built an end-to-end dual-tower VLM stack on **Qwen3-VL-8B** — chart plus delay-embedding streams, two-stage curriculum, tiered eval gating — and delivered **TSExam-HF 0.905** and **TSRBench overall 0.452** (3ep), up from stock **Qwen3-VL-8B** at **0.618 / 0.402**.

## Ecosystem

At Ben-Gurion University I lead a multimodal modeling project: teach general-purpose vision-language models to **reason** over time series — multiple-choice exams, numeric answers, temporal relations, captions — not just classify shapes. Stakeholders are researchers who need one model that generalizes across tasks, and downstream builders who need structured answers over sequential data (analogous to finance filings or payment traces). For two years the field chased text-token TS inputs and bespoke benchmarks; each paper claimed state of the art locally, but nothing transferred. When **TSRBench** launched as a multi-task north star — perception, reasoning, prediction, decision-making across 14 domains including finance — I anchored delivery on that benchmark. I owned technical direction end-to-end: dual-stream architecture, Qwen3-VL-8B integration, two-stage training recipe, YAML experiment matrix (**162 configs**, **125 scripts**), tiered eval harness, and multi-scale validation. Collaborators run Slurm jobs and data curation; I implement model patches, collators, gating logic, and eval protocol the lab adopted as standard.

## Issue

The baseline was **stock Qwen3-VL-8B** with no TS-specific stack: **TSExam-HF 0.618** (n=746) and **TSRBench overall 0.402** (n=4125). A general open VLM could not do exam-grade time-series reasoning out of the box — that was the delivery gap. We also evaluated alternatives that failed. **Text-token TS** burned context and missed plot structure. **Chart-only or delay-only** single streams lost information in ablations. **Per-benchmark model forks** would never unify on TSRBench. Proprietary VLMs orders of magnitude larger led the field. Operationally, full TSRBench eval is expensive; with eight GPUs and hundreds of hypotheses, I could not treat the north star as a daily loop. The delivery problem: **lift stock Qwen3-VL-8B to competitive TS reasoning** — **0.90+ TSExam** and **~0.45 TSRBench** — in one stack, and refuse to promote changes that win one slice and regress another.

## Objectives

1. **Close the VLM gap:** Lift **Qwen3-VL-8B** from **TSExam 0.618** and **TSRBench 0.402** to exam-grade and north-star competitive scores.
2. **Unified benchmarks:** One dual-tower architecture — not per-benchmark forks — improving both headline metrics together.
3. **Exam + north star together:** Reach **0.90+ TSExam** and **0.45+ TSRBench overall** without trading one off for the other.
4. **Ship discipline:** No feature merges unless **tiered eval** shows net improvement across benchmarks; parse reliability tracked separately from accuracy.

## Actions

**I chose dual visual streams over the alternatives and built the integration.** After ImagenTime, I pursued image representations in a **LLaVA-style** dual tower on **Qwen3-VL-8B**: matplotlib charts through frozen native ViT; delay embeddings through a custom **DinoVisionTower** and trainable merger. I rejected text-token and single-stream paths after pilots — chart-only regressed on topology slices; text-token stalled on context and parse reliability. I patched Qwen3-VL-8B forwards, built the **dual-stream collator** with M-RoPE type tags, and wired adapter merge across curriculum stages. That was weeks of integration risk; I de-risked with perception-only eval before spending 8B GPU weeks on language fine-tunes.

**I delivered a two-stage curriculum and made it the team's training protocol.** I considered end-to-end joint training from day one — faster on paper, but it hid perception bugs and produced **over-reasoning** on hard TSRBench tasks when vision was weak. Stage A: DINO LoRA + merger on caption/align data, **LLM frozen** — learn *how to see*. Stage B: merge Stage A, add LM LoRA, QA fine-tune — learn *how to answer*. I curated ChatTS alignment, CaTS, TSExam MCQ, TSExam-numeric, with holdouts against forgetting. I persuaded the team to adopt staging as a **gate**: no Stage B spend until Stage A cleared perception thresholds.

**I built tiered eval and config-first iteration as the delivery engine.** I implemented: loss sanity → TSExam subset → TSRBench subset → full north star; **parse-miss** separate from accuracy. Pilot harness ~15 min on 0.8B with noise floors (**TSExam ±0.3 pp** detectable). One hypothesis per YAML fork. Features shipped only on aggregate improvement; several TSExam-winning mixes **died** when reasoning slices regressed (see Ownership story). That discipline took us from **stock Qwen3-VL-8B** to the **3ep** champion without false promotions.

## Results

**Delivery vs stock Qwen3-VL-8B baseline:**

- **TSExam-HF:** **0.618 → 0.9048** (n=746) — **+28.7 pp** on best **3-epoch** run.
- **TSRBench overall:** **0.402 → 0.4524** (n=4125) — **+5.0 pp**.

Both headline benchmarks improved together on one dual-tower stack. Tiered gating + parse-miss logging prevented false wins; living config index for handoff.

**Broader impact (L7 signal):** Took **stock Qwen3-VL-8B** from failing exam-grade TS reasoning to **~90.5% TSExam** and **~45.2% TSRBench** — near proprietary frontier on the public north star (verify leaderboard before PS1). Open loaders, scripts, eval protocol. **ImagenTime → dual-tower VLM** is a deliberate research line. **Honest limit:** TSRBench +5 pp from stock is real but still below frontier; hard TR slices (~29% on earlier controls) and trillion-scale proprietary gap remain — Stage C GRPO is next.

## Learnings and Improvements

Delivering at L6 scope means naming the **right baseline** — **Qwen3-VL-8B** out of the box, not an internal checkpoint name interviewers will not recognize. The headline is **0.62 → 0.90 TSExam**; north-star lift is harder but still **+5 pp** on TSRBench. I separate shipping the **platform** from winning every slice. Methodology — config-first, tiered eval, promote on TSExam **and** TSRBench — ports to FinTech: multimodal docs, staged alignment → task FT, slice metrics before ship.

---

## Interview notes

### Personal ownership (say early if probed)

Project lead: architecture, curriculum, eval harness, experiment matrix. I patch Qwen3-VL-8B forwards, DinoVisionTower, collator. Team executes Slurm runs and data curation.

### Baseline vs delivered (memorize)

| | TSExam-HF (n=746) | TSRBench overall (n=4125) |
|--|-------------------|---------------------------|
| **Qwen3-VL-8B** (stock baseline) | 0.618 | 0.402 |
| **Our stack** (3ep best) | **0.905** | **0.452** |
| **Lift** | **+28.7 pp** | **+5.0 pp** |

### IC proof (artifacts I personally built/decided)

- Dual-stream architecture vs text-token / single-stream (pilot evidence).
- Patched Qwen3-VL-8B forwards; DinoVisionTower; dual-stream collator + M-RoPE.
- Two-stage curriculum; tiered eval + pilot noise floors; 162 configs / 125 scripts.

### Spoken script (~6–7 min)

I lead a multimodal project at Ben-Gurion: teach vision-language models to reason over time series — exam questions, numeric answers, temporal relations, captions. Stakeholders need one model that generalizes across tasks — the same shape of problem as multimodal finance docs.

When TSRBench published as a multi-task north star, I anchored delivery there. The starting point was **stock Qwen3-VL-8B** — no time-series stack, no custom training. It scored **TSExam-HF zero-point-six-one-eight** on seven hundred forty-six items and **TSRBench overall zero-point-four-zero-two** on four thousand one hundred twenty-five. A general open VLM could not do exam-grade time-series reasoning out of the box.

We also killed alternatives — text tokens, single visual streams, per-benchmark forks. Proprietary models far larger still led the field. Eight GPUs, hundreds of configs, expensive north-star evals — I could not run full TSRBench on every hypothesis.

My objectives: close the gap from **Qwen3-VL-8B**, one unified dual-tower stack, **zero-point-nine-oh-plus** TSExam and **zero-point-four-five-plus** TSRBench together, and no feature merges unless tiered eval passes on both benchmarks.

I designed a dual tower on **Qwen3-VL-8B**: matplotlib charts through frozen Qwen ViT, delay embeddings through custom DINO, patched forwards, dual-stream collator, two-stage curriculum — Stage A frozen LLM for vision, Stage B LoRA for QA. Tiered eval with parse-miss separate from accuracy; fifteen-minute pilots; one YAML per hypothesis. Mixes that won TSExam but lost reasoning slices died — that is how we climbed from stock baseline without false promotions.

On results — always name **Qwen3-VL-8B** as the baseline. TSExam **zero-point-six-one-eight to zero-point-nine-oh-four-eight** — plus twenty-eight points. TSRBench **zero-point-four-zero-two to zero-point-four-five-two-four** — plus five points. Both moved on one stack. That is the deliver-results headline.

Open stack, eval protocol, config index. Honest limit: hard reasoning slices and proprietary gap remain — we delivered the platform and the headline lifts first.

Lesson: baseline is stock **Qwen3-VL-8B**, tier eval like release gates, deliver both benchmarks — then chase hard slices. Same discipline for finance docs at scale.

### Short version (~90 sec)

Baseline **Qwen3-VL-8B**: TSExam **0.618**, TSRBench **0.402**. I built dual tower, two-stage curriculum, tiered eval on the same backbone. Delivered **3ep**: **0.905 / 0.452** — plus twenty-eight and plus five points. Features ship only on aggregate eval gates. Lesson: name the stock baseline, both benchmarks, eval gates before claim.

### Likely follow-ups

- Why **Qwen3-VL-8B** as baseline?
- Why dual stream vs chart-only?
- Is +5 pp TSRBench enough vs proprietary?
- TSRBench vs frontier gap?

### Weak spots / facts to verify

- [ ] TSRBench leaderboard rank before PS1.
- [ ] Collaborator split on "project lead."

### FinTech bridge (one clause)

Stock **Qwen3-VL-8B** on TS is like a stock LLM on payment docs — staged multimodal stack + eval gates before production-ready extraction.
