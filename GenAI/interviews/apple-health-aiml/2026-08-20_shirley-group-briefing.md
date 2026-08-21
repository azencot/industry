# Shirley Ren / Health AIML — group briefing

**When:** 2026-08-20 (prep session for HM screen)  
**Call:** Fri 2026-08-21, 11:05–11:50 AM PDT with **Shirley Ren** — fit, not a paper quiz  
**Use:** understand the group so “why this team” is a choice. Do **not** name-drop papers unless she goes there.  
**Spoken scripts / three HM topics:** [`2026-08-12_hm-screen-prep.md`](2026-08-12_hm-screen-prep.md)  
**Why-Apple-Health drill (2026-08-20):** [`2026-08-20_why-apple-health-drill.md`](2026-08-20_why-apple-health-drill.md)  
**Training-run drill (2026-08-20):** [`2026-08-20_training-run-drill.md`](2026-08-20_training-run-drill.md)

---

## What the group is

**Shirley You Ren** — Senior ML Manager / Principal Engineer, Health & Fitness. HM for [ML Research Scientist — Health AIML](https://jobs.apple.com/en-us/details/200670570-3337/machine-learning-research-scientist-health-aiml?team=MLAI) (Seattle, on-site).

JD in one line: research lead for **health/fitness representation models and multimodal models** that scale; LLM training experience; TS / SSL / cross-modal; **safe** LLM deployment in health and fitness.

Think **stack**, not a chatbot team:

```
Wearable series (accel, HR, PPG-like, workout history)
        ↓
Sensor / motion representations  (RelCon, speech-FM transfer)
        ↓
Language / reasoning layer       (TS encoder → LLM + CoT)
        ↓
User-facing features under privacy / Apple Intelligence
```

Your work lives on the middle two layers. Do not pretend you shipped Watch features. Do not pretend they are a paper-only lab.

**If asked what the team does:** “Foundational representations of wearable series, then a language layer that can talk about them under privacy and on-device constraints.”

Close collaborators on papers: **Jaya Narain**, **Maxwell Xu**, **Haraldur Hallgrímsson**. Names in the TS-LLM paper thanks: Vincent Chan, Feng Zhu.

---

## Sensor glossary (wrist / ear time series)

| Term | What | How measured | Typical use |
|------|------|--------------|-------------|
| **IMU** | Inertial measurement unit — motion chip | Accel + gyro (sometimes magnetometer) | Device motion/rotation. RelCon uses the **accel** stream of the Watch IMU |
| **Accel** | Accelerometry — 3-axis acceleration of the device, usually in *g* | MEMS accelerometer in Watch (or other IMUs). Often ~25–100 Hz. **25 Hz = 25 samples/s** → 10 s window = 250 samples/axis | Motion motifs: walk / run / swim / sit. RelCon is trained on this. Cheap, always-on |
| **HR** | Heart rate (bpm). Usually a **derived** series, not the raw waveform | Computed from PPG (Watch back, or AirPods in-ear). One number every few seconds; sometimes HRV | Effort / Training Load; Workout Buddy language |
| **PPG** | Photoplethysmography — **raw optical pulse waveform** behind HR | LEDs into skin; photodiode measures reflected light. Blood volume pulses with each beat | HR, HRV, rhythm morphology. High-fidelity, **power-hungry** |
| **PPG-like** | Shorthand for that optical-pulse family (Watch PPG, AirPods in-ear) — not an Apple product name | | |
| **ECG** | Electrical heart signal | Watch electrodes (digital crown / back). Different modality from PPG | Speech-FM paper evaluates some ECG/PPG tasks; don’t overclaim |

**Why both accel and PPG exist:** accel is low-power and always available; PPG is more informative for cardio but costs battery. Adjacent Apple work distills PPG representations into accel encoders. Do **not** attribute that distillation paper to Shirley (authors: Abbaspourazad et al.).

**Gait regression:** gait = how you walk. Regression = predict a **number**, not a class. HAR says `walking` vs `running`. Gait regression says stride velocity **1.32 m/s** or **double support time** (fraction of stride with both feet on the ground — rises when walking is cautious). RelCon’s claim is a frozen motion FM that transfers to **both** activity classification and gait numbers — walking mechanics, not only activity ID. Apple Health already surfaces related walking metrics (speed, double support, asymmetry).

**Longitudinal:** same **users over time** (personal baselines, missing days, slow trends) — not a one-off public clip. That is the setting contrast vs UCR / TSExam.

If she says PPG, IMU, or accel, she means **these device series**, not a UCR line chart. Dual visual encodings would not drop in. Transferable idea: which representation preserves the structure that matters (motifs in accel, pulse morphology in PPG, slower trends in HR).

---

## Thread 1 — sensor / motion foundation models (authorship)

### RelCon

[RelCon: Relative Contrastive Learning for a Motion Foundation Model for Wearable Data](https://machinelearning.apple.com/research/relative-contrastive-learning) — Xu, Narain, … **Ren**. Apple ML Research, Apr 2025.

- Wearable accel labels are scarce; an HAR-only model does not transfer to gait metrics.
- Time series as **motifs** (arm-swing of walking repeats). Learnable distance for motif similarity + **rotation invariance** (watch upside-down, loose strap).
- **Relative** contrastive loss: walking closer to running than to yoga — not hard yes/no pairs (vs SimCLR augmentations / REBAR hard positives).
- Scale: **1 billion segments**, **87,376** participants — that is **data**, not weights.
- Encoder: 1D **ResNet-34**, **~3.9M parameters**, 256-d embedding (2.56 s of 100 Hz 3-axis accel). Small **on purpose** (always-on IMU). Do not analogize to 7B/27B.
- Frozen backbone + small head on distinct tasks: HAR **and** gait regression.
- **REBAR** (Xu et al., ICLR 2024) is a **contrastive recipe** for picking positives, not an Apple billion-param FM. RelCon cites it as a pair-construction baseline.

### Speech FMs on wearables

[Speech Foundation Models Generalize to Time Series Tasks from Wearable Sensor Data](https://machinelearning.apple.com/research/speech-foundation) — Narain, Aldeneh, **Ren**. NeurIPS 2025 TS4H workshop.

- Speech and wearable sensors both encode time- and frequency-domain structure (shapelets, spectral power).
- Frozen **HuBERT / wav2vec 2.0** + probe (or light LoRA) beat SSL trained **on the sensor data itself** for mood classification, arrhythmia detection, activity classification.
- Ablation: **convolutional front-end** of speech models does a lot of the work (bandpass / motif-like filters).
- Under scarcity: **steal a pretrained encoder** before training a new FM.

**If she says “we probe speech FMs / train motion FMs, you’re a VLM person”:**

> Same bottleneck, different encoder. They get a wearable representation that transfers; I fused two views into an LLM. I’d rather compare encoder families on the team’s tasks than insist on matplotlib. Probing a strong pretrained encoder is often the right first move under scarcity — I’ve already lived the version where stacking more training on a bad mix made things worse.

---

## Thread 2 — time-series reasoning with LLMs (closest scientific overlap)

[Towards Time-Series Reasoning with LLMs](https://machinelearning.apple.com/research/towards-time) — Chow, Gardiner, Hallgrímsson, Xu, **Shirley You Ren**. Intern-heavy (Stanford / UIUC + Apple). Intro names **health coaching** as a reason the modality matters.

**Bet:** TS-LLM needs (1) perception, (2) contextualization, (3) deductive reasoning. Most models fail at **(1)**. Text dumps lose temporal structure; forecast-style TS-LLMs often drop the language head. They keep an LLM that **still speaks**.

**Architecture:** patch series → lightweight self-attention **TS encoder** → project into **Mistral-7B** embeddings → concat with text. Mean/variance also as text so scale is not lost. Can interleave multiple series; multivariate accel as “axis x, then y…” with a text prefix.

**Training (same shape as yours):**
1. Encoder warmup, LLM frozen. Curriculum: synthetic MCQ → synthetic captioning → real captioning.
2. LoRA SFT on encoder + projector + LLM, with GPT-4o-generated CoT.

**Evidence they care about:** trained-encoder captions help more than text-Mistral; t-SNE of LLM states varies smoothly with slope/frequency; 7B + TS encoder beats GPT-4o (text or plot) on several zero-shot UCR-style tasks.

**Appendix worth knowing:** GPT-4o plot **resolution** moves etiological reasoning a lot (small 0.41 → square 0.56 → wide 0.61 vs tokenization 0.32). Plotting works but is hyperparameter-fragile → they argue a **native TS encoder** is the honest inductive bias.

**Your disagreement, 30s then stop** (drill 2026-08-20 — never “images keep all information”; don’t dunk on TS-encoder maturity):

> Images were a way to steal a visual prior when the LLM couldn’t see the series — not because plots are the true representation. One view still loses information; that’s why I used two. A native TS encoder is the more honest bias if you have the data. I wouldn’t reprint charts on PPG. I’d compare encoder families — native TS, visual, speech-FM transfer — with the same eval gate. Same bottleneck: the model does not perceive the series until you represent it.

Overlap if it comes up naturally: reasoning in language over series, perception first, two-stage alignment, LoRA, CoT data. Do not lead with “your paper used Mistral-7B.” Honest limits (keep in your head): intern-scale, public/synthetic series, UCR proxy, 7B is not on-Watch — same class of limits as TSExam/TSRBench for you.

---

## Thread 3 — shipped product (attribution)

### Workout Buddy — do not over-claim

**Not** an Apple paper or newsroom byline under Shirley’s name. Inferred from **her LinkedIn**: she lists *Shipped Features: Workout Buddy — Apple Intelligence Comes to Fitness* (plus AirPods calorie model, Effort Rating & Training Load, FTP for cyclists, Cycle Tracking), linking the [watchOS 26 newsroom](https://www.apple.com/newsroom/2025/06/watchos-26-delivers-more-personalized-ways-to-stay-active-and-connected/).

Apple’s announcement quotes **David Clark** (watchOS Engineering). Workout Buddy is a **cross-functional** Apple Intelligence + Fitness feature. For a senior ML manager / PE, LinkedIn “shipped” usually means **her org contributed**, not that she trained the TTS or owns the Watch app.

**RelCon / speech-FM / TS-reasoning = authorship.** Workout Buddy = **self-reported shipped work.**

**Tomorrow:** do not say “your Workout Buddy paper” or “I know you shipped Workout Buddy.” If *she* mentions it, treat it as the team’s language-over-fitness-series surface. If she never does, stay with the papers plus “the org ships health/fitness ML, including Apple Intelligence fitness features.”

What the feature is (public): spoken personalized motivation from workout data + history (HR, pace, distance, rings, milestones). TTS trained on Fitness+ trainers. Nearby Apple Intelligence iPhone + Watch + headphones. On-device + Private Cloud Compute. English, subset of workout types. Exec line: “just getting started.” Research question underneath: language over longitudinal fitness series, at the right moment, without leaking user data — not clinical diagnosis.

### Other fitness stack she lists (problem-level only)

| Feature | What | Why it matters |
|---------|------|----------------|
| Effort rating + Training Load (watchOS 11) | 1–10 effort from HR/GPS/elevation/demographics; load ≈ effort × duration; 7-day vs 28-day | Longitudinal TS, personal baselines |
| FTP for cyclists | Threshold power | Domain metric from wearable series |
| AirPods calorie / HR | In-ear optical sensing | New modality; fusion with Watch |
| Cycle Tracking | Women’s health | Sensitive longitudinal signal; high safety/privacy bar |

---

## Mapping for the HM screen

**Locked ~50s (drill 2026-08-20 — say twice before the call):**

> The question I work on is how to represent time series so a model can use them — perception first, then language. That question isn’t unique to Apple. The setting is: the series already live on the device, they’re longitudinal and user-specific, and privacy / on-device change how you build the representation, not just the compliance appendix. I’m not a clinician and I won’t reprint TS-as-image on PPG. Year one I’d learn your signals and your eval, then ablate encoder families under your constraints. I want that problem here, not a cleaner public benchmark.

**If Google vs Apple:** same question; this setting and this seat in Seattle — not the logo.

**Three sentences (say out loud):**

> The thing I work on is representing time series so an LLM can use them — perception first, then language. That is the same problem class as a TS encoder into an LLM; I used two visual views, they also explore native encoders and transferring speech FMs onto wearables. Health AIML is where those series are real, longitudinal, and privacy-constrained, and where the language layer already has a product surface. I’m not trying to become a clinician.

**Why this team if the science is the same:**

> Academic TS-LLM is public benchmarks. Here the series are user-specific, longitudinal, and the eval is not “did TSExam move.” Language features over fitness series also mean wrong answers and overconfidence are first-class. I want that constraint on the representation problem.

**Why Apple (not a fan letter):** the series already live on the device; Health AIML is building the foundational TS / multimodal layer, not a chatbot wrapper; privacy / on-device are constraints on the *representation*. 9B/27B were iteration scale, not an on-Watch proposal.

**Why hire LLM training if RelCon is ~4M:** different **layer**. RelCon-class = compact always-on perception. This seat = representation → **language** (their TS encoder → Mistral-7B; speech-FM probes; fitness-LLM features under PCC). Do not walk in arguing they need a billion-param IMU encoder.

### Anti-patterns

| Don’t | Why |
|-------|-----|
| “I love Workout Buddy / I have an Apple Watch” | Tourist |
| “I’d port matplotlib onto PPG” | Didn’t hear the sensor |
| “I’m a health-ML person now” | You aren’t |
| Reciting RelCon’s 1B segments or **3.9M** | Paper quiz; this is fit. 1B = data; ~4M = weights. Don’t volunteer |
| “RelCon is too small; you need a billion-param FM” | IMU encoder is small on purpose. LLM hire is the **language** layer |
| 27B on-device | Product uses iPhone + PCC |
| Forecasting as the lead | They moved past forecast-only TS-LLMs |
| Attributing Workout Buddy as *her paper* | LinkedIn shipped claim, not authorship |
| Impact at scale / millions of users / “safe AI” | Generic; works at Google Health |
| “The company doesn’t matter” / academic shopping labs | Question same, **setting** different |
| Passion / narrative / “the work you are doing” | Tourist or paper-audition |
| “I don’t know yet” with no year-one next sentence | Pair with: their series, their eval, ablate encoders |
| “Images keep all information” / “TS encoders aren’t mature” | One view loses information; don’t dunk on RelCon / their encoder; don’t port matplotlib |

### Questions (pick 2)

1. For this seat in 6–12 months, is the priority **better wearable representations**, **the language/reasoning layer**, or the **eval/safety harness** that gates LLM features?
2. What does strong year-one look like — a representation that transfers across sensors, a component under a fitness-LLM feature, or eval infra?

---

## Exit check (≤20s each, no notes)

1. Health AIML as the stack diagram above.  
2. RelCon in one breath: motifs + relative contrastive + frozen motion FM.  
3. Their TS-LLM vs yours: native encoder vs dual visual; same two-stage + LoRA + perception bottleneck.  
4. Workout Buddy as a *constraint* if it comes up: language over personal series, on-device / PCC, not diagnosis — and you do not claim she authored the product.
