# Prior-loop STAR stories — paste into ChatGPT

Source material from two earlier loops. These are Omri Azencot's prepared stories. Do not invent metrics, collaborators, or outcomes that are not written here.

Loops:
- Amazon FinTech PS1: five DOC stories. Each has the written story, the ~8 minute spoken script, and the ~90 second version.
- Apple Health AIML on-site: five behavioral cards plus two 60-second backups. Each card is the story. The spoken block is the delivery.

How the stories relate, so they are not told as one anecdote:
- Deliver Results is the dual-tower VLM result (TSExam 0.618→0.905, TSRBench 0.402→0.452).
- Invent and Simplify / Apple card 1 is ImagenTime: time series as images. Card 1 is the disagreement. Backup B is the deadline cut on the same project.
- Ownership / Apple card 4 is the kill: temporal relations 26.9→21.9. One sentence of handoff only into the next story.
- Dive Deep / Apple card 3 starts after that kill: three failure regimes.
- Apple card 2 is a different failure: delay-only numerical collapse (0.17 vs 0.71 vs 0.79). Do not merge it with the kill.
- Learn and Be Curious is diffusion from the SDE up, seven papers. Do not retell ImagenTime's result here.
- Apple card 5 is Bosch Haifa modality translation. Research collaboration, not a product ship.
- Backup A is a collator bug a collaborator fixed. Not a supervision story.


# Amazon FinTech — DOC stories


---

# Deliver Results: Dual-tower VLM — TSExam 0.905, TSRBench 45.2% (3ep)

**Leadership Principle:** Deliver Results  
**Project:** Time-series VLM reasoning stack (Anchor A)  
**Status:** Draft v4 — DOC L6  
**Target length:** ~850 words (body) · **~8 min spoken** (descriptive primary)

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

### Spoken script (~8 min)

I lead a multimodal modeling project at Ben-Gurion University: teach general-purpose vision-language models to reason over time series — multiple-choice exams, numeric answers, temporal relations, captions — not just classify shapes on a plot. The stakeholders are researchers who need one model that generalizes across task types, and downstream builders who need structured answers over sequential data. The shape of the problem is very close to what I care about in finance: multimodal documents where you cannot trust a single headline metric and you need exam-grade reliability on specific field types.

For two years the field chased text-token time-series inputs and bespoke benchmarks. Each paper claimed state of the art locally, but nothing transferred. When TSRBench launched as a multi-task north star — perception, reasoning, prediction, decision-making across fourteen domains including finance — I anchored delivery on that benchmark. I owned technical direction end to end: dual-stream architecture, Qwen3-VL-8B integration, two-stage training recipe, a YAML experiment matrix with a hundred sixty-two configs and a hundred twenty-five scripts, tiered evaluation harness, and multi-scale validation. Collaborators run Slurm jobs and data curation; I implement the model patches, collators, gating logic, and the eval protocol the lab adopted as standard.

The baseline I always name in interviews is stock Qwen3-VL-8B — no time-series stack, no custom training. It scored TSExam-HF zero-point-six-one-eight on seven hundred forty-six items and TSRBench overall zero-point-four-zero-two on four thousand one hundred twenty-five. A general open VLM could not do exam-grade time-series reasoning out of the box. That was the delivery gap.

We also evaluated alternatives that failed, and I killed them with evidence rather than opinion. Text-token time series burned context and missed plot structure. Chart-only or delay-only single streams lost information in ablations — chart-only regressed on topology slices; text-token stalled on parse reliability. Per-benchmark model forks would never unify on TSRBench. Proprietary VLMs orders of magnitude larger still led the field. Operationally, full TSRBench evaluation is expensive. With eight GPUs and hundreds of hypotheses, I could not treat the north star as a daily loop. The delivery problem was concrete: lift stock Qwen3-VL-8B to competitive time-series reasoning — zero-point-nine-oh-plus on TSExam and roughly zero-point-four-five on TSRBench — in one stack, and refuse to promote changes that win one slice and regress another.

My objectives were testable against those baselines. Close the VLM gap from stock Qwen3-VL-8B. One unified dual-tower architecture, not per-benchmark forks. Reach exam-grade and north-star competitive scores together — not trade TSExam for TSRBench. And ship discipline: no feature merges unless tiered eval shows net improvement; parse reliability tracked separately from accuracy.

I chose dual visual streams after ImagenTime convinced me image representations were the right abstraction. I built a LLaVA-style dual tower on Qwen3-VL-8B: matplotlib charts through the frozen native ViT; delay embeddings through a custom DinoVisionTower and trainable merger. I patched Qwen3-VL-8B forwards, built the dual-stream collator with M-RoPE type tags, and wired adapter merge across curriculum stages. That was weeks of integration risk. I de-risked with perception-only evaluation before spending eight-GPU weeks on language fine-tunes.

I delivered a two-stage curriculum and made it the team’s training protocol. I considered end-to-end joint training from day one — faster on paper — but it hid perception bugs and produced over-reasoning on hard TSRBench tasks when vision was weak. Stage A: DINO LoRA plus merger on caption and alignment data, LLM frozen — learn how to see. Stage B: merge Stage A, add LM LoRA, QA fine-tune — learn how to answer. I curated ChatTS alignment, CaTS, TSExam MCQ, TSExam-numeric, with holdouts against forgetting. I persuaded the team to adopt staging as a gate: no Stage B spend until Stage A cleared perception thresholds.

I built tiered eval as the delivery engine. Loss sanity, then TSExam subset, then TSRBench subset, then full north star — with parse-miss logged separately from accuracy. Pilot harness about fifteen minutes on zero-point-eight-B with noise floors where TSExam moves of three-tenths of a point were detectable. One hypothesis per YAML fork. Several TSExam-winning mixes died when reasoning slices regressed — that discipline is how we climbed from stock baseline without false promotions.

On results — and I always anchor on stock Qwen3-VL-8B as the baseline. TSExam-HF went from zero-point-six-one-eight to zero-point-nine-oh-four-eight on our best three-epoch run — plus twenty-eight-point-seven percentage points. TSRBench overall went from zero-point-four-zero-two to zero-point-four-five-two-four — plus five points. Both headline benchmarks improved together on one dual-tower stack. Tiered gating and parse-miss logging prevented false wins; we have a living config index for handoff.

Broader impact: I took stock Qwen3-VL-8B from failing exam-grade time-series reasoning to roughly ninety-point-five percent TSExam and forty-five-point-two percent TSRBench on the public north star. Open loaders, scripts, eval protocol. ImagenTime to dual-tower VLM is a deliberate research line, not two unrelated projects.

Honest limit: plus five on TSRBench from stock is real but still below the proprietary frontier; hard reasoning slices and the trillion-scale gap remain. Stage C GRPO is next. The lesson I still use: name the right baseline, tier eval like release gates, deliver both benchmarks — then chase hard slices. Same discipline for multimodal finance docs at scale: staged alignment, task fine-tune, slice metrics before ship.

### Short version (~90 sec)

Baseline **Qwen3-VL-8B**: TSExam **0.618**, TSRBench **0.402**. I built dual tower, two-stage curriculum, tiered eval on the same backbone. Delivered **3ep**: **0.905 / 0.452** — plus twenty-eight and plus five points. Features ship only on aggregate eval gates. Lesson: name the stock baseline, both benchmarks, eval gates before claim.


---

# Invent and Simplify: ImagenTime — time series as images

**Leadership Principle:** Invent and Simplify  
**Project:** ImagenTime (NeurIPS 2024)  
**Status:** Draft v3 — DOC L6  
**Target length:** ~850 words (body) · **~8 min spoken** (descriptive primary)

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

### Spoken script (~8 min)

I was senior author on ImagenTime at Ben-Gurion University — generative modeling for time series from short synthetic benchmarks through ultra-long real-world sequences. The users were researchers and practitioners who needed realistic synthetic data for forecasting, anomaly detection, and simulation. The field was split in a frustrating way: strong models for short sequences, heavy bespoke architectures for long sequences, rarely one framework that could share code — and almost no reuse of the rapid progress happening in vision diffusion. That operational fragmentation was the ecosystem problem I cared about, not just another benchmark point.

After we had a strong VAE-based generator, the safe path was incremental improvement on that line, or building bespoke time-series diffusion — custom U-Nets, sequence-specific modules, more complexity every time length grew. I mapped three costs of that default before committing to either. On length: longer series meant heavier architectures for diminishing returns; short and long rarely shared one stack. On maintainability: every custom time-series model duplicated samplers and training recipes that vision had already solved at production quality. On speed: the standard denoising sampler needed on the order of a thousand model calls per sample — too slow to explore honestly at scale. I also considered non-invertible image tricks from the time-series classification literature. They can look fine visually but fail generation because you cannot decode back to a faithful series. The strategic question was whether we were capped by modeling or by representation — and whether simplification could beat complexity, not just match it.

My objectives were testable and tied to those costs. Beat strong time-series-specific diffusion baselines on short- and long-sequence metrics. Handle ultra-long series in one framework without a new custom architecture per length regime. Reuse vision diffusion so only the middle diffusion block is learned — encode and decode stay closed-form. And cut sampling from about a thousand model calls to a few dozen without measurable quality loss.

I challenged the default and named the alternatives I rejected. Incremental VAE was safe but capped. Bespoke TS diffusion was the community norm with rising complexity. I questioned whether we needed either if representation was wrong. The risk was real: reviewers and peers expect time-series-native models; a representation bet could destroy temporal structure silently if I did not validate inverses carefully.

I reframed the problem as representation and ran a disciplined de-risk loop before any diffusion spend. I surveyed time-series-to-image maps systematically. Line graphs were efficient but mostly blank pixels — rejected. Gramian angular fields use diagonal storage and do not scale to long sequences — rejected on ultra-long traffic and air-quality data. Folding and other maps from the literature were reasonable but weaker on average in our ablations than the two I kept. I committed to two invertible transforms with closed-form inverses: delay embedding, which was strong on short and ultra-long series, and short-time Fourier transform, which was strong on long periodic data. I validated inverse recovery on local spikes, long-range periodicity, and cross-channel structure before spending GPU weeks on diffusion.

Operationally I simplified the stack: encode, diffuse, decode — only diffusion is learned. No parallel custom time-series U-Net to maintain. When Karras EDM appeared in vision with strong quality at few steps, I pushed to adopt it here — about thirty-five model calls versus a thousand with the older sampler. That was not plug-and-play: aggressive fast settings hurt quality until I tuned the noise schedule and sampling parameters. That separation matters when I tell the results story — representation fixed length scaling; the sampler fix fixed iteration cost. Reuse also meant new vision samplers could be tested by configuration, not by rewriting time-series code.

The pivot was unconventional for a NeurIPS diffusion paper. I aligned co-authors with a proof of concept, not a slide deck. I ran small ablations showing structure preserved and benchmark lift over the incremental VAE line, then persuaded the team to stop investing in another bespoke architecture. I prefer to change direction with data — same habit I use today when eval slices regress and a mix has to die.

Results mapped cleanly to objectives. On quality, plus fifty-eight percent short-sequence discriminative score versus time-series diffusion baselines; plus one hundred thirty-three percent ultra-long classification — representation drove length scaling, not a bigger U-Net per regime. On unified length: twenty-four-step synthetics through seventeen-thousand-step traffic and eleven-thousand-step air-quality series by switching delay embedding versus STFT, not rebuilding the model. On simplification: we dropped a parallel TS diffusion codebase and shared vision infrastructure. On speed: roughly thirty times fewer model calls — a sampler change, separate from the representation win.

Broader impact: practitioners can generate long series with standard vision stacks instead of thousand-step custom models. NeurIPS twenty-twenty-four validated the result externally. Long-term leverage — and this is why I still tell this story in a VLM interview — the same representation instinct drives my dual chart-plus-delay encoding work on TSRBench. ImagenTime was generation; the VLM project is reasoning on the same bet that one view of sequential data is never enough. That is a research line, not a one-off trick.

What I would do differently with hindsight: publish the ablation kill criteria earlier as a checklist for collaborators — invertibility, slice recovery, ultra-long image size — so the team could reject transforms without waiting on me. That is the habit I am building now in the VLM eval protocol: encode the judgment in the process, not just in my head.

The lesson I still use: before building a bigger custom model, test whether representation lets you reuse mature adjacent tooling — with invertibility checks and slice metrics, not headline scores alone. For FinTech, the analogy is direct: tables, text, and numbers on a payment document — one view loses information. Pick the view first, then route or fine-tune. Do not cargo-cult bespoke extractors per document type.

### Short version (~90 sec)

Senior author on ImagenTime. Rejected incremental VAE and bespoke TS diffusion caps. Surveyed transforms — killed line graphs and GAF on length; committed invertible delay embedding and STFT after ablations. Reused vision diffusion; EDM cut ~1000 to ~35 model calls once tuned. Plus fifty-eight percent short, plus one-thirty-three percent ultra-long. Pattern now drives VLM dual tower. Lesson: abstraction before architecture.


---

# Ownership: Killed synthetic TR mix — per-task gates before promote

**Leadership Principle:** Ownership  
**Project:** Time-series VLM — TSRBench reasoning gap (Anchor B)  
**Status:** Draft v2 — DOC L6 (post AI review)  
**Target length:** ~750 words (body) · **~8 min spoken** (descriptive primary) · table for prep only

---

## Title

I set slice-level promotion gates — and killed a mix when the target task regressed exactly five points

## Outline

Our benchmark had plateaued near **46%** while **reasoning** sat near **29%**. I targeted **temporal relations**, built tiered synthetic exam data, and set **−3 pp overall / −5 pp per-task** gates **before** training — then **killed** the recipe when **TR fell 26.9% → 21.9%** despite a better reasoning average and **+7 pp** wins on other tasks.

## Ecosystem

At Ben-Gurion University I lead the **evaluation and training-direction** workstream on a time-series **vision-language** reasoning project. My formal goal was to improve reasoning scores on **TSRBench**; I also took responsibility for **promotion criteria** because the lab had no reliable way to stop slice regressions from hiding inside average gains. The team included me, a student who ran larger **8B** training jobs from my recipe, and lab members who used my readouts to decide which recipes earned the next **GPU** cycle. I recommend what ships, what dies, and what needs more study before we spend eight-GPU weeks again.

## Issue

Overall **TSRBench** had **plateaued near ~46%**. Proprietary systems sit in a **46–55%** band with a much stronger **reasoning** category — we were near **29%** on reasoning tasks. The risk was not “we need more data.” The risk was promoting a recipe because the **average** moved while the **target slice** got worse — wasting the next GPU cycle and eroding trust in our eval process. I manually reviewed reasoning items and chose **temporal relations (TR)**: weak scores, but the operations looked addressable — **segmentation**, **ordering**, **multi-hop** layouts over many segments.

## Objectives

**Goal:** Improve reasoning starting with **TR**, using tiered synthetic training examples (simple seg/ordering → complex multi-hop), not another blind data bucket.

**Guardrails (set before training):**

- **−3 pp** on **TSRBench overall** vs current best → do not promote.
- **−5 pp** on **any reasoning subtask** → do not promote.

**Execution:** I train **0.8B** validation; student runs **8B** on my recipe; **I** own the per-task readout and promote/kill recommendation.

## Actions

I designed two phases of **synthetic exam-style** data: phase one taught basic **segmentation and ordering**; phase two added **multiple hops** and ordering across **eight or more segments**. I wrote the failure gates **before** anyone launched the large run so we could not talk ourselves into a bad promote afterward.

I trained the **0.8B** model myself, then had a student run **8B** using my exact data recipe. I remained accountable for evaluation. I added a **per-task reasoning table** to the promotion readout — overall score and reasoning average were no longer enough to approve a mix.

The difficult part came after eval. The **reasoning average** rose **29.5% → 31.2%**. Two tasks gained about **seven points** each — the kind of headline that makes a recipe look ready for the next cycle, especially after **8B** GPU time was already spent. In lab review, that aggregate could have passed as progress. But **TR** — the task we designed the data for — dropped **26.9% → 21.9%**, **minus five points exactly**, hitting the gate I had set. **Numeric reasoning** also fell **3.4 points**. I recommended **against promotion** and stopped this synthetic path so we would not spend another large run on a recipe that had already damaged the target behavior.

## Results

**Prep table (do not read aloud in interview):**

| Task | Control | + synth | Δ (pp) |
|------|---------|---------|--------|
| reas avg | 29.5 | 31.2 | +1.7 |
| **TR** | **26.9** | **21.9** | **−5.0** |
| NR | 35.2 | 31.8 | −3.4 |
| AR / IR | — | — | +7.3 / +7.0 |

**Spoken summary:** Reasoning average **+1.8 pp**; two tasks **~+7 pp**; **TR −5.0 pp** (gate fired); **NR −3.4 pp**.

- Mix **not promoted** — avoided committing the **next GPU cycle** to a failing recipe.
- I updated the lab’s evaluation template: every reasoning experiment now reports **overall, reasoning average, and each subtask** against **pre-declared gates** — not aggregate movement alone.
- **TR remains open**; this synthetic lever was wrong, not the ambition. Deeper task-coverage work followed (separate Dive Deep story).

## Learnings and Improvements

Define **slice-level floors before training** and treat a **target-task regression** as a failed experiment even when the average improves. Targeted synthetic data can boost unrelated tasks while hurting the slice you aimed at — that is distribution shift. The durable outcome was the **promotion process**, not a TR win on this run.

---

### Spoken script (~8 min) — **use this in interview**

At Ben-Gurion University my formal role was main developer of the VLM stack, but the ownership moment was that I took responsibility for promotion criteria. My formal assignment was to improve reasoning scores on TSRBench — a multi-task benchmark that spans perception, forecasting, decision-making, and reasoning across thousands of problems. But the lab had not formalized how to stop a recipe when headline averages moved while a target slice regressed. We had been making GPU-heavy training decisions from aggregate benchmark movement, so I made myself accountable not just for running experiments, but for recommending what ships, what dies, and what needs deeper study before we commit another eight-GPU week.

When I looked at where we stood, the picture was clear but uncomfortable. Overall TSRBench had plateaued near forty-six percent on our best dual-tower stack — competitive on perception and forecasting in places, but not where proprietary systems were pulling ahead. Proprietary VLMs sat in a forty-six to fifty-five percent band, and they were meaningfully stronger in the reasoning category — where we were only around twenty-nine percent on the reasoning bracket average. That gap was the bottleneck, not raw perception. I had already delivered headline lifts on TSExam and overall TSRBench in the architecture story; this chapter was specifically about whether we could close reasoning without breaking the evaluation discipline that got us there.

The failure mode I cared about was not “we need more data.” It was promoting a recipe because the reasoning average moved, or because two unrelated tasks jumped, while the slice we had actually targeted regressed. That would waste the next GPU cycle — an eight-GPU week is not a free experiment in our lab — and teach stakeholders to trust the wrong signal in the weekly readout.

I did not pick the target task from a spreadsheet. I manually reviewed reasoning items on the benchmark — read the questions, traced what operation the model had to perform, and compared error patterns across subtasks. I chose temporal relations — TR — as the first lever. TR was weak, around twenty-seven percent on our control model, but when I read the items, the underlying operations looked bridgeable: find segments in a time series, put them in order, handle multi-hop layouts where you reason across eight or more segments. Numeric reasoning and interval reasoning were also weak, but TR had the clearest path through synthetic exam-style data. That was a hypothesis I could test with a tiered generator rather than another blind data bucket.

Before anyone launched a large run, I wrote two guardrails into the experiment plan. No more than a three-point drop on overall TSRBench versus our current best — do not promote. No more than a five-point drop on any individual reasoning subtask — do not promote. I designed the synthetic data in two phases on purpose. Phase one taught basic segmentation and ordering with simpler exam-style examples. Phase two added multiple hops and ordering across longer segment chains. The idea was tiered curriculum, not dumping synthetic volume and hoping the average moved.

I trained the smaller zero-point-eight-billion validation model myself. That let me iterate quickly on the data recipe before we spent real GPU budget. Then I had a student run the eight-billion model using my exact recipe — same phases, same mix — and I remained accountable for the evaluation readout and the promote-or-kill recommendation. I also changed what “evaluation” meant for this line of work. I added a per-task reasoning table to the promotion artifact. Overall TSRBench and the reasoning average were still reported, but they were no longer sufficient to approve a mix.

When results came back, the headline numbers looked like progress — and that is exactly why the gates mattered. The reasoning average improved from twenty-nine-point-five to thirty-one-point-two percent. Two tasks — arithmetic reasoning and interval reasoning — jumped about seven percentage points each. After an eight-billion run that had already consumed GPU time, that is an easy story for a lab update: average up, big wins on two slices, ready for the next cycle.

But TR — the task we had designed the synthetic data for — went from twenty-six-point-nine to twenty-one-point-nine. Minus five points exactly. That fired the gate I had written before training, not after. Numeric reasoning also fell three-point-four points. In lab review, I recommended against promotion. The difficult part was not the arithmetic. It was that without the per-task table, the average gain and the seven-point wins on AR and IR would likely have made this mix look viable for another large run. We would have spent more GPU time reinforcing a recipe that had already damaged the behavior we were trying to fix.

The mix was not promoted. That avoided committing the next GPU cycle to a failing path. More durably, I updated the lab’s evaluation template so every later reasoning experiment reports overall score, reasoning average, and each subtask against those pre-declared floors — not aggregate movement alone. TR remains an open problem; this synthetic lever was wrong, not the ambition. We redirected to deeper task-coverage analysis, which is a separate story.

The lesson I took forward is direct: define slice-level floors before training, and treat a target-task regression as a failed experiment even when the average improves. Targeted synthetic data can boost unrelated tasks — arithmetic and interval reasoning in this run — while hurting the slice you aimed at. That is distribution shift in practice, not a mysterious benchmark quirk. The durable outcome was the promotion process, not a TR win on this run. Temporal relations stayed on the roadmap, but with a different diagnosis: we needed task coverage and alignment analysis, not more of the same synthetic recipe.

### Short version (~90 sec)

My formal role was main developer for the VLM stack, but the ownership moment was that I took responsibility for promotion criteria. Our TSRBench result had reached about **46%**, which was strong against open-source and specialist models, but slicing showed reasoning was still weak — around **29–30%**, close to the **25%** random baseline. I decided the next meaningful step was not another small aggregate gain, but understanding and improving reasoning, starting with temporal relations, where we were at **26.9%**.

I knew the risk of over-focusing on one task, so before training I set hard regression gates: no more than **−3 pp** on overall TSRBench and no more than **−5 pp** on any reasoning subtask. I curated a TR-focused synthetic subset and tested it two ways: a short fine-tune on Stage B, and a full Stage B retrain from Stage A. The short fine-tune failed. The retrain was harder to judge: reasoning average improved about **+1.8 pp**, and AR/IR improved around **+7 pp**, but TR dropped **26.9 → 21.9**, exactly hitting the kill gate.

I killed that data path. The pressure was that the aggregate result looked like progress, and we had already spent compute, but the hypothesis had failed on the slice it was meant to fix. The durable result was a process change: our reasoning readouts now include overall score, reasoning average, and each reasoning subtask against pre-declared gates. My lesson was that ownership means protecting the objective, not defending an experiment.


---

# Dive Deep: TSRBench reasoning audit — three regimes, targeted coverage

**Leadership Principle:** Dive Deep  
**Project:** Time-series VLM — reasoning gap diagnosis (Anchor C)  
**Status:** Draft v1 — DOC L6  
**Target length:** ~800 words (body) · **~8 min spoken** (descriptive primary)

---

## Title

I audited every TSRBench reasoning task — and rebuilt training around three failure regimes instead of more data volume

## Outline

After operator-based synthetic data **regressed TR by five points** (see Ownership story), I stopped stacking buckets and **audited all reasoning tasks** on TSRBench. I classified gaps into **domain knowledge**, **operator depth**, and **task-specific formats** — then ran a two-track fix (ops + format conventions) that shows **~+5 pp** preliminary lift on **0.8B** with cleaner per-task error patterns.

## Ecosystem

At Ben-Gurion University I am **project lead** on a multimodal vision-language system for time-series reasoning — chart and delay-embedding inputs fused into one LLM that answers exam-style questions with text. Our north-star benchmark is **TSRBench**: thousands of problems across **perception, reasoning, forecasting, and decision-making** in fourteen domains including finance. Perception and headline scores had moved with the dual-tower stack (see Deliver Results); **reasoning** remained the weak bracket — roughly high twenties to low thirties percent while proprietary systems were stronger. I owned the diagnosis: which reasoning failures were fixable with training coverage versus which required domain knowledge a small model cannot carry.

## Issue

The obvious lever was more synthetic reasoning data. I had already mapped **seven or eight shared operators** — value extraction, segmentation, ordering, multi-hop layouts, trend and seasonality reads, and related primitives — that appeared across multiple TSRBench reasoning tasks. If I could generate exam-style examples for those operators at increasing difficulty, I expected a broad lift. I trained on that augmented mix and hit the **pre-declared gates** from our eval protocol: **temporal relations (TR) dropped more than five points** versus control. The reasoning average looked better on some slices; the target task got worse. I **did not ship** that mix (Ownership story) — but killing a bad recipe is not a diagnosis. The real question was *why* some tasks improved while TR regressed, and what we were actually missing across **numeric reasoning, entity reasoning, arithmetic reasoning, temporal relations**, and the rest of the reasoning bracket.

## Objectives

1. **Taxonomize failures:** Audit every reasoning task on TSRBench and classify gaps — not “add more data.”
2. **Step 1 — operator depth:** Extend synthetic coverage for the **seven–eight operators** already identified, with harder compositions.
3. **Step 2 — format and conventions:** Build synthetic data that teaches **task-specific formats** the model had never seen in TSExam (expected highest ROI).
4. **Step 3 — domain knowledge:** Incorporate domain context where a **0.8B** model can realistically absorb it; defer seismology-style background gaps.
5. **Validate on 0.8B first;** 8B runs in progress; per-task error analysis, not headline average alone.

## Actions

I spent several days on a **manual task audit** — read items task by task, tagged what operation the model had to perform, and compared error patterns to our training coverage in TSExam. That work split failures into **three regimes**.

**Regime 1 — missing domain knowledge:** Some tasks assume background the model does not have — seismology is a concrete example. A zero-point-eight-billion model will not reliably learn Richter-scale intuition from a few synthetic plots. I flagged these as **out of scope for Step 1–2** and reserved them for Step 3 or larger models.

**Regime 2 — operator depth:** Many tasks are compositions of primitives I had already named — simple segmentation and value reads scaling to harder multi-hop ordering. Failures here looked like **insufficient span and difficulty** in training, not missing perception. Our model already handled basic perception — extraction, segmentation, trend and seasonality reads — but stumbled when reasoning chains got longer.

**Regime 3 — unique formats and conventions:** Some tasks fail because the model does not know the **notation or scale** the question uses — for example the **Goldstein scale** in earthquake-intensity style items. That is not a bigger U-Net problem; it is a **coverage gap** — the format never appeared in training.

Before building more data, I wrote down what I believed was already solved: **perception-level time-series understanding** was largely in place from Stage A and TSExam perception slices. What remained was **reasoning composition, format literacy, and selective domain context** — not another blind multiplier on training volume.

I executed **Step 1 and Step 2** first because I expected format-and-convention coverage to be the best ROI — teach the model scales, labels, and answer templates it would see on TSRBench but not in our legacy exam mix. Step 1 deepened operator generators; Step 2 added synthetic items that introduced those missing formats explicitly. I held Step 3 for domains where a small model could not close the gap from data alone.

I trained the **0.8B** validation model on the new recipe and pulled **per-task** readouts the same way I had for the killed mix — so I could see whether we fixed the right failure modes.

## Results

**Preliminary (0.8B vs `stageb-weak11k` control):**

| Metric | Control (`reason-sbmix-weak11k`) | + audit data + Stage C | Δ |
|--------|----------------------------------|------------------------|---|
| TSRBench overall | **0.382** | **0.405** | **+2.3 pp** |
| TSRBench reasoning | **0.245** | **0.255** | **+1.0 pp** |

- **8B evaluation still running** — not claiming north-star promotion yet.
- **Per-task error analysis:** “Missing operation” failures dropped to a **minimum** on several slices; remaining errors look like **wrong reasoning on correctly parsed items** — closer to the control’s failure mode on hard items, not random format collapse.

**Diagnosis outcome (durable):**

- Three-regime taxonomy now drives what we generate — not “more reasoning bucket.”
- Step 2 (formats/conventions) prioritized over blind operator volume after the TR regression lesson.
- **Next:** widen span and coverage of the Step 1–2 generators; explore **Step 3** domain packs and **Stage C** gold-level **VRT** reinforcement where we have reliable labels.

## Learnings and Improvements

When progress stalls on a benchmark bracket, **instrument the tasks before adding data**. Headline reasoning average and bucket mixes hid a TR regression; the audit showed **three different failure types** that need **three different fixes**. Operator generators alone are not enough if the model has never seen the task’s format. I still treat **domain knowledge** as a separate lane — honest scope for model size matters. Same habit I would use on finance docs: slice errors by **field type, format, and domain** before scaling synthetic extraction.

---

### Spoken script (~8 min)

I am project lead on a multimodal time-series reasoning project at Ben-Gurion University. We teach a vision-language model to answer exam-style questions about plots and delay-embedding views of time series — not just classify shapes. Our north-star benchmark is TSRBench: thousands of problems across perception, reasoning, forecasting, and decision-making, spanning fourteen domains including finance. By the time I focused this story, we had already lifted headline scores with the dual-tower architecture — TSExam and overall TSRBench moved on stock Qwen3-VL-8B. The bracket that was still weak was reasoning — high twenties to low thirties percent on the reasoning tasks, while stronger proprietary systems were ahead. I decided to concentrate there because that was where the north star would break or hold for real exam-grade use.

My first attempt was the natural one: I had identified seven or eight operators that kept showing up across reasoning tasks — value extraction, segmentation, ordering, multi-hop layouts over segments, trend and seasonality reads, and a few related primitives. The hypothesis was simple. If I generate synthetic exam-style data that exercises those operators at increasing difficulty, I should lift multiple tasks at once. I built that augmented reasoning mix and ran it through the same eval discipline we use for promotion — per-task tables, not just averages. The mix failed a hard gate: temporal relations dropped more than five points versus control. I killed that recipe — that is the Ownership story — but the Dive Deep question was what to do after the kill. A negative result without diagnosis would just send us to another blind bucket.

So I stopped generating and audited. I went through the reasoning tasks on TSRBench systematically — numeric reasoning, entity reasoning, arithmetic reasoning, temporal relations, and the rest of the bracket. I read the items, tagged the operation each one required, and compared that to what our TSExam training mix actually covered. That took several days, but it changed the plan. Failures were not one thing. They fell into three regimes.

First, missing domain knowledge. Some tasks assume background a small model will not pick up from a few synthetic charts — seismology is the example I use in interviews. You are not going to teach Richter-scale intuition to a zero-point-eight-billion model with a handful of plots. I marked those for a separate Step 3 or for larger models, not for operator spam.

Second, operator depth. A large share of tasks are compositions of the primitives I had already named — start with simple segmentation and value reads, scale to harder multi-hop ordering. Here the model was not missing perception. We already had decent value extraction, segmentation, and basic trend and seasonality reads from earlier curriculum work — caption alignment, CaTS, TSExam perception slices. It failed when the reasoning chain got longer or the composition got harder — a coverage span problem, not a vision problem. That is an important distinction I only got by reading errors item by item: the chart was often parsed correctly; the chain broke on step three or four.

Third, unique formats and conventions. Some items fail because the model has never seen the notation the question uses — the Goldstein scale in earthquake-intensity style tasks is the concrete example. The model might segment the series fine and still pick the wrong answer because it treats the scale as arbitrary numbers. That is not fixed by training a bigger custom stack. It is fixed by putting that format into synthetic training data explicitly — teach the convention, not just more plots. That was my bet for the best return on investment after the TR regression showed that operator volume alone can lift the wrong tasks.

From that taxonomy I split the work into three tracks. Step one: deepen the operator generators I already had — more span, harder compositions. Step two: synthetic data that introduces missing formats and conventions — scales, labels, answer templates that appear on TSRBench but not in our legacy exam mix. Step three: domain-specific knowledge where a small model can realistically absorb it. I executed step one and step two first because I expected format literacy to be the highest-ROI fix after the TR regression taught us that operator volume alone can help the wrong tasks.

I trained the zero-point-eight-billion validation model on the new recipe and evaluated the same way I had on the killed mix — per task, with error patterns tagged, not just accuracy. Results are still preliminary, but directionally encouraging. On zero-point-eight-B versus `stageb-weak11k` control I am seeing **plus two-point-three points** on TSRBench overall (**0.382 to 0.405**) and **plus one point** on the reasoning bracket (**0.245 to 0.255**). Eight-billion runs are still in progress — I am not claiming north-star promotion yet. What matters more at this stage is the per-task shape of errors. I tag whether a miss is a missing operation — the model never attempted the right primitive — versus a reasoning error on a parsed item. On several slices, missing-operation failures dropped to a minimum compared to control. Remaining errors look more like the model reasoning incorrectly on items it at least parsed — closer to the control’s failure mode on hard questions, not random format collapse. That is the signal I was diving for: we are finally training on the right gaps.

Next steps are to widen span and coverage in the step one and step two generators, then selectively pursue step three domain packs and Stage C gold-level VRT reinforcement where we have reliable labels. The durable outcome is not just the preliminary two-point-three overall lift — it is that we diagnose before we scale. When a benchmark bracket stalls, I instrument the tasks, classify the failure regime, and match the data fix to the gap. Operator buckets, format conventions, and domain knowledge are different levers. Same discipline I would use on payment or filing extraction: do not cargo-cult volume until you know whether the miss is format, field coverage, or domain context.

### Short version (~90 sec)

Reasoning weak on TSRBench. Operator-based synthetic mix regressed TR five points — killed. I audited every reasoning task; three regimes: domain knowledge, operator depth, format/convention. Step 1 deepened operators; Step 2 added missing formats like Goldstein scale. Preliminary **+2.3 pp** overall / **+1.0 pp** reasoning on 0.8B vs `stageb-weak11k`; 8B WIP. Per-task misses from missing ops near zero; errors now look like reasoning, not format collapse. Lesson: instrument tasks before scaling data.


---

# Learn and Be Curious: Learned diffusion from the SDE up — turned a gap into a research line

**Leadership Principle:** Learn and Be Curious  
**Project:** Diffusion models (foundation work → ImagenTime / ImagenFew)  
**Status:** Draft v1 — DOC L6 (pre AI review)  
**Target length:** ~800 words (body) · **~8 min spoken** (descriptive primary) · backup variety story (non-VLM)

---

## Title

I admitted my group didn't understand diffusion, then learned it from the stochastic-process foundations up until I could build original work on top

## Outline

Diffusion models were becoming foundational, but I couldn't make real modeling decisions with them. I built a disciplined learning loop — math from the SDE view, hands-on reimplementation of fragile codebases, paused to fill a differential-equations gap — and turned that into **seven** diffusion papers at ICML/ICLR/NeurIPS plus reusable infrastructure behind **ImagenTime** and **ImagenFew**.

## Ecosystem

A few years into my faculty role at Ben-Gurion University, my group had a solid track record in sequential disentanglement, but diffusion models were appearing everywhere — in the papers I reviewed, in the literature, and in the work my strongest students kept flagging as the most exciting direction. I was not assigned this; I chose to make diffusion a core competency before it became table stakes. I drove the learning personally — I set the curriculum, worked the math myself, and wrote code alongside two students (Ilan and Nimrod) rather than delegating the understanding to them.

## Issue

The honest baseline was that none of us — including me — actually understood diffusion beyond surface level. The methods were mathematically heavy, tied to stochastic processes, and moving fast. The real risk was shipping shallow work: reusing a library, getting a plausible result, and never knowing *why* it worked or where it would break. The competing pressure was real — investing months in a fast-moving area could produce nothing publishable if the field moved on first. But staying superficial had a worse failure mode: irrelevance, missed top-tier publications, and weaker standing for funding and students.

## Objectives

**Goal:** Reach genuine mastery of diffusion — theory *and* implementation — to the point where I could make original modeling decisions, not just run existing code.

**Self-imposed bar:**

- Understand the **SDE / score formulation**, not just the discrete DDPM recipe.
- Own a **clean, correct, extensible codebase** instead of fighting fragile public ones.
- Convert the learning into **novel research**, for time series and beyond.

## Actions

I ran weekly three-to-four-hour deep-dive sessions, but treated them as hands-on technical work, not a reading group: focused paper/blog reading, rigorous walkthroughs of the math, joint coding, and idea generation in the same session.

The process quickly exposed a real gap. Once we framed diffusion through stochastic differential equations, I realized my students had little exposure to differential equations and almost none to stochastic ones — and I needed that footing to reason about samplers and noise schedules. Rather than paper over it, I paused the original plan and rebuilt the curriculum to detour through ODEs and SDEs first. It slowed us down and felt like falling further behind the field, but it changed how I could reason about *why* methods worked instead of copying them.

The second obstacle was tooling. The diffusion codebases at the time were poorly structured and fragile — small changes broke things unpredictably. Instead of working around the friction, I decided to own it: I cleaned up and rewrote key components to isolate the core ideas — the sampler, the noise schedule, the training objective, the evaluation — into a framework that stayed correct while making experimentation fast. That cost effort with no immediate paper, but it became the foundation everything else built on.

## Results

- We could read diffusion papers critically — understand the design choices and spot where new ideas fit — instead of being intimidated by them.
- The effort produced **seven diffusion papers**, all at top-tier venues (**ICML, ICLR, NeurIPS**).
- The cleaned-up codebase and intuition became reusable infrastructure — directly behind **ImagenTime** and **ImagenFew**, and every diffusion project since.
- New MSc students now ramp up far faster because I can teach the fundamentals clearly and the framework already exists; the expertise also led to talk and collaboration invitations inside and outside BGU.

## Learnings and Improvements

Curiosity only compounds when it's paired with a disciplined learning system: read the theory, implement the core pieces, debug the failure modes, then build. In fast-moving fields the easy path is to chase trends and accumulate surface knowledge. I learned to slow down, ask *why* a method is built the way it is, and invest in the foundational assumptions before building on them. I apply the same loop now to any new area — including the VLM work — where I'd rather own a clean reimplementation than inherit a fragile one.

---

### Spoken script (~8 min)

A few years into my faculty role at Ben-Gurion University, diffusion models were showing up everywhere — in papers I was reviewing, in the literature, and in the work my strongest students kept pointing to as the most exciting direction. My group already had a solid track record in sequential disentanglement, but I had to be honest with myself: I did not understand diffusion deeply enough to make real modeling decisions. I could have treated it as a trend to monitor from a distance, or delegated the learning to students and stayed at the level of high-level supervision. I chose the harder path instead. I decided to make diffusion a core competency before it became table stakes, and I drove that learning personally — I set the curriculum, worked through the math myself, and wrote code alongside two students, Ilan and Nimrod, rather than outsourcing the understanding.

The baseline problem was not lack of exposure. Diffusion was already in my teaching — students were presenting DALL·E and related work — and I was seeing it constantly in reviews. The problem was depth. The methods are mathematically heavy, tied to stochastic processes, and they were evolving extremely fast. There were already many papers, each building on subtle theoretical assumptions. If I approached the topic superficially, I would get shallow work: reuse a library, obtain a plausible-looking result, and never know why it worked or where it would break. That was the operational risk I cared about.

There was also a real strategic risk on the other side. Investing months in a fast-moving area could easily fail to produce publishable results if the field moved on before we caught up. I was aware of that. Still, I felt the long-term upside justified the bet. If I could truly understand diffusion models, it would open entirely new research directions. If I failed to master them, I would be building on sand in a field that was clearly becoming foundational.

My objective was explicit and ambitious. I was not aiming for familiarity. I wanted to close my own knowledge gap — theory and practice — to the point where I could confidently produce novel research in that domain, for time series tasks or otherwise. I set three bars for myself. First, understand the SDE and score formulation, not just the discrete DDPM recipe everyone was copying. Second, own a clean, correct, extensible codebase instead of fighting fragile public implementations. Third, convert the learning into real research output, not a private reading group that never shipped.

To do that, I organized weekly meetings with Ilan and Nimrod, but I designed them as intensive technical sessions, not casual seminars. Each meeting ran three to four hours. I combined focused reading of blogs and papers, rigorous walkthroughs of the mathematical foundations, joint coding, and brainstorming of applications and research ideas in the same sitting. The point was to keep theory and implementation tied together. If I could not implement a concept, I did not yet understand it well enough to build on it.

Very quickly, that process surfaced a gap I could not ignore. One of our early realizations was that diffusion models can be framed using stochastic differential equations. That insight was powerful — and immediately problematic. My students had limited exposure to differential equations, and almost none to stochastic ones. I needed that footing myself to reason about samplers and noise schedules rather than treating them as magic hyperparameters. Ignoring the gap would have limited our understanding to recipe-following. So I deliberately paused the original plan and redesigned the curriculum to include a detour through the basics of ordinary differential equations and SDEs. That slowed us down in the short term. At times it felt like we were falling further behind the field rather than catching up. But it fundamentally changed how I could read papers and make design choices — I could ask why a method was built the way it was, not just whether the numbers moved.

The second major obstacle was tooling. At the time, most diffusion codebases were difficult to work with — poorly structured, fragile, and clearly not written with extensibility in mind. Progress was slow and error-prone. Even small changes could break things unexpectedly. Rather than working around that friction, I decided to own it. I established a parallel process where I cleaned up the code, rewrote key components to isolate core ideas, and built a framework that preserved correctness while making experimentation feasible. I separated the sampler, the noise schedule, the training objective, and the evaluation logic so we could change one piece without breaking the whole stack. That required extra effort and did not immediately translate into a paper. But it created a foundation I could build on safely — and that foundation later supported projects like ImagenTime and ImagenFew.

Over time, the structured learning process paid off in ways that went beyond confidence. I was no longer intimidated by diffusion papers. I could read them critically, understand why things were done the way they were, and identify where new ideas could fit. That effort has led, to date, to seven papers on diffusion models, all accepted to top-tier venues such as ICML, ICLR, and NeurIPS. The theoretical understanding and the cleaned-up codebase continue to serve me in every diffusion-related project since. New MSc students can ramp up much faster because I am comfortable teaching the fundamentals clearly and because the infrastructure is already in place. The expertise also led to invitations for talks and collaborations both within Ben-Gurion and externally.

The lesson I took from that experience is direct, and I still apply it. Curiosity becomes impactful only when it is paired with a disciplined learning strategy. In fast-moving fields, it is easy to chase trends or accumulate surface-level knowledge. I learned instead to slow down, ask why things are done the way they are, and invest in understanding the foundational assumptions before trying to build on them. Read the theory, implement the core pieces, debug the failure modes, then build. That is the same loop I use now when I enter a new technical area — including the vision-language work on time-series reasoning — where I would rather own a clean reimplementation than inherit a fragile one I cannot reason about under pressure.

### Short version (~90 sec)

Diffusion was becoming foundational but I couldn't make real modeling decisions with it. I set an explicit goal — master it from the SDE view and own a clean codebase. I ran weekly deep dives, paused to fill a differential-equations gap even though it slowed us down, and rewrote the fragile public code into an extensible framework. That turned into seven diffusion papers at ICML/ICLR/NeurIPS and reusable infrastructure behind ImagenTime and ImagenFew. The lesson: curiosity only compounds when paired with a disciplined learn-implement-debug loop.


---

# Apple Health AIML — behavioral cards

Default length about 90 seconds. If they lean in, add the why and the reflection. Do not restart the plot.

1. Technical disagreement — ImagenTime, native 1D vs image-space modeling

What it should demonstrate: Technical disagreement resolved through hands-on experimentation. I proposed a non-obvious direction, took the strongest objections seriously, tested them directly, and let evidence—not seniority—decide.

Card

CONTEXT. In ImagenTime, we wanted one generative framework that could handle time series ranging from short benchmark sequences to more than 17,000 time steps. After establishing a strong VAE baseline, the conventional next step was to build a stronger native 1D generative model. I proposed a less obvious direction: transform the series into a structured 2D representation and reuse mature image-diffusion machinery.

TENSION. Several collaborators preferred staying in 1D, and their objection was technically strong. Mapping a sequence into 2D expands the representation, increases the cost of every diffusion step, and can make numerical information harder to recover. Their concern was that we might pay substantially more compute just to force a time series into an image architecture.

My hypothesis was that the additional representation cost might be worth it because the transformation would expose useful structure and let us reuse a much stronger and more mature generative stack. But at that point, both positions were hypotheses.

MY ACTION. Rather than argue that the image prior would compensate, I proposed three tests that could kill my own idea early:

1. Reconstruction fidelity: can we recover the original time series accurately enough from the representation?
2. Modeling value: does the representation actually improve generative quality at small scale?
3. Compute: is the quality improvement large enough to justify the expanded representation and additional cost?

I screened candidate representations before committing to expensive diffusion training. Simple line plots were extremely sparse as images. Gramian angular fields had unattractive scaling properties for long sequences, so I dropped those directions. Delay embeddings and STFT-like representations survived the reconstruction tests.

I then built a small proof-of-concept comparison rather than asking us to maintain two complete research stacks. I looked at whether the representation remained faithful, whether the image-space model actually gained quality at small scale, and whether the additional spatial cost was defensible.

The important part was that this was an experiment where my preferred 2D hypothesis could fail cheaply. Only after it survived those tests did we commit to the larger training campaign.

WHY. The real question wasn't "Are images better than sequences?" It was whether the representation exposed enough useful structure, and let us reuse enough mature diffusion machinery, to compensate for its larger footprint.

I wasn't trying to convince the collaborators that 2D was right. I was trying to design an experiment where either their hypothesis or mine could lose cheaply.

RESULT. It didn't fail. The evidence was strong enough that we committed to the image-space route.

What was particularly convincing was that the approach generalized across almost three orders of magnitude in sequence length. The same basic framework handled sequences from 24 to 17,544 time steps. On short-series unconditional generation, we improved the discriminative score over prior diffusion models by about 58% on average. On the long and ultra-long benchmarks, the classification score improved by about 133% on average.

There were also concrete cases where the gains were quite large. For example, on MuJoCo the discriminative error was 0.007 compared with 0.059 for DiffTime. On the 17,544-step Traffic dataset, classification was 0.684 versus 0.630 for LS4, while prediction error was 0.138 versus 0.170.

The work became ImagenTime at NeurIPS 2024.

I keep the scientific claims separate, though. Those results show that the overall image-space approach worked very well across very different sequence lengths. They do not prove that 2D representations are intrinsically superior to every possible 1D model.

REFLECTION. The collaborators' compute objection actually improved the work. It forced me to treat representation size, reconstruction fidelity, and computational cost as first-class technical constraints rather than focusing only on downstream quality. It also caused me to reject some of my own candidate representations before expensive training.

Today I would go one step further and quantify that Pareto tradeoff upfront: reconstruction error, representation size, training FLOPs, sampling cost, and downstream quality before committing the full run.


Spoken (~90 sec)

One technical disagreement that changed how I make architecture decisions happened during ImagenTime.

We were building a generative model for time series ranging from very short sequences to more than seventeen thousand steps. The conventional direction after our VAE baseline was a stronger native 1D model. I proposed something less obvious: map the time series into a structured 2D representation and reuse mature image-diffusion machinery.

Several collaborators pushed back, and I thought their objection was valid. The 2D representation could be much larger, every diffusion step would cost more, and the transformation could make numerical information harder to recover.

So rather than argue that the image prior would compensate, I proposed three tests that could kill my idea early: can we reconstruct the signal faithfully, does it actually improve generative quality at small scale, and is the compute tradeoff acceptable?

I screened the representations first. Line plots were mostly empty pixels. Gramian angular fields scaled poorly to long sequences, so I dropped them. Delay embeddings and STFT-like representations survived the reconstruction checks.

Then I built a small proof of concept rather than having us build two complete stacks. The important thing was that my own 2D hypothesis could fail cheaply.

It didn't. The evidence was strong enough that we committed to the image-space route. What convinced me was that the approach generalized across almost three orders of magnitude in sequence length. The same basic framework handled sequences from 24 to over 17,000 steps. On short-generation benchmarks we improved the discriminative score over prior diffusion models by about 58% on average, and on long and ultra-long benchmarks the classification score improved by about 133%.

That became ImagenTime at NeurIPS.

The lesson wasn't that 2D is universally better than 1D. It was that representation determines which modeling priors become available—and when there's a genuine architecture disagreement, I try to design the cheapest experiment where my own idea can lose.


If they lean in

Keep three technical questions separate:

1. REPRESENTATION
Does the mapping preserve the information needed for the task?

2. GENERATIVE PRIOR
Does putting the signal into that representation expose useful structure or allow the model to exploit machinery that would otherwise be unavailable?

3. END-TO-END EFFICIENCY
Is the resulting quality improvement worth the representation expansion and computational cost?

Do not use a later sampling-efficiency improvement as evidence for the representation hypothesis. Sampling efficiency is primarily question #3.


Follow-ups

What exactly was the disagreement?

Whether the benefits of image-space modeling could justify the representation expansion, additional compute, and potential loss of numerical accessibility compared with staying native in 1D.


What did you personally do?

I proposed the image-space hypothesis, screened the candidate representations, defined the reconstruction/quality/cost tests, and built and analyzed the small proof of concept before we committed to the larger experiments.


Why did collaborators prefer 1D?

It preserved the native structure, avoided representation expansion, and was computationally lower-risk. Their objection was legitimate.


Did you convince them?

I would say the experiment did. My contribution was designing a test where either hypothesis—including mine—could lose before we made the expensive commitment.


Did their disagreement actually change what you did?

Yes. It made reconstruction fidelity, representation size, and compute explicit decision criteria. More importantly, I dropped some of my own candidate representations because they failed those tests.


So were you right and they were wrong?

I wouldn't frame it that way. Their concern identified a real cost that remained in the successful system. What the experiments showed was that, in the regimes we tested, the modeling benefits outweighed that cost.


What evidence made you comfortable scaling it?

It wasn't one final benchmark number. First the representation survived the reconstruction test. Then the small-scale generative experiment showed enough benefit to justify further investment. The final evidence was that essentially the same framework worked from 24 to 17,544 steps and performed strongly across both short and ultra-long benchmarks.


Give me one concrete result.

On MuJoCo, for example, the discriminative error was 0.007 compared with 0.059 for DiffTime. At the other extreme, Traffic has 17,544 time steps, and we achieved classification of 0.684 versus 0.630 for LS4, with prediction error of 0.138 versus 0.170.


Could the gains simply come from architecture or capacity rather than the representation?

Partly, yes. The experiments establish the effectiveness of the overall approach, not that every improvement is causally attributable to the representation itself. A cleaner mechanistic experiment would control representation, architecture capacity, and initialization separately.


Then how do you know the representation mattered?

We have evidence from reconstruction behavior, representation screening, and downstream comparisons, but I distinguish that from a strong causal claim. Today I would run a representation × architecture × initialization factorial experiment if identifying the mechanism itself were the objective.


Why not just build the strongest possible 1D model?

That's the natural counterfactual. We compared against native time-series approaches, but I wouldn't claim we exhausted every possible 1D architecture. The decision we needed to make was whether there was enough evidence to invest in the image-space direction, not whether we had proved a universal superiority theorem.


Why not line plots?

They are intuitive for humans, but they are extremely sparse as images. For this generative formulation, most pixels contain no signal, so they were unattractive from both representation and computational perspectives.


What would have made you abandon the 2D approach?

Poor reconstruction, no small-scale quality advantage, or a compute increase large enough that the end-to-end Pareto point was worse than the native alternative.


What would you do differently today?

I would formalize the Pareto analysis earlier: reconstruction error, representation size, FLOPs, sampling cost, and downstream quality. And if resources allowed, I would run a more controlled representation-versus-architecture study to separate the mechanism from the overall system result.


The strongest sentence

"I wasn't trying to convince them that 2D was right. I was trying to design an experiment where either their hypothesis or mine could lose cheaply."


Do not

- Say "my students disagreed with me."
- Say "I set the research vision and convinced them."
- Say "2D is better than 1D."
- Say the representation preserves all information.
- Treat the final paper result as proof that the original mechanistic explanation was correct.
- Claim that every gain came specifically from the representation.
- Make the story primarily about leadership or resource allocation.

IC framing

"I proposed a non-obvious technical direction, personally tested the strongest objections, dropped parts of my own proposal that failed, and only scaled the idea after a cheap experiment showed that the tradeoff was worth pursuing."

---

2. Wrong hypothesis — delay-only numerical collapse

What it should demonstrate: Scientific maturity. Updating a research hypothesis that was motivated by your own previous success rather than defending it after the evidence changed.

Card

CONTEXT. ImagenTime had given me strong evidence that delay embeddings are useful representations for time-series generation. When I moved to multimodal reasoning, I hypothesized that the same representation would transfer more broadly—that a delay-based tower could expose both dynamical structure and enough numerical information for an LLM to reason about amplitude and values.

TENSION. This mattered architecturally. If delay alone captured both, the chart tower was unnecessary complexity. But there was a scientific risk in my reasoning: I was taking an inductive bias validated for generation and assuming it would transfer to a very different objective—numerical question answering.

MY ACTION. I turned that assumption into a matched representation bakeoff: delay-only, chart-only, and dual, with the same data and evaluation protocol. The numerical slice was deliberately useful because it could falsify the strongest version of my hypothesis. When delay failed badly, I did not try to explain away the result or discard the representation entirely. I narrowed the hypothesis and asked where its information was actually useful, then examined task-level failure modes and representation/encoder controls.

WHY. Representation quality is task-conditional. A representation can preserve structure that is excellent for generative modeling while making another property—such as absolute scale—difficult for a pretrained model to recover. The relevant question became not “Is delay a good representation?” but “Which information does each representation make accessible to this model for this task?”

RESULT. On ChatTS numerical reasoning, delay-only was roughly 0.17, chart-only roughly 0.71, and dual roughly 0.79. So the strong version of my hypothesis was clearly wrong: delay was not functioning as a general numerical interface. At the same time, delay remained useful on tasks where dynamical/topological structure mattered, including anomaly and causality slices on TSExam. We also found that simply adapting the native Qwen vision encoder was insufficient for the delay representation: qwendelay was about 0.60 versus 0.83 with DINO. Taken together, the results are consistent with complementary representations, but I would not claim that dual > chart alone proves complementarity.

REFLECTION. The mistake was not using delay embeddings. It was generalizing too aggressively from one objective to another. Today I would formulate the hypothesis from the beginning as task-conditional and design the falsifying slices earlier: absolute-value questions for numerical accessibility, and anomaly/dynamics tasks for structural information. More broadly, a representation that succeeds on one objective becomes a hypothesis—not a prior fact—when the objective changes.

Spoken (~90s)

One hypothesis I got wrong came directly from my own previous success.

In ImagenTime, delay embeddings worked very well as a representation for time-series generation. When I moved to multimodal reasoning, I generalized that result too aggressively. I expected a delay-based tower to expose not only dynamical structure but also enough numerical information for the language model to answer questions about values and amplitudes.

That mattered architecturally. If delay could do both, adding a chart representation was probably unnecessary complexity.

So rather than keep reasoning from ImagenTime, I set up a matched representation bakeoff: delay-only, chart-only, and dual, with the same data and evaluation protocol. Numerical reasoning was a particularly useful falsifier because the hypothesis made a very clear prediction there.

And it failed badly. On ChatTS numerical questions, delay-only was around 0.17, compared with roughly 0.71 for chart-only and 0.79 for dual.

At that point I changed the hypothesis rather than trying to rescue it. The useful question wasn’t “Is delay a good time-series representation?” It was “What information does this representation make accessible for this objective?” Delay remained useful on slices involving dynamical or topological structure, such as anomaly and causality, while the chart representation made scale, amplitude, and trend much more accessible.

We also found an encoder interaction: simply adapting Qwen’s native vision encoder to delay representations was substantially weaker than using DINO—about 0.60 versus 0.83. So representation and pretrained encoder prior weren’t separable in the simplistic way I initially imagined.

The lesson I took is that an inductive bias validated on one objective doesn’t automatically transfer to another. A successful representation becomes a new hypothesis when the task changes. Today I’d design the task-specific falsifiers much earlier.

If they lean in

Keep three claims separate:

1. Delay-only is poor for numerical QA in our setting.
    Strongly supported by the bakeoff.
2. Delay preserves/exposes information useful for dynamics/topology.
    Supported by its behavior on relevant task slices.
3. Delay and chart are genuinely complementary.
    Dual > chart is evidence consistent with this, but not sufficient by itself to establish the mechanism.

A stronger complementarity experiment would intervene on each representation and evaluate tasks constructed to require information uniquely accessible from each view, ideally with capacity/token-budget controls.

Also separate representation from encoder prior: the Qwen-vs-DINO result says the encoder matters substantially; it does not prove that one representation is intrinsically superior.

Follow-ups

They ask	You say
What exactly did you get wrong?	I generalized an inductive bias from generation to numerical reasoning. Delay was useful, but not as a general-purpose numerical interface to the LLM.
What evidence changed your mind?	The cleanest falsifier was ChatTS numerical: roughly 0.17 delay-only versus 0.71 chart-only. That gap was too large to explain away as noise.
Why keep delay after that?	Because the failure was task-specific rather than universal. It remained useful on tasks emphasizing dynamical/topological structure, and dual improved over chart alone. That justified investigating complementarity rather than simply deleting it.
Does 0.79 vs 0.71 prove complementarity?	No. It establishes an empirical gain from the combined system. Complementarity is an interpretation supported by the different slice behavior; a stronger causal test would control capacity and intervene on each representation.
Couldn’t dual simply win because it has more tokens or capacity?	Yes—that is an alternative explanation that the basic ablation doesn’t completely eliminate. I would capacity/token-match the control and then use representation shuffling or corruption on tasks where each view should matter.
Why didn’t you see this earlier?	I had evidence that delay was effective for generation and let that prior become too strong. I should have asked earlier which properties the new objective required the representation to expose.
What does the Qwen-vs-DINO experiment tell you?	That representation and encoder prior interact. A representation being information-rich does not mean an arbitrary pretrained encoder can readily extract that information.
Could a better delay encoder eventually match the chart?	Absolutely. Our result is about accessibility under the tested architecture and training regime, not an information-theoretic statement that delay cannot encode numerical values.
What’s the general lesson?	Representation quality isn’t absolute. I now ask: what information is preserved, what information is readily accessible to the chosen encoder, and what information does the downstream objective actually require?
How would this affect a new sensor problem?	I wouldn’t assume either charts or delay embeddings transfer. I’d define the information the task requires, propose several encodings, and run an early representation bakeoff before committing the larger model.

Do not

Say “delay doesn’t contain numerical information.” It may contain it; the model failed to access/use it effectively.

Say “dual proves complementarity.” Say the evidence is consistent with complementary failure modes.

Say “DINO proves delay is better.” The experiment shows an important representation × encoder interaction.

Say “ImagenTime proved delay is the right TS representation.”

Say images preserve all information.

Use the synthetic-TR kill story here.

Senior-IC framing:
“I let a successful result from my previous work become too strong a prior. When a task-specific falsifier contradicted it, I narrowed the claim, investigated where the representation was actually useful, and changed the architectural interpretation rather than defending the original hypothesis.”

---

3. Technical ownership under ambiguity — TSRBench reasoning audit

What it should demonstrate: Taking an ambiguous model failure and turning it into a concrete technical diagnosis and experiment sequence. Hands-on error analysis before scaling.

Card

CONTEXT. After the first synthetic reasoning mix failed its temporal-relations gate, reasoning was still the weakest part of TSRBench. We knew that simply adding plausible synthetic data could move the average while hurting the capability we were actually targeting.

TENSION. The failure was ambiguous. There were several technically plausible explanations: insufficient coverage of reusable temporal operations, compositions that were too deep, unfamiliar benchmark formats, missing domain knowledge, or even a representation limitation. Those explanations require different fixes. Another large training run without distinguishing them would tell us very little even if the score moved.

MY ACTION. I went back to the benchmark itself and audited the reasoning failures item by item. For each one, I looked at what operation the question required, whether that operation or format appeared in our training distribution, and whether the model appeared to have parsed the relevant time-series information correctly.

That gave me three useful working categories:

1. Knowledge gap: the task requires domain information the model does not have—for example specialized seismology concepts.
2. Operator/composition gap: the relevant primitives are present, but the model fails when it has to combine them into a longer reasoning chain.
3. Format gap: the underlying operation is within scope, but the benchmark expresses it through notation or conventions absent from training.

I then mapped those categories back to training interventions. Rather than mix everything together again, I generated targeted examples for the operator/composition and format gaps and used the 0.8B model as a fast experimental probe before repeating the experiment at 8B.

I also changed my evaluation from reasoning-average-only to failure-type and task-level readouts, including distinctions such as missing operation versus correctly parsed input followed by incorrect reasoning.

WHY. I wanted the next experiment to answer a diagnostic question, not just produce another score. If targeted operator data improved the failures I had classified as operator gaps but not the knowledge cases, that would support the diagnosis. If the predicted slices did not move, I would revise the taxonomy rather than immediately scale the intervention.

RESULT. On the first controlled 0.8B experiment, TSRBench overall moved from roughly 0.382 to 0.405, and reasoning from 0.245 to 0.255. I would not treat those aggregate gains as the main result. More useful was that several errors associated with missing operation coverage improved, while a residual class remained where the model appeared to parse the item correctly but still failed the reasoning.

That gave us a more specific next experiment and enough evidence to test the targeted recipe at 8B rather than use the large model for exploratory search.

REFLECTION. I should have done the item-level audit before generating the original synthetic mix. The benchmark already contained evidence that “reasoning” was not one failure mode. I spent compute learning something that careful error analysis could have exposed earlier. Now, when a heterogeneous benchmark stalls, I try to inspect failures first, formulate competing explanations, and make the next training run discriminate between them.

Spoken (~90s)

After I killed the first synthetic reasoning mix, the harder question was why reasoning was still weak.

There were several plausible explanations. Maybe we did not have enough examples of the temporal operations. Maybe the model knew the primitives but failed on longer compositions. Maybe it lacked domain knowledge. Maybe some benchmark formats were simply unfamiliar. Or maybe the representation itself was still limiting us.

Rather than generate another mixture, I went back to the benchmark and audited the failures item by item.

For each question, I looked at what operation it required, whether that operation and format existed in our training data, and whether the model appeared to have parsed the relevant time-series information correctly.

That separated the failures into three useful regimes. Some were knowledge gaps, like specialized domain concepts I wouldn’t expect a 0.8B model to infer from a few plots. Some were operator-depth failures: the primitives were familiar, but the model broke when it had to compose them. And some were format failures: the reasoning itself was within scope, but the notation or convention was absent from training.

I then turned those diagnoses into targeted training interventions rather than mixing them together. I used the 0.8B model as a fast probe and changed the evaluation so I could see whether the specific failure class I was targeting actually moved.

The first controlled run moved overall TSRBench from about 0.382 to 0.405 and reasoning from 0.245 to 0.255. But the more useful result was qualitative: several missing-operation failures improved, while another class remained where the model seemed to parse the input correctly but still reasoned incorrectly.

That made the next experiment much more specific.

What I learned is that when a benchmark stalls, I shouldn’t immediately ask “what should I train next?” I should first ask “what different failures are hiding inside this average, and what experiment would distinguish them?”

If they lean in

The story is a diagnostic loop:

failure → inspect examples → competing explanations → targeted intervention → predicted slice movement → revise or scale

The taxonomy is a working hypothesis, not ground truth.

The 0.8B model is a screening instrument, not evidence that 8B must behave identically.

Keep these failure types distinct:

Knowledge gap
The necessary external/domain information is absent.

Operator/composition gap
The ingredients are available, but the reasoning procedure fails.

Format gap
The capability may exist, but the input convention does not expose it in a familiar way.

Follow-ups

They ask	You say
What did you personally do?	I audited the benchmark failures, compared them with our training distribution, built the working taxonomy, designed the targeted interventions, and ran/analyzed the 0.8B screening experiments.
Why not just generate more reasoning data?	Because the previous experiment showed that more plausible data could improve the average while hurting the target capability. I wanted to know which failure I was treating before generating more.
Why not just scale to 8B?	Scaling would make the experiment more expensive without resolving the ambiguity. I used 0.8B to test whether an intervention moved the predicted failure class before repeating it at scale.
How did you know something was a format failure rather than reasoning?	I looked for cases where the underlying operation was represented in training and the model could handle analogous questions, but failed when the same operation appeared through an unfamiliar convention or notation.
How did you distinguish perception from reasoning?	Where possible, I checked whether the model correctly identified the relevant series structure or intermediate quantities before the final reasoning step. If it could parse the evidence but still produced the wrong relation, that pointed downstream of representation.
Could your taxonomy be wrong?	Absolutely. It was a hypothesis about the errors. That’s why I tied each category to an intervention with a predicted effect. If the intended slice didn’t move, I would revise the diagnosis.
Why 0.8B?	Fast iteration. I was testing whether the intervention had the expected directional effect, not trying to establish the final model quality.
What did the +2.3 points establish?	Very little mechanistically by itself. The useful evidence was which error classes moved. The aggregate gain told me the intervention wasn’t obviously destructive; the slice behavior told me whether my diagnosis had predictive value.
Why defer domain knowledge?	It was a qualitatively different intervention. I first wanted to test failures we could directly connect to missing operators or formats rather than mix broad knowledge augmentation into the same experiment.
What happened next?	The targeted small-model result justified testing the recipe at 8B. I would keep the 8B result separate until it is complete.
What would you do differently?	Audit first. I would sample and classify benchmark failures before designing the first synthetic-data generator.

If they ask where the leadership is

Don’t force it into a management story:

“For me the ownership was technical. We had several plausible directions, and rather than choose one based on intuition, I went into the failures myself, turned the explanations into testable interventions, and gave us a much cleaner basis for the next large experiment.”

If there was no interpersonal disagreement, say so. The ambiguity itself is enough.

Do not

Say “I allocated the 8B budget.”

Say “I aligned the team around my taxonomy.”

Say the taxonomy was objectively correct.

Say 0.8B predicts 8B.

Claim the representation was ruled out unless you actually established that.

Make 0.382 → 0.405 the success of the story.

Retell the TR kill. One sentence of context is enough.

IC framing

“After a failed intervention, I went into the benchmark myself, decomposed the aggregate failure into testable hypotheses, built targeted interventions, and used a cheap model to determine which diagnosis deserved a larger experiment.”

---

4. Kill decision — synthetic TR mix

What it should demonstrate: Senior-IC judgment under sunk cost. Pre-committed decision criteria. Protecting the hypothesis from being redefined by a favorable aggregate metric.

This is probably the strongest card. Vincent already expects it.

Card

CONTEXT. On TSRBench, overall performance had plateaued around 46%, while reasoning remained much weaker, around 29%. I chose temporal relations as a targeted intervention because the failure looked decomposable into teachable operations: segmentation, ordering, and multi-hop composition. I built a tiered synthetic training mix specifically around those operations.

TENSION. The expensive 8B run produced a result that was easy to misread. Aggregate reasoning improved from roughly 29.5% to 31.2%, and two other reasoning tasks gained about 7 points each. The compute was already spent, several metrics looked better, and the natural temptation was to call the experiment promising and scale the same recipe.

MY ACTION. Before launching the run, I had written promotion gates tied to the risks I cared about: no more than −3 pp overall and no more than −5 pp on any reasoning subtask. I also changed the evaluation readout so every reasoning task appeared explicitly rather than being hidden inside an average. The result that mattered was immediate: temporal relations—the task the synthetic data was designed to improve—fell from 26.9% to 21.9%, exactly −5.0 pp. Numeric reasoning also fell 3.4 pp. I recommended that we kill that training mix and stop spending compute on that direction.

WHY. The experiment was testing a specific hypothesis: this synthetic curriculum improves temporal-relation reasoning without materially damaging the rest of the system. Once the target task regressed substantially, gains elsewhere could not be used to redefine success after the fact. They might reflect redistribution of capacity or training-distribution shift, but they did not validate the hypothesis we had actually tested.

RESULT. We did not promote the mix. More importantly, the failure changed how I ran the next reasoning experiments: aggregate reasoning, overall score, and every reasoning slice became first-class promotion criteria. Temporal relations remained an open research problem; what we killed was the lever, not the objective. That directly led to the item-level reasoning audit in the next story.

REFLECTION. I would make one change upstream: perform the failure taxonomy before generating the first synthetic curriculum. The decision gate did exactly what it was supposed to do; the avoidable mistake was spending compute before we had decomposed the benchmark carefully enough. I still use predeclared slice-level floors when optimizing heterogeneous systems because aggregate metrics are especially dangerous when an intervention is targeted.

Spoken (~90s)

This is a case where the aggregate metric told us to keep going, but the experiment we had actually designed told us to stop.

On TSRBench, overall performance had plateaued around forty-six percent, and reasoning was much weaker, around twenty-nine. I picked temporal relations as the first targeted intervention because the failures looked teachable: segment the series, order events, then compose those operations into multi-hop questions. We built a tiered synthetic curriculum around exactly that.

Before launching the expensive run, I wrote the promotion criteria down. No more than a three-point regression overall, and no more than a five-point regression on any reasoning subtask. I also required the readout to show every reasoning task individually, because I did not want an average to hide a localized failure.

The 8B result was actually quite tempting. Reasoning average moved from about 29.5 to 31.2, and two other reasoning tasks improved by roughly seven points. After spending the GPU budget, that is exactly the kind of result you can rationalize into “let’s scale it further.”

But temporal relations—the task the data was specifically designed to improve—went from 26.9 to 21.9. Minus five points. Numeric reasoning also regressed.

So I recommended killing that mix.

The important part for me was that I did not let the favorable aggregate result redefine the hypothesis after seeing the data. The experiment was supposed to improve temporal relations without damaging the rest of the system, and it failed that test. The other gains might have been useful signals, but they belonged to a different hypothesis.

We stopped that recipe and moved to an item-level reasoning audit to understand the failure modes before generating more data.

What I would change today is upstream, not the kill decision: I would do the taxonomy before the first synthetic run. The predeclared gates worked exactly as intended.

If they lean in

Keep three decisions separate:

1. Was the run interesting? Yes. It changed several behaviors.
2. Did it validate the intended hypothesis? No. The target task regressed materially.
3. Should the entire research direction be abandoned? No. Kill the intervention, not the objective.

The senior-IC point is not “I was strict about metrics.”

It is:

I defined the decision rule before seeing the result, so sunk cost and attractive secondary metrics could not silently change what counted as success.

Follow-ups

They ask	You say
Why kill it if reasoning average improved?	Because the intervention targeted temporal relations, and temporal relations regressed from 26.9 to 21.9. The average improvement was scientifically interesting, but it did not validate the hypothesis we had tested.
Could the gains on the other tasks still make the mix useful?	Potentially, but that would be a new experiment. I would isolate the components responsible for those gains rather than promote a mixture that materially damaged its intended target.
Who wanted to keep it?	There wasn’t necessarily a person arguing aggressively for promotion; the result itself created that pressure. After an expensive run, positive averages and seven-point gains make continuation very easy to rationalize. The predeclared gate removed that discretion.
Why were the gates set at −3 and −5?	They were large relative to the improvements we were trying to earn and to the baseline level of those tasks. A five-point drop on a task in the mid-twenties is not noise I was willing to trade away for a modest average gain.
How do you know −5 wasn’t noise?	I would distinguish the promotion decision from a statistical-mechanism claim. The gate was a risk-control criterion: a regression that large was enough to prevent automatic promotion. If we wanted to understand whether it was systematic, that justified a targeted follow-up rather than another large run.
Why not just reduce the synthetic-data weight?	That’s a reasonable next experiment, but it would be a new hypothesis: that the direction is useful but the mixture coefficient is wrong. I did not want to continue scaling the original recipe after it failed its own gate.
Why not train longer?	Same issue. More compute does not repair a failed causal interpretation. First I wanted to know whether we had the wrong mixture, wrong task decomposition, or wrong data generator.
What did you personally own?	I defined the intervention, ran the small-model experiments, set the promotion gates, structured the per-task evaluation, and made the promote/kill recommendation. A collaborator reproduced the recipe at 8B.
How did you get buy-in?	The criteria were agreed before we had the result, and the per-task readout made the regression explicit. I did not need to argue that my interpretation was preferable after the fact.
What happened next?	I stopped treating “reasoning” as one failure mode and audited the benchmark item by item. That produced the operator-depth / format / domain-knowledge decomposition.
Was the synthetic-data idea itself wrong?	No. The specific curriculum and mixture were wrong for the target we had defined. Some of the positive secondary movement suggested synthetic data could still be useful if designed against a better failure taxonomy.
What would you do differently?	Error taxonomy first, generation second. The kill criterion worked; the expensive part was learning too late what categories of failure the benchmark actually contained.

Do not

Say “the average was misleading, so averages are bad.” Aggregate metrics are useful; they are just insufficient for targeted interventions.

Say “TR dropped, therefore the synthetic data caused distribution shift.” Distribution shift is a plausible explanation, not established fact.

Say “I killed synthetic data.” You killed that mix/recipe.

Turn this into a generic “ownership” story.

Present the thresholds as universal statistical truths. They were predeclared engineering/research risk criteria.

Retell the delay-only failure here.

Senior-IC framing:
“I defined success before seeing the expensive result. When the aggregate metric improved but the targeted capability crossed the predeclared failure floor, I refused to redefine the experiment post hoc, killed the intervention, and used the failure to redesign the next scientific question.”

---

5. Cross-functional collaboration — Bosch Haifa / real-world modality translation

WHAT THIS SHOULD DEMONSTRATE
Cross-functional collaboration across different technical expertise. I brought the
generative-modeling perspective; Bosch brought deep knowledge of the sensor system
and its real-world failure modes. I listened when their evidence challenged my
modeling assumptions, translated their operational constraints into an ML problem,
and worked with them toward a solution neither side would have reached independently.


CARD

CONTEXT.
I had an ongoing research collaboration with the Bosch Center for AI in Haifa around
modality translation: given observations in one modality, generate the corresponding
signal in another modality.

I was responsible for much of the generative-modeling side. We developed a latent
diffusion bridge framework with modality-specific representations and a shared
generative translation mechanism. On standard research benchmarks, the approach
worked very well.

The Bosch researchers had a different kind of expertise. They understood the actual
sensor systems, how the measurements were collected, and the failure modes that
appear in industrial data.


TENSION.
When we moved from the clean research benchmarks to Bosch's real sensor data,
performance degraded substantially.

My initial instinct was to view this mainly as a model-generalization problem:
perhaps we needed a stronger model, different regularization, or better training.

But discussions with the Bosch researchers changed that diagnosis.

They helped us understand that the real data violated assumptions that were almost
invisible in the benchmarks. Measurements could be irregularly sampled, noisy,
partially observed, and only imperfectly aligned across modalities.

That meant our abstraction itself was incomplete.

We had been thinking approximately:

    clean modality A -> modality B

whereas the actual problem was closer to:

    partial + noisy + irregular observations of A
                    ->
             useful estimate of B

That distinction changed what I thought we needed to solve.


MY ACTION.
I worked with the Bosch researchers to translate what they were observing in the
sensor pipeline into concrete modeling assumptions.

Rather than treating "the Bosch data is harder" as one generic domain-shift problem,
I tried to separate the sources of mismatch:

- irregular sampling,
- missing observations,
- measurement noise,
- and imperfect temporal correspondence.

On my side, I connected those constraints to our work on generative modeling of
irregular, noisy, and partially observed time series.

The important technical shift was that I stopped treating preprocessing as something
that should simply clean the industrial data until it looked like the benchmark.

For example, forcing irregular observations onto a clean regular grid can hide the
fact that some measurements were never observed and can create artificial temporal
precision.

Instead, we adapted the modeling formulation so that the observation process itself
was part of the problem: what was observed, when it was observed, and what information
was actually missing.

Throughout this process, I kept going back to the Bosch researchers with a concrete
translation:

    "If this is what the sensor is doing, then this is the assumption our model is
     currently making, and this is the experiment that should tell us whether that
     mismatch matters."

That gave us a shared technical language despite coming from different sides of the
problem.


WHY.
The key realization was that neither group had the complete diagnosis independently.

I understood the generative model and knew which assumptions it relied on.

The Bosch researchers understood the physical data-generation and measurement
process much better than I did.

If I had treated their observations merely as noisy data that needed preprocessing,
I would have optimized the wrong abstraction.

And if we had only described the sensor problems operationally, without translating
them into model assumptions, it would have been difficult to know what to change.

The collaboration worked because we connected those two views.


RESULT.
The robustness extensions substantially improved performance in the Bosch setting,
and the approach became a strong internal research baseline for subsequent work.

The collaboration also influenced my broader research direction. It helped motivate
work on modality translation and on generative modeling when time-series observations
are irregular, noisy, or incomplete.

I am careful about how I describe the impact: this was a research collaboration, so
I would not claim a Bosch product deployment that I did not observe. The concrete
impact I can defend is that we turned a method that looked strong on clean benchmarks
but struggled on their real data into a substantially more useful approach for their
setting.


REFLECTION.
The biggest thing I took from that collaboration is that benchmark generalization and
deployment generalization are different claims.

It also changed how I work with domain experts.

When someone who understands the data-generating process tells me that a model is
failing in a particular way, I don't treat that as an implementation detail outside
the ML problem. I try to translate it into:

    What assumption is my model making?
    Which real-world constraint violates it?
    What experiment would distinguish that explanation?

For me, that is the value of cross-functional work: not simply dividing tasks between
people with different expertise, but allowing expertise from another function to
change the technical problem I think I am solving.


======================================================================
SPOKEN VERSION — ~90 SECONDS
======================================================================

"One of my best examples of cross-functional collaboration is a long-running project
with researchers at the Bosch Center for AI in Haifa.

We were working on modality translation: generating one sensor modality from another.
I brought much of the generative-modeling perspective, and we developed a latent
diffusion approach that performed very well on standard research benchmarks. The
Bosch researchers, though, understood the actual sensor systems and industrial data
far better than I did.

When we moved to their real data, performance degraded substantially. My initial
instinct was to think of it as a model-generalization problem. But working through the
failures with Bosch changed my diagnosis. Their data violated assumptions that were
almost invisible in our benchmarks: sampling was irregular, measurements could be
missing or noisy, and modalities weren't always perfectly synchronized.

So I reformulated the problem. Instead of asking how to make their data look like our
clean benchmark, I started treating the observation process itself as part of the
modeling problem. I connected what Bosch was seeing to our work on irregular and
partially observed time series, and we translated each operational issue into a
modeling assumption and a testable intervention.

That substantially improved the approach on the Bosch setting and made it a strong
internal research baseline for subsequent work.

The part I value most is that neither side could have reached the same diagnosis
alone. I understood the model assumptions; Bosch understood what the sensors were
actually doing. The solution came from translating between those two views.

That experience changed how I approach cross-functional work. Domain expertise isn't
something I collect after designing the model. I want it early enough that it can
change the problem I think I'm solving."


======================================================================
IF THEY ASK: "WHAT DID YOU PERSONALLY DO?"
======================================================================

"My contribution was primarily on the modeling side. I helped design the generative
translation framework, and when it struggled on the Bosch data, I worked directly
through the mismatch between the assumptions in our model and the properties Bosch
was seeing in the sensor pipeline.

The important part wasn't simply tuning the model. I translated issues like irregular
sampling, missing observations, noise, and imperfect alignment into changes in the
generative formulation and into experiments we could use to test those explanations."


======================================================================
IF THEY ASK: "WHAT DID BOSCH CONTRIBUTE THAT YOU COULDN'T?"
======================================================================

"They had knowledge I simply didn't have: how the sensors and data-collection process
behaved in practice.

Looking only at the ML benchmark, I could see that performance had degraded. They
could explain why certain assumptions behind the benchmark didn't correspond to the
real measurement process.

That distinction mattered because otherwise I might have spent time increasing model
capacity or tuning optimization when the more fundamental problem was that our
observation model was wrong."


======================================================================
IF THEY ASK: "WHAT WAS DIFFICULT ABOUT THE CROSS-FUNCTIONAL PART?"
======================================================================

"The difficulty was that initially we described the same failure at different levels.

From my side, I was thinking in terms of distribution shift, representation, and
generative-model assumptions. From their side, the issues were concrete properties
of the sensor pipeline: this measurement arrives irregularly, this channel can
disappear, these two signals aren't actually synchronized as cleanly as the benchmark
assumes.

The useful step was translating between those descriptions. Once we could say,
'This sensor behavior violates this particular modeling assumption,' we could design
an experiment rather than just discuss the failure qualitatively."


======================================================================
IF THEY ASK: "WAS THERE A DISAGREEMENT?"
======================================================================

"I wouldn't characterize it as a major interpersonal disagreement. It was more an
initial difference in diagnosis.

My first instinct was to approach the degradation as a modeling/generalization
problem. Their knowledge of the sensor system made it clear that some of the problem
was more fundamental: the clean observation assumptions in our research setup did
not hold.

The important thing was that I changed my technical view based on their evidence
rather than trying to force the real data into the abstraction I had started with."


======================================================================
IF THEY ASK: "HOW DID YOU BUILD TRUST WITH THE OTHER GROUP?"
======================================================================

"I think the most useful thing was not pretending to know their domain better than
they did.

When they described a sensor issue, my job wasn't to immediately prescribe an ML
solution. I tried to understand the constraint precisely and then translate it back
into the assumptions of our model.

And in the other direction, I tried to make our modeling choices concrete enough
that they could challenge them. That created a much better loop than each group
working independently and exchanging results at the end."


======================================================================
IF THEY ASK: "WHAT WOULD YOU DO DIFFERENTLY?"
======================================================================

"I would involve the real observation process earlier.

We initially had strong benchmark results before fully stress-testing assumptions
like missingness, irregular sampling, noise, and imperfect alignment.

Today, especially for sensor or health data, I would define those deployment
conditions alongside the benchmark from the beginning and make them part of the
evaluation matrix.

That would expose assumption failures much earlier."


======================================================================
IF THEY ASK: "WHAT WAS THE IMPACT?"
======================================================================

"The robustness work substantially improved the approach in the Bosch setting, and
the resulting method became a strong internal research baseline for subsequent work.

I wouldn't claim downstream product impact that I didn't directly observe. The impact
I can defend is that Bosch brought us a real-data failure that our benchmark did not
capture, and together we turned that failure into a better modeling formulation and
a substantially stronger approach for their setting."


======================================================================
ONE-LINE L5 CROSS-FUNCTIONAL TAKEAWAY
======================================================================

"The strongest cross-functional collaborations I've had are not ones where different
groups simply divide the work. They're ones where another group's expertise changes
my technical understanding of the problem."

---

## 90-second cheat strip (memory only)

| # | One line |
|---|----------|
| 1 | 2D cost objection → invertibility + small POC → +58% / +132%; they bought the evidence |
| 2 | Delay should carry numbers → ChatTS 0.17 vs 0.71 vs 0.79 → delay is dynamics, not scale |
| 3 | After the kill, fog → three regimes → formats before domain; +2.3 pp 0.8B, 8B WIP |
| 4 | Average + AR/IR up; TR 26.9→21.9; pre-declared −5 pp; killed |
| 5 | Haifa, not Sunnyvale; latent bridge + contrastive/predictive; NeurIPS 2025; no ship claim |
| A | Ravel killed delay geometry → invariant + they own the test |
| B | NeurIPS: cut full 1D stack; screen then one 2D POC |

Practice: read each spoken block aloud once. Vincent mock: 1 or 4 first; keep 3 as the sequel to 4 if they ask “what happened after.” Sunday 9/6: speak A and B once (60s). Do not polish them into fifth and sixth 90s cards.

---

## Backup A — 60s — helping someone succeed (not a student-supervision story)

Use if asked: “Tell me about helping a colleague grow” / “coaching” / “mentorship.”  
**Hard rule:** do **not** open with PI, lab, or “my student.” The plot is a **technical block** you identified, a method you changed, ownership you left with them, and a result they produced.

**CONTEXT.** On the multimodal VLM stack, a collaborator was debugging why delay-embedding features looked wrong on multivariate series. Their loader flattened a `[C, T]` array into one long univariate. Delay geometry became garbage; dual-tower numbers on those tasks were noise.

**TENSION.** The obvious move was for me to take the collator and “just fix it.” That would have been faster for the next run and would have taught them nothing about the invariant.

**ACTION.** I showed the failure with one example: ravel concatenates channels in time, so the delay image is not a trajectory in R^C. I wrote the invariant we needed — *N series → N markers → N chart + N delay, channels stay channels* — and asked them to own the loader patch and a unit test that fails on ravel. I did not merge a silent fix.

**RESULT.** They landed the collator test. Multivariate delay stopped being a hidden confound. Later bakeoffs on those tasks became interpretable.

**REFLECTION.** Helping was changing the representation contract and giving them the test, not taking the file.

If they push “were they your student?”: *They were a collaborator on the codebase. The same move would apply to anyone stuck on a silent data bug. I do not treat this as management.*

---

## Backup B — 60s — deadline / execution under pressure

Use if asked: “difficult deadline” / “too much to do” / “how do you cut scope.”

**CONTEXT.** ImagenTime, NeurIPS cycle. We wanted one generative framework from short series to 17k steps. The conventional path was a stronger native 1D diffusion stack *and* the 2D image-space bet. There was not time or compute to do both at full fidelity.

**TENSION.** Shipping two incomplete stacks would have produced two weak papers’ worth of evidence and no discriminating comparison. The quality bar I cared about was: can we recover the series, and does 2D win at small scale?

**ACTION.** I cut the full 1D diffusion campaign. I kept a VAE baseline, a cheap representation screen (line plots and GAF died; delay/STFT-like survived invertibility), and one small 2D proof-of-concept. Full training only after those gates.

**RESULT.** The 2D path survived and became the paper. We did not get a polished 1D SOTA in that cycle. That was the cut.

**REFLECTION.** The deadline was met by **killing work that could not falsify the bet**, not by working longer on everything. If I redid it, I would pre-declare the screen as a kill criterion in writing even earlier.

Do not merge this with card 1. Card 1 is the disagreement. This card is **what you did not build** so the deadline held.
