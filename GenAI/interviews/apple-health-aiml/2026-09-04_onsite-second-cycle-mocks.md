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
| Sat 9/5 | **Vincent** basic 5Q | **Logged below** | Wellness nudge, not diagnosis. Repeat: n=20 ≠ OOD; no disclaimer-ship. Remaining Case #1: gestures, latency, new device. Case #2 still open. |
| Sat 9/5 | **Jonathan** 3Q | **Logged below** | Dual +0.08 needs drop/shuffle delay. Window ≠ subject. **DoF spoken** (TR mix kill). |
| Sat 9/5 | Yujie Block 14 / 11 | Open | Do **not** redo Blocks 1–5. |
| Sun 9/6 | **Tuesday full mock** | **Day file** | [`2026-09-06_tuesday-full-mock.md`](2026-09-06_tuesday-full-mock.md) — S1–S5 complete. Do not duplicate here. |
| Sun 9/6 | Jonathan ImagenFew 3-claim | Open | DoF is done. Still speak the three ImagenFew claims. |
| Sun 9/6 | Mixed interviewer | Open | Infer dimension. |
| Mon 9/7 | **Vincent** product/system | **Day file** | [`2026-09-06_tuesday-full-mock.md`](2026-09-06_tuesday-full-mock.md) — ~15 min; circular HR / random / 60%; Q4 unanswered. Do not duplicate here. |
| Mon 9/7 | **Haraldur** respiratory / labels | **Day file** | Same file — ~30 min; 1/8 PPV; window-from-Se; τ locked; Q8 unanswered. Do not duplicate here. |
| Mon 9/7 | Mini-loop (other three) | Open | Retrieval + remaining slots. |

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

## Vincent — basic 5Q, cardiac nudge (Sat 2026-09-05)

**Slot:** Tue 9/8 4:05 PDT.  
**Sheet:** [`2026-08-27_onsite-vincent.md`](2026-08-27_onsite-vincent.md) · Thu log: [`2026-09-03_onsite-vincent-practice.md`](2026-09-03_onsite-vincent-practice.md)  
**Constraint:** new case, not Block 0 recap. No transformer open. IC.

Covered: frame the product, near-chance ⇏ FM, n=20 slice, EHR blocked, XGBoost vs +1.5 deep. **Not covered:** gesture collision, deploy latency, new device generation, Case #2 4× budget.

### Scorecard

| Q | Topic | Verdict | One-line |
|---|-------|---------|----------|
| 1 | Decision / pop / FP-FN | Hit product, miss costs/axes | One nudge. **FP not negligible.** Design **for** age / body / wear-device-gesture, not “product is high-BMI.” |
| 2 | AUROC 0.52 ⇒ FM? | Hit no-scale | 0.52 → **Y, signal, eval bug**. Residual only if simple model is already useful. |
| 3 | 20 high-BMI positives, 0.55 | Repeat miss | **n=20 ≠ OOD.** CI / person units. **Hold or fallback. No disclaimer-ship.** |
| 4 | EHR link blocked | Claim right, gates inverted | Weaker \(Y\) and weaker claim. Gates fail ⇒ don’t ship, not “then use self-report.” No “<10%.” |
| 5 | XGBoost 0.78 vs deep 0.795 | Hit | Ship the robust simple model. Deep only if **operating point + sparse-wear floor** move. |

**Strongest:** don’t scale at chance; prefer XGBoost when deep dies on wear.  
**Weakest:** **disclaimer / legal-as-product**; **n=20 as shift**; **FP cheap because ignore**. Same Block 2 misses as Thu.

---

### Q1 — Early cardiac detection, broad population

**Prompt.** Leadership wants Watch early cardiac detection for everyone. ~90s: decision, when it fires, who acts, FP vs FN. One product. Three population axes. No model.

**MY ANSWER.** Wellness recommendations from cardiac detection. Pop: Watch users 20–99. Alert on every positive. FP negligible (user can ignore); FN high. \(Y\) mostly self-report. Axes: age; product attends to high BMI; note people with past history.

**CORRECTION.** One nudge is right — do not say “cardiac detection” next to self-report. **FP is alert fatigue**, not free. FN = no alert when the condition is present (missed suggestion), not “they take the alert seriously.” Name **when** (daily vs continuous vs post-workout). Watch wearers are already selected. **Design for** age, **body characteristics** (include the range; do not target high BMI), **wear / device / gestures that mimic**. Past history needs a permissible source.

**Axes restitch (spoken after the miss).** The population is Watch wearers, which is already selected. I would design for age, because prevalence and signal change across adulthood; for body characteristics, because the optical path is not the same for every wrist; and for wear and device generation, including gestures that can mimic the target. I would not restrict the product to high-BMI or to people with a known history — those are slices I must **measure**.

---

### Q2 — XGBoost AUROC ~0.52; colleague wants a Watch FM

**Prompt.** Scale up? Three checks first? When would you add complexity?

**MY ANSWER.** No. 0.52 ≈ chance: no signal or ill-defined problem. Want baseline to work on some of the population and fail a slice before going complex. Track AUROC/Se/Sp/PPV on slices; if all poor, bugs/data; if some work, debug poor slices (norm, scale, features); then maybe complex.

**CORRECTION.** No-scale is the lock. Three checks: **(1) \(Y\) / leakage / horizon** — self-report noise, wrong window, future in features; 0.52 can be the **ceiling**. **(2) Watch signal** — prevalence, wear, PPG quality, majority baseline. **(3) Eval bug** — participant split. Slice tables on **predeclared** axes after that. Do not hunt a lucky slice. Complexity only if the simple model is **already useful** and you can name what it cannot capture.

---

### Q3 — Overall 0.78; high-BMI 20 positives, AUROC 0.55; OOD / encoder / disclaimer

**Prompt.** Is 20 positives OOD? What before you conclude worse? Block, disclaimer-ship, or hold?

**MY ANSWER.** Compute high-BMI size and prevalence vs other subgroups. Se/Sp/PPV; if prevalence small, factor that in. If the whole group is small, cannot conclude — need more participants. Consult legal on disclaimer-ship; opt for that if allowed.

**CORRECTION.** **20 positives ≠ OOD.** Estimation, not shift. Need independent **people**, **CI**, **same units old vs new**. Wide interval ⇒ cannot conclude. **Disclaimer-ship is the miss.** Legal = collect/claim, not a footnote on a failed slice. **Hold** or **fall back**. Do not start a new encoder.

---

### Q4 — EHR link blocked; Watch + self-report remain

**Prompt.** Kill the product? What \(Y\)? What claim is illegal? Who, for which uncertainty?

**MY ANSWER.** Don’t kill immediately. Eval sensors + self-report Se/Sp/PPV + CI; predefine kill gates. If gates not met, use self-report as GT. Cannot claim true cardiac condition; switch to general wellness on profile. Only users with uncertainty <10%.

**CORRECTION.** Don’t kill the **nudge**; kill the **clinical claim**. Self-report **is** \(Y\) once EHR is gone. If gates **fail**, **don’t ship** — gates are not a prelude to “then use self-report.” No invented **<10%**. Privacy = link/claim; label partner = can self-report be \(Y\) for a nudge. Optional consented ECG panel if allowed, not a silent EHR substitute.

---

### Q5 — XGBoost 0.78 vs deep 0.795, deep dies on sparse wear

**Prompt.** Which ship? What would take the 1.5 points? One sentence on sparse-wear users.

**MY ANSWER.** Ship features+XGBoost even if CIs are tiny: simpler, cheaper, robust to sparse wear. Slice both models; if some slices are extremely strong for deep, reconsider while fixing poor slices (e.g. dropout sensor data for sparse wear).

**CORRECTION.** Ship XGBoost. +1.5 AUROC does not pay for a failed **sparse-wear** Watch population. Take deep only if **PPV / alerts per user-week at τ** move **and** a **predeclared sparse-wear floor** holds (plus latency/battery). Do not flip because one slice is strong. **Dropout** is train-time missingness for the deep model, not a ship reason. Prefer **route**: XGBoost when wear is sparse.

---

### Spoken restitch (Vincent — 90s)

I’d define a wellness nudge, not a cardiac diagnosis: when it fires, who acts, FP is alert fatigue. Population is Watch wearers; I design for age, body characteristics, and wear/device/gestures, and I measure those slices — I don’t target only high BMI. Near-chance XGBoost means I check labels, horizon, leakage, and whether the Watch can support the decision; I don’t start a foundation model. Twenty positives is uncertainty, not OOD; I don’t conclude, don’t disclaimer-ship, I hold or fall back. If EHR won’t link, the claim dies and self-report is the nudge label, with gates on that product. I’d ship features plus XGBoost at +1.5 AUROC if the deep model fails sparse wear; I only take deep if the operating point and that floor both move.

**Still open today:** gesture-collision injection; deploy latency; new device generation; Case #2 (4× budget). Do not restart Blocks 1–9.

---

## Yujie — Block 14 / 11 (Sat 9/5)

Open. Do not reopen Blocks 1–5. Ablations: matched token budget, shuffle, corrupt, missingness curves.

### MY ANSWER

_(append)_

### CORRECTION

_(append)_

---

## Jonathan — 3Q dual / splits / DoF (Sat 2026-09-05)

**Slot:** Tue 9/8 11:05 PDT.  
**Sheet:** [`2026-08-27_onsite-jonathan.md`](2026-08-27_onsite-jonathan.md) · 9/1: [`2026-09-01_onsite-jonathan-research-rigor.md`](2026-09-01_onsite-jonathan-research-rigor.md)  
**Constraint:** not a project recap. Claim → evidence → alternative → experiment → narrow.

Covered: dual +0.08 complementarity; ImagenFew window vs subject; researcher degrees of freedom (9/1 Q5). **Not covered:** ImagenFew three-claim defense (image-space scarcity / within-2D rep / robustness).

### Scorecard

| Q | Topic | Verdict | One-line |
|---|-------|---------|----------|
| 1 | Dual 0.17 / 0.71 / 0.79 | Tokens/HP hit; kill incomplete | Dual +0.08: matched tokens + CI on **dual−chart**. **Drop/shuffle delay** is the complementarity kill. Real jump is **0.17→0.71**. |
| 2 | Data-efficient — which unit? | Hit | Window split ≠ subjects. Interpolation; possible same-trajectory leak. |
| 3 | Hill-climbing vs hypothesis | Hit (the 9/1 miss) | Gates before the run; TR mix killed on the **intended** slice. Exploratory hole → confirmatory mix. |

---

### Q1 — Second stream adds information?

**Prompt.** Delay-only ≈0.17, chart ≈0.71, dual ≈0.79. Two alternatives that also produce +0.08; one experiment that kills complementarity. No ablation list.

**MY ANSWER.** (1) HP sensitivity (seed, LR, schedule, temperature, DE HPs). Experiment: sweep around 0.79, CIs; if they swallow 0.08, kill. (2) More tokens: chart+DE almost 2×. Experiment: chart | DE | dual at the same token budget; if the gain remains, complementarity is real.

**CORRECTION.** Both are real. Interval on **dual − chart**, same protocol. Matched tokens is the stronger “more stuff” test. **Narrow first:** the jump that needs a story is **0.17→0.71**, not +0.08. **Missing kill:** drop or **time-shuffle delay**, keep chart, matched budget. If 0.79 does not move, there is no complementarity.

---

### Q2 — ImagenFew data-efficient wrt which unit?

**Prompt.** Windows vs trajectories vs subjects. Allowed claim in each. What dies if only windows were held out?

**MY ANSWER.** Efficient wrt random windows. Allowed: generalize to other windows from the same dist. Cannot claim held-out trajectories or subjects — windows can come from test traj/subjects.

**CORRECTION.** Lock is right. Say **interpolation / within-trajectory**. Same-series windows can leak identity. Do not underclaim if trajectory/subject tables exist — match sentence to table. Data-efficient also means **vs a baseline at the same window budget**.

---

### Q3 — Degrees of freedom / hill-climbing

**Prompt.** Many knobs. Hypothesis-driven vs hill-climbing. Not “many datasets.” Exploratory vs confirmatory, one kill you used, one negative that changed the method.

**MY ANSWER.** Multimodal was weak on TSRBench TR. I built a synthetic TR-operator slice. Before train+eval I set gates: −3 pp overall, −5 pp on a single task. After: overall +2.1 pp, some tasks +7 pp, but the TR slice I cared about went 26.9→21.9. Clear kill: hit the gate **and** the task I made the data for got worse.

**CORRECTION.** This is the 9/1 Q5 answer. **I** set gates before the run; **I** killed when the intended slice fell. TSRBench failure **generated** the hypothesis; this mix **tested** it. Do not fake full pre-registration; do say you did **not** remix until TR went up. Direction on TR beats “hit −5.” After the kill, do not promote another mix on the same eval used to invent the recipe. Do not add “many datasets.”

---

### Spoken restitch (Jonathan — 90s)

I don’t claim the delay tower adds information from +0.08 until that gap survives matched tokens and a drop or shuffle of delay; the chart vs delay jump is the main representation result. Window-level scarcity supports other windows from a similar process, not held-out people. On the TR mix I predeclared kill gates, the target slice fell 26.9 to 21.9, and I killed the additive mix — that is how I separate a test from hill-climbing.

**Sunday leftover:** three ImagenFew claims only (image-space under scarcity; rep within 2D; persists across regimes). DoF is paid.

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
