# On-site — Haraldur Hallgrímsson (Wed 3:05 PDT)

Track: health / applied ML / wearable TS. Conf: very high. Most Apple-Health-specific Wednesday hour.

Who (private): Senior Applied RS, Health AI, Seattle. RelCon, TS-LLM, periodicity. Public: sensor FMs to Watch hypertension / AirPods calories (modeling and infra). Hub: 2026-08-27_onsite-prep.md

Cultural signal (do not recap papers): this group will keep periodic features + GBDT when they beat a deep TS model under missingness shift. SSL motion FMs exist too (~3.9M encoder, 1B segments — not 1B params).

Do not assume deep learning wins.

Do not name RelCon / periodicity paper / Workout Buddy / his LinkedIn posts. Do not say you shipped a Watch feature. Token schemes for three-year history live on the Yujie sheet — if he stays on labels / missingness / ship, stay here.

Posture in one line: I want to know not only whether the sophisticated model wins, but what it learned, under which data assumptions, and whether that advantage survives the distribution we actually deploy on.

Target profile: can reason about wearable ML from representation learning all the way to robust deployment.

---

## Saturday Block B — how to use this file

He might run Health Domain & Applied ML Judgment, or wearable representation / SSL / missingness. Prep both. Do not overfit one mapping.

Chain: wearable data -> representation -> training objective -> downstream model -> evaluation -> deployment shift -> product decision.

Weight (if you have a full day): ~30% health evaluation + applied judgment; ~25% missingness + shift + robustness; ~20% wearable representation / SSL; ~15% longitudinal + personalization; ~10% foundation-model / multimodal architecture details. Broader than a pure health-judgment prep; narrower than a generic multimodal interview.

Today (Sat, shared with Yujie, ~4h total): do H1, H3, H4, H7, then Mock H. Skip H9 unless a mock fails. Abstracts only — RelCon, Periodicity, Beyond Sensor Data — do not name-drop.

If unclear how he opens: start with task and data; let him pull architecture or product.

---

## Open (30s)

First I'd define the deployment setting — target, who acts, when the prediction is made, what history exists then, missingness, operating point, cost of FP vs FN. I'd put a strong statistical / tree / classical TS baseline on the table before I decide whether representation learning buys anything.

Then bakeoff. Do not jump to Transformer / foundation model / LLM.

---

## H1 — Deployment, then the data regime

### Start with the deployment problem

Before choosing an architecture, clarify:

- What exactly is the target?
- Who are the users?
- At what time is the prediction made?
- What data are available at that moment?
- What prediction horizon matters?
- What action follows the prediction?
- What are the costs of FP and FN?
- Is this screening, monitoring, recommendation, or intervention?

Strong answer style:

"Before choosing the model, I'd define the deployment setting because the target, available history, acceptable errors, and evaluation protocol all depend on how the prediction will be used."

### Wearable data — know the regime

Possible modalities: accelerometer / IMU; PPG; heart rate; HRV; sleep; workouts; steps; mobility; behavioral summaries; text / self-report; clinical labels.

They differ in sampling rate, noise, missingness, power cost, temporal semantics, and the relevant downstream horizon.

IMU: dense, high frequency, motion-heavy.

PPG: rich physiology, higher-frequency waveform, quality sensitive.

HR / HRV: lower-rate derived physiological signal.

Sleep / workouts / steps / mobility: minute to day.

Behavioral summaries: hour / day / week.

Text, self-report, clinical labels: different noise and delay.

Core question (same as Yujie): what temporal scale does the task require? That should drive representation choice. Sleep next night != 5-year risk != 10 s gait.

### Raw / local vs aggregate vs hierarchical

Do not force one representation across all temporal scales.

Raw / local signal model:

raw signal -> patch/window -> sensor encoder -> latent representation

Pros: preserves fine temporal detail; can discover features; useful for waveform-level tasks.

Cons: expensive; noisy; long sequences; data hungry.

A patch is tokenize-then-learn. A 100 Hz IMU patch of 1 s is still the waveform (100 samples -> one latent). The model can still see shape, transients, cadence.

Aggregate / behavioral features:

Examples: daily steps; resting HR; sleep duration; workout duration; periodic features; rolling statistics.

Pros: compact; interpretable; often aligned with longitudinal health outcomes; robust; cheap.

Cons: loses waveform detail; depends on feature engineering.

Aggregation is not one operator. Match the quantity:

- Totals: sum — steps, calories, minutes asleep.
- Levels: mean or median — HR, HRV, cadence. Median if outliers or holes.
- Extremes: min / max — peak HR, longest sedentary bout.
- Variability: std, IQR — irregularity, not the mean.
- Clock / routine: mean by hour-of-day, day-of-week, a few Fourier bins.
- Wear: hours observed, fraction worn. Never treat missing as 0 and then average.

Do not average 100 Hz IMU into one daily number and call it a representation. If the task is longitudinal (mood, risk, next-night sleep), start with behavioral aggregates + GBDT. If the task is local physiology (gait, arrhythmia, a workout bout), patch the raw window.

Hierarchical representation:

raw signal -> local encoder -> minute/hour latent -> day-level latent -> longitudinal model

Often a strong architecture for long wearable histories.

### What information does each representation preserve?

For every encoding, ask:

1. What information is preserved?
2. What information is discarded?
3. What is the token / compute cost?
4. What inductive bias is introduced?
5. What temporal scale is represented?
6. How robust is it to missingness?
7. Does it transfer across tasks?

This is the main framework for representation discussion.

### Sensor token budget

Raw 100 Hz stream: 100 samples/sec = 360,000 samples/hour. Cannot naively map each sample to one LLM token.

Need: raw signal -> patch / conv / local encoder -> compressed latent tokens -> higher-level model.

Main tradeoff: compression vs information loss.

### Asynchronous modalities

Example: IMU 100 Hz, HR 1 Hz, sleep every several minutes.

Do not force everything onto 100 Hz. That creates huge sequences, artificial interpolation, and unnecessary duplication.

Possible approach: encode each modality at native/local resolution -> compress -> align on a latent timeline -> cross-attend / fuse.

### Irregular sampling

Missing observation != zero.

Possible representation: (x_i, t_i) or (x_i, delta_t_i) or explicit event times.

Potential approaches: time embeddings; interpolation + mask; event-based models; irregular-aware encoders. Neural ODE / continuous-time models only if he goes there. Do not overcomplicate unless asked.

### When to use an LLM

Do not default to an LLM for low-level sensing.

Separate: (1) perception, (2) representation, (3) longitudinal reasoning, (4) language interface.

Native sensor model may handle 1-2.

LLM may help with combining semantic context, instruction following, summaries, heterogeneous modalities, natural language interaction.

Strong answer: "I would not feed raw high-frequency sensing directly into an LLM unless evidence showed that was beneficial."

---

## H2 — SSL, contrastive, distillation

### Why SSL

Typical health setting: unlabeled wearable data >> labeled health outcomes.

Pipeline: large unlabeled corpus -> SSL encoder -> frozen probe / fine-tune -> downstream tasks.

Possible objectives: contrastive learning; masked reconstruction; future prediction; temporal consistency; cross-modal alignment; knowledge distillation.

The key question is not "what SSL algorithm do you know?"

It is: what invariances and structure should the objective encode?

### Contrastive learning

Generic form: z_i = E(x_i)

InfoNCE-like objective:

L_i = -log [ exp(sim(z_i, z_i+) / tau) / sum_j exp(sim(z_i, z_j) / tau) ]

Focus on positive construction, not the formula.

Wearable questions:

- Is rotation an invariant? (watch orientation)
- Is small temporal jitter acceptable?
- Is crop preserving semantics? Same bout?
- Can time warping destroy cadence?
- Should different intensity levels count as similar?
- Does augmentation preserve physiology?

Strong line: "An SSL augmentation is a modeling assumption about invariance."

Do not copy image augmentations blindly.

### Relative / domain-aware similarity

Binary positive/negative pairing may be too crude.

Two sensor windows may be: nearly equivalent; related but not identical; unrelated.

A relative / domain-aware objective can represent a richer geometry.

Potential answer: "Generic contrastive learning can impose the wrong equivalence classes. For wearable signals I would prefer similarity definitions grounded in signal semantics or downstream invariances."

Do not name RelCon.

### Cross-modal distillation

Useful setup: rich modality at training -> teacher; cheap / widely available modality -> student.

Example: PPG teacher -> accelerometer student.

Use synchronized paired data to align representations.

Potential deployment advantage: train with rich modality, deploy with cheaper modality only.

Questions to ask:

- What information is predictable cross-modally?
- Does the student learn physiology or just activity?
- What happens under missing teacher data?
- Does transfer survive participant / device shift?

Wearable views are not a photo-caption pair. IMU does not substitute for PPG. Alignment only transfers what is actually shared.

### Foundation model evaluation

Do not call it useful because it is large.

Test: multiple downstream tasks; low-label regimes; linear probe; frozen encoder; full fine-tune; unseen participants; device shift; missingness; temporal scale transfer.

A foundation model should demonstrate transfer.

### Linear probe vs fine-tune

Linear probe: freeze representation, train a simple head. Question: is useful information already present in the frozen z?

Fine-tuning: allows the encoder to adapt.

If all gains appear only after full fine-tuning, the pretrained representation may be less universal than claimed.

### Label efficiency

One strong reason for sensor pretraining: performance as a function of labeled data — 1% / 5% / 10% / 100%.

If the pretrained representation greatly helps at 1-10% labels, that is meaningful evidence.

Do not only compare full-data accuracy.

### Negative transfer

A foundation model may improve some tasks and hurt others.

Possible reasons: wrong invariances; temporal-scale mismatch; compressed away an important feature; modality mismatch; domain shift.

Report task slices, not only the mean.

### 100x unlabeled IMU — answer spine

SSL pretrain; domain-appropriate invariances; frozen representation evaluation; label-efficiency curves; fine-tune; participant holdout; device / missingness stress tests; compare to a strong simple baseline on the same label budget.

If the FM loses at realistic labels, keep the simple model.

### PPG on 20%, IMU on 95%

Possible design: paired PPG/IMU cross-modal pretraining; PPG teacher; IMU student; IMU-only SSL on the remaining unpaired mass; deploy IMU if needed; verify knowledge transfer on downstream tasks.

---

## H3 — Missingness (architecture and statistics)

### Architecture

Suppose examples contain: IMU only; HR + sleep; PPG + IMU; all modalities.

Do not drop incomplete rows.

Possible handling:

A. Variable-length modality set: include only present modality tokens. Pack what you have. Like packing vs pad-to-max: only real tokens, modality ID, time, attention over what exists.

B. Fixed slots: learned missing token; presence mask; modality identity embedding. Same length every row. Simple batching. The dummy can become a shortcut for the missingness process.

Do not blindly encode missing as zero.

Architecture should distinguish "measurement is zero" from "measurement is unavailable."

Your lock: pack present modalities with IDs, not pad missing streams to a fixed slot. Add a small availability / wear-time vector so absence is explicit but not a fake waveform. Train with modality dropout so any subset works. Do not treat another sensor as a substitute view of the missing one. Then stress-test when the missingness process changes — that is the kill, not whether the forward pass accepts holes.

### Missingness as a statistical issue

Do not stop at masking.

Three questions:

A. Can the model technically handle missing data?

B. Is missingness informative? Often P(M | X, Y) != P(M). Reasons: device not worn; battery; illness; behavior; activity; adherence; poor sensor contact.

C. Will missingness shift? P_train(M) != P_deploy(M). Firmware, battery, adherence, illness. This can break a model that learned availability shortcuts.

Informative missingness is a signal and a shortcut risk.

Eval is not "can it impute." It is: does performance hold when the missingness process changes.

### Missingness stress tests

Do not evaluate only on naturally missing test data.

Create controlled tests:

- remove random channels
- remove specific high-value channels
- increase missing duration
- simulate lower wear time
- change modality availability pattern
- evaluate sparse-user subset

Plot performance vs missingness severity. Compare robustness curves, not only average performance.

### Most users don't wear continuously

First quantify: performance vs wear time.

Then consider: natural missingness; explicit availability; missingness-aware training; modality dropout; robust aggregate features; uncertainty; sparse-user subgroup; whether sparse use itself correlates with the target.

---

## H4 — Baselines, periodicity, kill the deep model

### Simple baselines are high priority

Do not assume deep model > simple model.

Build a baseline ladder:

1. population mean / simple heuristic
2. rolling statistics
3. periodic features
4. logistic regression / linear model
5. LightGBM / XGBoost
6. conventional / classical time-series model
7. pretrained sensor encoder
8. foundation model

Classical TS means statistical series models, not a third tree: seasonal naive, ETS / Holt-Winters, SARIMA, STL + a simple residual model, maybe Kalman / state-space. Use that rung when the task is the series (next-night sleep, resting-HR trajectory). Skip or treat as weak when the task is a label from messy wear — periodicity + GBDT already ate the clock. Do not open with ARIMA on raw IMU.

Question: what earns the complex model the right to exist?

Possible benefits: label efficiency; transfer across tasks; better robustness; personalization; improved difficult slices; reusable representation; scaling benefit.

Do not justify it with "average metric improved 0.5%."

### Periodicity

Wearable behavior often contains circadian, daily, and weekly structure.

Possible features: hour-of-day statistics; day-of-week statistics; Fourier / spectral features; seasonal averages; periodic embeddings.

Why can explicit periodic features work well? They inject known structure directly and may be robust under sparse observations.

"Why might LightGBM + periodic features beat a Transformer?"

Themes: correct inductive bias; lower sample complexity; less overfitting; explicit handling of sparse data; easier optimization; the deep model has to rediscover known periodic structure.

Do not name the paper.

### Transformer 0.91 -> 0.92 over LightGBM but dies under missingness

Reason from: deployment missingness; operating point; calibration; subgroup behavior; compute; maintenance cost.

Likely: the robust baseline may be preferable.

Could consider: hybrid; fallback; ensemble; missingness-specific routing.

### AUROC

AUROC = Area Under the ROC curve (ROC = receiver operating characteristic). ROC: sweep the score threshold; x = FPR = FP/(FP+TN), y = TPR = TP/(TP+FN). AUROC is the area under that curve.

Equation worth saying: AUROC = P(s+ > s-) + 0.5 P(tie). Same number as the Mann-Whitney rank statistic: average over every positive-negative pair of 1 if the positive scores higher, 0.5 if tied. Integral form is just area under TPR vs FPR — do not open with that.

Intuitively: pick one random positive and one random negative. AUROC is the chance the model scores the positive higher. 0.5 = coin flip ranking; 1.0 = every positive above every negative. It is threshold-free ranking quality, not "accuracy at the cutoff we would ship." It ignores calibration (0.9 vs 0.2 can rank the same as 0.51 vs 0.49) and ignores the FP/FN costs at one operating point. So 0.91 -> 0.92 means the deep model is slightly better at ordering people, not that it is the right deploy model — especially if the ranking collapses under missingness or the threshold you actually use does not move.

If they say "AUC," ask or assume AUROC — PR-AUC is a different curve.

### When should you kill the deep model?

Examples:

- no meaningful gain over simple baseline
- gain disappears on important slices
- poor missingness robustness
- calibration worse
- compute / latency too high
- unstable deployment behavior
- performance depends on a shortcut
- label-efficiency benefit absent

Your TR mix kill is the story: average up, slice down -> killed. Same instinct.

---

## H5 — Longitudinal and personalization

### Timescales

Seconds: waveform morphology.

Minutes: activity bouts.

Hours: sleep / activity sessions.

Days: behavioral state.

Weeks / months: trend.

Years: personal baseline / health evolution.

Do not tokenize every raw sample across one year.

Think: local encoding -> compression -> hierarchical aggregation -> longitudinal model.

### Personalization

Health signals vary substantially across individuals.

Useful decomposition:

observation = population component + personal baseline + deviation from personal baseline + noise

Often "70 bpm" may be less informative than "+15 bpm above this person's baseline."

Possible approaches: personal normalization; participant embedding; few-shot adaptation; personalized calibration; state memory; hierarchical models.

Beware participant memorization.

### Cold start

If using personalization: what happens for a new user?

Need a strategy: population model initially; gradually adapt; confidence increases with history; personalized thresholds after sufficient baseline.

Always distinguish existing-user prediction vs new-user generalization.

### Would you personalize?

Possibly.

Use: population model -> personal baseline -> personal calibration / adaptation.

But define: cold start; minimum history; new-user evaluation; leakage risk; robustness.

---

## H6 — Splits and leakage

Very high priority. Random window split can be wrong. Choose based on deployment.

### Participant-disjoint split

Train users != test users. Tests new-user generalization.

### Temporal split

Past -> train, future -> test. Tests future prediction for existing users.

### Both

Depends on product use case. Always ask: what generalization claim am I making?

How would you split a longitudinal wearable dataset? Start from the deployment goal. New-user deployment: participant-disjoint. Future prediction: temporal. Need both: participant + temporal constraints. Also prevent overlapping window leakage.

### Window overlap leakage

Example: train 00:00-00:30 and test 00:10-00:40 share 20 minutes. This can inflate performance dramatically.

Safer: split before creating overlapping windows, or enforce temporal separation.

### Other leakage sources

Check: future information in preprocessing; normalization using test / future statistics; participant ID; device / site ID; label-derived features; overlapping windows; downstream test contamination; repeated measurements from the same event.

### How do you know it learned physiology rather than user ID?

Test: participant-disjoint holdout; participant-ID probe; normalization; within-person vs cross-person tests; device holdout; temporal generalization.

---

## H7 — Labels, metrics, prevalence, calibration, operating point

### Health label quality

Labels may come from: clinician annotation; diagnosis; self-report; questionnaire; device-derived proxy; EHR; lab result; inferred label.

Ask: what exactly does this label represent?

Problems: noise; delay; subjective self-report; imperfect proxy; adjudication inconsistencies.

More model capacity can fit label noise better.

Potential actions: repeated labels; confidence weighting; adjudicated subset; robust loss; sensitivity analysis.

### Self-report as the target

Concerns: subjective labels; inconsistent reporting; temporal mismatch; missing labels; selection bias.

Possible actions: repeated measures; robust target definition; high-quality validation subset; label-confidence modeling; report uncertainty.

### Health metrics

Do not default to accuracy.

Sensitivity = TP / (TP + FN).

Specificity = TN / (TN + FP).

PPV / precision = TP / (TP + FP).

NPV = TN / (TN + FN).

Also: AUROC; AUPRC; calibration.

### Prevalence

Very important. PPV depends on prevalence.

Rare outcome: even good sensitivity / specificity can yield many false positives.

"AUROC = 0.95. Ready to ship?"

No. I need deployment prevalence, operating threshold, sensitivity, specificity, PPV/NPV, calibration, subgroup performance, and the cost of FP/FN.

### AUPRC vs AUROC

For rare outcomes, AUPRC can be more informative because it focuses on positive-class precision / recall behavior.

Do not say AUROC is useless. Say: it can look strong even when positive predictive value is poor under severe imbalance.

### Calibration

Discrimination: can the model rank high-risk above low-risk?

Calibration: does predicted probability correspond to real frequency?

If p = 0.8, then approximately 80% of similar predictions should be positive under good calibration.

Possible tools: reliability diagram; calibration error; temperature scaling.

Health risk estimates often need calibration, not only ranking.

### Operating point

Predict positive if score > tau.

Changing tau trades sensitivity vs specificity.

Correct tau depends on downstream action.

Low-cost passive suggestion: false positives may be tolerable.

High-stakes / intrusive alert: false positive burden may be unacceptable.

Strong question: which model is best at the operating region that matters? Not: which has the best global AUC.

### FP / FN cost

Always connect metric choice to consequence. What happens downstream when the model is wrong?

FN: missed condition / missed opportunity.

FP: unnecessary concern; alert fatigue; loss of trust; unnecessary follow-up.

Applied judgment means selecting metrics from consequences.

---

## H8 — Shift, shortcuts, does it use the sensor

### Distribution shift

Possible shifts: new device generation; firmware; sensor placement; geography; season; demographics; behavior; adherence; prevalence; missingness; clinical vs consumer population.

You cannot assume the test distribution is permanent.

### Device shift

"New watch generation causes performance drop."

Investigate: signal distribution; calibration; sampling rate; sensor noise; preprocessing; firmware; derived features; subgroup effects.

Possible actions: recalibration; domain adaptation; fine-tuning; representation alignment; new-device holdout during development.

New hardware generation breaks performance — walk: signal distribution -> preprocessing -> representation -> calibration -> task performance. Compare device-specific slices. Then recalibration, fine-tuning, domain adaptation, retraining, or a compatibility layer.

### Shortcut learning

The model may exploit participant identity, device type, site, missingness, or metadata instead of physiology.

Test using: participant holdout; new-device holdout; metadata ablation; modality shuffle; temporal shift; participant-ID probe.

### Does the model use the sensor?

Behavioral interventions:

1. remove modality
2. zero modality
3. shuffle modality between examples
4. time-shift modality

If performance barely changes, the model may be ignoring that signal.

This is stronger evidence than attention visualization.

---

## H9 — Fusion only if he pulls architecture (Yujie can leak)

If the interview shifts toward architecture, know three levels.

### Early / token fusion

Project modality tokens -> concat -> shared Transformer.

Pros: rich interactions; simple conceptually.

Cons: sequence explosion; quadratic attention cost.

### Cross-attention

Text / query stream attends to sensor stream.

Pros: modality separation; controllable fusion; useful for a long secondary stream.

Cons: extra architecture; modality may be ignored.

### Late fusion

Separate predictors / representations -> combine later.

Pros: modular; robust; easier missing-modality handling.

Cons: weaker early interactions.

Encoder bakeoff on IMU/PPG: same gate, no matplotlib on PPG. He coauthored native TS-LLM — Yujie's hour can leak here.

---

## Answer spine (almost every prompt)

1. Define deployment: who, when, what action.
2. Define data: modalities, temporal scales, labels, missingness.
3. Define baseline: what is the strongest simple model?
4. Choose representation: raw, aggregate, pretrained, hierarchical.
5. Choose training: supervised, SSL, distillation, multimodal.
6. Design split: participant / temporal / device.
7. Choose metrics from product consequences.
8. Stress test: missingness / shift / sparse users.
9. Check mechanism: ablate / shuffle / probe.
10. Scale only if justified.
11. State kill criteria.

If he is in applied judgment mode, lead: deployment -> metrics -> data quality -> missingness -> robustness -> baseline -> model.

If he is in representation / FM mode, lead: signal physics -> temporal scale -> representation -> SSL objective -> transfer -> missingness -> evaluation.

If unclear: start with the task and data, then let him pull you toward architecture or product judgment.

---

## Four stories (90s each, IC)

Story A — representation bakeoff: initial hypothesis -> compare encodings -> one fails -> kill / redirect -> lesson. Dual views: one encoding loses information — not "I reprint charts."

Story B — irregular / messy data: observation process, missingness, evaluation, robustness. ImagenFew / Bosch noisy data changed the generative model, not a Watch ship.

Story C — simple baseline challenge: a time when a simple baseline changed your interpretation. TR mix: average up, slice down -> killed.

Story D — applied decision: best average metric != best practical choice. Same kill.

### Scientific rigor follow-ups

Even if mapped to health judgment, expect scientific follow-ups.

Be ready for: strongest alternative explanation; what experiment falsifies your hypothesis; why this baseline; how many seeds; confidence intervals; what happens if your main ablation reverses; what is the simplest explanation of the gain; is it more parameters or a better representation.

### Strong ablations

For a multimodal / wearable system: remove modality; shuffle modality; random encoder; frozen encoder; simple handcrafted features; matched parameter baseline; matched compute baseline; no personalization; no missingness features; shorter history.

Use ablations to identify mechanism.

---

## Predicted / Haraldur-style (speak these)

1. Predict X from six months of wearable data — start (H1).
2. You have 100x more unlabeled IMU than labeled outcomes (H2).
3. Contrastive augs for IMU — what is invariant (H2).
4. PPG exists for 20%, IMU for 95% — teacher / student (H2).
5. Missingness after a Watch OS update (H3).
6. Most users don't wear continuously (H3).
7. Transformer +0.01 AUC, dies under missingness — which model (H4).
8. Why might periodic features outperform deep learning (H4).
9. When would you not train an FM / when do you kill the deep model (H4).
10. Population vs personalized; cold start; would you personalize (H5).
11. How would you split a longitudinal wearable dataset (H6).
12. How do you know it learned physiology rather than user ID (H6).
13. AUROC 0.95 — ship? (H7).
14. Screening nudge vs intrusive alert — calibration and tau (H7).
15. Self-report is the target (H7).
16. New hardware generation breaks performance (H8).
17. Benches aren't Watch data — transfer: longitudinal, missing days, multi-stream; not UCR plots.
18. Encoder bakeoff IMU/PPG — same gate; no PPG plots (H9).

---

## Traps

Don't open with Transformer + multimodal LLM.

Don't name RelCon / his papers / Watch hypertension posts.

Don't assume DL wins under missingness shift.

Don't ship on AUROC.

Don't drop incomplete rows or encode missing as zero.

Don't resample every stream onto 100 Hz.

Don't claim you shipped a Watch feature. Bosch irregular -> model change, not a product.

Don't recite 1B segments / 2.5B hours.

---

## Mock (35 min) — last Wednesday slot

Play shipped-product scientist. You have not shipped.

0-8: six months of wearable data, predict X — H1 open, then baseline ladder.

8-20: either 100x unlabeled (H2) or missingness shift / sparse wear (H3).

20-30: AUROC 0.95 or +0.01 deep vs GBDT under missingness (H7 / H4).

30-35: your Q — how they eval robustness (not "did you write RelCon").

Interviewer follow-ups to expect: why; what is the deployment assumption; what is your baseline; what could leak; what happens under missingness; how do you know the model uses the sensor; what metric matters; how would this fail on a new device; when would you kill it.

---

## Full-day Haraldur-only (if Sat/Sun has extra)

Block 1 (75): health evaluation — sensitivity, specificity, PPV/NPV, AUROC, AUPRC, prevalence, calibration, threshold. Practice: AUROC 0.95 — ship or not.

Block 2 (75): missingness + shift — IMU-only, HR+sleep, no PPG, sparse wear, new device. For each: architecture + training + evaluation.

Block 3 (60): wearable representation / SSL — contrastive, augs, masked modeling, cross-modal distill, linear probes, label efficiency.

Block 4 (60): longitudinal + personalization — one hour, one day, one year, new user, established user.

Block 5 (45): simple baseline challenge — for each problem name: simplest credible baseline; stronger tree/statistical model; deep model; what gain would justify complexity.

Block 6 (45): leakage + rigor — participant split, temporal split, overlapping windows, device shortcut, future leakage, self-report noise.

Block 7 (90): mock above with why / deploy / baseline / leak / missingness / uses-the-sensor / metric / new device / kill.

### Two-day version

Day 1 morning: health metrics + calibration + prevalence. Midday: missingness + deployment shift. Afternoon: longitudinal + personalization. Evening: 45-min mock.

Day 2 morning: SSL + sensor representation. Midday: simple baselines + FM evaluation. Afternoon: leakage + robustness + scientific ablations. Evening: 45-min mock + repair weakest topics.
