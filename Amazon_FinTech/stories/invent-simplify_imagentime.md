# Invent and Simplify: ImagenTime — time series as images

**Leadership Principle:** Invent and Simplify  
**Project:** ImagenTime (NeurIPS 2024)  
**Status:** Draft v2 — DCC L5 length + IC ownership  
**Target length:** ~680 words (body) · ~5–6 min spoken

---

## Title

Rethinking time series generation as a representation problem

## Outline

Instead of building a bigger time-series diffusion model, I changed the representation so we could reuse mature image-generation tools — improving short- and long-sequence benchmarks by 58% and 133% while cutting sampling from about 1000 model calls to 35.

## Ecosystem

At Ben-Gurion University I was senior author on ImagenTime, a generative modeling project for short through ultra-long time series — synthetic data, forecasting, and anomaly detection. Researchers and practitioners in the field needed realistic long sequences, but most generators were split: strong on short benchmarks or on long ones, rarely both in one framework. I owned the core technical bet — transform sequences into invertible images and plug in a vision diffusion backbone — plus the transform survey, ablation plan, and choice of EDM sampling. Collaborators on the team implemented training pipelines, ran benchmark sweeps, and co-authored the paper; I drove the representation hypothesis and the decisions on what to reject.

## Issue

The field's default next step after our strong VAE line was bespoke time-series diffusion: custom U-Nets and sequence-specific modules for every new length regime. That path had three operational problems. First, longer sequences forced heavier architectures for diminishing returns — short and long setups rarely shared one stack. Second, the best diffusion advances were landing in vision, so every custom TS model meant re-implementing samplers and training recipes we could not reuse. Third, iteration was slow: the standard denoising sampler needed on the order of **1000 model calls** to produce one sample. Incremental improvement on the VAE was safe but capped. I needed to test whether the bottleneck was the generative model itself, or how we encoded the signal.

## Objectives

1. **Quality:** Beat strong time-series-specific diffusion baselines on standard short- and long-sequence benchmarks.
2. **Length scaling:** Handle ultra-long real-world series (10K–17K steps) in the same framework as short sequences, without a new custom architecture per length.
3. **Simplification:** Reuse a mature vision diffusion stack — only the diffusion block should be learnable; encoding and inverse decoding stay closed-form.
4. **Speed:** Cut sampling cost by an order of magnitude — from ~1000 model calls to a much smaller number — without a measurable quality drop.

## Actions

**I challenged the default path.** The community norm was to design another specialized time-series diffusion architecture. I questioned whether we needed a new model at all. The main risk was that a representation shortcut could silently destroy temporal structure — local spikes, long-range periodicity, cross-channel relationships — and look fine on a plot but fail on generation metrics.

**I reframed the problem as representation and de-risked it in stages.** I surveyed time-series-to-image maps from the literature. Line graphs were fast but mostly blank pixels — not informative enough. Gramian angular fields essentially store the series on a diagonal and do not scale to long sequences — we would have needed enormous images. I focused on two **invertible** transforms with closed-form inverses: delay embedding and the short-time Fourier transform (STFT). I ran ablations across short, long, and ultra-long datasets before committing. Delay embedding worked especially well on short and ultra-long cases; STFT was strong on long periodic data. I only moved to the vision diffusion stack after inverse transforms showed we could recover the signal without losing the patterns that mattered for quality.

**I simplified the system by reuse, not reinvention.** The final pipeline has three parts: time series to image, a vision diffusion model, image back to time series. Only the middle block is learned. I adopted the **EDM** image diffusion backbone from the vision literature — a sampler that produces high-quality images in about **35 model calls** instead of hundreds or thousands with the older DDPM-style approach. Reuse was not plug-and-play: I had to pick image resolution and transform parameters so temporal detail survived while still fitting the diffusion model's assumptions. The first aggressive EDM settings cut steps but hurt quality; I tuned the noise schedule and sampling parameters until quality matched the slower baseline.

**I aligned the team on the pivot with evidence.** Because the image-representation idea was unconventional for time-series diffusion, I ran a small proof of concept — ablations showing invertible encodings preserved structure and beat the incremental VAE path — before we stopped investing in another bespoke TS architecture.

## Results

Mapped to objectives:

- **Quality (objective 1):** **+58%** mean improvement on short-sequence discriminative scores vs prior TS diffusion baselines; **+133%** on ultra-long classification scores — the representation change drove the largest gains on long data.
- **Length scaling (objective 2):** One framework handled 24-step synthetic benchmarks through ultra-long real series (e.g. ~17K-step traffic occupancy, ~11K-step air-quality stations) by switching delay embedding vs STFT — no new custom sequence model per length.
- **Simplification (objective 3):** Removed the need to maintain a parallel time-series diffusion codebase; new vision-side sampler improvements could be tested by configuration rather than rewriting TS-specific model code.
- **Speed (objective 4):** EDM reduced sampling from ~**1000** model calls to ~**35** (~30×) with tuned quality — the sampler change solved iteration cost, separate from the representation win.

**Practical impact:** Practitioners could generate long synthetic series with a standard vision diffusion stack instead of fragile custom architectures and thousand-step sampling. The work was accepted to **NeurIPS 2024** and became a reusable pattern — the same "render sequential data as images" instinct now drives my VLM reasoning work (chart + delay embedding on TSRBench).

## Learnings and Improvements

Many hard modeling problems are abstraction problems. Before I commit to a new architecture, I ask whether the right representation lets me reuse a mature, optimized stack from an adjacent domain. I also learned to de-risk representation bets with invertibility checks and slice-level metrics, not just headline scores — a simple encoding can look clean and still lose the structure users care about.

I apply that filter on messy structured data today: on finance-adjacent tasks, tables plus text plus numbers — one view often loses information the task needs. Pick the representation first; then fine-tune or route models, don't cargo-cult bespoke stacks.

---

## Interview notes

### Personal ownership (say early if probed)

Senior author on ImagenTime. I owned the representation hypothesis, transform survey and ablations, EDM backbone choice, and pivot decision. Collaborators implemented pipelines and ran full benchmark sweeps.

### IC proof (artifacts I personally built/decided)

- Transform selection and ablation plan (rejected GAF, line graphs; committed to delay embedding + STFT).
- EDM backbone integration and sampler tuning (quality vs ~35 model calls).
- Three-block architecture: invertible encode → vision diffusion (only learned part) → invertible decode.

### Spoken script (~5–6 min)

At Ben-Gurion I was senior author on ImagenTime — generative modeling for time series from short benchmarks up to ultra-long real-world sequences. The users were researchers and practitioners who needed realistic synthetic data for forecasting, anomaly detection, and simulation. But the field was splitting: models that worked on short benchmarks rarely scaled to long series, and long-sequence models were heavy custom architectures that could not reuse the rapid progress happening in vision diffusion.

The default path after our strong VAE generator was to keep going down bespoke time-series diffusion — custom U-Nets, sequence-specific modules, more complexity every time we added length. I saw three problems. First, longer sequences meant heavier architectures for diminishing returns. Second, the best sampler and training improvements were landing in image diffusion, and our TS-only stack could not inherit them. Third, iteration was slow: the standard denoising approach needed on the order of a thousand model calls to produce one sample. Incremental VAE improvement was safe, but capped.

My objectives were testable: beat strong TS diffusion baselines on short and long benchmarks; handle ultra-long series — ten to seventeen thousand steps — in the same framework; reduce custom modeling by reusing vision diffusion; and cut sampling by an order of magnitude without a quality drop.

I started by questioning the assumption that we needed a new time-series architecture. The main risk was that mapping series to images could silently destroy temporal structure — local spikes, long-range periodicity, cross-channel relationships — and look fine visually but fail on generation metrics.

So I surveyed transforms from the time-series-to-image literature and ran ablations before committing. Line graphs were fast but mostly blank pixels — not informative. Gramian angular fields store the series on a diagonal and blow up on long sequences. I focused on two invertible transforms with closed-form inverses: delay embedding and the short-time Fourier transform. I tested whether inverse decoding recovered the patterns that mattered on short, long, and ultra-long datasets. Delay embedding was especially strong on short and ultra-long cases; STFT was strong on long periodic data. Only after those checks held did I commit to plugging in a vision diffusion backbone.

That simplified the system operationally. The pipeline is encode, diffuse, decode — and only the diffusion block is learned. We did not need to maintain a parallel custom time-series diffusion codebase. When vision-side samplers improved, we could test them through configuration instead of rewriting model code.

For speed I adopted EDM from the vision literature — a sampler that can match quality in about thirty-five model calls instead of a thousand with the older approach. That was not plug-and-play. The first aggressive settings cut steps but hurt quality, so I tuned the noise schedule and sampling parameters until quality matched the slower baseline.

Because the representation pivot was unconventional, I aligned collaborators with a small proof of concept — ablations showing structure was preserved and the path beat incremental VAE investment — before we stopped building another bespoke TS architecture.

On results, I tie each outcome to the action. The representation change drove quality and length scaling: fifty-eight percent better on short-sequence discriminative scores and a hundred thirty-three percent on ultra-long classification versus strong TS baselines. The same framework handled twenty-four-step synthetic data through seventeen-thousand-step traffic series by switching encoding, not rebuilding the model. The sampler change drove speed: roughly thirty times fewer model calls. Practically, that meant researchers could generate long synthetic series with a standard vision stack instead of fragile custom models and thousand-step sampling. NeurIPS twenty-twenty-four was external validation; internally, the pattern now drives my VLM reasoning work — chart plus delay embedding on TSRBench.

The lesson I still apply: before building a bigger custom model, ask if the bottleneck is abstraction — can you represent the data so you reuse mature tools from another domain? I de-risk representation bets with invertibility and slice checks, not headline scores alone. For FinTech, it is the same discipline: on a payment document, tables plus text plus numbers — one view loses information. Pick the representation first, then fine-tune or route — do not cargo-cult another bespoke stack.

### Short version (~90 sec)

After a strong VAE generator, bespoke TS diffusion was hitting a length and maintenance ceiling, and sampling needed about a thousand model calls per sample. I owned the bet to map series to invertible images and reuse vision diffusion. I rejected transforms that lost structure — like line graphs and GAF on long data — and committed to delay embedding and STFT after ablations. EDM cut sampling to about thirty-five calls once tuned. Result: plus fifty-eight percent short, plus one-thirty-three percent ultra-long, simpler stack. Lesson: fix representation before inventing a new model.

### Likely follow-ups

- Why delay embedding vs STFT for different lengths?
- What exactly did collaborators do vs you?
- How does this connect to FinTech / doc IE?
- Why not stay on the VAE line?

### Weak spots / facts to verify

- [ ] Confirm collaborator split matches your memory (pipeline implementation vs your role).
- [ ] Ultra-long dataset names if probed: Traffic (~17K), KDD-Cup (~11K).

### FinTech bridge (one clause)

Tables + text + numbers on a payment doc — one view loses information; representation choice gates everything downstream, same as TS→image before diffusion.
