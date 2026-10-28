# Siemens loop — prep plan — revised 28 Oct 2026

Replaces the one-domain-per-day plan written earlier the same day.

**Loop:** Tue 3 Nov 2026, 1:00–4:00 PM PST. Wed 4 Nov, 4:00–7:00 AM Thailand. Bing Xiang, Vivek Govindan, Ramesh Nallapati. No hour is assigned to breadth, depth, or system design. Coding is still unconfirmed.
**Window:** 28 Oct through 2 Nov. About 5–6 hours a day. 2 Nov is consolidation. No new topic that day.
**Logs:** [`mocks.md`](mocks.md). Recall: [`2026-10-28_breadth-recall.md`](2026-10-28_breadth-recall.md). Stories: [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md).

Each day rotates depth, breadth, and system design. Do not give a whole day to one domain. Shift time toward the weaker domain when a mock says so.

| Block | Time |
|-------|------|
| ML depth | 75 min |
| ML breadth | 75 min |
| ML system design | 90 min |
| Targeted redo | 45 min |
| Leadership | 20 min |
| Log | 15 min |

Rotate which technical block comes last, so the same domain is not always the tired one. System design and breadth get the extra time. Depth is the stronger base.

A weakness stays open until a later question shows it without a hint. Understanding the explanation does not close it.

---

## How a block runs

1. **Recall, 15–20 min.** A few concepts. One question each. Correct, then move. Skip what is already fluent. Do not open eight new topics.
2. **Mock, 20–30 min.** One question. No hints and no score until the end. Follow-ups on what he said. He may stop.
3. **Feedback, 10–15 min.** Score, the miss, the stronger shape. A short answer is not a miss by itself. A follow-up distinguishes a gap from a choice to be brief.
4. **Redo, 10–20 min.** The one weakness. Do not replay the mock.

Depth stays on the CV: Koopman, probabilistic forecasting, diffusion for series, irregular observations, structured representations. Interviewers know ML and may not know Koopman. Flow matching is not a prep topic unless he brings it up. The 26 Oct flow-matching mock stays in the log. It is not this week’s depth syllabus.

---

## Scores already on the board

| Mock | Score | Still open |
|------|-------|------------|
| System design, 26 Oct, anomaly alerts | 6.5 | Requirements, baseline, event-level metric, shadow, monitor. Highest priority. |
| Breadth, 28 Oct, 20 inspections | 6.5 provisional | A cap is precision at K, not another threshold. The four-number exercise is unanswered. Calibration before a dollar threshold. |
| Depth, 28 Oct, Koopman | 7.5 | Diagnose before a new architecture. Unit-circle eigenvalues are not a stability certificate. A low-data win is a bias, not proof the plant is Koopman. Answers were short. |
| Depth, 26 Oct, VAE / diffusion / flow matching | 8 | Not this week’s syllabus. |

---

## Days

### Wed 28 — baselines

Breadth recall and the breadth mock are done. The Koopman depth mock is done.

Still today, if energy remains: one short predictive-maintenance design. Requirements, labels, the decision, serving, shadow, monitor. Then the open breadth arithmetic: precision at 10 and at 20, recall at 10 and at 20, on 1,000 machines and 40 failures with 8 and 12 hits.

### Thu 29 — forecasting and the budget

**Depth.** Koopman generative operators (NeurIPS 2026 on the CV): the problem, why a distribution, the architecture, the loss, how a forecast is drawn, the cost, the evidence, the limit. A 20-minute defense.

**Breadth.** Precision at K, recall at K, calibration, the cost threshold, ranking under a cap, leakage. The mock is an industrial classifier. State the decision and the constraint before naming a metric.

**Design.** Predictive maintenance, end to end: collection, labels, training, offline eval, online inference, the alert rule, monitor, retrain.

**Story.** One hard call under conflicting evidence. Bank **C**, the TR kill: gates before the run, 26.9 to 21.9.

### Fri 30 — irregular data and shift

**Depth.** Co-evolving EM for irregular series in a lifted representation (NeurIPS 2026 on the CV). Missingness, the procedure, what is simpler, how it is scored. Explain it to someone who does not work on irregular series. This paper is not the Bosch story. Bosch, if told, stays interpolation plus an observation mask.

**Breadth.** A model that is fine in one factory and worse in another. Name the kind of shift and the split that would show it before naming a fix.

**Design.** Multivariate anomaly streams: latency, deduped events, a false-alert budget, recovery, monitoring.

**Story.** A failed result and what changed. Bank **C** if Thursday did not use it. Otherwise the killed lever inside **A**.

### Sat 31 — generation and a forecast service

**Depth.** Diffusion for series from his own papers: conditioning, regular versus irregular, how a synthetic set is judged, sampling cost. Not flow matching. The mock is whether synthetic sensor sequences are useful: fidelity, and train-on-synthetic test-on-real against a real-data baseline.

**Breadth.** SGD versus Adam, schedules, batch size, instability, normalization, a model that trains and then fails to generalize. Diagnose before a new optimizer.

**Design.** Forecasts for thousands of devices: mixed rates, missingness, batch versus online, horizon cuts, drift.

**Story.** A technical direction others did not want. Bank **A**, ImagenTime. One number. GAF is dense. The sparse image is the line plot. EDM is the sampler.

### Sun 1 — judgment

**Depth.** Distillation (NeurIPS 2025), structured Koopman autoencoders (ICLR 2023), consistent Koopman autoencoders (ICML 2020). One contribution: what it changes, the ablation, the assumption, the failure.

**Breadth.** 25 minutes, mixed: imbalance plus shift, calibration when prevalence changes, ranking under a cap, leakage.

**Design.** One model family across several plants: data, training, serving, what is monitored, what is not shared across sites.

**Stories.** **B**, dual tower: TSExam was flat, matched controls. **E**, Bosch: the measurement changed the model. Research baseline. No product ship.

### Mon 2 — consolidation

No new topic.

- Depth, 20–25 min, two CV projects.
- Breadth, 20–25 min, mixed.
- Design, 30 min: requirements, architecture, data, training, serving, evaluation, monitor, failure modes.
- One page: the identities below, the design checklist, the four stories, the open misses.

Tue 3 Nov is sleep and a short reread. The Thailand start is 4:00 AM on Wednesday.

---

## Depth, in order

1. Koopman: lift versus a finite matrix, encoder–linear–decoder, the three losses, \(A^H\), spectrum, multi-step error, the bias and its limit.
2. Probabilistic forecast: the distribution, the loss, how a sample is drawn, the cost.
3. Generative series: diffusion, conditioning, irregular observations, synthetic data judged on a real holdout.
4. Then distillation, disentanglement, geometry, only as a defense of a CV line.

Unit circle, to say cleanly: for a diagonalizable \(A\) with every \(|\lambda|=1\), modes persist. Decay and exponential growth are excluded. A damped plant needs \(|\lambda|<1\). A Jordan block can grow polynomially. Diagnose reconstruction, one-step latent error, and error versus horizon before changing the architecture.

## Breadth, in order

Precision at K and recall at K. A cap of K inspections is those two numbers on each day’s ranking, not AUROC. Calibrate before \(p > C_{FP}/(C_{FP}+C_{FN})\). If costs differ by machine, rank by expected benefit, not by \(p\). Then shift, leakage, and optimization.

## Design, every time

Requirements, data and leakage, baseline, model, the metric that can kill it, serving, shadow then rollout, monitor and rollback. A strong model with no deployment is not a pass. Rare failures: event recall inside an alert budget, plus lead time. Twenty failures cannot support a tight interval.

---

## Stories

Twenty minutes a day. Two minutes each. “I,” one metric, the decision, the limit. Do not open with the lab, the headcount, or the grant. The CV lists the group and the funding. The spoken answer is the technical call.

| Theme | Use |
|-------|-----|
| A direction others resisted | **A** ImagenTime |
| Conflicting evidence | **C** TR kill |
| A second view | **B** Dual tower |
| A measurement that changed the model | **E** Bosch, interpolation plus a mask |
| A failed result | **C** or the killed representation inside **A** |
| Disagreement | The matched-control decision in **B**, or the kill in **C** |

Mentoring a 20-person group is not one of the six. If they ask how a capability was built, lead with the artifact.

---

## Interviewers

Hypotheses only. Sources and the conflicting titles are in [`README.md`](README.md). Do not assign a domain. Do not recite a title.

- **Bing Xiang, 1:00 PM PT.** Joined Data & AI, per Chandler’s May 2026 post. Long joint NLP and code record with Nallapati. Likely to ask whether a representation preserves the signal and whether the ablation killed the claim.
- **Vivek Govindan, 2:00 PM PT.** Public profile: senior principal ML engineer, Physical AI, Seattle, design and simulation; the same page still lists Amazon. Inference cost and a solver versus a surrogate are the plausible pressure. That matches the design gap. It is not an assignment.
- **Ramesh Nallapati, 3:00 PM PT.** His May 2026 post: VP of Applied Science for a Physical AI science group. Amazon Science still lists AWS. Likely to ask whether the average hides the rare failure.

Questions already chosen, two per hour, then stop: what result would drop an approach; when the model and the solver disagree, which one an engineer trusts; what has to be true before a model sits next to a simulator. Skip any he has already answered.

---

## By 2 Nov

He can defend two CV projects with the mechanism, the evidence, and the limit. He picks the metric from the constraint, including a top-K budget. A design names shadow, rollout, and the monitor before a second model. The four stories are the bank, not the org chart.
