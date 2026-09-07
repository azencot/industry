# Tuesday full mock — Sun 2026-09-06

Live-order simulation of **Tue 2026-09-08**. One file for the day. Append after each session.

**Order:** Jonathan 11:05 → Yujie 1:05 → Chung-Cheng 2:05 → Haraldur 3:05 → Vincent 4:05 PDT  
**Rule:** no per-question feedback; critique at session end. ~30 min/slot (live is 45).  
**Hub:** [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)  
**Mon 9/7 addendum:** Vincent (~15 min) and Haraldur (~30 min) mini-loops logged after Session 5.

| # | Person | Status | Clock | Notes |
|---|--------|--------|-------|-------|
| 1 | Jonathan Bourim | **Logged below** | ~32 min, stopped before last Q | Dual-tower only. DoF question unanswered. ImagenFew / Stage A / questions-for-him not reached. |
| 2 | Yujie Li | **Logged below** | ~22 min, stopped before PPG 200 ms | Activity-only. Patch vs latent. Missing-token without channel ID. 200 ms PPG unanswered. |
| 3 | Chung-Cheng Chiu | **Logged below** | ~30 min, stopped on 45% util Q | Answers recaptured closer to verbatim 2026-09-06. 256 vs 512 still a slip. Q4–Q7 critique was too harsh on intent. 45% util unanswered. |
| 4 | Haraldur Hallgrímsson | **Logged below** | ~30 min, stopped on sparse FPR floor | FP-cheap opening; 1/6 PPV; no-ship; people vs windows; router. Slide numbers ≠ PPV@τ + alerts/week. |
| 5 | Vincent Chan | **Logged below** | ~12 min, stopped on 5% / cut months | Language-layer bet; waterfall; n=20 not OOD and not ship. 5% chance and months 3–6 unanswered. |

---

## Day wrap (S1–S5)

Live-order mock **complete** (all five started; several stopped before 45 min). Tuesday still has ~15 min extra per slot: questions for them, ImagenFew, 200 ms PPG, 45% util, sparse FPR floor, Vincent 5%/cut.

| Person | Keep | Tuesday first sentence |
|--------|------|------------------------|
| Jonathan | TR kill 26.9→21.9 with gates | Problem/hypothesis, not architecture. DoF: post-hoc audit is a diagnosis. |
| Yujie | Task scope; native Hz; duration curve; no zero-fill | Patch length **is** resolution. Classification ≠ canned text Q. |
| Chung-Cheng | A vs P/G/O; FSDP comm tax; match batch | `global_batch = mb × world × accum` (512 not 256). |
| Haraldur | 1/6; two products; no-ship; people split; XGBoost | FP not cheap. Slide = PPV@τ + alerts/week + eval prevalence. **Mon 9/7:** Y ≠ report ≠ EHR; don’t pick the label window from Se; threshold → model → product. |
| Vincent | Language bet; people split; shuffle/zero; **n=20 ≠ OOD, no disclaimer** | Kill in month one; 5% above *which* chance; cut production months while n=20. **Mon 9/7:** uncertainty → cheapest falsifier, not a 4-week pipeline. |

---

## Session 1 — Jonathan Bourim (~32 min, stopped)

**Slot:** Tue 9/8 11:05 PDT · research depth & scientific rigor  
**Sheet:** [`2026-08-27_onsite-jonathan.md`](2026-08-27_onsite-jonathan.md)

Stopped on request before answering the last question (post-hoc vs pre-specified mismatch). Treat Q8 as **unanswered**.

### Scorecard

| | |
|--|--|
| Claim vs system | Opening was architecture/eval, not problem → hypothesis. Recovered once pushed. |
| Numbers without re-prompt | **Hit.** 0.17 / 0.71 / 0.79; TSExam 0.86–0.88; shuffled-chart ChatTS 0.37; TR 26.9 → 21.9; gates −3 / −5 pp. |
| Alternatives | **Partial.** Token-matched single towers volunteered. Shuffle/zero came one prompt late. Capacity (params, extra encoder) never separated from tokens. |
| Complementarity vs “both used” | **Needed prompting.** Destroy-input ≠ complementary information. Slice-specific movement was vague until the shuffle-charts follow-up. |
| Kill | **Strong.** Pre-specified gates, two settings, killed the mix that hurt the target slice. |
| Near-chance TR | **Overclaimed.** 26.9 vs ~25% random. “None of the explanations is that the system is not doing reasoning” is too strong. |
| Degrees of freedom | **Unanswered.** Last spoken turn was a three-part post-hoc audit. This is still the live risk. |
| Unreached (would still come up in 45 min) | ImagenFew; Stage A freeze / LoRA; rendering as bottleneck; why not improve chart-only; DINO vs Qwen; native TS FM; questions for him; pad/collator. |

**Strongest thread:** TR mix kill with numeric gates.  
**Weakest:** opening claim, then DoF — you diagnosed the eval *after* the failure and treated that diagnosis as the reason you were at chance.

### Exchanges

**Q1.** Tell me about a research project you’re proud of. What were you actually trying to establish?

**You.** Dual-tower Qwen3-VL; charts via Qwen ViT, DE via DINOv3; staged perception → reasoning; NTP; eval TSExam → ChatTS → TSRBench. Mechanism stated as fact (charts = amplitude, DE = dynamics).

**Miss.** System, not claim. First 30–45 s should be problem / hypothesis with no architecture.

**Q2.** How do you know the second tower adds information vs capacity / tokens / optimization?

**You.** DE vs charts similar on TSExam; ChatTS numerical DE 0.17 vs charts 0.71; DE better on anomaly; dual 0.79; same data and training budget; later token-matched single towers, qualitative result unchanged.

**Lock.** Numbers are the right shape. Dual +0.08 on numerics with a 0.17 branch still needs an intervention, not only a matched budget.

**Q3.** Drop / shuffle / time-shift delay and watch 0.79?

**You.** Zeroed each modality; shuffled each; all four dropped. Have not run tasks that require one view.

**Miss.** Those tests show both pathways are used. They do not prove complementary information. Honesty about the missing experiment was good.

**Q4.** When delay was destroyed, what moved — numerical, anomaly, or average?

**You.** Drop-other-modality aligned with the remaining single tower. Shuffle-charts still “decent.” General behavior within 1–2 pp.

**Miss.** Too coarse until the next prompt. “Decent” hid the slice.

**Q5.** Shuffling charts: what stayed decent, and how do you interpret answers when the chart is the wrong series?

**You.** TSExam ~0.86–0.88. ChatTS numerical to 0.37 (random 0.25). Some ChatTS items don’t need order. Called it legitimate.

**Partial.** 0.37 vs 0.71 is a real drop; 0.37 vs delay-only 0.17 is leftover signal. “Increased 20 pp” was confusing — say the **from/to** numbers. Do not call leftover signal a confirmation of complementarity.

**Q6.** Average held or improved, you still killed the change.

**You.** TR mix: 26.9% vs ~25% random. Gates −3 pp overall / −5 pp slice. Short FT on Stage B hit both gates. Mix into Stage B: +2.1 overall, some slices +7, TR 26.9 → 21.9. Killed. Then TSRBench audit.

**Hit.** This is the spoken lock. Keep it this tight on Tuesday.

**Q7.** Why believe the model is doing TR at all? Why did TR-targeted data make TR worse?

**You.** Rejected “not reasoning.” Manual QA + audit: (1) TSRBench domain knowledge the LM lacks; (2) 3 segments in train vs 8 in eval; (3) prompt format mismatch. Mix was off-distribution.

**Miss.** Those three explain why the mix failed to *help*. They do not by themselves explain 21.9 < 26.9, and they do not retire “near chance on this task.” Allow: the northstar slice is consistent with guessing *on that eval*; domain-knowledge contamination means TSRBench TR is not a pure temporal-reasoning test.

**Q8.** How do I know the three mismatches aren’t a post-hoc story? What would you have written down *before* item-by-item inspection?

**Unanswered.** Stopped here.

### Spoken restitch — worst miss (DoF)

Use if he stays on the audit:

“I did not pre-specify those three mismatches. The pre-specified claim was: TR-shaped synthetic data will raise TR without breaking the −3 / −5 gates. It didn’t. After the kill I inspected the eval and found domain knowledge, event-count, and prompt mismatch — that is a diagnosis, not evidence I had at mix time. To trust mismatch over ‘the model isn’t doing this task,’ I would have needed, before looking at items: a frozen sample of TSRBench TR labeled by operator, event count, and required world knowledge; a coverage table of the mix against that taxonomy; and a held-out confirmation set I would not retune on. I don’t have that. What I can say is: 26.9 vs 25% is near chance on this slice; the mix made it worse; the gates fired; I will not treat the post-hoc taxonomy as the cause until I test it with coverage-matched data or a cleaner TR probe.”

### Spoken restitch — opening (second miss)

“General-purpose VLMs don’t ingest continuous trajectories natively. I wanted to know which visual encoding makes temporal information accessible, and whether two encodings are complementary rather than redundant. The hypothesis was: charts expose amplitude and extrema; delay embeddings expose dynamics; both together should beat either alone on tasks that need both. The architecture is how I tested that — it is not the claim.”

### Next if this hour continues (do not run now)

One ImagenFew claim (image-space under scarcity) with alternatives, then stop. Do not redo dual complementarity.

---

## Session 2 — Yujie Li (~22 min, stopped)

**Slot:** Tue 9/8 1:05 PDT · multimodal architecture & time-series encoding  
**Sheet:** [`2026-08-27_onsite-yujie.md`](2026-08-27_onsite-yujie.md) · [`2026-09-05_yujie-advanced.md`](2026-09-05_yujie-advanced.md)

Stopped on request before answering Q7 (axis permute + 200 ms PPG on the existing design). Treat Q7 as **unanswered**.

### Scorecard

| | |
|--|--|
| Task scoping | **Hit.** Activity ≠ event detection ≠ QA. Keep that. |
| Native clocks / no common-Hz upsample | **Hit** in the opening. Then “resample to shrink tokens” mixed patch compression with resample language. |
| Physical time on tokens | **Named once**, not used later. |
| Token arithmetic | 900–1800 / 30 min ≈ 1–2 s. IMU 50 Hz → 50 samples/token. 50 tok/s × 30 min = **90k** — needed prompting. |
| Fusion | Xattn Q=text for a **no-text** classifier. Canned prompt is a dummy query. One KV bag; equal C was the drowning defense. |
| Patch = temporal resolution | **Missed, then partially recovered.** Claimed FT encoder / latent pool keeps a 300 ms step inside a 1 s patch. Duration curve was the right fix. |
| P×C / missing channel | Dropout + missing token, **no zeros**. **No channel ID.** Permute unanswered. |
| Windowing | 1–5 min crops + vote changes the 30 min model. Owned the long-event loss. |
| Unreached | 200 ms PPG; audio 16 kHz; clock drift; matplotlib-on-PPG; IMU ignored in xattn; new device Hz; questions for her. |

**Strongest thread:** scope the task; native-rate encoder; duration curve; don’t impute missing channels with zeros.  
**Weakest:** “the encoder will keep what the task needs” inside a 1 s mix — that is the Transformer-will-figure-it-out answer.

### Exchanges

**Q1.** PPG 128 / IMU 50 / HR 1 / sleep / text / 16 kHz audio; mixed tasks. Tokens, information, clocks, fusion.

**You.** Activity only. 900–1800 tokens/modality (1–2 s), maybe 450. Encoder at native Hz → latent resample → LM proj. Timestamp or Δt. PPG 64/128, IMU 25/50, IMU needs finer. Xattn not concat (watch quadratic). Q=text, KV=all modalities.

**Partial.** Good: task split, native Hz, time on tokens, don’t concat 6k into self-attn. Weak: audio ignored; HR already 1 Hz (don’t invent 1800 HR tokens as “resample”); Q=text for classification.

**Q2.** No user text. One KV bag — softmax ignores sparse streams.

**You.** Canned expert prompt. Every modality capped 900–1800, so PPG/IMU are resampled down. Drowning denied.

**Miss.** Equal **count** ≠ equal **information**. A canned prompt is a constant query; learned latent queries (or a classifier on encoder pooled states) are the classification architecture. Still one KV bag.

**Q3.** ~1 IMU token/s vs a few-hundred-ms step. What remains accessible? What experiment?

**You.** Not raw resample — latent resample after encode, so the step lives in the latent. Test: IMU-only, steps vs none, manual gold, short FT on a vanilla LM.

**Miss.** Latent pool cannot recover a step mixed **inside** the patch **before** the encoder. Vanilla-LM FT confounds preservation with LM capacity.

**Q4.** Patch length in samples/ms vs latent hop. Duration curve vs vanilla LM.

**You.** 50 Hz, patch = 50 samples = 1 s = 1 token. Encoder FT with the LM keeps task info in that vector. Duration curve 1 tok/s → 50 tok/s. Vanilla LM or own system both viable.

**Hit + miss.** 50 samples / 1 s is the lock number. FT-keeps-info is still wrong. Duration curve is the right experiment (Fri restitch: event inaccessible, not deleted).

**Q5.** FT does not restore resolution. 90k tokens at 50 tok/s. All axes mixed?

**You.** Shrink to 1–5 min (or 1/5 min) windows; overlap + majority vote / small net. Prefer all channels in one patch for cross-channel.

**Partial.** Diagnostic windows are fine. That is no longer the 30 min model. 90k handled by changing T, which can be the result.

**Q6.** Missing axis or permute. What long-horizon activity you gave up.

**You.** Channel dropout in train; special missing tokens; don’t drop the whole window; don’t zero-fill. If the event is longer than the crop, the choice is invalid; you had assumed ms-scale events.

**Hit + miss.** Missing-token / no zeros is correct. **Permute ≠ missing.** Joint P×C needs channel identity. Long-horizon loss owned.

**Q7.** Axis swap + 200 ms PPG: patch samples, 30 min token count, fusion with IMU. **Unanswered.**

### Spoken restitch — worst miss (patch vs “encoder will adapt”)

“Patch length is the temporal resolution the backbone can see. At 50 Hz, a 50-sample patch is one second and about fifty mixed samples in one vector. Fine-tuning the encoder can keep energy, a dominant frequency, maybe a count. It cannot place a 300 ms step inside that second or separate two steps 400 ms apart if those events were already pooled. Latent resampling after a 1 s patch does not restore milliseconds. I choose P from the task timescale, then I run a duration curve at a matched IMU token budget C on a short-event slice. 50 tokens per second on 30 minutes is 90k tokens — that is a probe, not the deploy config, so I crop or cap C and I do not let sequence length be the result.”

### Spoken restitch — classification fusion (second miss)

“Activity classification has no user text. A canned prompt is a dummy query I would pay T_text × T_mod for on every window. I would use a small set of learned queries, or pool the encoder and classify, and I would not dump PPG+IMU+HR into one KV bag. Equal token counts stop count-drowning; they do not make one PPG-second as informative as one HR sample.”

### Spoken restitch — Q7 if it comes back (do not run now)

“Permute: channel ID on the joint patch, plus a shuffle-axis test. 200 ms PPG at 128 Hz is ~26 samples. I would not reuse 1 s PPG patches. Encoder tokens ≤ event, then a bounded latent budget so 30 min does not become 230k raw samples. IMU stays on its own clock; fusion is after per-modality compression, with timestamps, not a shared 1 Hz grid.”

### Next if this hour continues (do not run now)

200 ms PPG on the existing design, then 16 kHz audio token tax. Do not reopen the 1 s IMU patch debate.

---

## Session 3 — Chung-Cheng Chiu (~30 min, stopped)

**Slot:** Tue 9/8 2:05 PDT · LLM training & infrastructure  
**Sheet:** [`2026-08-27_onsite-chung-cheng.md`](2026-08-27_onsite-chung-cheng.md)

Stopped on request before answering Q8 (vision towers, util 45%). Treat Q8 as **unanswered**.

**Log note (2026-09-06):** first writeup compressed answers and scored intent as misses. **You** lines below are closer to the spoken words. Critique is separate. Unfair bits called out.

### Scorecard (revised)

| | |
|--|--|
| Owned run | **Hit.** 8B Qwen3-VL, 8×A100 80GB, DDP, Stage A/B LoRA. |
| Bottleneck class | **Hit.** P/G/O do not scale with B,T; A blew up. Target global 64 at 8K = microbatch 8; only got 2 + accum. |
| Flash vs AC | **Hit.** Ablated AC vs accum; AC compute too high; Flash because mem peaked on attention tiles. |
| FSDP | **Hit.** Shards P/G/O; LoRA not full FT; bf16; would compute P+G+O vs A vs batch; estimate P+G+O < half GPU; network tax; object but would run the experiment. Frozen 16GB was **already inside** that <40GB estimate — not a recovery after forgetting P. |
| 8→64 mechanism | **Hit.** ×8 samples/step; faster schedule; warmup/LR; log LR and train/val vs **samples seen**. Overfit was one hypothesis, not the only one. |
| 8→64 arithmetic | **Slip.** Said 64 vs **256**. With microbatch 2, accum 4: 2×64×4 = **512**. |
| Matched-batch experiment | **Intentional, not a miss.** Accum 8 on 8 GPU and accum 1 on 64 GPU aligns the two runs (128 if microbatch 2). You said that was not the original recipe and you still wanted that test. When asked for original 64: microbatch 1, accum 1; if tokens/step equal, do not change steps. |
| Unreached | 45% util / input stall; two ranks late; resume diverge; questions for him. |

**Still a Tuesday risk (narrow):** say `global_batch = microbatch × world × accum` out loud once so 256 cannot appear. Plot vs samples **and** vs optimizer updates.

### What the first critique got wrong

- Q4 was not “LoRA made you forget frozen P.” You estimated **P+G+O < half of 80GB**. That budget only makes sense if frozen P is in it. “Parameters small vs model size” was about **trainable** LoRA, not “the 8B is gone.”
- Q5 “not really” was consistent with Q4, not a late save. 16GB frozen + LoRA G/O still < 40GB, so you would not wrap.
- Q6 did not “first blame overfit.” You said ×8 samples/step, adapt the schedule, **overfit as one hint**, warmup/LR as **another**, then log vs samples seen.
- Q7 accum 8 vs 1 was a **matched-batch experiment**, not a failed attempt to reproduce 64. You said so explicitly.

**What still stands:** 256 ≠ 512 if microbatch is 2. “Adapt the number of steps” at a **fixed token budget** needs one sentence: matching global batch already matches tokens/step, so step count stays.

### Exchanges (closer to spoken)

**Q1.** Largest owned setup: size, GPUs, parallelism, first constraint, how you knew.

**You.** Multimodal TS+text reasoner, Qwen3-VL 8B. Most training on 8×A100 80GB from NVIDIA. Stage A: DINOv3 LoRA + linear projector. Stage B: Qwen LoRA + DINOv3 LoRA. DDP. First constraint: memory — could not scale batch size and seq len beyond mild limits.

**Q2.** Which of P/G/O/A? Microbatch, T, vision tokens? Memory vs idle loader?

**You.** P, G, and O are not affected by batch size and seq len; activations blew up. Wanted global batch 64 with 8K seq ⇒ 8 samples microbatch per GPU; only got to two and added grad accum.

**Q3.** Saved activations vs attention tiles? Was 8K full context? What before microbatch 2?

**You.** Yes, 8K was the **total** sequence: ~200 vision (114 charts, 64 DE), rest for prompts. Varying question lengths; often need the entire 8K. Could not reduce T: capping prompts was a real bug and hurt results. Considered activation checkpointing and **ablated it vs grad accum**; extra compute from AC was too high vs accum. Reducing visual tokens did not make sense: only 200 already, below that TS resolution would hurt. Mem peaked on the activations on the attention tiles → FlashAttn **in addition to** grad accum.

**Q4.** Colleague wants FSDP to get microbatch 8 back. What does it buy?

**You.** FSDP shards P, G, and O. Not a full FT on LM / ViT / DINO — LoRA on all of them, so trainable params are small vs model size. bf16, two bytes per number. To decide if FSDP is worth it, calculate P+G+O vs A for several batch sizes. Rough estimate: P+G+O takes less than half of GPU mem; sharding incurs too much networking. In general object to FSDP, but would run the experiment to convince the colleague.

**Q5.** Frozen 8B still ~16GB per rank. Change the experiment? Wrap frozen backbone?

**You.** Not really. Rough estimate was already P+G+O < 40GB: that **includes** the frozen 16GB plus G+O for LoRA. If P itself were almost half (~40GB) you would consider wrapping. With 16GB, FSDP would be aggressive sharding and a lot of all-reduce / all-gather.

**Q6.** 8→64, same microbatch/accum/T/token budget, faster, val worse. What changed?

**You.** Each step now processes ×8 more samples. If nothing else changed, that is a faster training schedule. Total steps need to be adapted, which **hints** worse val may be overfit. **Another option:** warmup and LR mismatch; those should be adapted to the new speed. Verify by logging LR, train and val **vs amount of samples seen**, and look for deviation when the x-axis is aligned.

**Q7.** Two global-batch numbers with accum you used. First change if you want the same optimization.

**You.** Accum 4, so global batches 64 for 8 GPUs and **256** for 64 GPUs. Can match global batch instead: accum 8 on 8 GPUs and accum 1 on 64 GPUs as the first change; after that also consider changing number of steps (with the previous accum) and warmup/LR.

**Q7b.** 2×64×4 = 512 not 256; accum 8 vs 1 is 128 not original 64; if tokens/step equal why change steps?

**You.** Wanted an experiment on **aligned** global batch. Indeed not the original run; still want that test. To match 64 for the original run: microbatch 1 and accum 1. If tokens per step are equal, do not need to change #steps.

**Q8.** Text-only util holds; add two vision towers; util ~45%. Class? Measure first? **Unanswered.**

### Spoken restitch — only the 256 slip (keep short)

“Global batch is microbatch × world × accum. 2 × 8 × 4 = 64. Same recipe on 64 GPUs is 2 × 64 × 4 = 512. If I say 256 I dropped the 2. A matched 8-vs-64 bakeoff is a different recipe — I say the target global batch. Once tokens per step match, I do not add steps.”

### Spoken restitch — Q8 if it comes back (do not run now)

“Plus 200 tokens does not explain a collapse to 45% util. Competing classes: input stall (decode, DINO, collate two views, variable 8K pack), unfused vision path, comm / straggler. I measure GPU-busy vs dataloader wait, time in vision encoder vs LM, whether ranks arrive together. I do not add FSDP or GPUs until I know which clock is idle.”

---

## Session 4 — Haraldur Hallgrímsson (~30 min, stopped)

**Slot:** Tue 9/8 3:05 PDT · health domain & applied ML judgment  
**Sheet:** [`2026-08-27_onsite-haraldur.md`](2026-08-27_onsite-haraldur.md)

Stopped on request before answering the sparse-slice FPR / alerts floor (after “1–2% of PPV”). Treat that as **unanswered**.

**You** lines are close to spoken. Critique is separate.

### Scorecard

| | |
|--|--|
| Problem framing | **Partial.** Pop, daily 24h horizon, sensors, two label sources. Opening: FP cheap because ignore / cheap check. |
| Prevalence → PPV | **Hit** at 1% / 95% Se / 95% Sp → **1/6**. **Slip:** 5% + 95/95 does not restore 80% (that is 50%). |
| Two products | **Hit.** EHR-linked = health prediction / notification. Self-report = wellness. Do not silently swap Y. |
| Don’t invent epi | **Hit.** Not a clinician; 5% is an assumption on all Watch wearers in band; EHR-linked rate higher (selection). |
| Split | **Hit, branched.** Windows if same people; **people split** (+ bootstrap) if new people. For this Watch product, new wearers ⇒ people split as default. |
| Baseline | **Hit.** Features + XGBoost before deep / language. Se/Sp/PPV per age, train and deploy. AUROC + Brier named. |
| Ship on AUROC 0.95 / PPV 8% | **Hit.** “I am not shipping.” (Friday miss was not saying no first.) |
| Slide instead of 0.95 | **Miss vs lock.** You put prevalence, calibration, PR-ROC. Lock is **PPV at declared τ**, **alerts per user-week**, **eval prevalence**. You argued PPV was already 8% and alerts follow from PPV+calibration. |
| Daily FPR kill | **Hit.** 10% of healthy notified every day → kill; measure FPR. For a 24h product that is the alert-rate piece. |
| Sparse wear | **Partial.** Router (deep if full, XGBoost if sparse) is allowed. “Deep anyway if drop 1–2%” was underspecified until “of PPV”; absolute vs relative and sparse FPR floor unanswered. |
| Unreached | n=20 ≠ OOD; diagnosis vs care-seeking; missingness-as-shortcut vs impute; questions for him. |

**Strongest:** 1/6; two products; no-ship; people vs windows; XGBoost first; daily FPR kill.  
**Tuesday risk:** first sentence “FP are cheap”; slide = curve/calibration instead of PPV@τ + interrupts/week; 1–2% PPV as a deep-model gate.

### Exchanges

**Q1.** Watch, early cardiac, notify. What is Y, when, who, cost of wrong?

**You.** Early cardiac detection. Output is a notification that can be ignored. Population: Watch wearers, typical age 20–65. Data: PPG, IMU, derived HR. Labels: self-report and linked EHR if legal. Prediction, daily, horizon 24h, predict at the point before those 24h. FP not costly: ignore, or cheap check. FN more costly: false reassurance, product doesn’t help when the problem arises.

**Q2.** Wrist FPs are not free. PPV / alerts / prevalence. Self-report ≠ EHR.

**You.** Start with prevalence per age slice (young / mature / old). Measure PPV at a declared threshold (pending 95% Se). If PPV high enough (e.g. above 80%), that reinforces FP are cheap. Prefer linked EHR if possible; else defer to self-report.

**Q3.** 80% PPV at 95% Se — prevalence and specificity? If linkage blocked, what claim dies?

**You.** If prevalence 1%, aim 95% Sp → PPV 1/6, quite low, way below 80%, have to reconsider. If prevalence higher, say 5% for older ages, 80% could be appropriate. Two separate products: EHR-linked = health prediction with a viable notification; self-report = wellness recommendation.

**Q4.** At 5% with 95/95, PPV is 50% not 80%. Watch band vs EHR-linked?

**You.** Not a clinician; don’t know actual prevalence by age. 5% for old age is just an assumption of **all Watch wearers** in the band. EHR-linked subset: assume rate higher (people with EHR are conditioning-biased).

**Q5.** Eval so the reported number is the deployment number. Train vs test. First model before deep / language.

**You.** Depends on unit of independence. If product must gen to different windows of same people: random windows. If new people: split over people (probably bootstrap). Baseline: features + XGBoost — simple, fast, interpretable. Test Se/Sp/PPV per age band in training and in deployment. Want high discrimination (strong AUROC) and high calibration (Brier).

**Q6.** New wearers ⇒ people split. Colleague: AUROC 0.95 on EHR-linked, Watch PPV ~8%, ship? Three numbers instead of 0.95.

**You.** Not shipping. Three numbers at the operating point: prevalence, calibration, and PR-ROC — whether the probabilities relate to the actual event distribution.

**Q7.** Why not PPV at τ and alerts per wearer per week?

**You.** PPV at the threshold already known to be 8% (unless that was training not production), so didn’t mention it. Alerts per wearer is a direct consequence of marked positive; can be understood from PPV and calibration.

**Q8.** Same 8% PPV, different cadence. What alert rate still kills? How measure?

**You.** Original product predicts per 24 hours. If every day yields a notification for a large amount of users (say 10% of healthy people), kill the notification. Measure by calculating FPR.

**Q9.** ~40% nights missing. XGBoost holds on sparse; deep better on complete, drops on sparse. Which ship? What number takes deep anyway?

**You.** Ship both with a router (or MoE): deep when seq is full, XGBoost if sparse. Use the deep model anyway if the drop is very small, around 1–2%.

**Q10.** 1–2% of what?

**You.** 1–2% of PPV.

**Q11.** Absolute or relative? Predeclared FPR / alerts floor on the sparse slice. **Unanswered.**

### Spoken restitch — slide (worst miss)

“I do not ship on AUROC 0.95 from an enriched linked set when Watch PPV is 8%. The slide is eval **prevalence**, **PPV at the threshold we fire**, and **alerts per wearer per week** (for a daily product, FPR among healthy is the interrupt rate). PR-ROC and Brier are extra. PPV is precision of an alert; alert rate is how often we interrupt. Calibration does not turn one into the other. FP are not cheap because the user can ignore us — that is how they disable the product.”

### Spoken restitch — 95/95 arithmetic (keep)

“At 1% prevalence, 95% Se and 95% Sp: TP = 0.95×sick, FP = 0.05×healthy → PPV ≈ 1/6. At 5% the same 95/95 is 50%, not 80%. I do not invent prevalence; I measure it in the **notification** population, which is not the EHR-linked set.”

---

## Session 5 — Vincent Chan (~12 min, stopped)

**Slot:** Tue 9/8 4:05 PDT · technical leadership & system thinking · last of five  
**Sheet:** [`2026-08-27_onsite-vincent.md`](2026-08-27_onsite-vincent.md)

Stopped on request before answering Q4 (5% above which chance; what to cut in months 3–6). Treat Q4 as **unanswered**.

**You** lines close to spoken. Critique separate.

### Scorecard

| | |
|--|--|
| Pick a bet | **Hit.** Language layer, not both. |
| Population / labels | **Partial.** 20–65, all BMI (BMI named). Self-report for a chatbot is not a grounded-QA label. All-comers in six months is not a first slice. |
| Calendar | **Miss.** Six equal months is a waterfall. Eval and kill sit in months 4–6. Legal consulted — good. IC owns encoder+system — good. |
| Kill | **Late.** After month two, if prelim LM on encoded sensors is “extremely poor” *and* data/encoder check out. Shuffle/zero/remove or toy sensor-QA; if fail, improve encoder, don’t fuse. |
| Cheapest learn | **Pushed back, legitimate.** TS community: LMs don’t understand series; encoding/fusion is the open problem; frozen LMs near chance. Still owe a **non-LM encoder readout** and a defined chance baseline. |
| 5% above chance | **Underspecified.** Absolute 5% PoC, but chance-of-what unanswered. |
| n=20 | **Hit vs Sat miss.** Not OOD. Not ship. Extend expert n, pop stats vs general, prevalence in subgroup. Hold production until a more thorough study. Tension: “continue the six-month plan” still included month-6 production prelim until asked to cut. |
| Unreached | Gestures; latency; new device; XGBoost vs LM; BMI gap; Card 1/3/4 stories; questions for him. |

**Strongest:** one bet; participant split; sensor interventions; n=20 is uncertainty, no disclaimer.  
**Tuesday risk:** waterfall; kill after encoder month; 5% without a chance definition.

### Exchanges

**Q1.** Six months, IC. Language layer vs silent notification. Bet, who, kill, own vs others.

**You.** Bet on the language layer. For all Watch wearers, age 20–65, across all BMI. Labels self-reported. Data from Watch sensors. Output model text (chatbot), prompted through the day via UI buttons. Six months: (1) data gathering, processing, cleaning, normalization; (2) per-sensor encoder, pretrain; (3) fuse sensors into LM; (4) offline eval — claim is generalize to new wearers, so train/test sliced over participant; (5) expert eval; (6) production prelim tests. Personally own encoder + system development. Data gathering + eval: help from engineers and health experts, also for production. Consult legal on permitted responses and harness.

**Q2.** Month-one kill? Self-report ≠ “used the Watch.” First eval that sensors are used. If that fails, still fuse?

**You.** During encoding, want to know if sensor data has usable signal. Kill: prelim LM baseline that takes encoded sensors and answers basic questions (mimic production). If results extremely poor (unrelated answers, cannot extract basic information), go back and check data/encoder; if those are correct, kill. After month two. To test sensors used: zero or remove the stream, or shuffle; alternatively a toy train/test QA that specifically uses sensor info. If that test fails, will not fuse — go back and improve the encoder.

**Q3.** Frozen LM + daily summaries is cheaper. Month-one number. n=20, colleague says OOD + disclaimer, keep the plan.

**You.** Do not agree. Known issue in TS community: LMs do not understand time series; appropriate encoding and fusion is an open problem. Modeling encoder and fusion is what might make a frozen LM work or not. Several studies: frozen LMs reason poorly (close to chance) on TS. In tests with encoder and basic system, want above chance; specifically 5% abs above chance as a reasonable first PoC to build on. For the 20 people: extend that study; expert review on as many people as possible; want population statistics vs general pop; want prevalence of events in that subgroup. Will **not** treat as OOD, will **not** ship yet. Continue the six-month plan while **holding production** until a more thorough study is available.

**Q4.** 5% above chance of what, on which task, how many people? What in months 3–6 do you cut while expert n is still 20? **Unanswered.**

### Spoken restitch — program (worst miss)

“I bet on a language layer over Watch sensors, not a silent diagnostic notification. Month one is not a data lake: I take a small participant-disjoint set, a frozen non-LM readout of a cheap encoder (or even summary features) on the same basic questions I would ship, and a frozen LM with **no** sensors as the prior baseline. Chance is that no-sensor LM, or random among the actual choices — I write the number down. If the encoder readout is at chance, I do not spend month two on fusion. If the no-sensor LM is already good, fusion is not the product. Shuffle/drop of the sensor stream has to move the answers. n=20 expert misses is uncertainty: I do not disclaimer-ship, I do not call it OOD, I hold production and I cut month-six prelim until n is a decision. Encoding can still be the research bet — it does not license a six-month waterfall before a kill.”

---

## Day complete (Sun 9/6)

All five Tuesday slots mocked 2026-09-06. File is the day’s log.

---

## Mon 9/7 — Vincent mini-loop (~15 min, stopped)

**When:** Mon 2026-09-07 · technical leadership & system thinking  
**Slot:** Tue 9/8 4:05 PDT (last of five)  
**Sheet:** [`2026-08-27_onsite-vincent.md`](2026-08-27_onsite-vincent.md)

Stopped on request mid-Q4 (personalized “harder than typical”; majority-vote over history). Treat Q4 as **unanswered** in the room. Score for the completed segment: **~6.5/10**.

**You** lines close to spoken. Critique separate.

### Scorecard

| | |
|--|--|
| Opening product questions | **Hit.** Output, population, data, labels, prediction time, error costs — right instinct. |
| Constraint update | **Partial.** Four weeks → use existing data, skip collection. Then a week-by-week pipeline (labels → encoders → XGBoost → eval). |
| Minimum viable experiment | **Miss.** “Activity efficient?” defined from HR; XGBoost vs 50% random; 60% = go. Circular target, weak baseline, arbitrary gate. |
| Labels | **Miss.** SSL / generative “improve labels” does not create ground truth. Sparse labels as proxy was the recovery; the techniques stay for representations / pseudo-labels, not Y. |
| Population | **Partial.** All Watch wearers is the product aspiration. First experimental cohort should be a well-defined activity/slice where labels and sensor quality are strongest. |
| Accepting challenges | **Hit.** Did not defend every first choice. |
| Q4 (harder than typical) | **Unanswered.** Stopped at majority vote over history + feedback. |

**Strongest:** define the product before the architecture; simplify when the clock is four weeks; want signal before a multimodal LM.  
**Tuesday risk:** “what pipeline can I finish in four weeks?” instead of “what uncertainty do I kill?” Random is not the baseline. Do not define Y from the same HR you feed the model.

### Exchanges

**Q1.** Watch sensors → personalized explanations/answers about recent health and fitness. Research scientist: technically viable, what to build. From the beginning.

**You.** Define the product first: output, population, data, labels, prediction time and horizon, cost of errors. Wellness chatbot, text out. Population as wide as possible (all Watch wearers, ages, BMI). Data: PPG, IMU, derived HR, plus user text (menu or free). Predict when the user asks; recent 30–60 min covering walk/run/cycle; horizon a few hours. Labels via self-report; FP vs FN underspecified. Viability via a one-month program: collect, clean, basic multimodal (sensor encoders + pretrained LM). Objective NTP. Phase goal: does the LM perceive sensor values/segments, and can it do basic reasoning. Basic Q&A for that phase.

**Hit + miss.** Opening questions are the lock. Then you filled every slot (all-comers, 30–60 min, one-month collect+model) before a central uncertainty. Eventual population ≠ first cohort.

**Q2.** Historical Watch data exists; labels sparse/inconsistent. Product wants viability evidence in **four weeks**, not a collection campaign. Narrow the problem. Minimum viable experiment.

**You.** Use available data; skip collection. A few days improving labels (manual, SSL, or generative). Then a week of basic encoders. Then a week of XGBoost on sensor features for classification of what you want to extract. Final week eval. Goal: convince there is signal a baseline can extract. Results 15–25% better than random.

**Miss.** Four weeks became a waterfall (labels → encoders → XGBoost → eval). SSL/gen do not mint ground truth. Random + 15–25% is not a decision criterion. The question was the cheapest falsifier of the biggest uncertainty, not a four-week build plan.

**Q3.** SSL/gen are not ground truth for whether the sensor contains the thing you care about. “15–25% better than random” — better on what, why is random the baseline? Single narrow capability, baseline, specific yes vs stop.

**You.** Agreed, far from ideal. Would also collect better self-report labels; given time, treat sparse labels as best proxy; still improve via manual + those techniques. Random is right because it is “not using the signal”; if XGBoost beats it, signal exists and a more complex model can do better. Narrow task: “Was the activity efficient or not?” Binary. Decide true/false from whether HR follows the known pattern for that activity. Baseline still features + XGBoost vs 50% random. 60%+ at four weeks → invest.

**Miss.** Three stacked: (1) Y from HR + HR features = circular; (2) random is a weak lower bound — beat heuristic / population threshold / personalized history / logistic / XGBoost; the LM has to earn complexity; (3) 60% is arbitrary. “Better than not using the signal” does not license the multimodal language stack.

**Q4.** “Activity efficient” is a bad first capability (circular). 60% vs 50% is uninformative if a heuristic already gets 58%. New question: **“Did this workout look harder than what is typical for this user?”** Historical Watch per user, sparse explicit feedback. Target, simplest meaningful baseline, evidence you are not just rediscovering HR thresholds.

**You.** Baseline a majority vote over historical information and the feedback…

**Unanswered.** Stopped here.

### Spoken restitch — Q4 (unanswered in the room)

“Harder than typical for this user is a personalized deviation, not a global class. I build a per-user baseline from historical workouts of the same type: expected physiological response given workload (pace/power, HR, duration, recovery) and context. The target is whether this workout’s response sits unusually high on *that user’s* distribution. First model is not deep: standardized residuals, or a small regression of expected HR from workload and history. Sparse explicit ‘felt unusually hard’ is an **external** check, not the HR-derived label. Success is not beat-random. I compare a population threshold, the user’s historical mean, and the simple personalized model. I want a richer sensor representation to improve held-out **future-workout** prediction of the feedback signal, with intervals and consistency across workout types. If the simple personalized baseline matches the complex model, I do not need the multimodal language stack for this capability. If richer features move the external feedback and the gain survives future-workout eval, I have evidence beyond a fixed HR cutoff. If feedback is too sparse I narrow the claim: I can detect personalized physiological deviation; I will not claim subjective difficulty until an independent label ties that deviation to perceived hardness.”

### Spoken restitch — four-week go/no-go (worst miss)

“Given four weeks I am not prototyping the chatbot. The uncertainty is: do Watch signals contain enough **personalized** information to support answers beyond summaries and heuristics? I pick one narrow capability with the best independent label, freeze a small participant-disjoint eval set, and put heuristic and feature baselines on the board in the first days. Then I test whether learned sensor representations add anything, especially where the simple baseline fails. If they don’t, I stop before the language model. If they do, multimodal fusion is worth investigating. The go number is on the task metric and product-relevant slices, not an arbitrary lift over chance. If the premise fails in week one, I stop — I do not discover that in week four.”

### Corrections to keep

- **Uncertainty, not pipeline.** “Evidence in four weeks” → what must I eliminate, cheapest experiment whose result changes the decision. Not week-1 labels / week-2 encoders / week-3 XGBoost / week-4 eval.
- **Independent Y.** If the label is an HR rule, beating that rule with HR features is tautology. Manual labels only help if the annotator can actually see the target.
- **Meaningful baseline.** Heuristic, population threshold, personalized history, logistic, XGBoost, then encoder. Random is the floor, not the competitor. The sophisticated model earns its cost.
- **Gate from the decision.** “What result would change ship / kill / reformulate?” not “10 pp above chance.”
- **Cohort vs product pop.** Broad Watch wearers is the product. First falsification is a slice where labels and sensors are strongest; if it fails there, broadening will not save it.
- **SSL/gen.** Representations, pseudo-labels, denoising, data efficiency — not ground truth for an unobserved outcome.

### Framework (say this shape)

Product decision → central uncertainty → cheapest falsifier → simple meaningful baseline → success/kill criterion → only then add complexity.

### One-line for Tuesday

Not “what can I build?” — “what is the most important uncertainty, and what is the cheapest experiment whose result would actually change my decision?”

---

## Mon 9/7 — Haraldur mini-loop (~30 min, stopped)

**When:** Mon 2026-09-07 · health domain & applied ML judgment  
**Slot:** Tue 9/8 3:05 PDT  
**Sheet:** [`2026-08-27_onsite-haraldur.md`](2026-08-27_onsite-haraldur.md)

Stopped on request before answering Q8 (missingness vs population shift vs informative missingness). Treat Q8 as **unanswered**. Score for the completed segment: **~7/10** (better than the Vincent mini-loop).

**You** lines close to spoken. Critique separate.

### Scorecard

| | |
|--|--|
| Opening framework | **Hit.** Product → pop → data → labels → time/horizon → error costs → constraints. Logistic + XGBoost first. |
| Adapt timescale | **Hit.** Dropped monthly when told illness is days, not a month. |
| PPV arithmetic | **Hit.** 1% / 92% Se / 94% Sp → ~1/8 (true ≈ 13.4% = 1/7.5). |
| Eval vocabulary | **Hit.** Se/Sp/PPV, prevalence, calibration, CIs, participant-disjoint. |
| Labels | **Miss.** Widen window around self-report is a robustness *experiment*, not the label. Chose window from sensitivity. EHR as “ground truth.” Usage frequency → biological window. |
| Observation window | **Miss.** 30–60 min for 24h respiratory-onset is too short vs 24–72h + personal baseline. |
| Threshold vs product | **Miss.** Locked 95% Se / would not change τ at PPV ≈ 13%. Disclaimer instead of reformulating the claim. |
| Se/Sp + PPV | **Slip.** Cannot hold Se, Sp, and prevalence fixed and independently raise PPV. Need a better frontier (e.g. Sp at 90% Se). |
| Q8 | **Unanswered.** |

**Strongest:** framing; abandon monthly; 1/8 PPV; Se/Sp/PPV/calibration as the eval set.  
**Tuesday risk:** promoting self-report/EHR to Y; picking the endpoint from model Se; “I will not change the threshold.”

### Exchanges

**Q1.** Watch signals, early respiratory illness before the user notices. HR, activity, sleep, extra streams, longitudinal, imperfect labels. Formulate before a model.

**You.** Product, pop, data, labels, prediction time, horizon, error costs, production. Notify high risk. Broad pop later; first age bands with real prevalence. Historical sensors. Labels weak: link EHR, expert manual. Predict monthly, 12 alerts, horizon one month. FP cheaper than FN (follow-up test vs never addressed). Eval: Se 95%, Sp 90%, precision depends on prevalence. Baselines: logistic, features + XGBoost.

**Hit + miss.** Framework and baselines lock. Monthly is the wrong timescale for “before they notice.” FP-cheap is the Sunday miss again — a health notification is not free because a test exists.

**Q2.** Illness develops faster; continuous Watch; useful warning 1–2 days before onset. Reformulate time, window, horizon, label. No EHR for most; noisy self-report.

**You.** Multiple predictions per day if cheap. Notify only positives. Observation last 30–60 min. Predict at window end. Horizon next 24h. Self-report as internal eval; scarce EHR as external validation.

**Partial.** Timescale update is correct. 30–60 min is likely too short for resting-HR / sleep / activity / recovery deviation. Self-report ≠ internal gold; EHR ≠ automatic external gold.

**Q3.** Self-report delayed 0–3 days or never. Model predicts onset in next 24h. How does noise affect train/eval? Risk of learning reporting, not physiology.

**You.** Noise → spurious relations. Never-reporters: not much to do. For lagged reports: shift the positive label forward and backward so onset spans multiple days.

**Partial.** Window expansion is a robustness test. It is not automatically the right Y. Never-report is informative missingness / selection, not “nothing to do.”

**Q4.** Three windows: onset day only; −2/+1; −3/+3. Which is defensible? How does the small EHR-linked subset tell biology vs fitting self-report?

**You.** Choose the window from sensitivity scores and CIs. Then validate with EHR as ground truth: compare actual event times to the window; estimate how common the shift is.

**Miss.** Do not choose Y from which definition makes Se best. That optimizes the endpoint around the model. EHR is a clinical reference standard on a **selected** 5% (care-seeking), not ground truth for all Watch users.

**Q5.** Don’t pick the window from model Se. EHR-linked is 5% and selected. How to use it without treating it as perfect GT for everybody? What evidence that you detect **pre**-illness physiology, not post-onset physiology before they report?

**You.** From EHR, average Δt event→report as the min window for heavy Watch users. Widen with lower wear frequency up to −3/+1 days.

**Miss.** Wear frequency can correlate with reporting, health, age, SES, completeness. It does not tell you when biology started. Do not map usage → label window. Pre vs post onset needs an independent clock (care-seeking lag characterization + clinically plausible progression + sensitivity analysis), not a usage-conditioned window.

**Q6.** Retrospective participant-disjoint: Se 92%, Sp 94%, AUROC 0.96. Cohort prevalence 8%; deploy prevalence ~1% at a prediction point. Ready for prospective pilot? Extra numbers.

**You.** Also prevalence, precision, calibration — whether the operating point is useful.

**Hit.** Right extra numbers. AUROC on an 8% set does not license a 1% product.

**Q7.** At 1% with 92/94, what PPV? If most alerts are FP: change threshold, product, or model? How decide.

**You.** PPV ≈ 1/8. Severe illness, FN costly, would **not** change the threshold. Change product with a disclaimer that some notified users don’t have it, if testing is cheap/non-invasive; else wellness notification. Change the model if another baseline keeps Se/Sp inside 95% CIs and raises PPV a lot.

**Hit + miss.** 1/8 is excellent (10k points: 100 sick, TP 92, FP ≈ 594, PPV ≈ 13.4%). Then locked τ too early. Disclaimer does not buy utility. Sequence is threshold (is there a useful point on this curve?) → model (does a new frontier move Sp at fixed Se?) → product/pop/claim/kill. PPV is determined by Se, Sp, prevalence — you cannot hold Se/Sp and lift PPV.

**Q8.** Prospective: complete wear good; intermittent wear low Se and worse calibration; intermittent wear more common in some ages. Missing-data vs population-shift vs informative missingness? What before changing the model. **Unanswered.**

### Spoken restitch — labels / window (worst miss)

“I would not infer biological onset from self-report or EHR. Both are imperfect observations: biology → detectable physiology → symptoms → report → clinical record. Before a window I characterize timing disagreement on the linked subset and use domain knowledge of progression. Then I run sensitivity analyses across plausible windows. If the conclusion hinges on an arbitrary window, the endpoint is not identified. I do not pick the window that maximizes sensitivity. EHR is a clinical reference on a selected care-seeking slice, not GT for all Watch wearers, and wear frequency is not a biological clock.”

### Spoken restitch — PPV / threshold (second miss)

“At 1% with 92% Se and 94% Sp, PPV is about 1 in 8. That is not a ship number for a ‘you may be getting ill’ claim. First I look at the existing curve: is there a point with acceptable alert burden if I give a little Se. Then I ask whether a better model moves specificity at a fixed Se, or Se at a fixed alerts/user/week. If the frontier still cannot support the claim, I narrow the population, soften to a baseline-change wellness nudge, or kill. I do not freeze 95% Se, and I do not fix poor PPV with a disclaimer.”

### Spoken restitch — Q8 if it comes back

“I would not change the model first. Stratify jointly by wear completeness and age so they are not confounded. On complete-data users, synthetically mask using intermittent missingness patterns — if performance collapses, information loss explains part of the gap. Then compare age at matched missingness; a remaining gap is shift or another subgroup failure. Test whether the missingness pattern itself predicts the outcome or reporting — if yes, missingness is informative. Only then: missingness features / dropout, subgroup calibration, or different product behavior when data quality is insufficient.”

### Corrections to keep

- **Y is latent.** Self-report ≠ symptom onset ≠ biological onset ≠ EHR timestamp (care-seeking / test / coded diagnosis).
- **Don’t optimize the endpoint around Se.** Independent definition, then train, then eval. Alternate windows = sensitivity analysis.
- **EHR ≠ GT for everybody.** Selected 5%; use to characterize disagreement, not to copy a window onto all wearers.
- **Wear time ≠ biology.** Do not set the label window from usage frequency.
- **Window follows the phenomenon.** 24–72h + personal baseline is more plausible than 30–60 min for this claim.
- **Threshold → model → product.** Then pop / claim / kill. Disclaimer is not a product.
- **PPV is not a free knob** given Se, Sp, and prevalence. Compare Sp@Se or Se@alert-rate.

### Framework (say this shape)

Health claim → what exactly is Y → how is Y observed → errors/biases in that observation → information at prediction time → who must generalize → operating point that supports the product → what happens to a real user when wrong.

### One-line for Tuesday

What exactly is the health claim, how do I observe the outcome, and does my evaluation support the decision the product will actually make?

---

## Day complete (through Mon 9/7)

Sunday S1–S5 logged. Monday Vincent + Haraldur mini-loops logged above. Remaining Monday: retrieval + other mini-loop slots + stop — not another five-hour loop.

---
