# On-site — Haraldur Hallgrímsson (Wed 3:05 PDT)

Track: health / applied ML / wearable TS. Conf: very high. Most Apple-Health-specific Wednesday hour.

Who (private): Senior Applied RS, Health AI, Seattle. RelCon, TS-LLM, periodicity. Public: sensor FMs to Watch hypertension / AirPods calories (modeling and infra). Hub: 2026-08-27_onsite-prep.md

Cultural signal (do not recap papers): this group will keep periodic features + GBDT when they beat a deep TS model under missingness shift. SSL motion FMs exist too (~3.9M encoder, 1B segments — not 1B params).

Do not assume deep learning wins.

Do not name RelCon / periodicity paper / Workout Buddy / his LinkedIn posts. Do not say you shipped a Watch feature. Token schemes for three-year history live on the Yujie sheet — if he stays on labels / missingness / ship, stay here.

Posture in one line: I want to know not only whether the sophisticated model wins, but what it learned, under which data assumptions, and whether that advantage survives the distribution we actually deploy on.

---

## Saturday Block B — how to use this file

He might run Health Domain & Applied ML Judgment, or wearable representation / SSL / missingness. Prep both. Do not overfit one mapping.

Chain: wearable data -> representation -> training objective -> downstream model -> evaluation -> deployment shift -> product decision.

Weight (if you have a full day): ~30% health metrics + applied judgment; ~25% missingness + shift; ~20% wearable SSL / representation; ~15% longitudinal + personalization; ~10% fusion / LLM details.

Today (Sat, shared with Yujie, ~4h total): do H1, H3, H4, H7, then Mock H. Skip H9 unless a mock fails. Abstracts only — RelCon, Periodicity, Beyond Sensor Data — do not name-drop.

If unclear how he opens: start with task and data; let him pull architecture or product.

---

## Open (30s)

First I'd define the deployment setting — target, who acts, when the prediction is made, what history exists then, missingness, operating point, cost of FP vs FN. I'd put a strong statistical / tree / classical TS baseline on the table before I decide whether representation learning buys anything.

Then bakeoff. Not: Transformer + multimodal LLM.

---

## H1 — Deployment, then the data regime

Before a model: what is the target; who uses it; at what time; what data exist at that moment; what horizon; what action; FP vs FN cost; screening vs monitoring vs recommendation vs intervention.

"Before choosing the model, I'd define the deployment setting because the target, available history, acceptable errors, and eval protocol all depend on how the prediction will be used."

Modalities differ in rate, noise, missingness, power, semantics, relevant horizon:

- IMU: dense, high-Hz, motion.
- PPG: waveform physiology, quality-sensitive.
- HR / HRV: lower-rate derived.
- Sleep / workouts / steps / mobility: minute to day.
- Behavioral summaries: hour / day / week.
- Text, self-report, clinical labels.

Core question (same as Yujie): what temporal scale does the task require? Sleep next night != 5-year risk != 10 s gait.

Three families (do not force one across all scales):

Raw / local: signal -> patch/window -> encoder -> latent. Keeps fine detail; expensive, noisy, long T, data-hungry.

Aggregate / behavioral: daily steps, resting HR, sleep duration, periodic features, rolling stats. Compact, often aligned with longitudinal outcomes, robust, cheap. Loses waveform; depends on what you engineered.

Hierarchical: raw -> local encoder -> minute/hour latent -> day latent -> longitudinal model. Do not dump 100 Hz IMU for a year into one Transformer. 100 Hz is 360k samples/hour — not one LLM token per sample. Compress: patch / conv / local encoder -> few latents -> higher model. Tradeoff: compression vs information loss.

For every encoding ask: preserved; discarded; token/compute cost; inductive bias; temporal scale; missingness robustness; task transfer.

When to use an LLM: not the default for low-level sensing. Split perception / representation / longitudinal reasoning / language interface. Native encoder for 1-2. LLM if you need semantic context, instructions, summaries, heterogeneous text. "I would not feed raw high-Hz sensing into an LLM unless evidence showed it helped."

Async clocks: IMU 100 Hz, HR 1 Hz, sleep every few minutes — do not resample onto the fastest clock. Encode each at native/local rate, compress, align on a latent timeline, then fuse.

Irregular: missing != zero. (x, t) or (x, delta_t); time embeddings, mask, event models. Don't open with neural ODEs unless he goes there.

---

## H2 — SSL, contrastive, distillation

Typical health: unlabeled wearable >> labeled outcomes.

large unlabeled corpus -> SSL encoder -> frozen probe and/or light FT -> downstream.

Objectives you might name: contrastive, masked reconstruct, future predict, temporal consistency, cross-modal align, distill. The question is not "which paper." It is: what invariances and structure should the objective encode?

Contrastive (InfoNCE sketch): pull z and z+ together, push z against other z_j, temperature tau. The science is the **positive**. Wearable: is watch rotation an invariance? Small jitter OK? Crop still the same bout? Time-warp destroy cadence? Different intensity still "same"? Does the aug preserve physiology? "An SSL augmentation is a modeling assumption about invariance." Do not copy ImageNet crops.

Binary same/not-same can be too crude (nearly equivalent vs related vs unrelated). Prefer similarity grounded in signal semantics or downstream invariances — do not name RelCon.

Cross-modal distill: rich teacher at train (e.g. PPG), cheap student at deploy (e.g. IMU), paired sync data. Ask: what is actually predictable across modalities (physiology vs activity)? Missing teacher? Participant/device shift?

Eval an FM: many tasks; low-label curves (1% / 5% / 10% / 100%); linear probe and FT; unseen participants; device; missingness; timescale transfer. Linear probe asks: is the information already in the frozen z? If all gains need full FT, the representation is less universal than claimed. Negative transfer: report task slices, not only the mean.

100x unlabeled spine: SSL with domain invariances; frozen probe; label-efficiency curve; light FT; participant holdout; device/missingness stress; **same-label-budget simple baseline**. If the FM loses at realistic labels, keep the simple model.

---

## H3 — Missingness (architecture and statistics)

Do not drop incomplete rows (IMU-only, HR+sleep, PPG+IMU, all).

Architecture: variable set (only present modality tokens) or fixed slots (learned missing token, presence mask, modality ID). Do not encode missing as zero. Distinguish measurement is zero from measurement is unavailable.

Stats — three questions:

1. Can the model technically run with holes?
2. Is missingness informative? P(M | X, Y) often != P(M): not worn, battery, illness, adherence, contact, behavior.
3. Will missingness **shift**? P_train(M) != P_deploy(M) — firmware, battery, adherence, illness. A model that used availability as a shortcut dies.

Informative missingness is a signal **and** a shortcut risk. Eval is not "can it impute." It is: does performance hold when the missingness **process** changes.

Stress tests (not only naturally missing test data): drop random channels; drop a high-value channel; longer holes; lower wear time; change which modalities exist; sparse-user slice. Plot performance vs missingness severity. Compare **curves**, not only the average.

"Most users don't wear continuously": first plot performance vs wear time. Then natural missingness, explicit availability, dropout in train, robust aggregates, uncertainty, sparse-user subgroup, and whether sparse use **correlates with the label**.

---

## H4 — Baselines, periodicity, kill the deep model

Do not assume deep > simple.

Ladder: population mean / heuristic -> rolling stats -> periodic features -> linear / logistic -> LightGBM / XGBoost -> classical TS -> pretrained sensor encoder -> FM.

What earns the complex model: label efficiency, transfer, robustness, personalization, **hard slices**, reusable z, scaling. Not "+0.5% average."

Periodicity (method, do not name the paper): circadian / daily / weekly. Hour-of-day, day-of-week, Fourier, seasonal averages, periodic embeddings. Why GBDT + periodic features can beat a Transformer: right inductive bias, lower sample complexity, less overfit, explicit structure under sparse observations; the deep model has to rediscover the clock.

Transformer 0.91 -> 0.92 AUROC over LightGBM but **dies under missingness**: look at deploy missingness, operating point, calibration, subgroups, compute, maintenance. Often keep the robust baseline; or hybrid / fallback / route on missingness.

Kill the deep model when: no real gain vs simple; gain vanishes on the slices that matter; missingness brittle; worse calibration; too much compute/latency; unstable; shortcut; no label-efficiency win.

Your TR mix kill is the story: average up, slice down -> killed. Same instinct.

---

## H5 — Longitudinal and personalization

Seconds: waveform. Minutes: bouts. Hours: sleep/sessions. Days: behavioral state. Weeks/months: trend. Years: personal baseline.

Local encode -> compress -> hierarchical aggregate -> longitudinal model.

Observation ~ population + personal baseline + deviation + noise. "70 bpm" may mean less than "+15 vs this person."

Levers: personal norm, participant embedding, few-shot adapt, calibration, state memory, hierarchical models. Beware memorizing the person.

Cold start: population first; adapt as days accrue; confidence with history; personalized thresholds only after a baseline. Always split **new user** vs **known user**.

Would you personalize? Possibly: population -> personal baseline -> adapt. Define min history, new-user eval, leakage, robustness.

---

## H6 — Splits and leakage

Start from the deployment claim.

Participant-disjoint: new-user generalization.

Temporal (past train, future test): future prediction for people you already saw.

Often you need both. Always say what claim you are making.

Window overlap: train 00:00-00:30 and test 00:10-00:40 share 20 min — performance lies. Split **before** cutting windows, or enforce a gap.

Other leaks: future in preprocess; norm using test/future stats; participant or device or site ID; label-derived features; overlapping windows; eval contamination; repeats of the same event.

How do you know it isn't user ID: participant holdout; ID probe; within- vs cross-person; device holdout; temporal gen; personal norm.

---

## H7 — Labels, metrics, prevalence, calibration, operating point

Ask what the label **is**: clinician, diagnosis, self-report, questionnaire, device proxy, EHR, lab, inferred. Noise, delay, subjectivity, bad proxy, adjudication. Capacity can fit label noise. Levers: repeats, confidence weights, adjudicated subset, robust loss, sensitivity analysis.

Self-report as target: inconsistent, temporal mismatch, missing, selection. Repeated measures, tighter target, high-quality val subset, uncertainty.

Do not default to accuracy.

Sensitivity = TP / (TP+FN). Specificity = TN / (TN+FP). PPV = TP / (TP+FP). NPV = TN / (TN+FN). Also AUROC, AUPRC, calibration.

AUROC 0.95 — ship? No. Need deploy prevalence, threshold, sens/spec, PPV/NPV, calibration, subgroups, FP/FN cost.

PPV depends on prevalence. Rare event + pretty ROC => many false positives.

AUPRC: more honest on the positive class when rare. AUROC is not useless; it can look strong when PPV is poor.

Discrimination: rank high vs low risk. Calibration: p=0.8 means about 80% of similar cases are positive. Reliability diagram, calibration error, temperature scaling. Health risk often needs calibration, not only ranking.

Operating point: score > tau. Tau trades sensitivity vs specificity. Low-cost nudge: FP more OK. Intrusive alert: FP burden may be unacceptable. Best model in the **region that matters**, not best global AUC.

FN: missed condition / missed chance. FP: worry, alert fatigue, lost trust, extra follow-up. Metrics from consequences.

---

## H8 — Shift, shortcuts, does it use the sensor

Shifts: device gen, firmware, placement, geography, season, demographics, behavior, adherence, prevalence, missingness, clinical vs consumer.

New watch, performance drops: signal dist, calibration, sample rate, noise, preprocess, firmware, derived features, subgroups. Then recalibrate, adapt, FT, align z, or hold out new-device **in development**.

Shortcuts: participant, device, site, missingness, metadata — instead of physiology. Tests: participant holdout, new-device holdout, metadata ablation, modality shuffle, temporal shift, ID probe.

Does it use the sensor: remove modality; zero it; shuffle across examples; time-shift. If the number barely moves, it is ignoring that stream. Stronger than attention plots.

---

## H9 — Fusion only if he pulls architecture (Yujie can leak)

Early / token: project, concat, shared Transformer. Rich interactions; T explodes; T^2.

Cross-attn: query stream attends to sensor. Separation, long secondary stream; extra machinery; modality can be ignored.

Late: separate then combine. Modular, missing-modality easier; weaker early interaction.

Encoder bakeoff on IMU/PPG: same gate, no matplotlib on PPG. He coauthored native TS-LLM — Yujie's hour can leak here.

---

## Answer spine (almost every prompt)

1. Deployment: who, when, action.
2. Data: modalities, scales, labels, missingness.
3. Strongest simple baseline.
4. Representation: raw / aggregate / pretrained / hierarchical.
5. Train: supervised / SSL / distill / multimodal.
6. Split: participant / time / device.
7. Metrics from product cost.
8. Stress: missingness / shift / sparse users.
9. Mechanism: ablate / shuffle / probe.
10. Scale only if justified. State kill criteria.

If he is in **applied judgment** mode, lead: deploy -> metrics -> label quality -> missingness -> robustness -> baseline -> model.

If he is in **representation / FM** mode, lead: signal physics -> timescale -> representation -> SSL -> transfer -> missingness -> eval.

---

## Four stories (90s each, IC)

A. Representation bakeoff: hypothesis -> encodings -> one fails -> kill / redirect. Dual views: one encoding loses information — not "I reprint charts."

B. Irregular / messy: observation process, missingness, eval, robustness. ImagenFew / Bosch noisy data changed the **generative** model, not a Watch ship.

C. Simple baseline changed the interpretation. TR mix: average up, slice down -> killed.

D. Best average != best practical choice. Same kill.

Rigor if he goes there: strongest alternative; falsifying experiment; why this baseline; seeds / CIs; if the main ablation flips; simplest explanation of the gain; more params vs better z.

Ablations: drop modality; shuffle; random encoder; frozen encoder; handcrafted features; matched params/compute; no personalization; no missingness features; shorter history.

---

## Predicted / Haraldur-style (speak these)

1. Predict X from six months of wearable data — start (H1).
2. Population vs personalized; cold start (H5).
3. 100x unlabeled — SSL then probe then same-budget baseline (H2).
4. Contrastive augs for IMU (H2).
5. Missingness after a Watch OS update (H3).
6. When would you not train an FM (H4).
7. Participant vs time splits; overlap leak (H6).
8. Screening nudge vs intrusive alert — calibration and tau (H7).
9. Benches aren't Watch data — transfer: longitudinal, missing days, multi-stream; not UCR plots.
10. Encoder bakeoff IMU/PPG — same gate; no PPG plots (H9).
11. AUROC 0.95 — ship? (H7).
12. Transformer +0.01 AUC, dies under missingness — which model (H4).
13. Sparse wear (H3).
14. PPG on 20%, IMU on 95% — teacher/student (H2).
15. Self-report target (H7).
16. New hardware gen (H8).
17. Why periodic features can beat DL (H4).
18. When to kill the deep model (H4).
19. Physiology vs user ID (H6).

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

---

## Full-day Haraldur-only (if Sat/Sun has extra)

Block 1 (75): H7 — AUROC 0.95 ship-or-not.

Block 2 (75): H3 — IMU-only, HR+sleep, no PPG, sparse wear, new device; for each: arch + train + eval.

Block 3 (60): H2 — SSL, augs, distill, probes, label curves.

Block 4 (60): H5 — hour / day / year; new vs established user.

Block 5 (45): H4 — for each problem: simple baseline, tree/stats, deep, what gain justifies complexity.

Block 6 (45): H6 — participant, temporal, overlap, device shortcut, future leak, self-report noise.

Block 7 (90): mock above with why / deploy / baseline / leak / missingness / uses-the-sensor / metric / new device / kill.
