# On-site — second-cycle mock log (Fri 9/4 → Mon 9/7)

Living log for spoken mocks toward **Tue 2026-09-08**. Append here. Do not start a new mock file per person.

**Plan:** [`2026-09-03_four-day-final-plan.md`](2026-09-03_four-day-final-plan.md)  
**Hub:** [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)

**Format each mock:** setup → Q / MY ANSWER / CORRECTION → scorecard → spoken restitch (worst misses only).

Sheets stay sheets. This file is what was *spoken*.

| When | Person | Status | Notes |
|------|--------|--------|-------|
| Fri 9/4 | Chung-Cheng | In-sheet | Q1–Q5 in [`2026-09-04_chung-cheng-advanced.md`](2026-09-04_chung-cheng-advanced.md). Worst: Q3 global batch / steps at fixed tokens. Do not recopy. |
| Fri 9/4 | **Yujie** Blocks 1–5 | **Logged below** | Live Q→A→feedback. Did **not** answer Q5 as asked. |
| Fri 9/4 | **Haraldur** Lesson 1 | **Logged below** | Se/Sp/PPV, prevalence, AUROC, Brier, accuracy trap. Next: participant-disjoint / leakage, not another metric quiz. |
| Sat 9/5 | Vincent constraint-injection | Open | New cardiac case. Do **not** continue first-cycle Blocks 1–9. |
| Sat 9/5 | Yujie Block 14 / 11 | Open | Do **not** redo Blocks 1–5. |
| Sun 9/6 | Jonathan 3-claim + DoF | Open | Speak the 9/1 hill-climbing miss. |
| Sun 9/6 | Mixed interviewer | Open | Infer dimension. |
| Mon 9/7 | Mini-loop | Open | Retrieval only. |

---

## Yujie — Blocks 1–5 (Fri 2026-09-04, ~25 min)

**Slot:** Tue 9/8 1:05 PDT.  
**Sheet:** [`2026-09-05_yujie-advanced.md`](2026-09-05_yujie-advanced.md)  
**Constraint:** skip “patch + xattn.” Press information, tokens, proof.

Covered: patch duration (B1), resample-to-common-Hz (B3), concat vs xattn drowning (B5), audio token tax (B4). **Missed as asked:** 20-channel mixing (B2). Collapse diagnosis was volunteered instead.

### Scorecard

| Q | Block | Verdict | One-line |
|---|-------|---------|----------|
| 1 | Patch 1 s vs 200 ms event | Hit, underspecified | Event not deleted — **inaccessible**. Need samples/token vs event length. |
| 2 | Upsample IMU/HR to 128 Hz | Hit + miss | Multipliers right. **Physical time ≠ token index.** Implicit Hz-from-data is not alignment. |
| 3 | Concat self-attn vs xattn | Hit + miss | Quadratic + Q=text for QA. Compress **PPG**, do not special-case tiny HR. |
| 4 | 16 kHz audio budget | Hit, loose arithmetic | ~29M vs ~230k. Token count ≠ information. Fix **C** per modality. |
| 5 | P×20 mixing / missing / z-score | **Wrong question** | Answered collapse (useful). Still owe channel identity + subject norm. |

**Strongest thread:** tokens ≠ information; native-rate encode; softmax drowning.  
**Weakest:** physical time; answering the question you wished was asked.

---

### Q1 — 128 Hz PPG, ~200 ms event, 1 s non-overlap patches

**Prompt.** Colleague wants 1 s non-overlapping patches. What happens to the event? Pipeline? Experiments?

**MY ANSWER.** 200 ms events disappear. Raw → 200 ms patches → encode → latent resample → LM. Experiments: (1) raw bypass encoder; (2) finer patches.

**CORRECTION.** 1 s patch = **128 samples/token**; 200 ms ≈ **26 samples**. The event is still in the waveform; average/pool makes it **inaccessible**. Overlap / boundary placement matters. Latent resample is not morphology. (2) → **duration curve + short-event slice**, not “finer is better.” (1) confounds: ~**230k tokens / 30 min** raw PPG.

---

### Q2 — Resample PPG / IMU / HR to 128 Hz and concat

**Prompt.** Token counts? What was not added? Alternative? Where does physical time enter?

**MY ANSWER.** IMU ~×2.5, HR ×128; no new information; loses native frequency. Per-modality encoder at original Hz; unequal token counts. Physical time as extra tokens, or implicit because the model gets used to different frequencies.

**CORRECTION.** 128/50 ≈ **2.6×**, **128×** HR. No new measurements — copy/interpolate. Damage is **staircase**, **fake 7.8 ms grid**, token tax — not a Nyquist lecture. Native-rate encode is the default.

**Physical time is the miss.** Token index is not seconds (PPG token 100–200 ms vs sleep token 30 s). Do not add a “time modality” first. Put **timestamp / Δt / time-of-day on the tokens**, then fuse. Implicit “used to Hz” is not a shared clock.

30 min native HR ≈ **1.8k** samples; upsampled HR ≈ **230k**.

---

### Q3 — Native-rate streams; PPG ≫ HR; concat self-attn

**Prompt.** Cost? What goes wrong for HR? Fusion? Q vs KV for language-conditioned health QA?

**MY ANSWER.** Self-attn \((T_\text{text}+T_\text{HR}+T_\text{PPG})^2\). HR can be ignored. Cross-attn: Q=text, KV=concat PPG+HR, cost \(T_\text{text}\cdot(T_\text{HR}+T_\text{PPG})\). Still ignores HR. Remedies: latent fusion only for HR, or concat HR into the prompt.

**CORRECTION.** Quadratic and **Q=text, KV=sensors for QA** are right. Drowning is **softmax mass ∝ count**. Xattn only changes the bill.

Do not leave PPG+HR as one KV bag. Separate xattn per modality, or **fixed latent budget** (Perceiver / Q-Former) **before** text looks. Compress **PPG**; do not special-case the already-tiny stream. Prefix HR is valid **because HR is already small** (late fusion, not a general architecture). Detect ignore: shuffle/drop HR, auxiliary HR loss, attention mass on HR keys. Concat needs **modality IDs**. No-text classification → **learned latent queries**, not a dummy question.

---

### Q4 — Same 30 min + 16 kHz audio

**Prompt.** Raw sample counts vs PPG? Same unbounded native-rate path? Token budget? Fail if compressed too hard or given most of the sequence?

**MY ANSWER.** Audio \(16\text{k}\times1800\sim32\text{M}\); PPG \(\sim256\text{k}\). No — own encoder + resampling. Budget from event duration needed for the task. Too hard → useless/ignored. Too much → ignore other modalities.

**CORRECTION.** Exact: audio **~28.8M**, PPG **~230k**, ratio **~125×**. Own encoder + **bounded tokens** is the lock. Token count is not information: one audio token can cover thousands of samples; one HR token may be one beat. Too-hard compress = event still in waveform, **inaccessible** — detect with a **short-event / keyword / cough slice** under matched **C**. Cap **C per modality** (or learned queries); do not hope softmax is fair.

---

### Q5 — 20 IMU channels; patch = P × 20 (asked) vs collapse (answered)

**Prompt asked.** When is P×C reasonable? Missing channel at test? Channel order shuffled? Instead? Normalization — what does subject z-score erase?

**MY ANSWER (different question).** Three buckets if IMU looks unused:

- **Rep:** token budget / resample too hard. Experiment: raise C / finer hop; measure.
- **Fusion:** IMU xattn ~0 or IMU encoder ∇ ~0. Experiment: gradient norm; xattn residual / attention mass.
- **Eval:** test never needs IMU. Experiment: IMU-necessary questions; with > without.

**CORRECTION on collapse (good leftover).** Split is right. Name a **short IMU event slice**, not “measure results.” Stronger than attn/grad: **time-shuffle IMU** and **drop IMU**. If with≈without, either collapse **or** the benchmark is weakly IMU-dependent.

**CORRECTION on the actual Q5 (unspoken).** P×C mixing only when channels are **same device, same Hz, stable layout** (e.g. 3-axis accel that should interact inside a patch). Missing channel → dim change or garbage in a named slot. Order shuffle → encoder assumed **column identity**. Instead: **channel-id + mask**, or channel-independent then fuse; **modality-specific** across PPG vs IMU. Mixed units → **per-channel** norm. **Subject z-score can erase baseline physiology** (resting HR, typical accel, tremor amplitude). Use only if the task is within-subject change.

**Retry:** not spoken. Still owe a 60s P×C answer before Tuesday.

---

### Spoken restitch (Yujie — 90s)

I encode each modality at its native rate. I do not upsample HR to 128 Hz: that multiplies tokens without new measurements and invents a fake grid. Patch duration has to be shorter than the event I care about, or the event is in the recording and the encoder cannot see it. Token count is not information; audio at 16 kHz is ~125× PPG samples in 30 min, so it gets its own encoder and a **hard token cap**. Fusion for QA is text as Q, sensors as KV — that does not stop PPG drowning HR. I compress the wide stream to a fixed latent budget, or I prefix the tiny one. Positions are not time: I put timestamps on tokens. If a modality looks unused I check representation, fusion, and whether the eval even needs it — shuffle and drop, not only attention maps. I do not flatten 20 IMU channels into one patch unless layout is fixed; missing or shuffled channels break that. Subject-wise z-score can delete the health baseline I wanted.

---

## Haraldur — Lesson 1 metrics (Fri 2026-09-04, ~25 min)

**Slot:** Tue 9/8 3:05 PDT.  
**Sheet:** [`2026-09-01_onsite-haraldur-health-evaluation.md`](2026-09-01_onsite-haraldur-health-evaluation.md) · person: [`2026-08-27_onsite-haraldur.md`](2026-08-27_onsite-haraldur.md)  
**Constraint:** no encoder menu, no RelCon. Press who is sick, who got an alarm, prevalence, ship.

Covered: screening vs clinic, Se/Sp → PPV arithmetic, AUROC vs ship, Brier / reliability, always-negative accuracy. **Not covered:** participant-disjoint split / leakage.

### Scorecard

| Q | Topic | Verdict | One-line |
|---|-------|---------|----------|
| 1 | Watch notify vs clinic anticoagulation | Hit, incomplete | Different problem. Watch still needs PPV / alert rate; **do not copy τ**. |
| 2 | Se/Sp 90/90 at 50% vs 1% | Arithmetic miss | **TP = 0.9 × sick.** A: PPV 90%. B: **≈8.3%**. Name **prevalence**. |
| 3 | AUROC 0.95 on enriched set | Ranking hit, ship soft | **No.** Product slide: PPV@τ, alerts/user-week, eval prevalence — not AUROC+. |
| 4 | Brier / reliability / show \(p\) | Hit | Brier = mean \((p-y)^2\), \(y\in\{0,1\}\). Bin on **predicted** \(p\). Don’t show raw \(p\). |
| 5 | Accuracy 99% at 1% prevalence | Hit | Always-neg baseline. PPV **undefined**, not 0. |

**Strongest:** screening ≠ clinic; Se/Sp ≠ PPV; always-negative accuracy.  
**Weakest:** **0.9 × N_sick** under pressure; **explicit no-ship**; PPV with **zero alarms**.

---

### Q1 — Same model, Watch notify vs clinic anticoagulation

**Prompt.** Rare arrhythmia. Watch: push + 30 s ECG user may skip. Clinic: confirmatory tool that can start anticoagulation discussion. Same ML problem? Which error is expensive? Which metric first? Do not list six metrics.

**MY ANSWER.** Not the same problem: different population (Watch users vs patients) and different outcome (cheap suggestive ECG vs confirmatory). Watch: FN expensive → report sensitivity first. Clinic: FP expensive → report precision.

**CORRECTION.** Different **population, action, and Y** is the lock. Watch is not FN-only: users skip and disable noisy alerts — report **PPV and alerts per user-week** with sensitivity. Clinic: **specificity and PPV**, not precision alone. **Same cutoff is illegal**; consumer Watch is low prevalence, clinic is enriched. Name **prevalence** as the mechanism and **who labels Y**.

---

### Q2 — 90/90 Se/Sp; PPV at 50% vs 1%

**Prompt.** A: 1,000 people, 50% prevalence. B: 10,000 people, 1%. TP, FP, PPV both. What did 90/90 fail to tell?

**MY ANSWER.** A: TP=500, FP=50, PPV=500/550=10/11. B: TP=100, FP=990, PPV=100/1090=10/109. 90/90 does not say how often positives are correct (or how many FPs).

**CORRECTION.** Structure right. **TP = 0.9 × sick**, not the prevalence count. A: TP=**450**, FP=50, PPV=**90%**. B: TP=**90**, FP=990, PPV=90/1080≈**8.3%**. 90/90 is silent on **prevalence**: a 10% FPR at 1% is 990 FPs vs 90 TPs.

---

### Q3 — AUROC 0.95 on enriched test; Watch PPV ≈8%; ship?

**Prompt.** Colleague: ranking is excellent, ship the notification. What does AUROC not tell? Three numbers on the slide instead of 0.95.

**MY ANSWER.** AUROC is ranking, not Se/Sp/PPV or the threshold. Put those on the slide (plus AUROC). Also unknown calibration; measure in bins or Brier. Did not say no to ship in the first sentence.

**CORRECTION.** **No.** 0.95 on ~50% event rate plus Watch PPV ≈8% is a notification users ignore. AUROC is also silent on **eval prevalence**. Product three: **PPV at declared τ**, **alerts per user-week**, **eval prevalence**. Calibration is a fourth if scores are shown or used as risk — do not bury the ship call.

---

### Q4 — Brier, reliability diagram, show \(p\) on the Watch?

**Prompt.** Formula; x/y and how you bin; why AUROC 0.95 can still be uncalibrated; show \(p\) to the user?

**MY ANSWER.** Brier = sum of squared diff prediction vs outcome; lower better. Bins e.g. 0–0.1; mean outcome vs mean prediction; diagonal ideal. AUROC does not constrain output values; “80%” is not 80 prevalence. Do not share \(p\), especially uncalibrated — unnecessary alarm, can be harmful.

**CORRECTION.** Brier is **mean** \((p_i-y_i)^2\) with \(y_i\in\{0,1\}\), not distance to true P. Reliability: **bin on predicted \(p\)**; x = mean \(p\), y = mean \(y\). Empty high-\(p\) bins are common at 1% prevalence. Say **personal risk**, not population prevalence. Even if calibrated, this product is usually a **binary alert at τ**, not a percent.

---

### Q5 — Accuracy 99% at ~1% prevalence

**Prompt.** Useful? Trivial baseline? Se and PPV under that baseline? Slide instead of 99%?

**MY ANSWER.** Probably not. Always-negative has 99% accuracy and is the baseline. Se=0, PPV=0. Put Se and PPV on the slide.

**CORRECTION.** Always-negative is the lock. Se=0 is exact. **PPV is undefined** (TP=FP=0), not 0. NPV=99%, Sp=100%. Se+PPV is the right swap for 99%; still pair PPV with **τ** and **eval prevalence**.

---

### Spoken restitch (Haraldur — 90s)

I would not treat Watch notification and clinic anticoagulation as one classifier. Screening: don’t miss, but report PPV and alerts per user-week at the Watch prevalence, and pick τ there. 90% Se and 90% Sp at 1% prevalence is about 90 TP and 990 FP, PPV ≈ 8% — that is why I do not ship on 90/90 or AUROC 0.95 from an enriched set. AUROC is ranking only. Brier is mean squared error of \(p\) vs a 0/1 label; reliability bins on predicted \(p\). I do not put an uncalibrated percent on the Watch. 99% accuracy at 1% prevalence is the always-negative baseline; sensitivity is 0 and PPV is undefined because there are no alarms.

**Next drill:** participant-disjoint split / leakage. Not another metric quiz.

---

## Vincent — constraint-injection (Sat 9/5)

Open. New cardiac early-detection, broad population. Framework: objective → population → data → labels → baseline → model → eval → deploy → monitor. Inject; **modify, do not restart.**

Do not restudy [`2026-08-27_onsite-vincent.md`](2026-08-27_onsite-vincent.md) Blocks 1–9. First-cycle log stays [`2026-09-03_onsite-vincent-practice.md`](2026-09-03_onsite-vincent-practice.md).

### MY ANSWER

_(append)_

### CORRECTION

_(append)_

---

## Yujie — Block 14 / 11 (Sat 9/5)

Open. Do not reopen Blocks 1–5. Ablations: matched token budget, shuffle, corrupt, missingness curves.

### MY ANSWER

_(append)_

### CORRECTION

_(append)_

---

## Jonathan — 3-claim defense + degrees of freedom (Sun 9/6)

Open. Speak the 9/1 miss: exploratory vs confirmatory; held-out confirmation; kill criteria. Do not fake pre-registration.

### MY ANSWER

_(append)_

### CORRECTION

_(append)_

---

## Mixed interviewer (Sun 9/6)

Open. Infer the dimension. Example sequence in the 4-day plan.

### MY ANSWER

_(append)_

### CORRECTION

_(append)_

---

## Mini-loop (Mon 9/7)

Open. 5 × ~20 min, random order. Log only holes.

### Holes

_(append)_
