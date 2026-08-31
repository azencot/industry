# On-site — Yujie Li (Wed 10:05 PDT)

Track: Tyler #2 — multimodal architecture and time-series encoding. Conf: high.

Who (private): Senior MLE, Seattle; headline Apple health AI. Coauthor Beyond Sensor Data / WBM — 2.5B hours, 162k people, tokenization + architecture, 57 health tasks. CV / representation background. Hub: 2026-08-27_onsite-prep.md

Opens Wednesday. First two minutes: encoding / architecture → stay here. Labels / 162k / missingness-as-shortcut / ship / PPV / calibration → Haraldur.

Health / wearables are an important application context. This is NOT primarily a health-domain interview.

Do not name WBM / ICML. Do not recite 2.5B hours. Do not force matplotlib onto PPG. Do not say images keep all information.

---

## Primary goal

Demonstrate that you can design and reason about multimodal architectures involving time series.

The core questions are:

- How should continuous signals become model tokens?
- Which encoder is appropriate?
- How do heterogeneous modalities interact?
- When should fusion occur?
- How do different clocks and temporal resolutions interact?
- How should time itself be represented?
- When should representations be shared versus modality-specific?
- How do we know the model really uses each modality?
- How do we choose among competing architectures?

Do not spend much time on: basic LLaVA mechanics; basic Flamingo mechanics; deriving vanilla attention; generic CLIP explanations; health metrics such as PPV / calibration; product operating thresholds. You know enough of those. Use LLaVA / Flamingo only as architectural reference points.

The emphasis is: TIME SERIES + MULTIMODAL REPRESENTATION + FUSION + TEMPORAL STRUCTURE.

One sentence to remember: I'd separate the problem into representation, temporal alignment, and fusion: first make each modality compact without discarding task-relevant information, then decide at what temporal and semantic level the modalities actually need to interact.

---

## Four modules

MODULE 1 — ENCODE THE TIME SERIES

MODULE 2 — DESIGN THE MULTIMODAL ARCHITECTURE

MODULE 3 — HANDLE TIME, CLOCKS, ALIGNMENT, AND MISSINGNESS

MODULE 4 — TRAIN, DIAGNOSE, AND CHOOSE BETWEEN ARCHITECTURES

The four mental frameworks:

1. ENCODING: information preserved + information discarded + token count + inductive bias

2. ARCHITECTURE: where does each modality get encoded? + where do modalities interact? + what information bottleneck exists?

3. TEMPORAL STRUCTURE: sampling rate + physical time + alignment precision + relevant task timescale

4. MODEL SELECTION: hypothesis -> controlled experiment -> failure analysis -> scale or kill

---

## Saturday / how to use this file

Start at Module 1. Largest learning block. Practice: given a series, propose 3 encodings and compare them with the four questions. Wearable cases are one application, not the only ones — Session 6 uses audio + telemetry + text on purpose.

If she opens with tokens / encoders / fusion, stay. If she opens with labels / prevalence / ship, answer briefly and do not turn the hour into Haraldur Module 1.

---

## Module 1 — Encode the time series

Core question: How should a continuous time series become a sequence of representations that a multimodal model can use?

This should be the largest learning module.

### 1.1 Start from the raw object

Suppose x in R^(T x C), where T = time samples and C = channels.

Examples: univariate heart rate; multivariate 3-axis accelerometer; very multivariate industrial telemetry.

Before choosing an encoder ask: sampling frequency? number of channels? regular or irregular? context length? local vs global patterns? absolute scale important? frequency-domain information important?

Do not start with "I'll use a Transformer."

### 1.2 Point-wise tokens

Simplest representation: one timestamp -> one token.

x_t in R^C -> linear projection -> z_t in R^d

Advantages: minimal information loss; simple.

Problems: huge sequence length; poor efficiency; little local inductive bias.

For high-rate signals this quickly becomes impossible. Example: 100 Hz * 1 hour = 360,000 tokens. Not reasonable for ordinary Transformer attention.

### 1.3 Patch tokens

Group P timesteps: [x_t, ..., x_(t+P-1)] -> projection / encoder -> one token.

Then token count N ~= T / P.

This is analogous to ViT patches but in time.

Understand the patch-size tradeoff.

SMALL P: preserves fine detail; precise temporal localization; many tokens; high compute.

LARGE P: strong compression; cheaper; can destroy high-frequency structure; worse event localization.

Patch size is therefore not merely a hyperparameter. It defines the temporal resolution visible to the backbone.

### 1.4 Patch encoder options

A patch does not have to be flattened and linearly projected.

Possible:

A. linear projection — cheap, minimal prior

B. 1D CNN — strong local temporal prior

C. small Transformer — more flexible

D. state-space / recurrent encoder — potentially efficient for long signals

E. spectral encoder — explicit frequency-domain structure

Important interview question: "What does the encoder assume about the signal?"

### 1.5 Convolutional downsampling

Useful pipeline: raw signal -> conv -> nonlinearity -> stride / downsample -> latent sequence.

Why convolution can be useful: local translation equivariance; efficient; good local waveform processing; hierarchical receptive field; built-in temporal compression.

You should be able to compare explicit non-overlapping patches vs learned strided convolution.

### 1.6 Multivariate series

Suppose x_t in R^C. There are several ways to tokenize.

A. CHANNELS TOGETHER — one token per time patch containing all C channels. Pros: cross-channel relationships available immediately. Cons: fixed channel set; harder missing-channel handling.

B. CHANNEL-SEPARATE TOKENS — token for (channel, time-patch). Pros: flexible; explicit channel identity. Cons: sequence grows by factor C.

C. CHANNEL ENCODER FIRST — encode channels locally, then produce a joint temporal token.

Tradeoff depends on whether channel interactions are local and strong, or heterogeneous and loosely related.

This applies beyond health: sensors; industrial telemetry; finance; climate; scientific measurements.

### 1.7 Channel identity

If channels become separate tokens, the model needs to distinguish them.

Typical representation: z = content embedding + channel embedding + time embedding.

This parallels modality embeddings in multimodal models.

Question: should channel identity be a learned categorical ID, or encode physical metadata such as units, sensor type, spatial location? This can matter for transfer.

Multivariate is not "just concat" without identity and time (Feng leftover).

### 1.8 Numeric text serialization

Represent values as text: "2.31, 2.27, 2.36, ..."

Potential benefits: direct use of pretrained LLM; no new encoder; sometimes surprisingly strong for small datasets.

Weaknesses: terrible token efficiency; tokenizer artifacts; magnitude structure poorly represented; context explosion; weak continuity bias.

Treat as a useful baseline. Not a natural default for dense signals. This is the HM-screen "text dump" family.

### 1.9 Discretization / tokenizer

Alternative: continuous value -> quantization -> discrete symbol. Or: patch -> VQ encoder -> codebook ID.

Now time series becomes something more analogous to language.

Benefits: discrete generative modeling; compact symbolic vocabulary; potentially common backbone.

Risks: quantization error; codebook collapse; semantic meaning of tokens unclear; task-relevant information may disappear.

Important conceptual question: "What information must the tokenizer preserve?"

"Just quantize everything into a Transformer" is a hypothesis. Bake it off in Module 4.

### 1.10 Frequency domain

For signals with oscillatory structure: x(t) -> FFT / STFT / wavelet -> spectral representation.

Useful when periodicity matters; frequency components are physically meaningful; local spectra matter.

STFT gives time x frequency. Now you can patch a spectrogram, use a CNN, use a ViT, or build a dedicated time-frequency encoder.

Tradeoff: time resolution vs frequency resolution.

Do not claim STFT is universally better. It exposes one useful inductive bias. Do not name the periodicity paper if this leaks into Haraldur's hour.

### 1.11 Image / chart representation

Your existing work fits here.

Time series -> rendering -> vision encoder -> visual tokens.

Why it can work: exploit pretrained visual representations; shape / trend appears visually; bypass need for training a TS encoder from scratch.

Why it can fail: renderer decides what information survives; numerical precision can be lost; token / compute efficiency may be poor; not natural for raw dense signals.

Important framing: "Image encoding is a transfer strategy, not necessarily the natural representation of the time series."

Your own ablations are useful evidence here. Do not say images keep all information. You used two views because one encoding loses information. Images were a stolen visual prior when the LM could not see a short series. Year one: same eval gate, compare encoder families on their streams. I would not port matplotlib onto PPG.

### 1.12 Delay / state-space representations

A time-series sample can also be mapped into a representation like [x_t, x_(t-tau), x_(t-2tau), ...].

Potential benefit: expose dynamics / state geometry.

This is another example of representation = inductive bias.

Useful interview point. Different encodings expose different properties:

- raw: local values
- spectral: frequency
- delay: dynamics / state
- chart: shape / trend
- patch: learned local structure

### 1.13 Normalization is part of encoding

Options: global normalization; channel-wise normalization; per-series normalization; per-window normalization; instance normalization.

These are NOT equivalent.

Per-series normalization removes absolute scale. Good if shape matters and scales vary arbitrarily. Bad if absolute level carries information (example: resting HR).

Potential question: "Why did the model fail after normalization?" Because preprocessing may have removed the predictive feature.

### 1.14 Time-series encoding framework

For every encoding candidate ask exactly four questions:

1. What information does it preserve?
2. What information does it lose?
3. How many tokens does it produce?
4. What inductive bias does it impose?

Example — STFT. Preserves: local frequency structure. Loses / transforms: some temporal precision and raw phase depending on representation. Tokens: depends on window / hop / frequency bins. Bias: periodicity / spectral patterns matter.

Example — chart. Preserves: visual shape / trend. Loses: numerical precision, depending on rendering. Tokens: vision patch count. Bias: visual structure transfers.

Pass condition for Module 1: given any time series, you can propose 3 plausible encodings and compare them using information, token count, inductive bias, and task requirements.

### Spoken (2026-08-29) — Module 1 drill

Q1. One hour of 100 Hz, 3-axis IMU. Three encodings with preserves / loses / token count / inductive bias. Which for 5-second activity vs next-week state?

First take: patch — preserves temporal structure, loses a bit of info, N = T/P, neighborhood matters. STFT — preserves freq, loses temporal info, tokens P*F, bias = wide freq range. Chart — preserves numerical range, loses high-freq detail, N = image tokens, bias = numerical range and structure.

Miss: no task pick. "Loses a bit" is not an answer. STFT does not throw time away (time–frequency tradeoff). Chart flipped: rendering loses precision, keeps shape; bias is a visual prior. One hour is 360,000 samples — say the number. 3-axis: channels together vs per-axis tokens.

Lock: (1) 2 s patches, channels together — keeps local waveform, loses intra-patch freq and finer localization, ~1800 tokens/hour, local stationarity. (2) STFT — keeps local spectrum, trades time vs freq resolution, frames × bins, periodicity is the object. (3) Chart — keeps shape, loses numerical precision, vision-token count, stolen visual prior. Reject point-wise (360k tokens). Five-second activity: small P or conv (0.2–2 s). Next-week state: daily / event aggregates or hierarchy, not a flat hour of IMU. Chart only as a short-series transfer baseline.

Q2. P = 10 vs P = 1000 on that IMU. What clock does the backbone see? When does the large patch destroy the task?

First take: 5 s = 500 steps; P=10 → 50 tokens, P=1000 → 1 token. Next-week: 360k*7, so P=1000 is ok and P=10 is too many. P=1k destroys when it leaves too few tokens.

Miss: 360k*7 is 7 hours, not a week. A week of 100 Hz is 360k*24*7 if worn continuously — still huge at P=1000 (~60k tokens). The kill is not token count. P=1000 is a 10 s clock; a 5 s event is smeared inside one patch. Next-week state is not a flat patched week.

Lock: Phenomenon scale vs patch scale. P=1000 means the backbone sees 10 s blobs. Next week: compress to days / events, then a small model.

Q3. Z-score each 2-second window. When right, when did you delete the feature?

First take: wrong if the feature is periodic at 2 s and z-score kills the trend.

Miss: the corpse is mean and energy (level / intensity), not "periodicity." Shape inside the window survives.

Lock: Per-window z-score sets that 2 s mean to 0 and std to 1. Right when the task is waveform shape and people / devices have different scales. Wrong if the feature is how hard they moved, absolute accel, or a baseline you need across windows.

---

## Module 2 — Design the multimodal architecture

Core question: Once each modality has a representation, how should the representations interact?

Do not reduce this to concat vs cross-attention. There are more architectural decisions.

### 2.1 Modality-specific encoders

Architecture: x_A -> E_A -> z_A; x_B -> E_B -> z_B; x_C -> E_C -> z_C.

Useful when modalities differ strongly. Examples: image, audio, time series, text. Or: PPG, IMU, sleep / events.

Pros: encoder optimized for signal physics; easy use of pretrained modality models.

Cons: many parameters; representation spaces may not align; harder scaling with many modalities.

### 2.2 Shared encoder

Alternative: x_A, x_B, x_C -> shared encoder.

Possible if modalities have similar structure or are transformed into a common representation. Need modality identity embeddings.

Benefits: parameter sharing; potentially better transfer; simpler architecture.

Risks: incompatible modalities interfere; one modality dominates; shared representation may be too restrictive.

Important question: "What structure is actually shareable?"

### 2.3 Shared backbone + modality adapters

Middle ground: modality-specific front end -> common latent dimension -> shared Transformer.

Example: IMU -> conv encoder, PPG -> conv encoder, HR -> projection, then a shared temporal backbone.

This is often a strong multimodal design. Front end handles signal-specific physics. Backbone learns shared higher-level relationships.

### 2.4 Projector

If z_m in R^(T_m x d_m) and the shared model expects d, use P_m: R^d_m -> R^d.

But dimensionality is only part of the issue. The projector also helps adapt representation geometry, not merely tensor shape.

This is the more sophisticated way to discuss LLaVA-style projectors. Do not spend the hour on LLaVA mechanics.

### 2.5 Early token fusion

Concatenate [z_A ; z_B ; z_text], then shared self-attention.

Benefit: every token can interact with every other token.

Cost: attention scales with total tokens (T_A + T_B + T_text)^2.

Problem: a long sensor stream can swamp text / context.

Also need: modality embeddings; time encodings; correct masking.

### 2.6 Cross-attention

Keep representations separate.

Example: Q = language / context, K,V = time-series representation. Or: Q = latent bottleneck, K,V = each modality.

Benefits: controlled interaction; avoid putting all tokens in the same sequence; supports different lengths; useful with pretrained frozen backbones.

Costs: additional modules; fusion happens only at chosen layers; modality may be ignored.

Important design dimension: WHERE do you insert cross-attention? Every layer? Sparse layers? Only top layers?

Earlier fusion: more low-level interaction. Later fusion: strong modality specialization.

This is the Flamingo-shaped idea applied to sensors — use it as a reference point, do not recap Flamingo.

### 2.7 Latent bottleneck / resampler

Important architecture to understand conceptually.

Long modality sequence z_1 ... z_10000. Instead of feeding all 10,000 tokens, use M learned latent queries q_1 ... q_M that cross-attend to the modality.

Output: M latent tokens, where M << 10000.

This is Perceiver / Q-Former / resampler-style thinking.

Why useful: fixed token budget; compress variable-length modalities; reduce LLM context cost.

Main risk: information bottleneck.

Question: how large should M be? Empirical tradeoff between compression and retained task information.

### 2.8 Hierarchical fusion

Not all modalities need to fuse at once.

Example: high-rate A + high-rate B -> local multimodal encoder -> event representation. Then events + text + low-rate context -> higher-level model.

This creates multiple fusion scales. Useful when modalities interact differently at different levels.

### 2.9 Bidirectional vs causal encoding

A sensor encoder does not automatically need causal masking.

If encoding an observed historical window, bidirectional attention may be fine.

If doing streaming / online inference, causal encoding may be required.

Then the language decoder can still be causal.

Architecture can therefore contain a bidirectional modality encoder + a causal language decoder. Important distinction.

### 2.10 Frozen vs trainable encoders

Options:

A. freeze modality encoder — cheap; preserves pretrained features; less overfitting

B. train projector only — LLaVA-like alignment stage

C. LoRA / adapter encoder

D. full fine-tuning

E. joint training from scratch

Decision depends on: amount of paired data; domain shift; encoder quality; compute; required specialization.

Your IC evidence: LoRA on the delay-image tower, freeze vs train, dual-stream collator. Say I, not we.

### 2.11 Alignment objectives

Different ways to align modalities.

CONTRASTIVE: matched representations close.

GENERATIVE: predict one modality / text conditioned on another.

MATCHING: binary matched / mismatched objective.

DISTILLATION: teacher modality -> student modality.

JOINT TASK LOSS: let the downstream supervised objective create alignment.

These create different representations. Do not assume contrastive alignment is always necessary. Do not name RelCon.

### 2.12 Multimodal instruction tuning

Once the modality representation is understandable to the LLM: input modality; User: "Describe..."; Assistant: ...

Teach not merely representation alignment, but how to USE the modality while following instructions.

For this interview: know it, but do not spend excessive time on LLaVA mechanics.

### 2.13 Architecture framework

For a multimodal architecture ask:

1. What does each modality encoder do?
2. Which parameters are shared?
3. Where do modalities first interact?
4. How often can they interact?
5. Is there an information bottleneck?
6. How many tokens enter the shared backbone?
7. Which components are frozen / trainable?
8. What objective creates alignment?

Pass condition for Module 2: given three modalities, you can design at least three distinct architectures and explain their computational and representational tradeoffs.

### Spoken (2026-08-29) — Module 2 pass condition

First take: (1) sep enc + concat — physics-aware / pretrained vs more params and handling; concat is simple and full mix vs quadratic in seq len. (2) sep enc + xattn — cost T*T_mod; more params; partial interaction. (3) shared rep + concat — fewer params, aligned rep; needs paired data and modality IDs.

Miss: did not instantiate the three streams or token math. Xattn con is neglect + chosen layers, not "more params"; cost is Tq*Tkv, not a vague T*T_mod. Shared-encoder con is not paired data — it is shareable structure; unpaired unimodal data can still work with IDs. Real cons: physics clash, dominance, tight shared space. Skipped the 2.3 middle (specific fronts → project → shared backbone) and the resampler bottleneck.

Lock: Instantiate audio 16 kHz + 10 Hz telemetry + text. Native-encode each; do not resample telemetry to 16 kHz.

Arch 1 — separate physics-aware encoders + concat: full mix, cost (T1+T2+T3)^2, need modality ID + time + mask + projectors. Long sensor stream can swamp text. First interaction = first shared self-attn. Token count into the backbone = sum of all modality tokens.

Arch 2 — separate encoders + cross-attn: cost about Tq*Tkv, so you do not put 10k sensor tokens into LLM self-attn. Interaction only at the layers you insert (early = low-level mix, late = specialist encoders). Real failure: B is ignored. Test: shuffle / drop B.

Arch 3 — shared backbone + concat only if structure is shareable, with IDs. Not "needs paired data."

Default I would actually draw: modality-specific fronts, project, shared Transformer; resampler (M queries, M << T) if LLM context is the tax. Information bottleneck is then explicit.

---

## Module 3 — Handle time, clocks, alignment, and missingness

Core question: Multimodal time series are not just multiple arrays. They occupy physical time.

This should be a major focus.

### 3.1 Index != time

For regularly sampled data, token index approximates time.

For irregular data, token 11 and token 12 could be 10 ms apart or 6 hours apart.

Therefore sequence position alone may not encode physical timing.

Need potentially: absolute timestamp; delta time; elapsed time; time-of-day; periodic encoding.

### 3.2 Multiple clocks

Example: audio 16 kHz; IMU 100 Hz; HR 1 Hz; event log irregular.

Naive approach: upsample everything to the fastest clock. Usually bad.

Why: sequence explosion; duplicated slow measurements; artificial interpolation; compute wasted; no new information.

Better: encode each modality at its useful native rate. Then fuse representations.

### 3.3 Two types of alignment

Important distinction.

PHYSICAL ALIGNMENT: do observations occur at the same time?

SEMANTIC ALIGNMENT: do they describe the same underlying event / state?

Example: IMU spike at t; heart-rate response may occur at t + delta. Exact timestamp equality is not necessarily the correct alignment.

Cross-attention can help learn soft temporal correspondence.

### 3.4 Hard alignment

Examples: bin everything into 1-minute intervals; nearest-neighbor match; interpolate.

Benefits: simple; fixed tensors; easy batching.

Costs: introduces assumptions; can blur events; can create fake data.

Use when alignment tolerance is scientifically justified.

### 3.5 Soft alignment

Encode each stream independently with time information. Then cross-attention, or attention restricted to a temporal neighborhood.

This allows learned associations across clocks.

Potentially: attention score depends on content similarity + time-distance bias. Conceptually useful even if implementation differs.

### 3.6 Time encodings

Potential components:

POSITION: order in sequence.

ABSOLUTE TIME: timestamp.

DELTA TIME: time since previous observation.

CALENDAR / PERIODIC: hour, day, season.

These answer different questions. Do not conflate positional encoding with physical-time encoding.

### 3.7 Irregular series

Representation can be (x_i, t_i) or (x_i, delta_i).

Possible models: time-aware attention; event Transformers; interpolation + mask; continuous-time models; neural ODE-style approaches; decay mechanisms.

You do NOT need deep knowledge of every approach.

Know the design issue: the model must know observation times and distinguish "no measurement" from "measurement equals zero."

Don't open with neural ODEs unless she goes there.

### 3.8 Missing modality

Example: sample A text + IMU; sample B text + PPG; sample C IMU only.

Do not discard samples.

Architectural choices: (A) variable modality set — include only available streams; (B) learned missing token; (C) availability mask; (D) modality dropout during training.

Need modality identity as well.

If she stays on architecture, pack present tokens. If she stays on "is missingness a shortcut / do we ship," that is Haraldur.

### 3.9 Partial missingness within a stream

Separate from an entire missing modality.

Example: PPG exists from 0–10 min and 20–30 min, but not 10–20 min.

Representation should preserve observation mask / time gap. Do not necessarily interpolate everything.

### 3.10 Temporal resolution of fusion

Important question: at what time resolution should modalities interact?

Example: audio + IMU may require sub-second fusion. HR + sleep: minute-scale fusion may be enough. Sensor + clinical note: possibly event / day-level fusion.

Fusion rate should be dictated by the phenomenon.

### 3.11 Causality

If the model predicts the future, do not allow future sensor tokens to leak through alignment or interpolation.

For offline understanding tasks, bidirectional modality context may be acceptable.

Always ask: is this offline representation, or online forecasting?

### 3.12 Clocks framework

For multimodal temporal data ask:

1. What is each modality's native rate?
2. What timing precision matters for the task?
3. Is hard synchronization scientifically meaningful?
4. Should fusion be hard-aligned or learned?
5. How are gaps represented?
6. Is the model causal?

Pass condition for Module 3: given asynchronous modalities, you do not immediately resample. You reason from the required temporal precision and interaction.

### Spoken (2026-08-29) — Module 3 pass condition

First take: each stream has its own encoder; keep encodings temporally related, not necessarily the same timestep; for health, same event is more realistic; do not drop irregular events when missing; each stream encodes a timestamp or time delta; then fuse with concat / xattn.

Miss: never said the fail line — I would not resample to the fastest clock. "Temporally related" did not split hard bins vs soft / learned alignment. Overfit to health: audio + machine telemetry may need tighter physical sync; precision comes from the task. Time is usually a token embedding (t, Δt, hour-of-day), not "the encoder knows how." Missing ≠ 0; do not interpolate holes away. Fusion rate (100 ms vs bout vs day) is a third knob. If you forecast, no future through the aligner.

Lock: Each stream stays on its native clock with its own encoder. I would not upsample to 16 kHz. Tokens get t or Δt so index is not time. I align to the event the task cares about, not necessarily the same sample index. Gaps stay as missing, not zero. Then concat or xattn at that fusion rate.

---

## Module 4 — Train, diagnose, and choose between architectures

Core question: How do we know one multimodal architecture is actually better?

This module combines training strategy with architectural science.

### 4.1 Build a representation bakeoff

Suppose candidates: (A) numeric text, (B) patched native encoder, (C) chart / image, (D) spectral representation.

Do not debate from intuition alone.

Keep fixed: train / test data; downstream task; language backbone where applicable; training budget; evaluation protocol.

Measure: task quality; token count; FLOPs; latency; memory; label efficiency; robustness.

HM-screen three families (text / patched native / images) are hypotheses here, not a 2–3 min recap of Shirley. Caption eval is not CE / ROUGE (Feng leftover) if a language head appears.

### 4.2 Separate encoding from fusion

Do not change everything simultaneously.

Experiment 1: same fusion, different encoders.

Experiment 2: same encoders, different fusion.

Otherwise you cannot tell why the model improved.

### 4.3 Information bottleneck sweep

If using patch size P or M resampler tokens, sweep compression.

Example: M = 8, 32, 128, 512.

Ask: when does performance saturate? This tells you how much modality information is actually needed.

Your cls_only vs patches (~64x compression, about -6 pp) is IC evidence for this sweep. Say I.

### 4.4 Token-cost curves

Compare performance vs number of modality tokens.

A representation giving +0.5% quality at 20x token cost may not be attractive. This is especially important when fusing with an LLM.

### 4.5 Pretraining / freezing bakeoff

Compare: frozen encoder + projector vs encoder LoRA vs full encoder fine-tune vs joint training.

This answers: does adaptation matter? And: where does improvement come from?

### 4.6 Alignment objective bakeoff

Could compare: task loss only vs contrastive + task vs generative alignment + task.

Do not automatically add more losses. Check whether the alignment objective improves actual downstream behavior.

### 4.7 Modality neglect

Critical multimodal failure. Model nominally receives A and B but predicts almost entirely from A.

Test: REMOVE B; SHUFFLE B; TIME-SHIFT B; REPLACE B WITH NOISE.

If quality barely changes, B is not meaningfully used.

Attention visualization alone is not enough.

### 4.8 Modality dominance

One modality may dominate due to: easier optimization; larger token count; stronger pretrained encoder; more informative labels; larger embedding scale.

Things to inspect: gradient norms by encoder; embedding norms; ablations; learning curves; modality-specific performance.

Potential interventions: balanced sampling; normalization; modality dropout; auxiliary objectives; architectural bottleneck.

### 4.9 Representation scale mismatch

Suppose ||z_image|| ~= 2 and ||z_sensor|| ~= 100. This can affect shared attention / fusion.

Need: projection; normalization; initialization; possibly learned scaling.

Multimodal alignment is numerical as well as semantic.

### 4.10 Training stages

Possible staged setup:

STAGE 1: train projector / alignment; freeze large backbones.

STAGE 2: unfreeze / LoRA shared model; perform multimodal instruction / task training.

STAGE 3: domain / task specialization.

But do not present staged training as mandatory. Alternative: joint end-to-end training when enough data / compute exist.

Your Stage A then B (caption prior, then task) is the IC story. I owned the recipe and the gate.

### 4.11 Paired vs unpaired data

Some modalities may be jointly observed only rarely.

Example: lots of IMU; lots of text; small paired IMU-text set.

Possible strategy: unimodal pretraining + paired alignment + multimodal task tuning.

Architecture / training strategy should exploit all data, not only fully paired samples.

### 4.12 Scale after representation is validated

Before making the model much larger, ask whether scaling fixes the real limitation.

If encoding discarded important information, a larger LLM cannot recover it.

If fusion ignores a modality, a larger LLM may ignore it even better.

Important line: "Model scale cannot recover information removed by representation."

27B != TSRBench unless the representation and gate earned it.

### 4.13 Failure-diagnosis framework

If a multimodal model performs poorly, inspect:

1. INPUT REPRESENTATION — did encoding preserve information?
2. MODALITY ENCODER — does each encoder produce useful features?
3. ALIGNMENT — are embeddings compatible?
4. FUSION — can information actually cross modalities?
5. OBJECTIVE — does the loss require multimodal use?
6. DATA — are examples solvable from one modality alone?
7. OPTIMIZATION — do gradients reach each component?

This is a much better answer than immediately changing architecture.

### Module 4 practice

Case 1: native TS encoder beats chart representation. Ask why. Design experiments to determine whether the gain is from information preservation, token count, architecture, pretraining, or optimization.

Spoken Case 1 (2026-08-29):

First take: information — train a TS decoder to recover the signal; vary chart resolutions. Token count — compare performance across token counts via different TS encoder dims vs different chart resolutions. Pretraining — zero-shot TS enc vs chart, then FT both.

Miss: token count is not encoder hidden dim. Chart res is rendering, not N. Zero-shot TS is meaningless if the TS encoder has no prior. Skipped architecture (same fusion / head, only swap encoder) and optimization (same data, steps, LR, seeds).

Lock: Hold fusion and the head fixed; swap only the encoder. Information: reconstruct the series from native latents; for the chart, recover numbers / high-freq from the image and raise render resolution — if the gap closes, the renderer threw information away. Token count: match N into the same backbone (sweep P or M vs ViT patches / image size / merge); plot quality vs N. Pretraining: only zero-shot if both have a prior; then freeze+probe vs FT. If the chart only looks good with a pretrained ViT and the TS encoder is random, the native win may be in-domain training. Same train recipe so it is not just optimization.

Case 2: dual modality beats single modality by 2%. Test shuffled second modality; missing second modality; parameter-matched control.

Case 3: cross-attention underperforms concatenation. Potential reasons: cross-attention inserted too late; insufficient capacity; modality ignored; fusion needs low-level interaction; optimization issue.

Case 4: performance improves as patch size increases until P=64 and then falls. Interpretation: compression initially removes redundancy, then begins removing task-relevant information.

Pass condition for Module 4: you can diagnose a multimodal result using experiments rather than architecture preference.

---

## Integrated architecture cases

These should be the bulk of your actual practice.

Case A — audio + telemetry + text. Inputs: audio at 16 kHz; machine telemetry at 10 Hz; maintenance notes. Task: answer questions about machine condition. Design: audio encoder? telemetry encoder? text model? fusion level? alignment? token compression? Then ask: would you resample telemetry to 16 kHz? No. Why? This is useful because it removes you from the health setting.

Spoken integrated Case A (2026-08-30):

Opening first take: separate towers for audio and telemetry; normal LLM text tokens. Patch / encode / aggregate 16 kHz audio, perhaps with a pretrained STFT-based encoder. Encode telemetry patches [T, C] jointly because channel-separate tokens multiply length. Keep encoders separate because signal structure differs. Put time in patches. Use text-query cross-attention over sensor K/V; concat only if the sensor sequence can be compressed safely; resample only if events survive.

Follow-up: 24 hours, failure at 14:32:04, audio precursor at 14:31:57. First take switched to event tokens containing signal + timestamps / delta-time, retaining local irregularities and ignoring normal periods. Correctly chose text Q and audio + telemetry K/V with cost about T_text * (T_audio + T_telemetry), but did not compute raw counts or distinguish hard vs soft alignment.

Challenge: a slow 30-minute drift also causes failures and replacing audio with noise changes little. Updated representation to coarse aggregated normal coverage + fine event tokens; selected soft alignment; proposed remove / zero / random / shuffle audio. Diagnosis order: data -> optimization -> fusion -> encoder.

Factual correction: zero replacement is OOD and not strong evidence. Prefer the valid missing path, cross-example shuffle, or time-shift. Raw scale: audio = 16,000 * 86,400 = 1.3824B samples; telemetry = 10 * 86,400 = 864K timestamps x 20 = 17.28M values.

Missing decision: make the information bottleneck explicit. Coarse tokens preserve complete-day coverage / slow drift; fine tokens preserve anomalies. Do not irreversibly discard all local latents before seeing the query. Sweep the coarse / fine or resampler budget.

Spoken lock: I would use separate native encoders: an audio front end, likely spectral or convolutional, and a multichannel telemetry encoder. I would not resample telemetry to 16 kHz. Each produces timestamped local latents. I would preserve the day at two resolutions: coarse tokens for full coverage and slow drift, plus fine tokens around candidate events. Because the audio precursor and telemetry response are seven seconds apart, I would keep physical timestamps and use soft alignment, with text as Q and the timestamped sensor memory as K/V. If memory is too large, I would sweep a resampler budget rather than discard all normal intervals. To test audio use, I would remove, shuffle, and time-shift it; then probe the audio encoder before blaming fusion or optimization.

Rapid checks:

1. Correct: upsampling 10 Hz telemetry to 16 kHz bloats the sequence with invented / repeated values; retain native-rate encoders. Add: compress locally, timestamp the resulting latents, then fuse.

2. Miss: soft alignment is not variable-length bins. Hard alignment forces shared bins / nearest matches before fusion. Soft alignment keeps independently timestamped streams and learns correspondence, optionally with a time-distance bias or local window. Choose soft here because the meaningful response is delayed by seven seconds, not primarily because of token count.

3. Partial: unchanged output after time-shifting audio suggests aligned audio is ignored. Check whether the task is solvable from audio with an audio-only probe, then verify the encoder preserves the feature and whether gradients reach it. Do not jump first to an unspecified cross-attention parameter.

Spoken follow-up mock (2026-08-31), 15 min, mid-conversation. Already treated as covered: native encoders, no resample to 16 kHz, projector, concat vs cross-attention as a named fork. Prompt: 24 h of 16 kHz audio, 20-channel telemetry at 10 Hz, maintenance note; fail at 14:32:04; audio interesting at 14:31:57. How many tokens enter fusion, and is the seven-second lag binning or learned alignment?

First take: second-scale bins explode; slow/fast event tokens; a few hundred tokens per modality (lower if concat); soft alignment so short events survive a long record.

Follow-up: raw sample counts; what is stored for the whole day versus only around candidates; who proposes the candidates. First take: audio ~1.5B; telemetry ~1.8M; pretrained encoders, then fine-tune with the LLM so events are learned; ~1000 tokens per stream; wide embedding plus fine-tuning will represent the original well.

Follow-up: 1000 tokens over 86400 s is about 86 s per token if the day is tiled; a seven-second precursor sits inside one token; pick a second finer memory (with M) or admit the seven-second structure is gone. First take: hierarchical bins; extra ~100 tokens; text attends “low-level” first, then top-k “high-level”; delta-time between tokens.

Miss: telemetry is 864k timestamps (~17.28M values if 20 channels are flattened), not 1.8M. Raw samples are not tokens. “Event-based” can drop the precursor before the note queries memory. Coarse and fine were named backwards (aggregate was called low-level; local detail was called high-level). Top-k over 86-second pools cannot retrieve a seven-second event that was already averaged away. Delta-time is spacing inside one stream; the cross-modal lag needs physical time. Wider hidden size and fine-tuning do not restore a time resolution the encoder discarded. No remove / shuffle / time-shift of audio.

Spoken lock: I would keep each stream on its own sampling rate and I would not upsample telemetry to 16 kHz. Over 24 hours that is about 1.38 billion audio samples and 864 thousand telemetry timestamps, or about 17 million values if the 20 channels are flattened, so the language model never sees raw samples. I would keep two resolutions that both cover the day. Coarse tokens tile the full 24 hours so a slow drift is still present; a thousand such tokens is on the order of a minute each, which is the clock the language model sees at that stream. Fine tokens use a much shorter hop, on the order of the seven-second precursor, with a budget I would sweep rather than fix in advance — for example 32, 100, and 256. I would not throw those fine latents away before the note can attend to them, and I would not rely on a separate peak detector to decide what is kept. Looking first at coarse tokens and then zooming into the top-k does not recover an event that was already mixed inside an 86-second pool. Making each token wider, or fine-tuning the language model, also cannot restore time resolution that the encoder already discarded. Because the audio cue and the telemetry failure are seven seconds apart, I would put physical timestamps on the latents, not only the gap between consecutive tokens in one stream, and I would let the model learn correspondence: text as queries, timestamped sensor memory as keys and values. If that memory is still too large I would sweep a resampler while keeping the coarse day, rather than dropping all quiet intervals. To check that audio is used I would remove it, shuffle it across examples, and time-shift it, then probe the audio encoder before I change fusion.

Case B — video + time series. Inputs: video; accelerometer; GPS. Task: understand physical activity. Questions: image / video patches vs IMU patches; timestamp alignment; shared latent space; cross-attention vs joint tokens; different clock rates.

Case C — wearable health. Inputs: PPG; IMU; HR; sleep; text / self-report. Use health as one application of the same architectural principles.

Case D — industrial sensor foundation model. 100 heterogeneous channels; different rates; many missing channels; years of data. Question: shared encoder or per-sensor encoder? How do you tokenize channel / time? How do you avoid sequence explosion?

Case E — multimodal forecasting. Historical numerical sequence + text events + images / context. Task: forecast future numerical trajectory. Question: at what point do modalities fuse? Does the future decoder need direct access to every modality?

These cases make your reasoning general rather than Apple-Health-specific.

---

## Likely Yujie questions

Q1. How would you encode a continuous time series for an LLM?

Spoken Q1 (2026-08-29):

First take: multiple ways — (1) one token per sample, (2) patchify and encode, (3) TS as an image, (4) state-space / delay, (5) STFT.

Miss: a menu, not an LLM answer. Skipped numeric text (the trivial LLM baseline). Did not reject point-wise on token count. No preserve / lose / N / bias, no projector / resampler, no bakeoff, no task pick.

Lock: Text-of-numbers is a short-series baseline, not the default (no new encoder, terrible N, weak continuity). Reject one token per sample on anything dense — 100 Hz × 1 hour = 360k. Default if local structure matters: patch, native encoder, project to d_LLM (or resample to M tokens). Chart → ViT only if the series is short and I am stealing a visual prior — not "images keep the numbers," not raw PPG. STFT if the object is spectral; delay / state if the object is dynamics. Tokens get modality + time IDs. Then a matched-N bakeoff (Case 1). Do not open with a Transformer on 360k samples.

Q2. What are the tradeoffs between patching and discretization?

Spoken Q2 (2026-08-29):

First take: patching reduces N = T/P; too wide loses info, too small too many tokens. Discretization: pick bins and how many; loses info (span); fits LLM better because tokens are discrete. Binning every numeric value is very costly, too many tokens.

Miss: treated both as N-reduction. Patching groups time; the patch is still a continuous vector. Discretization is a codebook bottleneck (quantization error, collapse, clipped range), not P. "Fits the LLM" is only for token-ID generative modeling — an LLM can take continuous patch embeddings via a projector. Per-sample bins are still ~T tokens.

Lock: Patching is time-resolution vs token count; the patch stays a real vector you project. Discretization is a vocabulary bottleneck — useful for discrete generative TS, bad if I need the actual values. I would not bin every sample. If I discretize, I VQ the patches and I ask what the codebook must preserve.

Q3. How would you decide patch size?

Spoken Q3 (2026-08-29):

First take: decide from signal nature and the effect in question; high freq → smaller P; long event → wider P; ablate task vs multiple P; if larger P does not change results, take the minimal token count.

Miss: long event ≠ wide patch. A 30-minute workout is context; P should match the local pattern, then pool. High-Hz IMU does not force small P unless the task uses that freq. P should be stated in seconds, then converted to samples (device rate can change).

Lock: P is the backbone’s clock. Set it from the phenomenon the task needs, not from T or from how long the record is. Sweep P; quality rises while you strip redundancy, then falls when you eat the event (Case 4). On the plateau, take the fewest tokens. A long horizon gets hierarchy, not a 30-minute patch.

Q4. When is a convolutional encoder preferable to direct patch projection?

Spoken Q4 (2026-08-29):

First take: conv is locally translation equivariant; may use fewer params than a dense proj; conv can be trained separately; direct proj has to deal with noisy and huge data.

Miss: "trained separately" is true of any front end, not conv vs linear. Direct proj is not uniquely stuck with huge noisy data — it is the minimal prior. Dense flatten of a fat patch is what blows params; a small-P linear map can be cheaper than a deep conv.

Lock: Linear proj is a flat map of the patch — cheapest prior; use it when P is already small or data is scarce. Conv front end when local motifs and shift-equivariance matter, and I want shared filters plus stride to compress. Bake off both under the same N and the same backbone.

Q5. How would you handle multivariate series with hundreds of channels?

Spoken Q5 (2026-08-29):

First take: (1) split channels → univariate, no seq explosion, but no cross-channel interaction. (2) encode multivariate [P, C] → d; info loss but cross-channel rep.

Miss: inverted the token math. Split multiplies N by C — that is the explosion. Channels together keeps N = T/P; the cost is a fat P×C → d bottleneck and a fixed channel set. Skipped group-then-joint and channel IDs / metadata.

Lock: If I split 200 channels I multiply N by 200. I’d keep channels in the patch or in small groups so N stays T/P, accept a P×C→d bottleneck, and mask missing sensors. I’d only tokenize channels separately when I need to drop them independently or their physics don’t share a patch. Channel identity (and units / type / location) if tokens are separate.

Q6. Would you use one encoder per modality or a shared encoder?

Spoken Q6 (2026-08-29):

First take: shared if paired data, shareable bias, low mem, fewer components. One encoder per modality if physics-adapted, strong pretrained, modalities very different, no shared bias, no paired data.

Miss: paired data is not the fork. A shared encoder needs shareable structure + IDs; unpaired unimodal batches are enough. Pairing is for alignment. "No pairs ⇒ separate" is backwards — scarce pairs is when you unimodal-pretrain specialists, then a small paired align stage. Skipped the 2.3 middle.

Lock: Share a backbone only if the structure is shareable, with IDs — mem and simplicity, not pairing. If physics or pretrained specialists disagree, separate fronts. Default draw: specific encoders, project, shared Transformer.

Q7. How would you combine time series and text?

Spoken Q7 (2026-08-29):

First take: (1) concat TS tokens after enc → proj with text tokens; (2) xattn, text = Q, TS = K/V.

Miss: named the two fusions (that is Q8) without the pipeline. Did not say encode/compress first, modality + time IDs, resampler if N is huge, or neglect test.

Lock: Q7 is the stack, not the fork. Encode the series at a useful rate, project to d_LLM, add modality + time IDs, then fuse with text. Do not concat raw 100 Hz with words. Cheap stage: freeze LLM, train projector. Then LoRA if needed. Ablate the series so it is not a text-only model. How they fuse is Q8.

Q8. When would you concatenate modality tokens versus use cross-attention?

Spoken Q8 (2026-08-29):

Same two designs as the Q7 first take. Logged here as the when / tax, not a second architecture menu.

Lock: Concat after project — full mix, cost (N_ts+N_text)^2, sensor can swamp text. Use when N_ts is already small (behavioral / resampled / daily). Xattn, text = Q, TS = K/V — cost ~ N_text*N_ts, LLM does not self-attend 10k sensor tokens; fail is neglect (shuffle / drop TS). If even that is too many tokens, M latent queries (Q9), then concat or xattn those M.

Q9. Why would you introduce a latent resampler?

Q10. How do you choose the number of latent modality tokens?

Q11. How do you handle two modalities sampled at very different rates?

Q12. Why not just resample everything to the same frequency?

Q13. How do you encode irregular observation times?

Q14. How do you distinguish positional encoding from physical-time encoding?

Q15. Where should multimodal fusion happen?

Q16. When should fusion happen at multiple levels?

Q17. How would you train when only a small subset of samples has all modalities?

Q18. How do you tell whether the model actually uses modality B?

Q19. Why might cross-attention fail?

Q20. Why might early fusion fail?

Q21. What happens if one modality produces 100x more tokens than another?

Q22. How would you prevent one modality from dominating?

Q23. How would you compare native TS encoding against image encoding?

Q24. What information might STFT expose that raw patches do not?

Q25. When would discretizing time series into tokens make sense?

Q26. Would you freeze the modality encoder?

Q27. What does staged multimodal training buy you?

Q28. Can a larger LLM compensate for a poor time-series encoder?

Q29. How would you design a multimodal representation bakeoff?

Q30. How would you diagnose a model whose multimodal validation loss improves but whose downstream TS reasoning does not?

Also keep: sampling rate changes across device gens; token budget — what do you drop first.

---

## Recommended practice schedule

Allocate approximately 40% learning / review, 60% architecture exercises.

Session 1 — Time-series encoding, ~2 hours. Learn / review: patches; convolutional downsampling; multivariate tokenization; continuous vs discrete tokens; STFT / spectral representations; normalization; physical-time encoding. Practice: given 5 time series, propose 3 encodings each. For every encoding explicitly say: preserves; loses; token cost; inductive bias.

Session 2 — Multimodal architectures, ~2 hours. Review: modality-specific encoders; shared encoders; adapters / projectors; early fusion; cross-attention; latent bottlenecks / resamplers; hierarchical fusion. Practice: design 3 architectures for the SAME problem. Example: audio + telemetry + text. Architecture A: joint tokens. Architecture B: cross-attention. Architecture C: hierarchical / resampler. Then compare.

Session 3 — Time + alignment, ~90 min. Review: physical vs positional time; multiple clocks; hard vs soft alignment; irregular sampling; causality. Practice: 16 kHz audio + 100 Hz IMU + 1 Hz signal + irregular events. Design fusion without naive global resampling.

Session 4 — Training + failure modes, ~90 min. Review: frozen vs trainable encoders; staged training; alignment objectives; missing modalities; modality dominance; modality neglect. Practice diagnosis: "Model ignores sensor." "Cross-attention fails." "More modality tokens hurt." "Joint training destabilizes pretrained LLM."

Session 5 — Representation bakeoff, ~60 min. Compare: numeric text; patch encoder; STFT; chart / image; discrete codes. Define: hypothesis; controlled experiment; metrics; token budget; ablations; kill criterion.

Session 6 — Yujie mock, 45–60 min. One evolving architecture problem. Example: "We have audio, several time-series sensors, and text." Then progressively: rates differ by 1000x; half modalities missing; text model is pretrained; sensor data abundant; paired text / sensor data scarce; need long history; model ignores sensor; inference budget tight. Adapt the architecture each time.

First Wednesday slot is this mock shape, not a health-metrics hour.

---

## What to memorize

Only four frameworks.

Framework 1 — TIME-SERIES ENCODING: information preserved + information lost + token count + inductive bias.

Framework 2 — MULTIMODAL ARCHITECTURE: encoder per modality -> projection / common representation -> fusion location -> shared backbone / decoder.

Framework 3 — TEMPORAL FUSION: native rate -> local encoding -> temporal compression -> alignment -> fusion.

Framework 4 — DIAGNOSIS: representation -> encoder -> alignment -> fusion -> objective -> data -> optimization.

---

## Final pass condition

You are ready when Yujie can give you an unfamiliar multimodal problem and you naturally ask:

1. What is each modality mathematically?
2. What information needs to survive encoding?
3. What temporal resolution does the task require?
4. How many tokens will each representation generate?
5. Which encoder biases are useful?
6. Which parts of the architecture should be modality-specific?
7. Which parts should be shared?
8. Where should modalities interact?
9. Do they need exact synchronization?
10. How should physical time be represented?
11. How should missing modalities be handled?
12. What information bottleneck am I introducing?
13. What objective will make modalities align?
14. How will I test whether the model actually uses each modality?
15. What controlled experiment would choose between the candidate architectures?

---

## Traps

Don't replay Shirley's 2–3 min encodings as the whole hour. Use the four encoding questions.

Don't make LLaVA vs Flamingo the hour. Use them as reference points for projector and cross-attention.

Don't say images keep all information. Own ablation.

Don't recite 2.5B hours / 162k / 57 tasks.

Don't name WBM / ICML.

Don't force matplotlib onto PPG.

Don't resample every stream onto the fastest clock.

Don't let a larger LLM "fix" a bad encoder.

Don't turn her hour into PPV / calibration / ship unless she pulls it.
