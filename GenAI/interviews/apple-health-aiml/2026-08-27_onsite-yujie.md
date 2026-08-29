# On-site — Yujie Li (Wed 10:05 PDT)

Track: multimodal architecture and time-series encoding (behavioral, not only 100 Hz). Conf: high.

Who (private): Senior MLE, Seattle; headline Apple health AI. Coauthor Beyond Sensor Data / WBM — 2.5B hours, 162k people, tokenization + architecture, 57 health tasks. CV / representation background. Hub: 2026-08-27_onsite-prep.md

Opens Wednesday. First two minutes: encoding → stay here. Labels / 162k / missingness / ship → Haraldur (four modules: problem, representation, evidence, decision).

Do not name WBM / ICML. Do not force TS-as-image onto PPG. Do not only talk PPG at 100 Hz / IMU at 50 Hz. Do not recite 2.5B hours — she wrote it.

Do not spend another hour on LLaVA, Flamingo, generic projector vs cross-attention, or image-language architectures. You already know those ideas.

The goal is to show you can reason about: what a token should mean for wearable / time-series data; how temporal scale changes the representation; how heterogeneous modalities should be encoded; where and when modalities should fuse; how to handle long histories; how to handle asynchronous and missing streams; how to choose among representations scientifically.

Central question: "What is the right representation of this signal for the task I actually care about?"

One sentence to remember: the representation should be derived from the temporal scale and information requirements of the task; I would only scale an encoding after a controlled bakeoff shows that the information it preserves actually matters.

---

## Four modules

MODULE 1 — DEFINE THE TEMPORAL OBJECT

MODULE 2 — TURN TIME SERIES INTO USEFUL TOKENS

MODULE 3 — FUSE HETEROGENEOUS MODALITIES

MODULE 4 — CHOOSE THE REPRESENTATION WITH EVIDENCE

The four mental models:

1. TEMPORAL OBJECT: task horizon + signal resolution + context horizon

2. TOKENIZATION: information preserved + information discarded + token cost + inductive bias

3. FUSION: what needs interaction + when it needs interaction + how expensive that interaction is

4. REPRESENTATION DECISION: hypothesis -> controlled bakeoff -> slice analysis -> scaling decision

---

## Saturday / how to use this file

Sat leftover after Haraldur Module 1: Yujie Session 1 (temporal object cases) then Session 2 encodings if time. Abstracts only. Do not name-drop WBM.

If she opens with encoding, stay on tokens and clocks. If she opens with labels / population / ship, hand off in your head to Haraldur and still answer — but do not turn her hour into AUROC-0.95.

---

## Module 1 — Define the temporal object

Core question: Before choosing an encoder, what temporal phenomenon am I modeling?

### Why this matters

A time series does not have one natural representation. The correct representation depends heavily on the temporal scale of the question.

Example: the same IMU stream could support 2-second gesture detection; 30-second activity recognition; 30-minute workout characterization; daily activity summary; 6-month health prediction. These are different modeling problems. A representation that is excellent for one may destroy the information required by another.

Sleep next night != 5-year diabetes risk != a 10 s gait motif.

### 1.1 Three timescales

For every problem, identify:

A. SIGNAL RESOLUTION — how quickly is the raw process sampled?

IMU: 100 Hz. PPG: tens to hundreds of Hz. Heart rate: seconds. Sleep: minutes. Daily behavior: hours / days.

B. LOCAL PHENOMENON SCALE — how long is the pattern of interest?

Heartbeat: < 1 second. Gait cycle: ~1 second. Activity episode / bout: minutes. Sleep stage: minutes. Workout: tens of minutes.

C. TASK CONTEXT HORIZON — how much history is required to make the decision?

Activity classification: seconds. Sleep quality: hours. Weekly health state: days / weeks. Longitudinal risk: months.

These three scales do NOT have to match.

### 1.2 Local detail vs long-range context

This is a central architectural tension. High temporal resolution preserves detail. But high resolution across long context creates huge sequences.

IMU at 100 Hz: 1 second = 100 samples; 1 hour = 360,000 samples; 1 day = 8.64 million samples.

Therefore raw high-frequency signal + long context cannot normally be handled as a flat token stream. You need temporal compression. Do not dump 100 Hz IMU for 3 years into one Transformer.

### 1.3 Hierarchical temporal modeling

Default mental model for long wearable histories:

raw signal -> local encoder -> short-timescale latent -> coarser aggregation -> longitudinal representation

Example: IMU 100 Hz -> 2-second patches -> activity latents -> minute representation -> hour representation -> daily behavioral representation.

This lets different layers specialize in different temporal scales.

Key question: "What information can safely be compressed at each level?"

### 1.4 Behavioral tokens

For long-term wearable modeling, the useful "token" may not be a raw sensor patch.

It may represent: a sleep episode; a workout; a resting-HR summary; a mobility event; a daily activity profile; a circadian pattern; an exercise bout; a behavioral state.

This is important. Instead of one token = one raw sample, consider one token = one semantically meaningful event or temporal unit.

This dramatically changes context length, interpretability, model efficiency, and inductive bias.

A behavioral token is a person-scale event or day summary, not a 100 Hz sample. Different semantic clocks than PPG / IMU / ECG.

### 1.5 Event-based vs grid-based time

GRID-BASED REPRESENTATION. Example: every hour [HR, steps, sleep, activity, ...].

Pros: easy alignment; simple batching; standard Transformer input.

Cons: artificial discretization; many empty bins; slow modalities get repeated; timing precision lost. Missing cells explode length.

EVENT-BASED REPRESENTATION. Example: 08:05 workout starts; 08:47 workout ends; 23:10 sleep begins; 07:03 sleep ends.

Pros: sparse; natural for irregular events; preserves timing.

Cons: more complicated modeling; event semantics must be defined (what you chose to name); variable sequence length.

Do not assume regular binning is always correct. Do not resample every stream onto the fastest clock.

### Module 1 practice

Case A: You have one year of IMU, HR, sleep, and workout history. Predict next-week health state.

Answer: (1) which temporal scales matter, (2) which raw information can be compressed, (3) what should the tokens mean, (4) where should the hierarchy change resolution.

Week-level lock (same instinct as Haraldur): daily / event behavioral tokens + a simple baseline first, not a flat 100 Hz year.

Case B: Same signals, but target becomes "Detect a 5-second movement abnormality." How does the entire representation change?

Case C: Same target, but history increases from 1 day to 1 year. What changes?

Also walk three years of mixed history — her predicted open — with the same four questions.

Pass condition: for any time-series problem, you naturally identify signal resolution + phenomenon scale + context horizon before choosing an encoder.

---

## Module 2 — Turn time series into useful tokens

Core question: How should continuous or irregular signals become discrete model representations?

Mental model: for every encoding ask (1) what information is preserved, (2) what information is discarded, (3) what is the token cost, (4) what inductive bias is introduced.

This is the most important framework for this interview. Fifth check: what temporal scale does the downstream question require?

### 2.1 Numeric text serialization

Example: "72, 73, 76, 81, 85, ..."

Advantages: trivial integration with LLM; no new encoder required; works for very short / simple sequences.

Problems: poor token efficiency; tokenizer not designed for numeric structure; decimals and magnitudes can fragment unpredictably; weak inductive bias for continuity; long sequences consume huge context.

Good answer: useful as a baseline for short / simple data. Poor default for dense wearable signals. This is the "text dump" family from the HM screen — not your bet for Watch streams.

### 2.2 Fixed patches

Split sequence into windows: x_1...x_T -> patch_1 ... patch_N. Then patch_i -> linear projection / CNN / local encoder -> token_i.

Benefits: reduces sequence length; preserves local structure; straightforward Transformer integration.

Key design parameter: PATCH SIZE.

Small patches: preserve fine detail; many tokens.

Large patches: compact; lose local structure.

This is a rate-distortion-style tradeoff. A 1 s IMU patch at 100 Hz is still the waveform (100 samples -> one latent).

### 2.3 Convolutional front end

Use local convolutions to filter noise, detect local motifs, downsample, and produce a latent sequence.

Example: 100 Hz IMU -> strided conv -> 25 Hz latent -> further temporal compression.

Advantages: strong local inductive bias; efficient; natural for waveform data.

Potential limitation: fixed local receptive field unless deeper / hierarchical.

### 2.4 Learned sensor encoder

A modality-specific encoder might be: CNN; temporal Transformer; state-space model; hybrid conv + attention; pretrained sensor foundation model.

Output: z_m in R^(T_m x d_m). Then optionally project z_m -> R^(T_m x d_common).

Important question: should each modality have its own encoder, a shared encoder, or a shared backbone + modality adapters?

Use separate encoders when signal physics differ strongly. Use shared structure when representations are sufficiently related and data supports learning common features.

Patched native encoder = honest inductive bias if you have the data. That is the family you would bake off against text and images — not "I would plot PPG."

### 2.5 Aggregate / statistical tokens

Instead of raw patches, compute mean, variance, quantiles, trend, spectral energy, periodic statistics, activity duration, sleep summary. Then encode these summaries as tokens / features.

This can be highly competitive for long-horizon tasks.

Do NOT treat feature engineering as primitive. It encodes strong prior knowledge. If the outcome lives in a statistic you did not compute, the model cannot invent it.

### 2.6 Frequency-domain representation

For periodic or oscillatory signals, STFT / FFT / wavelets can expose structure that is difficult in the raw time domain.

Examples: cadence; respiration-like periodicity; gait frequency; vibration patterns.

Possible pipeline: raw signal -> STFT -> time-frequency patches -> encoder.

Tradeoff: frequency representation can make periodic structure explicit but may lose some temporal precision.

When should I use it? When the phenomenon is naturally spectral or local periodicity matters. Do not name the periodicity paper if this leaks into Haraldur's hour.

### 2.7 Image / chart representation

You know this well. Use it carefully.

Potential advantage: exploit strong pretrained visual models; visual prior can capture shape / trend.

Problems: rendering choices become inductive bias; possible information loss; inefficient representation; likely inappropriate for raw high-rate PPG / IMU.

Strong answer: images can be a useful representation baseline or transfer strategy, but I would not assume they are the natural representation for wearable waveforms.

Do not say "images keep all information." You used two views because one encoding loses information. Images were a stolen visual prior when the LM could not see a short series — not because plots are the true object. Year one: same eval gate, compare encoder families on their IMU / PPG / longitudinal signals. I would not port matplotlib onto PPG.

### 2.8 Discrete / quantized tokens

Continuous signal can be mapped to discrete codes: x -> encoder -> codebook -> token IDs.

Potential benefits: compatible with token-based generative modeling; compact; shared vocabulary possible.

Risks: quantization error; codebook collapse; arbitrary discretization; information bottleneck.

Important question: does the discrete vocabulary capture meaningful sensor states?

"Just quantize everything into a Transformer" is a hypothesis, not a default. Bake it off (Module 4).

### 2.9 Time information

For regularly sampled patches, relative position may be enough.

For irregular data, the model needs actual timing information.

Possible inputs: timestamp; delta time; time-of-day; day-of-week; elapsed time since previous event.

Do not assume token position == physical time. For irregular streams, position 20 and position 21 might be 1 second apart or 3 hours apart.

Multivariate is not "just concat" without modality identity and time (Feng leftover).

### 2.10 Normalization

Sensor modalities differ greatly in scale.

Need to think about: global normalization; per-channel normalization; per-user normalization; per-window normalization.

Each changes information.

Example: per-window centering may remove absolute baseline. That could be good for activity classification. But terrible if absolute resting HR is clinically meaningful.

Normalization is part of the representation.

### 2.11 Token budget

Every representation should have a token-budget calculation.

12 months of daily tokens: ~365 tokens. Easy.

12 months of hourly tokens: ~8,760 tokens. Possible but substantial.

12 months of 1-minute tokens: ~525,000 tokens. Not reasonable for ordinary Transformer context.

Three years of 100 Hz IMU is not a token plan. Temporal compression must match context horizon.

If the budget is tight, drop the finest clock first on streams the task does not need at that resolution — not "drop PPG because it is annoying."

Device gens can change sample rate. Do not assume one patch size survives a new watch. Recompute tokens / hour and whether the local encoder still sees the phenomenon scale.

### Module 2 practice

For each of these tasks, choose an encoding:

A. 30-second activity recognition

B. sleep-stage prediction

C. one-week health prediction

D. one-year longitudinal behavioral modeling

E. anomaly detection from PPG

For each answer: (1) token definition, (2) patch / time scale, (3) normalization, (4) positional / time encoding, (5) token count, (6) information lost, (7) simplest baseline.

Then compare: numeric text; patches; conv encoder; aggregate features; spectral representation; discrete tokens. Images only if the series is short and you are stealing a visual prior — say so.

Pass condition: you can compare representations using information + token cost + inductive bias rather than saying "Transformers usually work well."

---

## Module 3 — Fuse heterogeneous modalities

Core question: After each modality has a sensible representation, where and how should they interact?

Mental model: fusion depends on (1) temporal alignment, (2) relative sequence lengths, (3) information interaction required, (4) missingness, (5) computational budget.

### 3.1 Do not fuse raw clocks blindly

Example: IMU = 100 Hz; HR = 1 Hz; sleep = minutes.

Bad default: upsample everything to 100 Hz and concatenate.

Why bad: huge redundant sequence; slow channels become staircases; no new information is created; compute explodes.

Better: encode each stream at a meaningful native / local resolution.

### 3.2 Multirate encoding

Example: IMU -> high-rate encoder -> 1 token / several seconds. HR -> lower-rate encoder -> 1 token / tens of seconds. Sleep -> event representation. Then align at a coarser latent level.

This is likely one of the most important design ideas to articulate.

### 3.3 Early fusion

Example: [z_IMU, z_HR, z_sleep] -> shared Transformer.

Advantages: rich interaction; simple unified modeling.

Disadvantages: large joint sequence; expensive (T^2); modalities can interfere; difficult when clocks differ strongly.

Use when token counts are manageable, fine cross-modal interaction matters, and alignment is reasonably clear.

### 3.4 Cross-attention

One modality attends to another. Example: Q = longitudinal behavioral tokens; K,V = sensor tokens.

Advantages: avoids concatenating everything; allows selective information retrieval; preserves modality structure. Useful when one stream is very long, modalities differ in resolution, or fusion should happen selectively.

Risk: the model can learn to ignore the secondary modality. Need utilization tests.

This is the Flamingo-shaped idea applied to sensors — do not spend the hour on Flamingo.

### 3.5 Late fusion

Separate modality representations z_IMU, z_PPG, z_sleep, then combine: concat / MLP / ensemble / higher-level Transformer.

Advantages: modular; easy missing-modality handling; easier debugging.

Disadvantages: may lose fine-grained interactions.

Good baseline. Do not dismiss it.

### 3.6 Fusion level

Critical question: at what level should modalities meet?

Raw PPG + raw IMU? Possibly useful for local physiological-motion artifact handling.

Sleep summary + millisecond PPG? Probably not directly.

Possible hierarchy: RAW LEVEL for tightly synchronized signals; EVENT LEVEL for activity / workout episodes; DAY LEVEL for longitudinal behavior.

The right answer may involve MULTIPLE fusion levels.

### 3.7 Alignment

Different streams may not be perfectly synchronized.

Possible approaches: explicit timestamp alignment; temporal windows; nearest-neighbor matching; interpolation; cross-attention using time embeddings; learned latent alignment.

Do not create false precision. If HR is sampled every minute, aligning it to a specific 10-ms IMU sample may be meaningless.

### 3.8 Missing modalities

Architecture should naturally support subsets.

Options: omit unavailable tokens; learned missing embedding; explicit availability indicators; modality-specific masks.

Training: preserve natural missingness, plus potentially use modality dropout.

Goal: the model should not assume every modality is always present.

If she stays on architecture, pack present tokens and add availability. If she stays on "is missingness a shortcut / do we ship," that is Haraldur.

### 3.9 Modality identity

If tokens enter shared space, the model should generally know their source.

Possible: z = content_embedding + modality_embedding + time_embedding.

This helps distinguish an IMU token from an HR token from a sleep token, especially when dimensions are projected into a common space.

### 3.10 Modality neglect

Suppose text or behavioral summaries predict most of the label. Then the model may ignore richer sensor data.

Test: remove modality; shuffle modality; time-shift modality. If output barely changes, fusion may be nominal rather than real.

This should be part of architecture evaluation. Stronger than attention plots.

### 3.11 Longitudinal + local fusion

Useful design pattern: LOCAL SENSOR ENCODERS -> LOCAL MULTIMODAL FUSION -> BEHAVIORAL / EVENT TOKENS -> LONGITUDINAL MODEL.

Example: IMU + HR during a workout -> workout representation. Then workout tokens + sleep tokens + daily behavior -> month-level model.

This is much more plausible than one giant flat sequence.

### Module 3 practice

You have IMU 100 Hz; HR 1 Hz; intermittent PPG; sleep stages; workouts; one year of history. Design the architecture.

Do it in layers: (1) native modality encoders, (2) local compression, (3) temporal alignment, (4) fusion level, (5) behavioral token creation, (6) longitudinal model, (7) missing modality handling.

Then change assumptions.

Change A: PPG exists only during workouts.

Change B: target depends strongly on beat-level PPG morphology.

Change C: target is weekly behavioral health state.

Change D: IMU becomes unavailable for 50% of users.

Change E: you need inference on-device.

Pass condition: you can move the fusion point up or down the hierarchy depending on where cross-modal interaction is actually needed.

---

## Module 4 — Choose the representation with evidence

Core question: There are many plausible encodings. How do I decide which one to use?

Mental model: HYPOTHESIS -> CONTROLLED BAKEOFF -> SLICE ANALYSIS -> SCALING DECISION.

This is where you should lean into scientific judgment.

### 4.1 Do not argue architectures philosophically

Question: should I use text serialization, a native sensor encoder, or an image representation?

Weak answer: "Native time-series encoders are better because they preserve structure."

Better: "I would identify what each representation claims to preserve, then compare them under a matched experimental setup."

Your HM-screen three families (text / patched native / images) fit here as hypotheses, not as a 2–3 min recap of Shirley.

### 4.2 Define representation hypotheses

TEXT HYPOTHESIS: numeric serialization is sufficient because the task depends on coarse values and sequences are short.

PATCHED ENCODER HYPOTHESIS: local temporal motifs matter and should be learned natively.

IMAGE HYPOTHESIS: pretrained visual priors provide useful shape representations despite rendering loss.

AGGREGATE HYPOTHESIS: the long-horizon task depends mostly on stable behavioral statistics.

Each is testable.

### 4.3 Controlled bakeoff

Hold fixed as much as practical: train / validation / test split; downstream task; training data; evaluation; compute budget; decoder / head; parameter budget when possible.

Compare representations.

Measure: task performance; training compute; inference cost; token count; robustness; label efficiency.

Also: token utilization / throughput; linear probe of the representation. Caption eval is not CE / ROUGE (Feng leftover) if a language head appears.

Year one on this team: same eval gate, compare encoder families on their streams.

### 4.4 Slice by temporal characteristics

Average score can hide why an encoding works.

Create slices: short vs long horizon; periodic vs non-periodic task; dense vs sparse data; high vs low sampling rate; full vs missing modalities; waveform-sensitive vs aggregate-sensitive task.

Then ask: which representation wins where? You may discover no single representation dominates.

### 4.5 Information-loss ablations

If using compression, vary patch size: 1 sec; 5 sec; 30 sec; 5 min. Observe performance. This reveals which temporal resolution actually matters.

Similarly, history length: 1 day; 1 week; 1 month; 6 months. This tests whether long context carries useful signal.

### 4.6 Match representation cost

If one encoding produces 100 tokens and another 10,000, an accuracy comparison alone is incomplete.

Measure performance vs token budget / compute. Potentially plot accuracy vs FLOPs or accuracy vs token count. This makes representation efficiency explicit.

A 2% gain at 10x token count is not automatically better.

### 4.7 Label efficiency

A pretrained representation may be valuable even if full-data performance gains are modest.

Evaluate 1% / 5% / 10% / 25% / 100% labels. If a pretrained sensor encoder wins strongly with limited labels, that can justify it.

### 4.8 Transfer

A representation intended to be foundational should work across multiple tasks, multiple temporal scales, different participants, different signal quality, and possibly different devices.

Do not call it a foundation representation based on one downstream benchmark. Do not recite 162k / 57 tasks as if you ran them.

### 4.9 Simple baseline

For every fancy representation include a strong cheap baseline. Example: daily behavioral features + LightGBM.

If that matches a huge model, ask: what is the complex representation adding? Potential answers: transfer; low-label performance; difficult task slices; multi-task reuse; richer outputs. If none: do not scale it.

### 4.10 Know when to scale

Do NOT start with the largest model.

Suggested progression: small controlled experiments -> identify promising representation -> stress-test -> scale only the winner.

Define kill criteria. Kill an encoding if: no gain over simple baseline; gains disappear under matched compute; only improves easy slices; token cost is excessive; missingness robustness is poor; transfer benefit absent.

Your TR mix kill and dual-view ablation are the IC stories: average up / slice down; one encoding loses information.

### Module 4 practice

Bakeoff case: four candidate encodings — (A) numeric text, (B) native patches, (C) chart / image, (D) daily behavioral tokens.

Design an experiment. Answer: (1) hypothesis for each, (2) common downstream model, (3) matched data, (4) compute / token controls, (5) evaluation tasks, (6) temporal slices, (7) missingness slices, (8) label-efficiency test, (9) kill criteria.

Then: what result would convince you to choose each representation?

Pass condition: you can turn architecture debate into a controlled scientific experiment.

---

## The most important integrated case

Practice this repeatedly:

We have one year of wearable data: IMU at 100 Hz; intermittent PPG; HR; sleep; workouts; behavioral summaries. We want a model that supports several downstream health tasks. Design the representation and architecture.

Your reasoning should be:

STEP 1 — DEFINE TASK SCALES. Which tasks require seconds, minutes, days, months?

STEP 2 — DEFINE LOCAL REPRESENTATIONS. IMU: local patches / native encoder. PPG: local physiological encoder. HR: lower-rate temporal encoding. Sleep / workouts: event representations.

STEP 3 — TEMPORAL COMPRESSION. raw -> local latent -> events / behavioral tokens.

STEP 4 — FUSE AT APPROPRIATE LEVELS. Fine fusion only where needed. Coarse fusion for longitudinal reasoning.

STEP 5 — REPRESENT TIME. Physical timestamps / delta time / periodic information.

STEP 6 — HANDLE MISSINGNESS. Availability-aware architecture.

STEP 7 — LONGITUDINAL MODEL. Operate on a compact behavioral / event-level sequence.

STEP 8 — DEFINE BASELINE. Engineered behavioral features + simple model.

STEP 9 — BAKEOFF. Native vs aggregate vs alternative representations.

STEP 10 — SCALE WINNER ONLY AFTER EVIDENCE.

Also run the same spine on three years — that is the likely open.

---

## Likely Yujie-style questions

Q1. What is a token in a one-year (or three-year) wearable record?

Q2. How would you represent IMU at 100 Hz together with daily sleep summaries?

Q3. Why not resample everything onto one common clock?

Q4. When should I use raw signals versus behavioral aggregates?

Q5. How would you choose patch size?

Q6. How do you represent irregular observation times?

Q7. At what level should PPG and IMU fuse?

Q8. How would your architecture change for a 5-second target versus a 6-month target?

Q9. How do you know a compressed representation did not discard important information?

Q10. Why might a behavioral-token model beat a raw-sensor model?

Q11. How would you compare a native time-series encoder against numeric text serialization?

Q12. What would make you choose an image representation?

Q13. If one modality is absent for most users, how should fusion change?

Q14. How would you model a year of history without an enormous context?

Q15. How would you evaluate whether longer context genuinely helps?

Q16. What should be shared across modality encoders?

Q17. When would you use a common encoder versus modality-specific encoders?

Q18. How would you exploit millions of unlabeled sensor hours?

Q19. What experiment tells you whether a representation is truly transferable?

Q20. You get a 2% gain but 10x token count. Is it better?

Q21. Sampling rate changes across device gens. What happens to your tokens?

Q22. Concat vs cross-attn vs native encoder — one discriminating experiment.

Q23. Token budget: what do you drop first?

Q24. Feng leftover: caption eval != CE / ROUGE; multivariate != just concat without identity / time.

---

## Recommended practice schedule

The goal is ~35% learning, ~65% active design practice.

Session 1 — Temporal object, ~75 min. 30 min learning: temporal scales; event vs grid; hierarchical modeling; behavioral tokens. 45 min cases: same signal, different prediction horizons. Practice redesigning representation when task scale changes.

Session 2 — Encoding, ~90 min. 40 min learning: patches; conv encoders; aggregate representations; frequency domain; discrete tokens; time encoding; normalization. 50 min: encode five different time-series tasks from scratch.

Session 3 — Fusion, ~90 min. 30 min learning: multirate streams; fusion levels; early vs cross vs late fusion; missingness; alignment. 60 min: IMU + PPG + HR + sleep architecture exercise. Continuously change assumptions.

Session 4 — Representation bakeoff, ~75 min. 20 min review: controlled experimentation. 55 min: design representation comparisons. Force yourself to define hypothesis, control, slices, cost metric, kill criterion.

Session 5 — Integrated mock, 45–60 min. One evolving design problem. No trivia. The interviewer keeps changing target horizon, modality availability, token budget, device constraints, dataset size. You continually adapt the architecture.

Mock (35 min) — first Wednesday slot. Broad: add PPG + IMU + behavioral history. Drill: tokenize three years. Scenario: matched bakeoff, no matplotlib on PPG.

---

## What to memorize

Very little.

Framework 1 — TEMPORAL OBJECT: signal resolution + local phenomenon scale + context horizon.

Framework 2 — REPRESENTATION: information preserved + information lost + token cost + inductive bias.

Framework 3 — FUSION: what needs interaction + at what temporal level + at what computational cost.

Framework 4 — DECISION: hypothesis -> controlled bakeoff -> slice analysis -> scale or kill.

---

## Final pass condition

You are ready when Yujie can give you a sensor / time-series problem you have never seen before and you naturally reason:

1. What temporal phenomenon am I trying to capture?
2. What is the raw sampling scale?
3. How much context does the task require?
4. What should one token represent?
5. What information can I safely compress?
6. Which information cannot be lost?
7. Should modalities meet locally or only after compression?
8. How do I represent physical time?
9. How do I handle missing / asynchronous streams?
10. What is the strongest simple representation baseline?
11. What experiment distinguishes the candidate encodings?
12. Does the additional representation complexity earn its cost?

---

## Traps

Don't replay Shirley's 2–3 min encodings as the whole hour. Use clocks + token cost + timescale.

Don't make LLaVA vs Flamingo the hour. Wearable token design.

Don't say images keep all information. Own ablation.

Don't recite 2.5B hours / 162k / 57 tasks.

Don't name WBM / ICML.

Don't force matplotlib / VLM images onto PPG.

Don't dump 100 Hz for three years into one Transformer.

Don't hand her Haraldur's AUROC-0.95 ship question unless she pulls labels / missingness / product.
