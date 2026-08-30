# On-site — Haraldur Hallgrímsson (Wed 3:05 PDT)

Track: health / applied ML / wearable TS. Conf: very high. Most Apple-Health-specific Wednesday hour.

Who (private): Senior Applied RS, Health AI, Seattle. RelCon, TS-LLM, periodicity. Public: sensor FMs to Watch hypertension / AirPods calories (modeling and infra). Hub: 2026-08-27_onsite-prep.md

Cultural signal (do not recap papers): this group will keep periodic features + GBDT when they beat a deep TS model under missingness shift. SSL motion FMs exist too (~3.9M encoder, 1B segments — not 1B params).

Do not assume deep learning wins.

Do not name RelCon / periodicity paper / Workout Buddy / his LinkedIn posts. Do not say you shipped a Watch feature. Token schemes for three-year history live on the Yujie sheet — if he stays on labels / missingness / ship, stay here.

The goal is not to memorize a collection of health-ML facts. The goal is four reusable reasoning skills. Everything else belongs under one of them.

---

## Likely interview space

Prepare for the intersection of:

- Health Domain & Applied ML Judgment
- wearable / sensor representation learning
- time-series and longitudinal modeling
- scientific rigor
- robustness to real-world health data

MODULE 1 — FORMULATE THE RIGHT ML PROBLEM

MODULE 2 — DESIGN THE RIGHT REPRESENTATION

MODULE 3 — DETERMINE WHETHER THE RESULT IS REAL

MODULE 4 — DECIDE WHETHER THE MODEL IS GOOD ENOUGH TO USE

The four mental models:

1. PROBLEM: target -> available information -> deployment setting -> error consequences

2. REPRESENTATION: timescale + information required + availability + computational cost

3. SCIENTIFIC RIGOR: claim -> alternative explanation -> discriminating experiment

4. APPLIED DECISION: benefit - failure risk - operational cost

Senior loop: PROBLEM -> REPRESENTATION -> EVIDENCE -> DECISION

---

## Saturday Block B — how to use this file

Do not grind the old H1–H9 list. Today: Module 1 cases (already started), then Module 2 main case + missingness, then Module 4 ship (0.90 vs 0.92 vs 0.925). Abstracts only — RelCon, Periodicity, Beyond Sensor Data — do not name-drop.

If unclear how he opens: start with the problem (Module 1); let him pull representation or ship.

Open (30s): First I'd define the deployment setting — target, who acts, when the prediction is made, what history exists then, missingness, operating point, cost of FP vs FN. I'd put a strong statistical / tree / classical TS baseline on the table before I decide whether representation learning buys anything. Then bakeoff. Do not jump to Transformer / foundation model / LLM.

---

## Module 1 — Formulate the right ML problem

Core question: Before I build a model, what exactly am I trying to predict, using what information, for whom, and for what purpose?

### Why this matters

Many health-ML failures happen before architecture enters the picture.

A technically excellent model can be meaningless if:

- the target is poorly defined
- future information leaks into the input
- the evaluation population differs from deployment
- the prediction horizon is inappropriate
- the metric does not correspond to the product decision
- the labels are weak proxies for what we actually care about

The goal of this module is to learn to turn an ambiguous health problem into a precise ML problem.

### 1.1 Target definition

Learn to ask: "What exactly is Y?"

Example: "health deterioration" could mean hospitalization within 7 days; a clinically diagnosed event; elevated resting HR; self-reported symptoms; reduced activity; physician intervention. These are completely different targets.

You need to distinguish the TRUE CONSTRUCT (what we actually care about) from the OBSERVED LABEL (what is available in the dataset).

Example: true target = depressive episode; observed label = weekly self-report questionnaire. Then Y_observed != Y_true, and label noise becomes part of the modeling problem.

Learn: labels can be noisy; delayed; subjective; proxies; selected; and label availability itself can be non-random.

Interview habit: when given a vague health target, clarify what generates the label before discussing the model.

### 1.2 Prediction time and horizon

Define t = prediction time.

Then inputs must satisfy: X = information available at or before t.

The target might be: Y = event during [t, t + Delta].

Example: use previous 30 days of wearable data to predict an event during the next 7 days. This immediately defines what data are legal.

Learn to distinguish retrospective classification ("What happened?") from prospective prediction ("What will happen?"). The latter requires strict temporal causality.

Common failure: computing a daily feature using the entire day when prediction was supposed to occur at noon. That creates future leakage.

### 1.3 Deployment population

Ask: "Who must this model work for?"

Possibilities: users already seen during training; completely new users; users with long history; new users with no history; a specific device generation; a broad consumer population; a clinical population.

This determines evaluation design.

If deployment is to NEW USERS: train participants != test participants.

If deployment predicts FUTURE STATE for existing users: train on past, test on future.

If both matter: you may need multiple evaluation protocols.

Key concept: the train/test split should represent the generalization claim.

### 1.4 Available information

Inventory what exists at prediction time.

Example: IMU; PPG; heart rate; sleep; workouts; demographics / context; historical measurements; self-report.

For each modality ask: always available? intermittently available? derived or raw? what sampling rate? how much history? available on all devices? available at inference?

Important distinction: TRAINING-TIME INFORMATION vs DEPLOYMENT-TIME INFORMATION.

A modality may be available during training but unavailable or too expensive during deployment. That can motivate distillation or privileged-information training.

IMU vs accelerometer: an accelerometer is one 3-axis linear-acceleration sensor (including gravity unless you subtract it). An IMU is the package — typically accelerometer + gyroscope (6-axis), sometimes + magnetometer (9-axis). In this loop people often say IMU for "the motion stream." If he asks what you encode, say 6-axis IMU unless the data are accel-only. Gyro makes orientation / cadence explicit; accel-only has to infer tilt from gravity.

### 1.5 Error consequences

Do not select metrics before understanding the downstream action.

Ask: "What happens when the model predicts positive?"

Example A: a low-cost wellness recommendation. False positives may be relatively tolerable.

Example B: a warning that strongly alarms the user or triggers medical follow-up. False positives may be very costly.

Example C: screening for something dangerous. False negatives may be particularly costly.

This determines the operating point later. Say FP vs FN, not TP/FP.

### 1.6 Basic health metrics

Know these well enough to reason with them.

Sensitivity / recall: TP / (TP + FN). "Among true positives, how many did I catch?"

Specificity: TN / (TN + FP). "Among true negatives, how many did I leave alone?"

PPV / precision: TP / (TP + FP). "Among people I alerted, how many were actually positive?"

NPV: TN / (TN + FN). "Among people I did not alert, how many were actually negative?"

Also understand AUROC, AUPRC, calibration.

Do not memorize them as vocabulary. Understand which question each answers. Sensitivity and PPV correspond to very different product concerns.

AUROC = Area Under the ROC curve (ROC = receiver operating characteristic). ROC: sweep the score threshold; x = FPR = FP/(FP+TN); y = TPR = TP/(TP+FN). AUROC is the area under that curve.

Equation worth saying: AUROC = P(s+ > s-) + 0.5 P(tie). Same number as the Mann-Whitney rank statistic: average over every positive-negative pair of 1 if the positive scores higher, 0.5 if tied. Integral form is just area under TPR vs FPR — do not open with that.

Intuitively: pick one random positive and one random negative. AUROC is the chance the model scores the positive higher. 0.5 = coin flip ranking; 1.0 = every positive above every negative. It is threshold-free ranking quality, not "accuracy at the cutoff we would ship." It ignores calibration (0.9 vs 0.2 can rank the same as 0.51 vs 0.49) and ignores FP/FN costs at one operating point. If they say "AUC," ask or assume AUROC — PR-AUC is a different curve (precision vs recall). AUPRC is more honest on the positive class when the event is rare. AUROC is not useless; it can look strong when PPV is poor.

### 1.7 Prevalence

High priority. PPV depends on prevalence.

Suppose an event is extremely rare. Even a classifier with apparently excellent sensitivity and specificity may produce many more false positives than true positives.

Therefore AUROC = 0.95 does NOT imply ready for deployment.

Need to know: prevalence; operating threshold; sensitivity; specificity; PPV / NPV; calibration; consequence of errors.

You should be able to reason through a simple numerical example. 10,000 users, prevalence 1% => 100 true cases. Sensitivity 90% => 90 TP and 10 FN. Specificity 90% => 0.10 * 9,900 = 990 FP. PPV = 90 / (90+990) ≈ 8%. Most alerts are wrong even though AUROC could look fine. That is why you do not ship on 0.95.

### 1.8 Calibration

Distinguish DISCRIMINATION (can the model rank high-risk examples above low-risk examples?) from CALIBRATION (do predicted probabilities correspond to actual frequencies?).

If the model says risk = 0.8 for many examples, roughly 80% should experience the event under good calibration.

A model can have excellent AUROC and poor calibration.

Learn conceptually: reliability diagrams; calibration error; temperature scaling / post-hoc recalibration; calibration can shift after deployment.

Health risk estimates often need calibration, not only ranking.

### Module 1 practice

Case A: "Predict whether a health event will occur during the next week using the previous six months of Apple Watch data."

Before mentioning architecture, define: (1) target, (2) label source, (3) prediction time, (4) prediction horizon, (5) available inputs, (6) population, (7) action following prediction, (8) error costs, (9) evaluation split, (10) primary metrics.

Week-level target lock (2026-08-29): start from daily behavioral aggregates + periodic features + GBDT. Not a Transformer, not raw IMU patches. Escalate only if the tree loses on the slices that matter.

Spoken Case A (2026-08-29):

First take: (1) health event next week yes/no; (2) label source = train + test data; (3) prediction time = a week; (4) horizon = a week; (5) inputs = previous six months; (6) population = Apple Watch users; (7) action depends, might trigger healthcare intervention; (8) costs depend, FP or FN might be costly; (9) split so there is no dist shift: current vs unseen data; (10) accuracy, precision, recall, F1.

Miss: restated the prompt. Label source is how Y is generated, not "the dataset." Confused t with Delta. Six months is the window, not the modality inventory. "Watch users" is not a population. "Depends" is not an action or a cost. Split should match the generalization claim, not "avoid shift." Do not open with accuracy on a sparse event.

Lock: I'd lock Y first — say hospitalization in the next 7 days from EHR, not "a health event." Score at a fixed t, using only data available then; horizon is [t, t+7d]. Inventory IMU / HR / sleep / intermittent PPG and wear; PPG may be train-only. Population: consumer Watch, and I need new-user and known-user claims separately. Working action: a follow-up prompt, so FP is costly. Split: participant-disjoint and a temporal holdout, not a random window cut. I would not lead with accuracy — prevalence, PPV at tau, and calibration. Then daily aggregates + GBDT, not a Transformer.

Case B: "Predict today's sleep quality."

Ask: before sleep? during sleep? after waking? self-reported quality or physiological proxy? Notice how the ML problem changes completely.

Case C: "Detect activity from accelerometer."

Notice how different this is from six-month health prediction: local timescale; dense labels potentially available; raw waveform much more relevant; personalization requirements differ.

Pass condition: given an ambiguous health problem, you can spend 1–2 minutes turning it into a precise ML problem before choosing a model.

---

## Module 2 — Design the right representation

Core question: Given the task and available wearable data, what representation preserves the useful information without making the problem unnecessarily difficult?

Mental model: for every representation consider TIMESCALE + INFORMATION REQUIRED + AVAILABILITY + COMPUTATIONAL COST.

Do not begin with "Which Transformer should I use?" Begin with "What information does this task require?"

### 2.1 Multiple temporal scales

Wearable data naturally exist at very different timescales.

Milliseconds / seconds: waveform morphology; PPG; ECG; fine motion.

Seconds / minutes: activity; exercise; gait; acute physiological response. A bout is one contiguous episode — a 12-minute walk, a workout, a sedentary stretch — not a single sample and not the whole day.

Hours: sleep; workouts; daily behavior.

Days / weeks: circadian behavior; lifestyle; longitudinal changes.

Months: personal baseline; long-term trends.

Architecture should respect this hierarchy.

Important insight: a representation appropriate for 5-second activity recognition may be terrible for predicting a health outcome three months later. Sleep next night != 5-year risk != 10 s gait.

### 2.2 Raw signal representation

Example: IMU at 100 Hz.

raw samples -> patch/window -> CNN / Transformer / sensor encoder -> local latent

A patch is tokenize-then-learn. A 1 s patch at 100 Hz is 100 samples -> one latent. The model can still see shape, transients, cadence.

Benefits: preserves fine temporal information; learns features rather than relying on handcrafted statistics; appropriate when waveform details matter.

Costs: enormous sequence length; expensive; noisy; difficult for long histories.

Do NOT feed every raw sample directly into a large language model.

Raw 100 Hz: 100 samples/sec = 360,000 samples/hour. Cannot naively map each sample to one LLM token. Need: raw signal -> patch / conv / local encoder -> compressed latent tokens -> higher-level model. Main tradeoff: compression vs information loss.

When to use an LLM: not the default for low-level sensing. Split perception / representation / longitudinal reasoning / language interface. Native encoder for 1-2. LLM if you need semantic context, instructions, summaries, heterogeneous text. "I would not feed raw high-frequency sensing directly into an LLM unless evidence showed it helped."

### 2.3 Aggregated representation

Examples: daily step count; resting HR; HR variability summaries; sleep duration; workout minutes; daily activity statistics; periodic / circadian features.

A behavioral aggregate is a person-day (or hour/week) summary of what they did, not the waveform of how the sensor moved. Behavioral = activity and routine at human timescales. Physiological / local = the signal itself (PPG pulse shape, 10 s gait, 100 Hz IMU).

Benefits: compact; interpretable; cheap; often aligned with longitudinal outcomes; potentially robust to sparse observations.

Costs: fine signal structure is destroyed; representation reflects prior assumptions.

"Depends on feature engineering" is not only that the reduce changes per signal (sum steps, median or resting HR, not a mean of 100 Hz IMU). You chose the sufficient statistics before the model sees the data: which summaries; which window (calendar day, night only, hour-of-day bins); what already ran upstream (steps and sleep duration are detector outputs; resting HR needs a rest rule); how holes are treated (average only worn minutes, plus wear time — or you bake "not worn" into fake 0 bpm); what you threw away (waveform, a 10 s gait event). If the outcome lives in a statistic you did not compute, LightGBM cannot invent it. Raw / local: the encoder can still discover features from the patch.

Aggregation operators, match the quantity:

- Totals: sum — steps, calories, minutes asleep.
- Levels: mean or median — HR, HRV, cadence. Median if outliers or holes.
- Extremes: min / max — peak HR, longest sedentary bout.
- Variability: std, IQR — irregularity, not the mean.
- Clock / routine: mean by hour-of-day, day-of-week, a few Fourier bins.
- Wear: hours observed, fraction worn. Never treat missing as 0 and then average.

Important question: "Does the downstream target actually require the information that aggregation destroys?" If not, aggregation may be preferable.

Week-level risk: start with daily behavioral aggregates + GBDT. Do not average 100 Hz IMU into one daily number and call it a representation. If the task is local physiology (gait, arrhythmia, a workout bout), patch the raw window.

Classical / conventional TS (the rung after trees, before a pretrained encoder): statistical series models — seasonal naive, ETS / Holt-Winters, SARIMA, STL + residual, maybe Kalman / state-space. Use when the task is the series (next-night sleep, resting-HR trajectory). Skip or treat as weak when the task is a label from messy wear — periodicity + GBDT already ate the clock. Do not open with ARIMA on raw IMU.

### 2.4 Hierarchical representation

This should be your default mental model for long histories.

Example: raw IMU -> seconds-level encoder -> minute representation -> hour representation -> day representation -> longitudinal model.

Similarly: PPG -> local physiological representation -> coarser temporal representation.

Then combine modalities at an appropriate level.

This avoids: raw 100 Hz x six months -> giant sequence.

Local encode -> compress -> hierarchical aggregate -> longitudinal model. Escalate to this only if daily aggregates + a tree lose on the slices that matter. Compression vs information loss is that second step, not the open.

### 2.5 Periodicity

Wearable behavior contains strong known structure: circadian; daily; weekly; seasonal.

Possible representations: hour-of-day statistics; day-of-week statistics; Fourier features; periodic embeddings; historical averages by temporal phase.

Understand WHY explicit periodic representations can beat deep models: strong inductive bias; lower sample complexity; compact long-history representation; robustness under sparse observations; the deep model does not need to rediscover known structure.

Important applied lesson: known structure should be a baseline, not something the neural network gets credit for rediscovering.

Do not name the periodicity paper.

### 2.6 Self-supervised representation learning

Motivation: unlabeled sensor data >> labeled health outcomes.

Use: large unlabeled corpus -> pretrain encoder -> transfer to downstream tasks.

Possible objectives: contrastive learning; masked reconstruction; predictive learning; temporal consistency; cross-modal alignment / distillation.

The interview-level question is: "What structure should the pretraining objective encourage the representation to preserve?"

Not: "What SSL algorithm do you know?"

### 2.7 Contrastive learning

Basic idea: related samples -> nearby embeddings; unrelated samples -> separated embeddings.

InfoNCE-like objective:

L_i = -log [ exp(sim(z_i, z_i+) / tau) / sum_j exp(sim(z_i, z_j) / tau) ]

Do not spend much time memorizing the equation. The hard problem is: "What is a positive pair?"

For images: different crops may preserve semantic object identity.

For wearable signals: the answer is domain dependent.

Potential transformations: orientation; jitter; crop; noise; temporal shift; scaling. Each transformation makes an assumption.

Key sentence: "An SSL augmentation defines an invariance I am asking the model to learn."

Therefore: if cadence matters, aggressive temporal warping may be harmful. If orientation is irrelevant, rotation invariance may help. If orientation itself carries task information, forcing rotation invariance can destroy useful information.

Binary same / not-same can be too crude (nearly equivalent vs related vs unrelated). Prefer similarity grounded in signal semantics or downstream invariances. Do not name RelCon. Do not copy ImageNet crops.

### 2.8 Cross-modal distillation

Suppose: PPG = rich physiological modality, sparse / expensive; IMU = widely available, cheaper.

During training: PPG teacher and IMU student, representation alignment on paired sync data.

At deployment: IMU only.

Question: can knowledge contained in PPG improve the IMU representation?

This is useful when a modality is available during training but not reliably available during deployment.

Need to evaluate whether the student learned physiological information rather than merely correlated activity shortcuts.

Wearable views are not a photo-caption pair. IMU does not substitute for PPG. Alignment only transfers what is actually shared (motion, maybe intensity) — not the physiology the missing sensor owned. Do not call this CLIP in the room.

Also ask: what happens under missing teacher data? Does transfer survive participant / device shift?

PPG on 20%, IMU on 95%: paired cross-modal pretraining; PPG teacher; IMU student; IMU-only SSL on the remaining unpaired mass; deploy IMU if needed; verify transfer on downstream tasks.

### 2.9 Multimodal fusion

Know three broad strategies. Do not claim one is universally best. Choose based on temporal resolution, modality length, data amount, missingness, and task interaction requirements.

A. Token / early fusion: sensor tokens + other tokens -> shared Transformer. Benefit: rich interactions. Cost: sequence length / attention cost (T^2).

B. Cross-attention: one stream attends to another. Benefit: keep streams separate and fuse selectively; useful for a long secondary stream. Cost: additional architecture and possibility of ignoring the modality.

C. Late fusion: separate representations / predictors -> combine later. Benefit: simple, modular, often robust to missing modalities. Cost: less rich interaction.

Encoder bakeoff on IMU/PPG: same eval gate, no matplotlib on PPG. He coauthored native TS-LLM — Yujie's hour can leak here.

### 2.10 Asynchronous modalities

Example: IMU 100 Hz; HR ~1 Hz; sleep minutes; behavioral summary daily.

Do NOT automatically resample everything to 100 Hz.

Better mental model: encode each modality at useful native resolution -> compress -> associate with time -> fuse at an appropriate coarser level.

Why? Upsampling slow signals creates no new information, increases sequence length, and introduces artificial repetition / interpolation.

Irregular sampling: missing observation != zero. Possible representation: (x_i, t_i) or (x_i, delta_t_i) or explicit event times. Approaches: time embeddings; interpolation + mask; event-based models; irregular-aware encoders. Neural ODE / continuous-time only if he goes there.

### 2.11 Missing modalities

Distinguish two levels.

ARCHITECTURAL: can the model process arbitrary subsets? Possible: present tokens only; missing-modality token; explicit availability mask; modular encoders.

STATISTICAL: does absence itself carry information? Often P(M | X, Y) != P(M): not worn, battery, illness, adherence, contact, behavior. And will it shift? P_train(M) != P_deploy(M) — firmware, battery, adherence, illness.

Do not encode missing as ordinary zero unless zero cannot be confused with a legitimate observation and missingness is explicitly represented. Distinguish "measurement is zero" from "measurement is unavailable."

Do not drop incomplete rows. Missingness often tracks the label. Complete-case training is a different population.

Common correct move: keep the example, reduce only over what was observed, and tell the model what was missing.

Sequence path: pack present tokens (like packing vs pad-to-max). Fixed slots (learned [MISS], same length every row) are the pad-to-max analogue — simple, but the dummy can become a shortcut.

Your lock: pack present modalities with IDs, not pad missing streams to a fixed slot. Add a small availability / wear-time vector so absence is explicit but not a fake waveform. Train with modality dropout so any subset works. Do not treat another sensor as a substitute view of the missing one.

Availability tags ENABLE the shortcut; they do not alleviate it. You add them because absence can be a real signal. You fight the shortcut with modality dropout in train and eval under a different missingness process (drop PPG, lower wear, OS-like pattern). If the number dies when you hide PPG availability, you learned "PPG missing," not physiology.

Aggregate / GBDT path: compute each stat only on worn samples (mean HR over minutes that exist). Add wear / availability features. LightGBM can split on NaN. This is why periodic + trees often survive missingness: a daily mean over 8 worn hours still exists; a Transformer that wanted a full grid does not.

Eval is not "can it impute." It is: does performance hold when the missingness process changes. Stress: drop random channels; drop a high-value channel; longer holes; lower wear; change which modalities exist; sparse-user slice. Plot performance vs missingness severity. Compare curves, not only the average.

"Most users don't wear continuously": first plot performance vs wear time. Then natural missingness, explicit availability, dropout in train, robust aggregates, uncertainty, sparse-user subgroup, and whether sparse use correlates with the label.

### Module 2 practice

Main case: You have IMU at 100 Hz; intermittent PPG; heart rate; sleep; workouts; 12 months of history. Design a representation for predicting a health outcome one week ahead.

Work through: (1) relevant temporal scales, (2) local encoders, (3) compression, (4) longitudinal representation, (5) fusion, (6) missing modalities, (7) simple alternative.

Then change ONE assumption at a time.

Change A: target becomes 5-second activity recognition. How does representation change?

Change B: PPG disappears for 80% of users. What changes?

Change C: history increases from one month to two years. What changes?

Change D: you only have 5,000 labels but millions of unlabeled sensor hours. What changes?

Change E: daily aggregate features perform almost as well as the deep model. What experiment do you run next?

Pass condition: given a wearable problem, you can derive the representation from the task's temporal and informational requirements rather than starting from your favorite architecture.

---

## Module 3 — Determine whether the result is real

Core question: A model improved a benchmark. Why should I believe the claimed explanation?

Mental model: CLAIM -> STRONGEST ALTERNATIVE EXPLANATION -> CHEAPEST DISCRIMINATING EXPERIMENT.

This is the central scientific-rigor framework.

Example claim: "Multimodal fusion improves health prediction."

Alternative explanations: extra parameters; participant leakage; modality correlates with device type; additional modality encodes missingness; preprocessing differs; one easy subgroup drives the average gain.

Each explanation implies a different experiment.

### 3.1 Participant leakage

Wearable signals contain strong individual signatures.

If windows from participant A occur in both train and test, the model may recognize A rather than learn transferable physiology.

Therefore, for new-user generalization: train participants != test participants.

Do not merely randomly split windows.

How do you know it learned physiology rather than user ID: participant-disjoint holdout; participant-ID probe; personal normalization; within-person vs cross-person tests; device holdout; temporal generalization.

### 3.2 Temporal leakage

For prospective health prediction: features must contain only information available before prediction time.

Watch for: centered moving averages; normalization using future values; features computed over the entire day; interpolation using future observations; labels indirectly entering preprocessing.

### 3.3 Overlapping windows

Example: train window 00:00–00:30; test window 00:10–00:40. Twenty minutes are identical. Performance may be severely inflated.

Better: split participants / time first, THEN construct windows, or enforce a gap.

### 3.4 Identity / device shortcuts

The model may learn participant -> label, device generation -> label, site -> label, missingness pattern -> label, instead of health state.

Possible experiments: participant-disjoint test; device holdout; participant-ID probe; remove metadata; stratify by device; balance shortcuts where possible.

### 3.5 Modality utilization

Claim: "PPG improves the model."

Do not rely on attention weights. Intervene.

REMOVE: no PPG.

SHUFFLE: PPG_i -> PPG_j.

TIME SHIFT: PPG(t) -> PPG(t + Delta).

If performance barely changes, the model probably does not depend strongly on the aligned PPG signal.

This is an important multimodal evaluation principle. Stronger than attention plots.

### 3.6 Baseline design

Build a hierarchy.

1. mean / heuristic
2. handcrafted statistics
3. periodic features
4. logistic regression
5. LightGBM
6. conventional temporal model
7. pretrained representation
8. foundation model

A strong baseline should capture obvious known structure.

Question: "Does the complex model learn something genuinely new, or merely rediscover a feature that could have been explicitly represented?"

What earns the complex model: label efficiency; transfer; robustness; personalization; hard slices; reusable z; scaling. Not "+0.5% average."

Your TR mix kill is the story: average up, slice down -> killed. Same instinct.

### 3.7 Matched comparisons

If model A beats model B, ask what changed. Possibilities: architecture; parameter count; data amount; augmentation; optimization; training compute; pretraining corpus.

Try to isolate causal factors.

Example: if a pretrained model wins, compare against same architecture random initialization; supervised-only training; frozen pretrained encoder; fine-tuned pretrained encoder.

This distinguishes architecture benefit from pretraining benefit.

### 3.8 Linear probes

For a pretrained representation: freeze encoder -> train a simple linear head.

Question: "Is the information already present in the representation?"

Then compare linear probe vs fine-tuning.

If gains appear only after complete fine-tuning, the pretrained representation may be less generally useful than claimed.

### 3.9 Label efficiency

Foundation representations should often help especially when labels are scarce.

Evaluate 1% / 5% / 10% / 25% / 100% labels. Plot performance vs labeled-data amount. This can be more informative than one full-data result.

100x unlabeled spine: SSL with domain invariances; frozen probe; label-efficiency curve; light FT; participant holdout; device / missingness stress; same-label-budget simple baseline. If the FM loses at realistic labels, keep the simple model.

### 3.10 Robustness

Do not evaluate only IID average performance.

Stress: missing modalities; reduced wear time; new participants; new device; temporal shift; different seasons; different history lengths.

You want performance(condition), not merely mean performance.

### 3.11 Uncertainty in the experiment

Know enough to discuss: multiple random seeds; confidence intervals; bootstrap where appropriate; paired comparisons; subgroup sample sizes.

You do not need a statistics lecture. But avoid treating 0.842 vs 0.847 as automatically meaningful.

Ask: variance? confidence interval? repeated runs? paired evaluation?

### 3.12 Ablations should test hypotheses

Weak ablation: "Remove layer X because reviewers expect an ablation."

Strong ablation: hypothesis — long history improves prediction because it captures personal baseline. Experiment: compare 1 day / 1 week / 1 month / 3 months and examine which users / tasks benefit.

Every important design choice should correspond to a scientific hypothesis that can be tested.

Other strong wearable ablations: remove modality; shuffle modality; random encoder; frozen encoder; simple handcrafted features; matched parameter baseline; matched compute baseline; no personalization; no missingness features; shorter history.

Rigor follow-ups he can ask even in a health-judgment hour: strongest alternative explanation; what experiment falsifies your hypothesis; why this baseline; how many seeds; CIs; what if the main ablation reverses; simplest explanation of the gain; more parameters vs better representation.

### Module 3 practice

This module should be mostly interactive practice. Claim -> alternative -> experiment.

Claim 1: "Our multimodal model improves AUROC by 4 points." What else could explain it? Design experiments.

Claim 2: "SSL pretraining improves downstream performance." Possible alternatives: architecture difference; more data exposure; optimization advantage. Design controls.

Claim 3: "One year of history is better than one month." Could mean genuine long-term signal; participant identification; more observations; less missingness. Separate them.

Claim 4: "Personalization improves prediction." Could mean useful personal baseline or participant memorization. Design evaluation. Always split new user vs known user. Cold start: population first; adapt as days accrue.

Claim 5: "PPG + IMU beats IMU." Could mean actual physiological information; PPG availability shortcut; parameter increase. Design interventions.

Pass condition: whenever you hear "Method X improved performance," your immediate reaction becomes "What is the strongest alternative explanation, and what experiment would distinguish them?"

---

## Module 4 — Decide whether the model is good enough to use

Core question: Even if the result is scientifically real, is this the model I would actually choose?

Mental model: BENEFIT - FAILURE RISK - OPERATIONAL COST.

This is Applied ML Judgment.

### 4.1 Benefit

Do not ask only: "How much did average AUROC improve?"

Ask: WHERE did the improvement occur?

Possibilities: important high-risk users; rare cases; low-label regime; sparse users; new users; common / easy examples.

A 1-point average gain can be extremely valuable or meaningless depending on where it comes from.

### 4.2 Operating point

Suppose the model produces score s. Prediction: positive if s > tau.

Changing tau changes sensitivity vs specificity. The correct threshold depends on the downstream action.

Therefore compare models at the operating region that matters, not only global AUROC.

Low-cost nudge: FP more OK. Intrusive alert: FP burden may be unacceptable.

### 4.3 Prevalence and PPV

Suppose prevalence = 1%. Even a strong classifier can create many false positives.

Practice the toy: 10,000 users, 100 true cases. Apply sensitivity and specificity and count TP, FP, FN, TN. This makes PPV intuition concrete. You should be able to do this without formulas if necessary. Worked numbers are in 1.7.

### 4.4 Calibration in deployment

If output is used as risk, probability quality matters.

Need to consider: calibration on validation data; calibration by subgroup; recalibration after device / population shift; whether uncertainty should affect downstream action.

Do not confuse ranking with probability estimation.

### 4.5 Missingness robustness

Suppose: deep model normal data 0.92, heavy missingness 0.74. LightGBM normal 0.90, heavy missingness 0.86.

Which wins? Depends on how common heavy missingness is and how important those users are.

This illustrates: average IID performance != deployment utility.

Transformer 0.91 -> 0.92 AUROC over LightGBM but dies under missingness: look at deploy missingness, operating point, calibration, subgroups, compute, maintenance. Often keep the robust baseline; or hybrid / fallback / route on missingness.

### 4.6 Distribution shift

Expect P_train(X,Y) != P_deploy(X,Y).

Potential causes: new Watch generation; firmware; season; geography; changing user behavior; different population; missingness; prevalence; sensor placement; clinical vs consumer.

You need PRE-LAUNCH stress tests and held-out domains, and POST-LAUNCH monitoring and a recalibration / retraining strategy.

New watch, performance drops: signal dist, calibration, sample rate, noise, preprocess, firmware, derived features, subgroups. Then recalibrate, adapt, FT, align z, or hold out new-device in development.

### 4.7 Personalization

Potential benefit: personal baseline may matter more than population baseline.

Example: HR = 75 may be normal for one user and abnormal for another. Observation ~ population + personal baseline + deviation + noise. "70 bpm" may mean less than "+15 vs this person."

Possible approaches: baseline normalization; personalized calibration; user representation; adaptation after sufficient history; few-shot adapt; state memory; hierarchical models. Beware memorizing the person.

Ask: "What happens on day one?" Cold start needs a population-level solution.

Also evaluate separately: established users vs new users. Define min history, leakage, robustness.

### 4.8 Model complexity

Suppose foundation model AUROC 0.92, LightGBM 0.91.

The foundation model may require much more compute; complex infrastructure; difficult debugging; frequent retraining; greater latency; less interpretability.

The question is not "Is 0.92 greater than 0.91?"

It is: "Does the incremental benefit justify the incremental system and failure cost?"

### 4.9 Simple model as fallback

The choice need not be binary.

Possible system: rich-data users -> deep model; sparse-data users -> robust baseline.

Or: deep representation -> simple downstream predictor.

Or: ensemble / fallback when a modality is unavailable.

System design can exploit complementary strengths.

### 4.10 Kill criteria

Before expensive development, define: "What result would make me stop?"

Examples: no meaningful improvement over a strong baseline; improvement disappears on participant holdout; gain disappears under realistic missingness; an important subgroup worsens; calibration unacceptable; compute cost unjustified; model depends on a shortcut; no label-efficiency benefit; representation fails transfer.

This is particularly important for senior-level applied research. A good scientist should be willing to kill their preferred model.

### 4.11 Monitoring after deployment

Deployment is not the end of evaluation.

Potential monitoring: input distribution drift; missingness distribution; device mix; prediction distribution; calibration where delayed labels become available; performance slices; alert rate.

Question: "What would tell you that the model needs recalibration or retraining?"

### Module 4 practice

Main case: you have three models.

Model A — LightGBM: AUROC 0.90; cheap; well calibrated; robust to missingness.

Model B — Deep TS model: AUROC 0.92; moderate compute; performance drops for sparse users.

Model C — Foundation model: AUROC 0.925; expensive; strong low-label transfer; less tested under device shift.

Choose one. Then change ONE assumption at a time.

Change 1: prevalence = 1%.

Change 2: false positives trigger an intrusive user notification.

Change 3: 40% of users have sparse sensor coverage.

Change 4: new Watch hardware launches next year.

Change 5: product expands to a population poorly represented in training.

Change 6: foundation model improves sensitivity substantially at the operating point despite only a small AUROC gain.

Your answer should change when the evidence changes.

Pass condition: you do not automatically choose the highest-performing model. You can explain (1) what evidence matters, (2) what tradeoff matters, (3) what additional experiment would change your decision.

### Spoken integrated case (2026-08-30)

Opening: predict "health deterioration during the next week" from six months of Watch data. Turn it into a precise ML problem, then choose a first model and evaluation.

First take: customer is the Watch user and output is for personal knowledge; label may be user report, so consider an expert-created set; prediction time is the end of six months and horizon is one week; target is event yes/no or deterioration level. Proposed precision, recall, and AUROC based on FP/FN severity, then deferred representation because the answer was long.

Miss: did not make Y, action, or error cost concrete. "Train + test data" is not a label source; six months is a rolling lookback, not the prediction time. Skipped population detail, split, first model, prevalence, PPV, and calibration.

Follow-up assumptions: hospitalization in the next 7 days from linked clinical records; non-emergency clinician-review queue; consumer Watch users including unseen users; HR, sleep, workouts, steps, IMU-derived activity, intermittent PPG, and wear indicators.

First design take: modality-specific native-rate encoders, no resampling, pack available streams with IDs, modality dropout, local patching then hierarchy, target 2K–4K tokens over a two-week lookback. Split each user's six months into consecutive train / val / test and slide two-week input windows. For hospitalization, said FP should be avoided and "lowest precision." Proposed an autoencoder anomaly score as the baseline.

Miss: overbuilt before establishing the strongest simple model and silently changed the six-month lookback to two weeks. Time-only segments leak participant identity and do not test unseen users. "Lowest precision" was inverted. A reconstruction anomaly detector is not the strongest baseline when supervised labels exist.

Lock: For a week-level target, start with daily behavioral aggregates, periodic features, wear indicators, and LightGBM. The hierarchical encoder is the challenger. Use participant-disjoint evaluation for new users with temporal ordering / holdout; do not randomly split overlapping windows.

Decision update: deep hierarchy AUROC 0.92 vs LightGBM 0.90; prevalence 1%; same users leaked across train/test; sparse-wear AUROC deep 0.74 vs LightGBM 0.86; sparse users are 40%; clinician capacity is 100 alerts per 10,000 per week.

First take: participant / future leakage may invalidate the gain, especially for a rare event; use participant splits and sparse-wear training; choose LightGBM; set a threshold around 0.8 because it is above the deep model's 0.74, even if that produces 120 alerts.

Factual correction: 0.74 and 0.86 are AUROCs, not score thresholds. AUROC is threshold-free ranking quality. Rarity does not itself make 0.92 unreal; it makes AUROC insufficient because PPV may be poor. Tau is the score cutoff: alert if s > tau. Choose tau on validation data to satisfy the 100 / 10,000 (top 1%) queue capacity, then report sensitivity, PPV, and calibration there. Precision / PPV = TP / (TP + FP). Recall / sensitivity = TP / (TP + FN).

Evidence lock: identity — participant-disjoint test and participant-ID probe. Wear shortcut — stratify by wear, ablate availability features, and impose controlled missingness shifts. Capacity — parameter / compute-matched control with the same split, data, and head.

Spoken lock: I would choose LightGBM now because 40% of deployment is sparse and it remains at 0.86 there, while the deep model falls to 0.74. Before treating the two-point IID gain as real, I would rerun a participant-disjoint temporal evaluation, probe user identity, ablate wear indicators, and use matched-capacity controls. I would not derive the threshold from AUROC. I would choose it on validation data to respect the 100-alert capacity, then compare sensitivity, PPV, and calibration at that operating point.

---

## How the four modules connect

These are not four independent topics. They form one pipeline.

Module 1 — What problem am I solving? Output: precise target + deployment scenario + evaluation goal.

Then Module 2 — What information and representation does that problem require? Output: representation + architecture / training strategy + simple baseline.

Then Module 3 — Did the proposed approach actually work for the reason I think? Output: credible evidence + ablations + robustness results.

Then Module 4 — Is the demonstrated benefit worth deploying? Output: model / system decision + operating point + failure strategy + monitoring.

---

## Recommended practice schedule

Do not spend the majority of time reading. Target approximately 40% learning, 60% active practice.

Session 1 — Module 1, ~90 minutes. 30 min learning: targets / proxies; temporal prediction setup; participant vs temporal split; health metrics; prevalence; calibration. 45 min cases: future health event; sleep quality; activity recognition. 15 min: explain the framework from memory.

Session 2 — Module 2, ~2 hours. 45 min learning: sensor timescales; raw vs aggregate vs hierarchical; periodicity; missingness; asynchronous modalities. 30 min learning: SSL; contrastive learning; cross-modal distillation. 45 min case: IMU + PPG + HR + sleep + 12 months history. Continuously change assumptions and redesign.

Session 3 — Module 3, ~90 minutes. 30 min learning: participant leakage; temporal leakage; overlapping windows; shortcuts; ablations; linear probes; robustness. 60 min: claim -> alternative explanation -> experiment drills. Do at least 6 claims. This should be almost entirely spoken.

Session 4 — Module 4, ~90 minutes. 30 min learning: operating points; PPV / prevalence; calibration; shift; model complexity; monitoring. 60 min: model-selection scenarios. Change deployment assumptions repeatedly.

Session 5 — integrated mock, 45–60 minutes. One evolving problem, not a quiz.

Opening: "We want to predict a health event one week ahead from wearable data."

Module 1: What exactly are you predicting? What data can you use? How would you split the data?

Module 2: You have IMU, PPG, HR and sleep. How would you represent them? Most PPG is missing. What changes? You have millions of unlabeled hours. What changes?

Module 3: Your model beats LightGBM by 4 points. Convince me the gain is real. The same users were accidentally present in train and test. What do you expect? After fixing it, the gain becomes 1 point. PPG shuffling changes nothing. What does that tell you?

Module 4: Would you ship the deep model? Now the event prevalence is 1%. Now false positives are expensive. Now a new device generation launches. What do you choose?

Play shipped-product scientist. You have not shipped. Your Q at the end: how they eval robustness — not "did you write RelCon."

---

## What to actually memorize

Very little.

Framework 1 — PROBLEM: target -> available information -> deployment -> error consequence.

Framework 2 — REPRESENTATION: timescale + information required + availability + cost.

Framework 3 — SCIENTIFIC RIGOR: claim -> alternative explanation -> discriminating experiment.

Framework 4 — APPLIED JUDGMENT: benefit - failure risk - operational cost.

Everything else should be understood rather than memorized.

---

## Final pass condition

You are ready when Haraldur can give you a health / wearable problem you have never seen before and you do not need to remember a prepared answer.

Instead you naturally reason:

1. What exactly is the problem?
2. What information does solving it require?
3. What representation preserves that information?
4. What is my strongest simple baseline?
5. What result would convince me the complex model actually helps?
6. What alternative explanation could account for that result?
7. What experiment distinguishes the explanations?
8. Does the result survive missingness, new users, time and device shift?
9. Does it perform well at the operating point that matters?
10. Is the improvement worth the additional complexity?

That is the capability this preparation should build.

---

## Spoken (2026-08-29) — Module 1 + 2.11 drill

Logged here so the four-module rewrite does not drop the first takes.

Q1. Six months of Watch data (IMU, HR, sleep, sometimes PPG). Predict next-week risk of a sparse health event. What do you pin down before a representation? Raw patches, daily behavioral aggregates, or a hierarchy?

First take: users, TP/FP cost, error robustness; raw patches on low-freq HR/sleep; agg / hierarchy on high-freq IMU/PPG; info loss vs efficiency.

Miss: skipped who acts / when / what action / screening vs intervention / prevalence. Said TP/FP (use FP/FN). Representation inverted.

Lock: Week-level target. Lock users, action, timing, FP/FN, and prevalence, then start from daily behavioral aggregates + periodic features + GBDT. Not a Transformer, not raw IMU patches. Escalate only if the tree loses on the slices that matter: local encoder on high-Hz -> day latents -> week model. Compression vs information loss is that second step, not the open.

Q2. A third of person-days IMU-only, a third HR+sleep, a third have PPG. How do you train without dropping incomplete days, and how do you keep "PPG was absent" from becoming a shortcut?

First take: do not drop rows; pack observed tokens; tags for missingness; no zeros; availability vector to alleviate shortcuts.

Miss: availability enables the shortcut; it does not alleviate it. Didn't say modality dropout or eval under a changed missingness process. Didn't say the GBDT version (reduce only over worn time + wear hours).

Lock: Keep every day, pack what's worn, never fill zeros, pass a small availability vector because absence can be a real signal. Train with modality dropout. Test with PPG gone / lower wear. If performance rides on the missingness bit, treat that as a shortcut. Same story for trees: aggregate over observed time, plus wear as a feature.

Q3. After a Watch OS update, wear time drops and PPG is missing more often. Train AUROC is still 0.91. What do you check, and what would make you keep the aggregate / GBDT model?

First take: analyze failed negatives; if they are mostly missing-PPG then PPG is crucial; if not, keep the model.

Miss: train AUROC is the trap. Error analysis is not the first check. "Failures are missing-PPG" can mean the model used absence as the predictor.

Lock: Train AUROC is not the deploy number. Eval on the new wear / PPG pattern, plot performance vs wear and vs PPG present/absent, compare tree vs deep on that shift. Keep the aggregate model if the sophisticated one dies there.

---

## Four stories (90s each, IC)

A. Representation bakeoff: hypothesis -> encodings -> one fails -> kill / redirect. Dual views: one encoding loses information — not "I reprint charts."

B. Irregular / messy: observation process, missingness, eval, robustness. ImagenFew / Bosch noisy data changed the generative model, not a Watch ship.

C. Simple baseline changed the interpretation. TR mix: average up, slice down -> killed.

D. Best average != best practical choice. Same kill.

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
