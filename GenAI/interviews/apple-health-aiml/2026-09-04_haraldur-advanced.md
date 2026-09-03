# Friday — Haraldur advanced (second cycle)

**When:** Fri 2026-09-04 · Block 3 (60 min) + Block 4 (45 min)  
**Plan:** [`2026-09-03_four-day-final-plan.md`](2026-09-03_four-day-final-plan.md)  
**Do not reread:** Lesson 1 metrics, the PPV primer, or “DL will win.” You already have sensitivity/specificity/PPV, prevalence, calibration, participant splits, prospective vs retrospective.

This file adds three **higher-level** failure classes that look like model failure and often are not.

---

## How to use

1. Read **Learning A–C**. Speak the lock.  
2. **Cases 1–4** with notes closed. Force a label: model failure / data shift / label shift / selection bias / workflow. Competing explanations required.  
3. Then **Keys**.

If you start with AUROC, interrupt yourself: *what decision, in whom, against what reference.*

---

# Learning (60 min)

## A. Label quality / reference standard

Health labels are **not** ground truth. They are a measurement process.

| Label | What it usually is | Typical failure |
|-------|--------------------|-----------------|
| Self-report | Symptom, diagnosis memory, logging | Under-report, over-report, missingness tied to engagement |
| Diagnosis / ICD | Care that happened in a system | Care-seeking, coding, access — not disease |
| Clinician annotation | Expert on a snapshot (ECG strip, note) | Inter-rater disagreement; spectrum of who gets read |
| Device confirmation (e.g. patch ECG) | A better sensor, still imperfect | Only collected on some people (see B) |
| Proxy | Hospitalization, med start, “AF related visit” | Downstream of the care system |

**Label sensitivity:** P(labeled + | true +).  
**Label specificity:** P(labeled − | true −).

If many true positives never get a code, the “negative” class is contaminated. The model can look worse **or** better than it is, depending on whether it agrees with the code or with biology.

Questions to ask before you trust a number:

- What is the reference? Who assigned it?  
- Could the negative class contain undiagnosed positives?  
- Does label quality **differ across populations** (age, BMI, language, care access)? If yes, a “fairness gap” may be a **label gap**.  
- Apparent ceiling: you cannot beat a noisy label on that label. You can still be useful on a **better** reference collected on a subset.

**Lock:** *I treat the label as a measurement with Se/Sp, not as disease. If those differ by group, I will not interpret an AUROC gap as a sensor-model gap until I have checked the reference.*

---

## B. Selection bias

Who is in the dataset is a pipeline, not a coincidence.

Ask four filters:

1. **Who wears the device?** Engagement, affluence, health interest, occupational constraints, skin / fit.  
2. **Who has labels?** EHR linkage, study consent, completed onboarding.  
3. **Who gets a confirmatory test?** Often: symptomatic, already flagged, already in cardiology.  
4. **Who completes follow-up?** Sicker people may drop **or** stay in care; both distort.

Classic trap: only symptomatic users obtain confirmatory ECG. Then:

- Labeled data ≠ deployment population (mostly asymptomatic screening).  
- Prevalence in the labeled set is inflated.  
- PPV in deployment collapses even if Se/Sp on the labeled distribution were honest.  
- The model may learn **“looks like someone who got an ECG”** (care-seeking, button-press, nighttime wear) rather than arrhythmia.

This is **verification bias** / selection, not “the model overfit the PPG encoder.”

**Lock:** *I draw the funnel: wear → link → label → follow-up. If a confirmatory test is downstream of symptoms or of the model itself, I do not treat that labeled set as the deployment population.*

---

## C. Decision utility

AUROC / PPV are not the product.

The model sits in a **workflow**: alert → user sees it → maybe a confirmatory test → maybe a referral → capacity.

Speak in **counts**, not only rates:

| Quantity | Why |
|----------|-----|
| Alerts / user / week | Burden; ignore-rate; sleep disruption |
| PPV at the operating point | Among alerts, how many are true |
| Number needed to test (≈ 1/PPV, roughly) | Confirmatory tests per true case |
| Extra true cases found vs extra false referrals | Capacity of the downstream clinic / ECG patch program |
| Time-to-detection vs time-to-action | A 30s lead is not a 30 min lead |

A model can have stable Se/Sp and still be **useless** if alerts explode, or **harmful** if false referrals swamp the true ones.

Operating point is a **policy** choice (who is inconvenienced, who is missed), not a default 0.5 threshold.

**Lock:** *I will not ship on AUROC. I want alerts per user-week, PPV at a declared point, downstream tests generated, and whether the lead time matches the intervention. If those fail, the metric success was not a product success.*

---

# Cases (45 min) — do not read keys yet

For each: what could be true, how you tell them apart, what you would **not** conclude from the headline metric.

**Case 1.** Your model performs worse prospectively than retrospectively.

**Case 2.** PPV drops dramatically after deployment even though sensitivity and specificity appear stable.

**Case 3.** A subgroup has worse results, but signal quality is also worse.

**Case 4.** Your model predicts clinician diagnosis extremely well. How do you know it predicts **disease** rather than **care-seeking behavior**?

Force a distinction: model failure · data shift · label shift · selection bias · workflow effects. Often more than one.

---

# Keys (after speaking)

## Case 1 — Prospective worse than retrospective

**Do not conclude:** “the architecture is wrong” as the first line.

**Competing explanations**

| Class | Mechanism |
|-------|-----------|
| Selection | Retrospective set is a convenient linked cohort; prospective is all comers |
| Label shift | Retrospective labels from chart review; prospective from a different process (or none) |
| Data shift | New firmware, season, wear behavior, missingness that was imputed in the old extract |
| Leakage gone | Retrospective had future information / same-episode ECG in features |
| Workflow | Prospective users react to the product (wear more, or ignore sensors) |
| Model | True overfitting to the old extract — possible, last after the above |

**Discriminate**

- Same **frozen** model, same **label protocol**, on a time-split of the *old* extract vs the new stream. If time-split already dropped, it was shift/leakage in historical data. If only the new stream drops, it is deployment shift.  
- Compare missingness, firmware, prevalence, who got labels.  
- Audit a sample of prospective “errors” against a **held gold** (patch ECG), not against the operational label.

**Intervene:** do not immediately retrain on mixed prospective labels (that can bake in the new workflow). Shadow mode, protocol-matched eval, then decide whether to adapt.

**Tradeoff:** waiting for prospective gold is slow; adapting on operational labels is fast and often learns the clinic, not the disease.

---

## Case 2 — PPV collapse, Se/Sp “stable”

**First identity (you already know):**  
PPV depends on **prevalence** (and on how the threshold is applied). Stable Se/Sp **on the labeled test set** plus lower deployment prevalence → PPV must fall.

**That is not the only story.**

| Class | Mechanism |
|-------|-----------|
| Prevalence | Screening population ≪ study prevalence |
| Selection | Study required symptoms / prior AF; deployment is everyone |
| Threshold / workflow | Deployment uses a different operating point, or alerts fire more often (multiple windows per day) |
| Label in production | “True” in production is a sparser confirmation (only some alerts get ECG) — **ascertainment** makes PPV look worse or better |
| Calibration / score shift | Se/Sp were computed after choosing a threshold on the old score distribution; scores shifted, so the *same numeric threshold* is not the same Se/Sp |

**Discriminate**

- Recompute PPV from **declared Se/Sp and deployment prevalence** (Bayes). If that already matches the drop, you do not need a new architecture.  
- Check whether production Se/Sp were actually measured on a gold subset or **assumed** from the retrospective test set.  
- Count alerts/user/week, not only PPV.

**Conclude:** this is often **expected epidemiology + selection**, not a silent model bug. You still may **not ship** if PPV at real prevalence is unusable — that is a **utility** failure, which can be real even when the ROC is honest.

**Miss if:** you said “the model overfit” without prevalence, or you said “just raise the threshold” without alerts/user/week and missed cases.

---

## Case 3 — Subgroup worse, signal quality also worse

**Do not conclude fairness-as-weights, and do not conclude “just a sensor problem,” until you split the two.**

Three hypotheses:

1. **Measurement:** PPG quality (perfusion, motion, skin, fit, BMI-related optical path) is worse → *any* method that uses that channel will drop.  
2. **Label:** the subgroup has noisier or differently ascertained labels (older adults: more undiagnosed AF *and* more coded AF).  
3. **Model:** the representation overfits the majority’s morphology; quality-matched, the gap remains.

**Discriminate (this is the hour)**

- Stratify by a **quality metric** (SNR, missingness, motion) first, then by subgroup **within** quality bins.  
  - Gap **disappears** inside bins → mostly measurement. Fix device, wear, or refuse to score low-quality windows (with a coverage cost).  
  - Gap **remains** inside bins → model or label. Then check label Se/Sp by group if you can.  
- Baseline: **same-split XGBoost / GBDT** on quality features + heart-rate stats. If GBDT has the same gap, the deep model is not uniquely unfair — the **signal may not be there**.  
- Do not reweight the loss until this table exists. Reweighting a bad label or a missing optical signal does not create information.

**Tradeoff:** dropping low-quality windows improves reported metrics and can **deny** the subgroup the product. Coverage is part of the fairness claim. Say that out loud.

---

## Case 4 — Predicts clinician diagnosis extremely well. Disease or care-seeking?

**This is the trap.** Diagnosis is a **behavior of the health system**, not a wearable ground truth.

The model can nail ICD codes by learning:

- Who wears the Watch at night and logs symptoms  
- Who has primary care / who lives near a hospital  
- Age, BMI, already on beta blockers (if those leak into features or proxies)  
- “Looks like the kind of person we work up”

That can yield AUROC 0.95 vs diagnosis and still fail vs **patch-ECG AF**.

**Discriminate**

- Evaluate against a **protocol-collected reference** that does not require the patient to seek care (study patch, systematic sampling), on people who **would not otherwise have been diagnosed**.  
- **Time:** does the model fire **before** the first diagnosis, or only around visits? Pre-diagnostic lead is weaker evidence of care-seeking leakage; same-day / post-visit is suspicious.  
- **Ablate** care-proximal features (visit counts, prior codes) if they exist. If performance collapses, you were predicting the clinic.  
- **Negative controls:** outcomes that should *not* be in the PPG (e.g. a billing artifact). If you predict those too, you have system leakage.

**You do not know it predicts disease until a reference that is not the care process says so.**

**Lock:** *High AUROC vs diagnosis is a hypothesis that I predicted disease. The experiment that would kill it is a systematically collected physiologic reference, in people who did not self-select into a workup.*

---

## Self-score

- [ ] Named at least two classes before “train a bigger model”  
- [ ] Case 2 used prevalence / Bayes, not a new encoder  
- [ ] Case 3 stratified quality **then** group, and mentioned coverage  
- [ ] Case 4 refused to treat ICD as disease  
- [ ] At least one case ended in a **utility** sentence (alerts, NNT, who is denied)
