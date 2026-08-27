# Bosch 20 min — previous-work Q&A (generative + Bosch)

**When:** after the 25-min VLM talk, before the 15-min coding walkthrough. **Thu 2026-08-27.**  
**Audience:** Shabnam (and whoever else is on the hour). They already heard the VLM. This block is *other* work, not a second talk.  
**Goal:** they leave thinking *he already does modality translation and frequency-aware generation with Bosch AI, as an IC, and wants that class of work inside RTC.*  
**Do not:** walk the CV, replay the talk, pitch forecasting FMs, name Apple, claim Haifa papers shipped in a BU.

Talk notes stay in [`talks/ts-vlm/2026-08-26_bosch-speaker-notes.md`](../../../talks/ts-vlm/2026-08-26_bosch-speaker-notes.md). Coding numbers stay in [`2026-08-26_take-home-submit.md`](2026-08-26_take-home-submit.md). Seat / reloc / one-model rewrites stay in [`2026-08-13_hm-screen-debrief.md`](2026-08-13_hm-screen-debrief.md).

---

## How to use the 20 minutes

They asked for **previous work**, not a bio. Default:

1. If they stay on the talk (dual tower, curriculum, TSRBench) — answer; don’t yank to papers.
2. If they ask “what else?” / Bosch / generative — **this file**.
3. If they ask a CV walk — **20s landing**, then stop. Do not offer UCLA, geometry, or the lab.

**Lead with LDDBM.** Synth-FAR if frequency / synthetic data. Edge-graph if traffic / ADAS scene structure. ImagenTime if they want the generative *line* behind the talk.

Say **I**. Bosch scientists were collaborators, not reports. Last author on all three Haifa papers = academic PI + technical collaborator, **not** Bosch FTE.

---

## 20-second landing (if they ask background / “other work”)

> Besides the VLM you just saw, the through-line is generative modeling for sequential and multimodal data — how you represent a signal, and how you map one modality into another. With Bosch Center for AI in Haifa I worked on a latent diffusion bridge for modality translation, frequency-aware synthetic time series, and score-based graph generation for traffic scenes. Different group from Sunnyvale. I want that class of work inside RTC, with the transfer bar you described.

Do **not** add PhD/UCLA/PI/students unless they ask.

---

## Bosch — BCAI Haifa, not her team

Collab is **Bosch Center for AI, Haifa** (Dotan Di Castro and colleagues). **Shir** intro’d; don’t narrate a Shir–Shabnam mix-up. Don’t imply you already sit on SoundSee / CR/RHI1-NA.

| Paper | Venue | One-line | When to pull |
|-------|-------|----------|--------------|
| **LDDBM** — *Towards General Modality Translation with Contrastive and Predictive Latent Diffusion Bridge* | NeurIPS 2025 | Shared-latent diffusion **bridge** between arbitrary modalities (no shared raw dimension). Contrastive alignment + predictive translation loss. | **Default.** Closest to her sensor+vision charter. |
| **Synth-FAR** — *A Synthetic Frequency-Autoregressive Driven Framework for Time Series Forecasting* | TMLR 2026 | Fourier diagnosis: models fail on mixed / unseen frequencies. Synthetics = AR + frequency mix; can augment or replace scarce real data. Faster/better than Kernel-Synth in that paper. | Frequency, labels scarce, FM data pipelines. |
| **Reviving Life on the Edge** | TMLR 2025 | Joint score-based **node + edge** graph generation. Traffic scenes as graphs; edges carry the interaction, not just topology. | ADAS / scene structure. Don’t call it a shipped ADAS stack. |

Authors (for “who did what,” not to recite): LDDBM equal-first **Nimrod Berman** (Bosch + BGU) and **Omkar Joglekar** (Bosch + TUM); you last. Synth-FAR: **Liran Nochumsohn** first; Bosch: Moshkovitz, Avner, Di Castro; you last. Edge-graph: Berman, Kosman, Di Castro; you last.

### LDDBM — spoken (~35s)

> Most diffusion is one modality. Modality translation is different: you have a paired source and target that may not even share a dimension — views to a 3D shape, low-res to high-res, and in principle a sensor to another sensor. LDDBM puts both in a shared latent space and learns a **denoising diffusion bridge** there, not a Gaussian prior in raw space. Contrastive loss keeps paired latents semantically aligned; a predictive loss makes the decoded target actually match. I framed that research problem with Bosch scientists as coauthors. I don’t claim I wrote every training loop. I also don’t know if a business unit picked it up — that was Haifa research, which is why I want to do this *inside* RTC.

If they ask architecture one level down (only if asked):

> Encode each modality, bridge in latent space with a domain-agnostic noise predictor, decode. Conditioning is cross-attention from the source latent. The point of the latent is that the two signals don’t have to be the same size or the same clock.

If they ask “would you run this on audio and a camera?”:

> That’s the job class — virtual sensing / translation when you have paired examples. I would not drop it in as the perception stack for *description*. Event detect might want a native encoder. Description and questions might want the VLM. Translation between sensors is where a bridge earns its keep. Bake off by task.

### Synth-FAR — spoken (~30s)

> We asked why forecasters fail when data is scarce. In frequency space the failure is specific: mixed frequencies, and frequencies they didn’t see in train. Synth-FAR builds a generator from autoregressive structure plus a frequency mix, using only the target sampling rate. You can mix it with real data or use it when real data is thin. It’s synthetic **for coverage**, not a fake north star — I’d still gate on a held-out real sensor set. I care about the frequency diagnosis and the generator design; I’m not claiming I ran every Chronos bakeoff in the paper.

Do **not** turn this into a Chronos-vs-LightGBM riff. If they hear “forecasting”: “That paper is a data-pipeline result for FMs. The *product* verbs here are still classify, describe, fuse.”

### Edge graphs — spoken (~25s)

> Most graph generators ignore edge attributes, or bolt them on after the topology. In a traffic scene the edge *is* the interaction — relative motion, not just who is next to whom. We generate nodes and edges jointly under a score-based model so those pieces stay coupled. It’s ADAS-adjacent generative research. I would not claim it is a driving stack.

### “Did Bosch put these in products?” (she asked this once)

Keep the honest line:

> I don’t know. Those were research collabs with Haifa, not Sunnyvale. I wouldn’t claim a BU transfer I didn’t see. That’s the reason this role is interesting: the success bar you described is whether a business unit can use it.

### “What did *you* do?” (PI trap)

> I was the academic PI and a technical collaborator, not a Bosch employee. On LDDBM I owned the research framing — why a latent bridge, why contrastive plus predictive, not a modality-specific architecture. On Synth-FAR the line I care about is the frequency failure mode and the synthetic generator. I don’t claim I implemented every loop. What I want now is to be the IC who owns architecture, experiments, and eval **inside** this team.

If they push “so you didn’t code it”: name one decision you actually made; if a piece was theirs, say so. Don’t inflate.

---

## Generative line (not Bosch) — the work behind the talk

Use this if they ask “before the VLM” or “you’ve done a lot of generation.” **Do not** list seven papers.

Through-line: **representation first, then a generative model you can actually sample.** Same instinct as dual-tower: one view of a series is not enough.

| Work | Venue | Pocket | Numbers you may say |
|------|-------|--------|---------------------|
| **ImagenTime** | NeurIPS 2024 | TS → invertible image → vision diffusion → back. **STFT** for long periodic / high-freq; **delay embedding** for short and ultra-long. Killed line graphs and GAF. EDM ~35 model calls vs ~1000. | **+58%** short discriminative vs TS diffusion; **+132%** ultra-long classification. One stack from 24-step to ~17k-step series. |
| **ImagenFew / data-scarce** | NeurIPS 2025 | Same image-diffusion idea when labels / series are thin. | **+55%** with **5%** of the data (CV setting in that paper). |
| **Irregular TS** | NeurIPS 2025 | Completion + masking; don’t pretend every sensor is uniformly sampled. | ~**70%** discriminative gain, ~**85%** compute cut — only if they ask irregular sampling. |
| **One-step distillation** | NeurIPS 2025 | Reverse process as an operator; distill a multi-step teacher to a one-step student. Proof the SDE view paid off. | Validated on **images**. Don’t invent FID/speedup. Don’t claim it shipped on Bosch sensors. |

### ImagenTime — spoken (~40s) — this is the gen answer they should hear

> The VLM uses two pictures of a series because ImagenTime already showed the representation is the bottleneck. I didn’t want a bigger time-series U-Net. I mapped the series to an invertible image, reused vision diffusion, and mapped back. Invertibility was the kill criterion — Gramian fields and line plots look like pictures but you can’t recover the signal. STFT won on long periodic structure; delay embeddings won on short and ultra-long. That’s the same split as high-frequency mics versus slow telemetry. Quality went up about 58% on short series and more than double on ultra-long versus time-series diffusion baselines, and sampling dropped from about a thousand model calls to a few dozen. I owned the representation bet and which transforms to kill. Co-authors ran a lot of the training sweeps.

### ImagenTime → her sensors (only if they connect it)

> I would not upsample a slow channel onto an audio grid. I would pick the renderer the way we picked STFT vs delay: by the physics of that sensor, then share the backbone. I have not run STFT inside the VLM you saw.

### Irregular / scarce — spoken (~20s)

> Real sensors drop samples. We treated irregularity as a first-class generation and completion problem, not as imputation you hide in preprocessing. Separately, in the data-scarce setting the same image-diffusion stack still moved quality with a few percent of the data. Synthetic and scarce are tools; a held-out real set is the gate.

### One-step — spoken (~15s)

> Sampling cost is a product constraint. I treated the reverse diffusion as an operator you can distill, so a student approximates many steps in one. That work is on images. I would bring the *habit* — cheap sampling as a requirement — not a checkpoint.

---

## LDDBM vs VLM (they will ask; you already have this)

> Different jobs. **LDDBM** maps A→B in a shared latent when you need translation or virtual sensing. The **VLM** answers questions and describes, with language and image context. I would not pick an ideology. Vibration event-detect might want a native encoder. Description plus a camera might want a VLM. Sensor-to-sensor might want a bridge. Frozen task suite, then bake off.

---

## Practice set (say these out loud once)

**Tonight: B1, B2, G1, B4.** Rest once.

### B1. “You’ve worked with Bosch — tell us about it.”

Landing + LDDBM 35s. Stop. Don’t dump all three papers unless they ask.

### B2. “How is that different from the VLM talk?”

LDDBM vs VLM. One sentence: talk = reason over a rendered series; LDDBM = generate / translate across modalities.

### B3. “Synth-FAR is forecasting. This team isn’t.”

> The *finding* is frequency: mixed and unseen bands. The *artifact* is a generator you can put in a foundation-model data mix. I would use that habit on vibration and audio vocabularies where labels are scarce. I would not walk in with a forecast head.

### B4. “What did you personally implement?”

IC verbs on ImagenTime (transforms, invertibility, EDM). On Haifa papers: framing + which losses / which failure mode; don’t steal first-author loops. “I want to own the loops here.”

### G1. “Walk us through your generative work.”

ImagenTime 40s. Offer LDDBM if they want multimodal. Do not recite seven venues.

### G2. “Why images / diffusion for time series at all?”

> Adjacent tooling was mature; TS-native diffusion was duplicating samplers. The risk was destroying time. Invertible maps were the test. Once that held, vision progress transferred for free.

### G3. “One encoding for all sensors?”

Shared backbone, different tokenizers / rates. STFT vs delay as the empirical proof. Don’t upsample. Same answer as panel 24–25; don’t say “her HM question.”

### G4. “A result that didn’t work.” (if they leave the talk)

VLM TR mix: average up, TR 26.9→21.9, killed. Or ImagenTime: fast EDM settings hurt until the noise schedule was tuned. Pick **one**.

---

## If they pull the rest of the CV

One clause, then return.

| They ask | You say | Then |
|----------|---------|------|
| PhD / UCLA / geometry | Technion PhD, UCLA postdoc, sequential and geometric methods early. | “The last several years are generative + multimodal, which is what I want to talk about.” |
| Lab / students / grants | Technical collaborator; I own architecture and eval. | IC. Don’t count students. |
| Koopman / VAEs | Dynamical sequential models; I moved on to diffusion because sampling and representation scaled better. | ImagenTime. |
| Forecasting FMs / Chronos | Useful forecast baselines; not this JD. | Classify / describe / fuse. |
| Apple / other processes | Exploring a few industry science roles. This problem is high priority. | Stop. |
| Autism / JAMA | Applied vision work; not this loop. | Stop. |

---

## Anti-patterns (this block only)

| Avoid | Do |
|-------|-----|
| Second 20-min VLM recap | One pointer, then gen or Bosch |
| Paper dump (7 diffusion, 40 pubs) | ImagenTime + LDDBM |
| “My students at Bosch…” | Named collaborators; I framed / I decided |
| “We productized this at Bosch” | Don’t know; Haifa ≠ RTC |
| Forecast-head identity | Frequency + synthetics + translation |
| SoundSee / ISS quiz | Let her name products |
| Manager / PI origin story | IC who wants to own the loops here |

---

## Close the block (if they leave you a last sentence)

> The VLM is how I reason over a series once it admits an image. The generative work is how I get representations and translations when the sensors don’t share a clock or a dimension. I want to do that here, gated on whether it moves a product slice.

Then coding. Don’t eat the 15 min.