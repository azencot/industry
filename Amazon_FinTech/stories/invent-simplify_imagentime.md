# Invent and Simplify: ImagenTime — time series as images

**Leadership Principle:** Invent and Simplify  
**Project:** ImagenTime (NeurIPS 2024)  
**Status:** Draft v3 — DCC L6  
**Target length:** ~850 words (body) · ~6–7 min spoken

---

## Title

Rethinking time series generation as a representation problem

## Outline

Instead of building a bigger time-series diffusion model, I changed the representation so we could reuse mature image-generation tools — **+58% / +133%** benchmark gains, **~30×** fewer sampling steps — and established a reusable pattern that now drives my VLM reasoning stack and how I approach multimodal finance data.

## Ecosystem

At Ben-Gurion University I was **senior author** on ImagenTime — generative modeling for short through ultra-long time series used in forecasting, anomaly detection, and synthetic data generation. Practitioners and researchers needed realistic **long** sequences; the field was split between short-sequence generators and heavy long-sequence architectures that could not share code or reuse vision advances. I owned the core hypothesis — time series as invertible images plus vision diffusion — the transform survey and ablation plan, EDM backbone choice, and the decision to stop incremental VAE investment. Co-authors implemented training pipelines and ran benchmark sweeps; I drove which paths to kill and when the team pivoted. NeurIPS 2024 validated the result externally; internally, the insight became the **intellectual line** from generative TS → dual-encoding VLM reasoning — an L7-style leverage point across projects, not a one-off trick.

## Issue

After a strong VAE-based generator, the **safe** path was incremental improvement or bespoke time-series diffusion — custom U-Nets, sequence-specific modules, more complexity per length regime. I mapped three operational costs of that default. **Length:** longer series meant heavier architectures for marginal gains; short and long rarely shared one stack. **Maintainability:** every custom TS model duplicated samplers and training recipes that vision had already solved. **Iteration speed:** the standard denoising sampler needed on the order of **1000 model calls** per sample — too slow to explore honestly at scale. I also considered **non-invertible** image tricks from the TS-classification literature; they could look fine visually but fail generation because you cannot decode back to the series faithfully. The strategic question was whether we were capped by **modeling** or **representation** — and whether simplification could beat complexity, not just match it.

## Objectives

1. **Quality:** Beat strong TS-specific diffusion baselines on short- and long-sequence benchmarks (same metrics in results: discriminative / classification scores).
2. **Unified length:** One framework from 24-step synthetic through **~17K-step** real series without a new custom architecture per length.
3. **Simplification:** Reuse vision diffusion — only the diffusion block learned; encode/decode closed-form.
4. **Speed:** Cut sampling from **~1000 → ~35 model calls** without measurable quality loss.

## Actions

**I challenged the default and named alternatives I rejected.** Incremental VAE — safe but capped. Bespoke TS diffusion — community norm, rising complexity. I questioned whether we needed either if representation was wrong. Risk: reviewers and peers expect TS-native models; a representation bet could destroy temporal structure silently.

**I reframed as representation and ran a disciplined de-risk loop.** I surveyed TS→image maps. **Line graphs** — efficient, mostly blank pixels, rejected. **Gramian angular fields** — diagonal storage, **does not scale** to long sequences, rejected on ultra-long. **Folding** and others in ablations — reasonable but weaker on average than delay embedding and STFT. I committed to two **invertible** transforms with closed-form inverses: **delay embedding** (strong short + ultra-long) and **STFT** (strong long periodic). I validated inverse recovery on local spikes, long-range periodicity, and cross-channel structure before any diffusion spend.

**I simplified operationally via reuse.** Pipeline: encode → vision diffusion → decode; **only diffusion is learned**. I adopted **EDM** from vision — ~**35 model calls** vs ~**1000** with the older sampler — not plug-and-play: first fast settings hurt quality until I tuned noise schedule and sampling parameters. Reuse meant new vision samplers could be tested by **configuration**, not rewriting TS U-Net code.

**I influenced the team to pivot with a POC, not a slide.** The image path was unconventional for TS diffusion. I ran small ablations showing structure preservation and benchmark lift over the incremental VAE line, then aligned co-authors to stop investing in another bespoke architecture. That data-first persuasion is how I prefer to change direction — same habit I use when eval slices regress today.

## Results

- **Quality (obj 1):** **+58%** short-sequence discriminative vs TS diffusion baselines; **+133%** ultra-long classification — **representation** drove length scaling.
- **Unified length (obj 2):** 24-step synthetics through **~17K-step** traffic / **~11K-step** air-quality series — switch DE vs STFT, not rebuild model.
- **Simplification (obj 3):** No parallel TS diffusion codebase; vision infrastructure shared.
- **Speed (obj 4):** **~30×** fewer model calls — **sampler** change, separate from representation win.

**Broader impact:** Practitioners generate long series with standard vision stacks, not thousand-step custom models. **NeurIPS 2024** external validation. **Long-term leverage:** dual chart + delay encoding in my VLM north-star work on TSRBench — same abstraction filter I apply to finance docs (one view loses fields).

## Learnings and Improvements

Hard modeling problems are often abstraction problems — but L6 delivery requires **proving** simplification with invertibility checks, slice metrics, and operational maintainability, not elegance alone. I now ask on every project: can adjacent-domain tooling absorb the problem if I represent the data correctly? That question shipped ImagenTime, then the VLM stack, and is how I would approach invoice and remittance intelligence without bespoke extractors per doc type.

---

## Interview notes

### Personal ownership (say early if probed)

Senior author. Owned hypothesis, transform ablations, EDM choice, pivot decision. Co-authors: pipelines, benchmark runs, paper writing.

### IC proof (artifacts I personally built/decided)

- Transform kill list (line graphs, GAF; commit DE + STFT).
- EDM integration + sampler tuning.
- Three-block encode → diffuse → decode architecture.

### Spoken script (~6–7 min)

I was senior author on ImagenTime at Ben-Gurion — generative modeling for time series from short benchmarks through ultra-long real-world sequences. Users were researchers and practitioners who needed realistic synthetic data for forecasting, anomaly detection, and simulation. The field was split: strong short-sequence models, heavy long-sequence models, rarely one framework — and almost no reuse of the rapid progress in vision diffusion.

After a strong VAE generator, the safe path was keep improving that line or build bespoke time-series diffusion — custom U-Nets, more modules every time length grew. I mapped three costs. Length scaling meant heavier architectures for diminishing returns. Maintainability meant duplicating samplers vision had already solved. Speed meant about a thousand model calls per sample with the standard denoising approach — too slow to explore honestly.

I also considered image tricks from classification that are not invertible — they can look fine but you cannot decode back to a faithful series. The strategic question was whether we were capped by modeling or representation.

My objectives were testable: beat TS diffusion baselines on short and long metrics, handle ultra-long series in one framework, reuse vision diffusion with only the middle block learned, cut sampling from about a thousand to a few dozen model calls without quality loss.

I challenged the default. Incremental VAE was safe but capped. Bespoke TS diffusion was the community norm. I asked if we needed either.

I surveyed transforms and ran a de-risk loop before diffusion spend. Line graphs — mostly blank pixels, rejected. Gramian angular fields — do not scale to long sequences, rejected. Folding and other maps from the literature were reasonable but weaker on average in our ablations than the two I kept. I committed to invertible delay embedding and short-time Fourier transform after tests on short, long, and ultra-long data — checking inverse recovery on spikes, periodicity, cross-channel structure. Delay embedding strong on short and ultra-long; STFT strong on long periodic data. The key judgment call was invertibility: if you cannot decode faithfully, generation metrics lie.

Operationally I simplified: encode, diffuse, decode — only diffusion learned. No custom time-series U-Net to maintain. When Karras EDM appeared in vision with strong quality at few steps, I pushed to adopt it here — about thirty-five model calls versus a thousand with the older sampler. Not plug-and-play: aggressive settings hurt quality until I tuned the schedule. That separation matters in the results story — representation fixed length scaling; sampler fixed iteration cost.

The pivot was unconventional. I aligned co-authors with a proof of concept — ablations showing structure preserved and benchmarks beating the incremental path — before we stopped building another bespoke TS architecture. I persuade with data, not slides.

Results tied to actions. Representation drove quality and length: plus fifty-eight percent short, plus one-thirty-three percent ultra-long versus TS baselines. Same framework from twenty-four-step synthetics through seventeen-thousand-step traffic by switching encoding. Sampler drove speed: roughly thirty times fewer model calls. We dropped a parallel TS diffusion codebase.

Broader impact: practitioners use standard vision stacks. NeurIPS twenty-twenty-four validated externally. Long-term — the same representation instinct drives my VLM work: chart plus delay embedding on TSRBench. That is a research line, not a one-off — ImagenTime was generation; the VLM project is reasoning on the same bet that one view of sequential data is never enough.

What I would do differently with hindsight: I would publish the ablation kill criteria earlier as a checklist for the team — invertibility, slice recovery, ultra-long image size — so collaborators could reject transforms without waiting on me. That is the L7 habit I am building now: encode the judgment in eval protocol, not just in my head.

Lesson I still use: before a bigger custom model, test whether representation lets you reuse mature adjacent tooling — with invertibility and slice checks, not headline scores. For FinTech: tables, text, numbers on a payment document — one view loses information. Pick the view first, then route or fine-tune — do not cargo-cult bespoke extractors per doc type.

### Short version (~90 sec)

Senior author on ImagenTime. Rejected incremental VAE and bespoke TS diffusion caps. Surveyed transforms — killed line graphs and GAF on length; committed invertible delay embedding and STFT after ablations. Reused vision diffusion; EDM cut ~1000 to ~35 model calls once tuned. Plus fifty-eight percent short, plus one-thirty-three percent ultra-long. Pattern now drives VLM dual tower. Lesson: abstraction before architecture.

### Likely follow-ups

- Why DE vs STFT when?
- What did co-authors do vs you?
- How did you persuade the pivot?
- Link to current VLM / FinTech?

### Weak spots / facts to verify

- [ ] Co-author contribution split.
- [ ] Traffic ~17K, KDD-Cup ~11K if probed.

### FinTech bridge (one clause)

Representation choice gates downstream extraction — same as TS→image before diffusion, or chart + embedding before LLM on payment docs.
