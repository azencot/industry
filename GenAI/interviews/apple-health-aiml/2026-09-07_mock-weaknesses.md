# Last correction sheet — mock weaknesses (Mon 2026-09-07)

**Live:** Tue 2026-09-08.  
**Mocks:** [`2026-09-06_tuesday-full-mock.md`](2026-09-06_tuesday-full-mock.md)  
**Hub:** [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)

These are mostly **not** knowledge gaps. Recurring pattern: reason to the right answer, but the **first formulation** is sometimes too strong, too specific, or optimizes the wrong quantity.

**Tuesday goal:** slow down the first 20 seconds.

Frame → identify uncertainty → then commit.

---

## 1. Vincent — don’t build a pipeline before the decision

**Weakness.** Four weeks became: week 1 labels → week 2 encoder → week 3 XGBoost → week 4 eval. Risk: discover in week 4 that the premise was wrong.

**Fix.** Biggest uncertainty first, then cheapest falsifier → simple baseline → success/kill → only then complexity.

**Line.** “I’m not trying to prototype the whole system in four weeks. I’m trying to eliminate the highest-risk assumption.”

---

## 2. Vincent — random is often too weak a baseline

**Weakness.** Compared to random/chance to decide whether a technology was useful.

**Why.** Chance says whether any signal exists. It does not say the complicated model earns its complexity.

**Fix.** Compare to the simplest credible alternative: heuristic, personalized history, logistic, XGBoost, simple unimodal.

**Question.** “What would we actually deploy if we did **not** build my model?”

---

## 3. Vincent — don’t invent arbitrary go thresholds

**Weakness.** “60% vs 50% random means go.” “15–25% improvement means viable.”

**Fix.** Success criteria follow the product/research decision: what improvement changes the decision, where the simple baseline fails, critical slices, complexity/latency cost. Do not pick a number because it sounds substantial.

---

## 4. Vincent — avoid waterfall thinking

**Weakness.** Data → encoder → fusion → eval → production as sequential months.

**Fix.** Cheap baseline immediately → falsify → add a component → evaluate → promote/kill → scale. Every expensive step needs a reason to exist.

---

## 5. Jonathan — claim first, architecture second

**Weakness.** Opens with Qwen + DINO + dual tower + Stage A/B instead of the scientific question.

**Fix.** First 30 s: problem → hypothesis → what would falsify it. Then architecture.

**Line.** “The architecture was how I tested the hypothesis; it wasn’t the scientific claim.”

---

## 6. Jonathan — observation ≠ mechanism

**Weakness.** Dual > chart → complementary. Method wins with scarce data → representation causes data efficiency.

**Fix.** Separate observation from interpretation. “We observe dual > chart under matched training. Complementary information is one explanation. Extra capacity/tokens/encoder interaction are alternatives.” Then name the discriminating experiment.

---

## 7. Jonathan — post-hoc diagnosis is not prior evidence

**Weakness.** After TSRBench failed: domain knowledge, event-count mismatch, format mismatch — used as explanations.

**Fix.** “I did not pre-specify those.” The pre-specified hypothesis failed. The audit generated **new** hypotheses that now need confirmation.

**Line.** “That audit is a diagnosis, not evidence I had before the result.”

---

## 8. Jonathan — allow the ugly interpretation

**Weakness.** TR 26.9% vs ~25% chance; resisted “maybe guessing on this slice.”

**Fix.** Allow: “On this evaluation, the result is consistent with near-chance behavior.” Then investigate why. Do not defend the model emotionally.

---

## 9. Yujie — be precise about compression

**Weakness.** “1 s patch destroys a 200 ms event” was too strong as a critique of *me*, but wording can sound like fine-tuning restores temporal resolution. That is **not** the claim.

**Correct claim.** For classification, the global model may not need raw 200 ms localization. A high-rate **local encoder** can see the event before compression and map it to a semantic latent (“movement occurred”).

Pipeline: raw high-rate → local high-resolution encoder → learned semantic/event features → temporal compression → long-context model.

**Line.** “I don’t need the global model to reconstruct the 50 Hz timeline. I need the local encoder to preserve a sufficient statistic for the downstream task.”

---

## 10. Yujie — task-required resolution determines design

Distinguish **sampling** resolution, **representation** resolution, **task-required** resolution.

30-min activity classification: a short event can be compressed after detection. Event localization / count / morphology / two events 200 ms apart: may need a finer pathway.

**Line.** “If the task changes from classification to localization, my compression strategy must change too.”

---

## 11. Yujie — physical time ≠ token position

**Weakness.** Timestamps named, not always used through the design.

A PPG token may summarize 100 ms; HR 1 s; sleep 30 s. Token index spacing does **not** imply equal physical time.

Use native-rate encoding + physical timestamp / Δt + fusion after compression. Do not upsample everything to the fastest clock.

---

## 12. Chung-Cheng — calculate global batch out loud

**Weakness.** microbatch 2 × world 64 × accum 4 said as **256**. Correct: **512**.

**Fix.** Always say `global_batch = microbatch × world × accum`, then calculate slowly.

Why it matters: world size can change global batch, optimizer updates, warmup-in-tokens, LR schedule, generalization.

---

## 13. Chung-Cheng — diagnose before naming technology

**Weakness.** Not severe, but “OOM → FSDP” / “slow → more GPUs” gets punished.

OOM: P / G / O / A? Slow: compute / comm / data / sync? Unstable: data / opt / numerics / distributed state? Then intervene.

**Line.** “I want to know what resource is limiting me before choosing the parallelism strategy.”

---

## 14. Haraldur — label source ≠ true outcome

Biggest health-judgment issue. Do not casually equate self-report, EHR, symptom onset, biological onset.

Latent health event → imperfect observable reference standards. EHR may be care-seeking / diagnosis time / coding. Self-report may be perceived symptoms / delay / reporting behavior.

**Line.** “I would treat both self-report and EHR as imperfect measurements of the underlying endpoint and characterize their disagreement.”

---

## 15. Haraldur — don’t choose the label that makes the model look best

**Weakness.** ±1 / ±3 day window chosen primarily from model sensitivity. That lets performance define ground truth.

**Fix.** Define a plausible endpoint independently (domain knowledge, measurement properties, reference-standard analysis). Alternate windows = **sensitivity analysis**.

**Line.** “If the conclusion changes dramatically across plausible label definitions, that’s itself an important uncertainty.”

---

## 16. Haraldur — threshold → model → product

**Weakness.** Low PPV → “I don’t want to change the threshold.” Don’t lock τ early.

1. **Threshold** — useful point on the current curve?  
2. **Model** — can another model move the frontier?  
3. **Product / population** — change intervention, narrow pop, change claim, or kill.

**Line.** “I’d first ask whether the existing model has a useful operating point before rebuilding the model or changing the product.”

---

## 17. Haraldur — PPV ≠ alert burden

PPV: when I alert, how often am I right?  
Alert rate: how often do I interrupt the user?

Same PPV, very different interrupt frequency. Wearable: alerts / user / week (or false alerts / user / week). Often more product-relevant than AUROC.

---

## 18. Haraldur — don’t call false positives “cheap”

Better: “The relative cost of a false positive is lower than a false negative in this workflow, **assuming** confirmation is cheap and non-invasive.”

FP still creates anxiety, follow-up, alert fatigue, disengagement. A notification users learn to ignore is a failed product.

---

## 19. Across all five — don’t resolve uncertainty too fast

Pressure to pick a label / threshold / architecture / patch size / success criterion immediately.

Senior: “That depends on X, and X is currently the uncertainty I would resolve.” Then design the experiment. Uncertainty is not weakness. Unstructured uncertainty is.

---

## 20. Across all five — first-sentence discipline

Classify the question before answering.

| Person | First sentence |
|--------|----------------|
| Chung-Cheng | What is the bottleneck? |
| Yujie | What information does the task require? |
| Jonathan | What exactly is the claim? |
| Haraldur | What health decision and endpoint are we evaluating? |
| Vincent | What decision/uncertainty should this program resolve? |

Then answer.

---

## Five mantras

| Person | Mantra |
|--------|--------|
| Jonathan | Observation first. Mechanism second. |
| Yujie | Preserve the information the task needs before compressing. |
| Chung-Cheng | Diagnose the bottleneck before choosing the systems tool. |
| Haraldur | Define the endpoint and operating decision before trusting the metric. |
| Vincent | Find the highest-risk assumption and falsify it cheaply. |

---

## Final 30–60 minutes (then stop)

No more knowledge. Pause before committing; define the actual question; separate observation from explanation; refuse unjustified numbers; name the cheapest discriminating experiment.

A strong answer can sound like: first hypothesis X because Y; Z is an important alternative; distinguish with this experiment; that result decides proceed vs change direction.

### Option A — 30 min

1. **10 min** — read this sheet slowly.  
2. **15 min** — five answers aloud, one per person:  
   - Jonathan: strongest claim of the multimodal work?  
   - Yujie: how can a 200 ms event survive compression?  
   - Chung-Cheng: 64 GPUs worsen validation. What changed?  
   - Haraldur: self-report noisy, EHR selected. What is Y?  
   - Vincent: four weeks. What do you do?  
3. **5 min** — stop.

### Option B — 60 min

1. **15 min** — read this sheet.  
2. **30 min** — five questions × ~6 min. Each: first sentence → framework → answer → one alternative → one experiment.  
3. **10 min** — behavioral cheat strip: ImagenTime disagreement; wrong hypothesis; TSRBench ambiguity; TR kill; Bosch cross-functional. [`2026-08-30_behavioral-stories.md`](2026-08-30_behavioral-stories.md).  
4. **5 min** — one page: Jonathan → **claim**; Yujie → **information**; Chung-Cheng → **bottleneck**; Haraldur → **endpoint**; Vincent → **uncertainty**.  
5. Stop.

---
