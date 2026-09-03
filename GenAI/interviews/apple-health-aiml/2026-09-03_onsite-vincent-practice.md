# On-site — Vincent: whole-system mock log (Thu 9/3)

Companion to [`2026-08-27_onsite-vincent.md`](2026-08-27_onsite-vincent.md). Stories: [`2026-08-30_behavioral-stories.md`](2026-08-30_behavioral-stories.md). Hub: [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md).

**Status:** In progress. **Block 0 spoken.** **Block 2 follow-ups partial** (n=20 / block / large gain / fix-hurts-average). Block 1 not started. Main Block 2 (“is the difference real?” + diagnostic tree) not spoken as a whole.  
**Slot:** Tue 9/8 4:05 PDT. Last of five.

**Outcome so far:** Right altitude (no transformer open). Largest misses: near-chance ⇒ deeper model (Block 0); **n=20 ⇒ OOD** and **legal disclaimer / ignore 1–2 pp** (Block 2). Small n is uncertainty, not shift. Average AUROC does not license a failed slice.

Append later blocks under the same headings: MY ANSWER → CORRECTION → RESTITCH (if needed).

---

## Block 0 — 15 min mental warm-up

Prompt: one imaginary problem — “Predict a health/fitness state from Apple Watch sensor data.” Speak 1–10 without notes. Target: one 5–7 min coherent system, not ten disconnected bullets. Do not jump to transformer / xattn / FM.

### MY ANSWER

1. Target pop is Apple Watch users; regular people, coming with various kinds of health/fitness states and conditions.

2. The decision may be lifestyle change or recommendation for expert eval. Arriving at an accurate decision is fundamentally supported by the prediction. At this point, not considering critical health decisions.

3. Since the target pop is users, labels are self-reported. That means missing/scarce labels, with high noise.

4. Data can be all sensor data arising from the Watch: PPG, HR, IMU, and other direct/aggregate measures.

5. Simplest useful baselines: linear/logistic regressions, ARIMA, features + XGBoost. Might also consider an existing strong deep model, assuming there is one for the particular problem at hand that does not require complex adaptations.

6. Inspect baseline results: if near chance or generally not useful, turn to more complex models.

7. Eval should be tiered. Small toy data with gold labels → medium toy+real mix with gold labels → large real-world data with noisy labels. Might add more levels if first levels were not satisfactory based on predefined gates.

8. Scarce wearers could be very noisy; people with health conditions might affect sensors or their interpretability; people with rare conditions (very low prevalence).

9. Deployment can be tiered: if offline evals succeed → shadow mode → full online. If full or partial slices meet harness gates, stop deployment and analyze model behavior wrt slice/full data.

10. Need software engineers to implement the deployment side; clinical experts to design toy data and eval; legal people to decide if this can be a product; marketing to ad this product; salesmen to decide about costs vs memberships.

### CORRECTION

Keep: non-diagnostic scope; noisy/scarce labels instinct; XGBoost as a first rung; staged offline → shadow; clinical/legal as partners.

| # | Miss | Fix before live |
|---|------|-----------------|
| — | Ten bullets, not one system | Open: decision → population → what data/labels are *allowed* → then model class |
| 1 | “Watch users / regular people” | Selected population. Name axes: age, BMI/body characteristics, wear pattern, device generation, gestures that mimic the event |
| 2 | Lifestyle *or* expert eval | Two products. Pick one for the warm-up. Say *when* the prediction is made and FP/FN cost |
| 2↔3 | Users ⇒ self-report | Expert-eval cannot use self-report as ground truth. Wellness nudge can, with the noise named. How is GT established? |
| 4 | “All Watch sensors”; HR as independent | PPG + IMU as core; HR often derived. Sampling, missingness, labeled vs unlabeled. Permissibility: collected / linked / retained / used for *this* purpose. Do not claim Apple policy |
| 5 | ARIMA + deep model in the baseline slot | Baseline = summary features + logistic / XGBoost. Deep is the next rung. ARIMA only if the task is a univariate forecast |
| **6** | **Near chance ⇒ go deeper** | **Largest miss.** Near chance ⇒ diagnose labels, splits, prevalence, whether the Watch signal can support the decision. Complexity only when the simple model is already useful and you can name a residual |
| 7 | Toy → mix → noisy-large as the harness | That is a research program. Harness: participant-disjoint, operating point, calibration, subgroup floors, missingness, device/time shift, CIs at independent-unit level. Gates predeclared |
| 8 | Wear / comorbidity / rarity only | Add BMI/body characteristics, age, gesture collision, new device generation |
| 9 | Stop when slices *meet* gates | Inverted. Stop when slices **fail**. Add on-device vs cloud, latency/battery, missing sensor, bad input, monitoring, rollback |
| 10 | Marketing, sales, “legal decides if product” | Cut marketing/sales (managerial). Name the *uncertainty* each function resolves: sensor (body–signal?), clinical (label / clinical meaning?), privacy (can collect/use?), stats (is the subgroup gap real?), eng (device constraints?). You own the technical decision |

Next drill if short on time: **why near-chance would not license a foundation model.**

### RESTITCH (~90s)

I’d first define the decision and the population before choosing a model. For this warm-up I’d treat it as a non-diagnostic Watch signal that might support a lifestyle nudge, not a clinical call. The population is Watch wearers, which is already selected, and I’d design for age, body characteristics, wear behavior, device generation, and gestures that can mimic the target. Labels are not automatically self-report: I’d say how ground truth is defined, how scarce and noisy it is, and what is legally usable. Data starts from the sensors that are actually available and permissible — PPG and IMU as the core, with derived heart rate not counted as independent. I’d start with summary features plus logistic regression or XGBoost. If that is near chance, I diagnose labels, splits, and whether the signal exists; I add complexity only when a simple model is useful and I can name what it cannot capture. Evaluation is participant-disjoint, with an operating point tied to the nudge, subgroup floors, missingness, and device shift. Deployment is offline, then shadow, then limited rollout, and I stop if a predeclared slice fails. Sensor, clinical, privacy, and engineering partners resolve specific uncertainties — not whether this should be a marketed product.

---

## Block 1 — Design the whole health ML system

Not started. Sheet: most important Vincent question.

### MY ANSWER

_(append)_

### CORRECTION

_(append)_

---

## Block 2 — Overall win, population fails

Main question not spoken as a whole. First move on the sheet: **is the difference real?** Then why (data / sensor / representation / model / eval). Follow-ups 1–4 spoken; 5–11 not started.

### MY ANSWER (follow-ups 1–4)

**20 positive cases.** Want subgroup size. If the subgroup is small, the entire slice is OOD. If subgroup size is on par with other groups, compare prevalence (20 / subgroup size) to other subgroups. If prevalence is very low, might have trained/eval while missing low-prevalence modes.

**Block deployment?** Need FN cost. If missing these 20 pos people has critical health implications, block deployment for the whole subgroup and defer to manual intervention if it makes sense. If the decision is not critical, consult legal whether continued deployment with a disclaimer of errors for that subgroup is reasonable.

**Overall gain is very large.** Decision principle based on subgroup size. Aim for a product available to all users. If the failing subgroup is very small, might reroute their data through a more stable baseline while retaining better overall performance.

**Fixing the subgroup reduces average performance.** Analyze how the change harmed other groups, per subgroup, to understand cause wrt the change. The change might have exposed a limitation of the previous system even though former average was better. Alert depends on reduction scale. If small (within 1–2 pp) might ignore it, assuming non-critical decisions. Being inclusive trumps small metric differences.

### CORRECTION

Keep: do not conclude from n=20 without denominators; FN cost matters; fallback/baseline routing for a failing slice; old average might have been a shortcut — *if* you can show it.

| Follow-up | Miss | Speak instead |
|-----------|------|----------------|
| n=20 | **Small subgroup ≠ OOD.** OOD is a shift. Small n is an **estimation** problem. 20 positives can sit inside 10k people (low prevalence + noisy TPR), or 20 events from 3 people (not 20 independent units) | First: is the gap **real**? CIs at the independent-unit (person) level. Compare new vs old model on the *same* units. 20 pos ⇒ usually **cannot conclude** the new model is worse. Low prevalence is a hypothesis, not something n=20 proves |
| Block? | Manual intervention is not a Watch product. **Disclaimer / consult legal** is the Block 0 product-manager trap | With n=20 you almost never block on the metric alone. If the *decision* cannot tolerate a real slice failure: hold the new model, don’t surface the score on that slice, or fall back. Legal/privacy answers what you may collect or claim — not whether a disclaimer makes a failed slice shippable |
| Large overall gain | “Principle = subgroup size.” 2% of Watch users is huge in absolute numbers. Average gain does not license harming an important population | Size is an input, not the rule. Is the gap real? What is FN/FP cost for *this* decision? Mitigations: hold, slice-gate, different threshold, fallback model, collect more evidence. Routing to a stable baseline is a good *option*, not automatic because the group is “small” |
| Fix hurts average | “Ignore 1–2 pp.” Slogan: “inclusive trumps metrics.” Exposed-old-shortcut needs a **discriminating experiment**, not a story | Predeclare a subgroup floor. If the drop is within uncertainty, say that — do not “ignore.” If the floor is met and the decision’s cost structure supports it, you may accept a small average loss. If a named important slice fails, you do not ship on average AUROC |

Diagnostic tree almost unused (sensor/BMI/wear, tokenization, negative transfer, calibration, threshold). These follow-ups turned into policy before diagnosis.

Not yet: 2% of users; don’t know why; collect more evidence; separate model; different threshold; physiology vs sensor artifact; who you involve (named uncertainty, not legal-for-disclaimer).

### RESTITCH (these four only)

Twenty positives is a statement about event count, not about shift. I would not conclude the new model is worse until I know the independent-unit sample size, the confidence interval on the slice metric, and whether the old model was better on those same people. If the interval is wide, I collect more evidence — I do not block and I do not ship. If the gap is real, the decision depends on FN cost for this product, not on a disclaimer. A large average gain does not license a failed important slice; a fallback or a hold is on the table. If repairing the slice hurts the average, I want to know whether the old average was a shortcut I can show, and whether a predeclared floor is still met. I would not ignore a 1–2 pp drop by slogan.

---

## Block 3 — Data collection + legal/privacy

Not started.

### MY ANSWER

_(append)_

### CORRECTION

_(append)_

---

## Block 4 — Fixed budget (size / data / resolution / modality)

Not started.

### MY ANSWER

_(append)_

### CORRECTION

_(append)_

---

## Block 5 — Research system at scale

Not started. Stories: ImagenTime, TSRBench 0.8B probe, TR mix kill.

### MY ANSWER

_(append)_

### CORRECTION

_(append)_

---

## Block 6 — Cross-functional (Bosch)

Not started. Card: [`2026-08-30_behavioral-stories.md`](2026-08-30_behavioral-stories.md) #5.

### MY ANSWER

_(append)_

### CORRECTION

_(append)_

---

## Block 7 — Deployment case

Not started.

### MY ANSWER

_(append)_

### CORRECTION

_(append)_

---

## Block 8 — Rapid-fire (15 × 30–60s)

Not started.

### MY ANSWER

_(append)_

### CORRECTION

_(append)_

---

## Block 9 — L5 self-check

Not started.

---

## Running corrections (promote if they fail twice)

| Still wrong | Speak instead |
|-------------|----------------|
| Near-chance baseline → bigger model | Diagnose label / split / prevalence / whether the signal exists |
| Users ⇒ self-report | How is ground truth established for *this* decision? |
| Marketing / sales / “I asked the team” | Named uncertainty + IC verb |
| All Watch sensors | Permissible subset; HR often derived from PPG |
| Slices *meet* gates → stop | Slices **fail** gates → stop |
| Small n / small % ⇒ OOD or ignorable | Small n = uncertainty. Small % of Watch is still many people. Is the gap **real**? |
| Disclaimer / consult legal to ship a failed slice | Hold, gate, fallback, or collect evidence. Legal ≠ a waiver |
| Ignore 1–2 pp if “inclusive” | Predeclared floor + cost of the decision. Within noise ≠ ignore |

---

## Hand-off

```
@GenAI/interviews/apple-health-aiml/2026-09-03_onsite-vincent-practice.md
@GenAI/interviews/apple-health-aiml/2026-08-27_onsite-vincent.md
Vincent mock in progress. Block 0 done. Block 2 follow-ups 1–4 logged. Small n ≠ OOD; do not disclaimer-ship a failed slice; do not ignore 1–2 pp. Main Block 2 diagnosis and Block 1 still open. Append; do not rewrite Block 0.
```
