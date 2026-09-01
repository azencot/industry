# On-site — Haraldur: Uncertainty, clinical validation, and deployment judgment

Companion to [`2026-08-27_onsite-haraldur.md`](2026-08-27_onsite-haraldur.md), [`2026-09-01_onsite-haraldur-health-evaluation.md`](2026-09-01_onsite-haraldur-health-evaluation.md), [`2026-09-01_onsite-haraldur-model-usability.md`](2026-09-01_onsite-haraldur-model-usability.md), [`2026-09-01_onsite-haraldur-generalization-leakage.md`](2026-09-01_onsite-haraldur-generalization-leakage.md), and [`2026-09-01_onsite-haraldur-problem-design.md`](2026-09-01_onsite-haraldur-problem-design.md).

```text
HEALTH ML — LESSON 5
UNCERTAINTY, CLINICAL VALIDATION & DEPLOYMENT JUDGMENT
======================================================

CORE IDEA

A good benchmark result is not the same as:

1. a statistically reliable result
2. a clinically meaningful improvement
3. a model that generalizes
4. a system that is safe/useful in deployment


The central question is:

"How much evidence do I need before trusting this model
for the intended health decision?"


A useful progression is:

POINT ESTIMATE
    ↓
UNCERTAINTY
    ↓
SUBGROUP ROBUSTNESS
    ↓
EXTERNAL VALIDATION
    ↓
PROSPECTIVE VALIDATION
    ↓
DEPLOYMENT / MONITORING


======================================================
1. POINT ESTIMATES ARE NOT ENOUGH
======================================================

Suppose:

Model A sensitivity = 88%
Model B sensitivity = 92%


Can I conclude B is better?

No.

I need to know:

- number of positive cases
- uncertainty / confidence intervals
- whether predictions are independent
- whether both models were evaluated on the same examples
- whether the difference is consistent across relevant slices


If only 25 positive participants exist, a difference of
one participant can change sensitivity by:

1 / 25 = 4 percentage points.


So:

88% vs 92%

may represent a very small amount of evidence.


KEY PRINCIPLE:

Always interpret effect size together with uncertainty.


======================================================
2. NUMBER OF WINDOWS ≠ NUMBER OF INDEPENDENT SAMPLES
======================================================

Suppose:

120 participants

but each participant contributes:

1000 windows.


Then I have:

120,000 windows.


Do I have 120,000 independent observations?

NO.


Windows from the same participant are correlated.


They may share:

- physiology
- disease status
- baseline heart rate
- behavior
- sensor characteristics
- temporal context


Therefore:

effective evidence may be much closer to the number of
participants than the number of windows.


This matters for:

- confidence intervals
- statistical testing
- train/test splitting
- bootstrapping


Memory:

"Don't confuse repeated measurements with independent people."


======================================================
3. CONFIDENCE INTERVALS
======================================================

A point estimate tells me:

"What did I observe?"


A confidence interval tells me approximately:

"How uncertain is this estimate due to finite sampling?"


Example:

Sensitivity = 92%

95% CI = [78%, 98%]


This tells a very different story from:

Sensitivity = 92%

95% CI = [90%, 94%]


Same point estimate.

Very different certainty.


For health applications with small positive populations,
sensitivity estimates can have surprisingly wide intervals.


======================================================
4. BOOTSTRAPPING
======================================================

Bootstrapping is one practical way to estimate uncertainty.


Basic idea:

1. sample test units WITH REPLACEMENT
2. calculate metric
3. repeat many times
4. examine distribution of metric


But:

WHAT SHOULD I RESAMPLE?


If my data contains many windows per participant,
I generally should NOT treat windows as independent.


Instead, if participant is the independent unit:

RESAMPLE PARTICIPANTS.


For each sampled participant:

include that participant's relevant observations.


This preserves within-person dependence better than
independently resampling windows.


KEY PRINCIPLE:

Bootstrap at the level corresponding to the independent
unit / generalization claim.


======================================================
5. PAIRED MODEL COMPARISON
======================================================

Suppose Model A and Model B are evaluated on the same people.

Their errors are PAIRED.


This is useful because I can ask:

On which examples does B improve over A?

For example:

- both correct
- A correct / B wrong
- A wrong / B correct
- both wrong


Rather than only comparing:

Metric(A) vs Metric(B)


I want uncertainty on:

Metric(B) - Metric(A)


For example, with participant-level bootstrap:

resample participants
    ↓
evaluate A
    ↓
evaluate B
    ↓
compute difference
    ↓
repeat


This gives a distribution for the improvement.


The question becomes:

"How consistently does B outperform A under plausible
resampling of the population?"


======================================================
6. STATISTICAL SIGNIFICANCE ≠ PRACTICAL SIGNIFICANCE
======================================================

Suppose a huge study finds:

AUROC:

0.900 → 0.903


and the difference is statistically significant.


Does that mean the new model matters?

Not necessarily.


Ask:

Does it improve the actual operating point?

For example:

At 95% sensitivity:

Does specificity improve?

Does precision improve?

How many false alerts are avoided per 1000 users?


Health-system decisions should be expressed in terms of
meaningful consequences when possible.


KEY DISTINCTION:

STATISTICAL:

"Is this difference likely to be noise?"


PRACTICAL / CLINICAL:

"Is this difference large enough to matter?"


======================================================
7. SUBGROUP UNCERTAINTY
======================================================

Suppose overall:

Sensitivity = 93%


Then:

Group A = 95%
Group B = 82%


This deserves investigation.


But suppose Group B contains only:

12 positive participants.


Then its 82% estimate may have very large uncertainty.


Therefore subgroup analysis needs BOTH:

performance

AND

sample size / uncertainty.


Do not make strong conclusions from tiny slices.


At the same time:

large uncertainty does NOT mean ignore the subgroup.


It may mean:

"We need more evidence before claiming this system works
well for this population."


======================================================
8. MULTIPLE SUBGROUPS
======================================================

Suppose I evaluate:

10 age groups
5 devices
10 activity categories
20 medical conditions


Eventually some slice will look unusually good or bad
by chance.


Therefore:

Avoid searching through hundreds of slices and then treating
the most extreme result as a confirmed discovery.


Better:

Predefine important slices based on:

- deployment requirements
- domain knowledge
- known measurement differences
- safety concerns


Exploratory slicing is still useful.

But distinguish:

EXPLORATORY FINDING

from

CONFIRMED RESULT.


======================================================
9. INTERNAL VALIDATION
======================================================

Suppose I:

train on participants from Study A

and

test on held-out participants from Study A.


This is valuable.

But train and test still share:

- recruitment process
- devices
- data pipeline
- geography
- labeling procedure
- study protocol


Therefore strong internal validation establishes:

"Generalization within this study setting."


It does NOT automatically establish:

"Generalization everywhere."


======================================================
10. EXTERNAL VALIDATION
======================================================

A stronger test uses meaningfully different data.


Examples:

- another cohort
- another site
- another geography
- another device generation
- another acquisition protocol
- another time period


Why?


Because deployment introduces distribution shift.


External validation asks:

"Does the model survive when important parts of the
data-generating process change?"


If performance collapses externally:

Do not immediately retrain the architecture.


First identify:

WHAT CHANGED?


Population?

Prevalence?

Measurement?

Missingness?

Label definition?

Device?

Workflow?


======================================================
11. RETROSPECTIVE VALIDATION
======================================================

Most ML development starts retrospectively:

We already have a dataset.

We train and evaluate on historical data.


This is useful for:

- hypothesis generation
- architecture development
- benchmarking
- initial validation


But retrospective datasets can differ from actual deployment.


Potential problems:

- selection bias
- artificial data completeness
- retrospective labels
- workflow information
- leakage
- different prevalence
- different user behavior


Therefore:

Strong retrospective performance is evidence.

It is not the end of validation.


======================================================
12. PROSPECTIVE VALIDATION
======================================================

In prospective evaluation:

the model/evaluation procedure is defined first

and then

new data are collected / evaluated going forward.


This is stronger evidence about real-world behavior.


It can reveal:

- actual missingness
- real user adherence
- unexpected sensor failures
- population shift
- workflow problems
- alert burden
- changing prevalence


A model that works retrospectively may degrade prospectively.


Memory:

Retrospective:

"How would my model have performed on existing data?"


Prospective:

"How does my fixed model perform on what happens next?"


======================================================
13. MODEL PERFORMANCE ≠ CLINICAL UTILITY
======================================================

Suppose:

AUROC = 0.95


That sounds excellent.


But imagine deployment produces:

10 alerts per person per week

and:

90% are false positives.


The system may be unusable.


Or suppose:

Sensitivity = 99%

but:

the prediction occurs only 30 seconds before the event

while useful intervention requires 30 minutes.


Again:

excellent metric

but poor utility.


Therefore ask:

"What happens downstream when this model makes a prediction?"


======================================================
14. THINK IN ABSOLUTE COUNTS
======================================================

Percentages can hide operational consequences.


Suppose:

10 million users

condition prevalence = 0.1%


Even a small false-positive rate can create enormous
numbers of alerts.


Instead of only reporting:

Specificity = 99%


also ask:

How many false positives per:

1000 users?
100,000 users?
day?
week?


Similarly:

How many true cases are missed?


This makes model performance operationally interpretable.


======================================================
15. FALSE-ALERT BURDEN
======================================================

For wearable systems, false alerts can cause:

- alarm fatigue
- anxiety
- unnecessary clinical visits
- unnecessary testing
- users ignoring future alerts


Therefore precision and specificity may matter even when
screening emphasizes sensitivity.


The correct tradeoff depends on:

WHAT HAPPENS AFTER THE ALERT?


If the next step is:

"Take another passive measurement"

false positives may be relatively cheap.


If the next step is:

"Visit a specialist"

the cost is higher.


If the next step is:

"invasive procedure"

the required evidence is much stronger.


======================================================
16. CALIBRATION AND DECISION-MAKING
======================================================

If the model outputs probabilities used for risk decisions,
calibration matters.


Suppose:

Predicted risk = 80%


If actual risk among such predictions is only 30%,
downstream decisions based on that probability may be wrong.


Therefore deployment validation should consider:

- discrimination
- operating-point performance
- calibration


And calibration may need reassessment after distribution shift.


======================================================
17. DEPLOYMENT IS ANOTHER EXPERIMENT
======================================================

Even after strong prospective validation:

do not assume performance stays fixed forever.


Things change:

- users
- prevalence
- devices
- firmware
- sensors
- behavior
- clinical practice
- data pipelines


Therefore deployment requires monitoring.


Useful things to monitor:

INPUTS

- missingness
- signal quality
- feature distributions
- device mix


OUTPUTS

- score distribution
- alert rate
- calibration


WHEN LABELS BECOME AVAILABLE

- sensitivity
- specificity
- precision
- subgroup performance


CORE IDEA:

Deployment is not the end of evaluation.


======================================================
18. DISTRIBUTION SHIFT AFTER DEPLOYMENT
======================================================

Suppose alert rate suddenly doubles.


Don't immediately retrain.


First diagnose:

Did disease prevalence change?

Did sensor behavior change?

Was there a firmware update?

Did missingness change?

Did the population change?

Did the model itself change?

Did the downstream threshold change?


Again:

DIAGNOSE BEFORE INTERVENING.


======================================================
19. WHEN IS A MODEL "GOOD ENOUGH"?
======================================================

There is no universal number.


Not:

AUROC > 0.9

Not:

Accuracy > 95%


Instead:

"Good enough for WHAT?"


I want to know:

1. Intended health decision

2. Cost of false positives

3. Cost of false negatives

4. Required operating point

5. Performance uncertainty

6. Relevant subgroup performance

7. Calibration

8. External/prospective evidence

9. Operational burden

10. Comparison with existing alternative


A model should be judged relative to the decision
it is supposed to improve.


======================================================
20. MODEL VS EXISTING STANDARD
======================================================

Suppose my new model has:

AUROC = 0.94


That alone doesn't tell me whether it is useful.


What is the alternative?


Maybe:

existing system = 0.93


Then ask:

Does the new system:

- improve sensitivity at required specificity?
- reduce false alerts?
- work with less data?
- detect earlier?
- generalize better?
- work for more users?
- reduce cost?


The relevant question is often:

"What incremental value does this model provide over
what we can already do?"


======================================================
21. A REUSABLE EVIDENCE LADDER
======================================================

Think of increasing evidence:


1. TRAINING PERFORMANCE

   Did optimization work?


2. INTERNAL HELD-OUT VALIDATION

   Does it generalize to unseen examples/users
   in the same study?


3. TEMPORAL VALIDATION

   Does it generalize forward in time?


4. EXTERNAL VALIDATION

   Does it generalize to a different population,
   device, site, or acquisition process?


5. PROSPECTIVE VALIDATION

   Does a fixed model work on newly arriving data?


6. REAL-WORLD DEPLOYMENT

   Does it provide useful benefit in the intended workflow?


Each step supports a stronger claim.


======================================================
22. INTERVIEW CASE
======================================================

INTERVIEWER:

"We have a new wearable model.

The old model has:

Sensitivity = 88%

The new model has:

Sensitivity = 92%

We have tens of thousands of test windows.

Should we replace the old model?"


WEAK ANSWER:

"Yes, four percentage points is a meaningful improvement."


STRONG ANSWER:

"Not yet.

First I'd determine the independent sample size. If those
tens of thousands of windows come from a small number of
participants, treating the windows as independent would
greatly overstate our certainty.

Since both models are evaluated on the same participants,
I'd compare them in a paired way and estimate uncertainty
on the performance difference, ideally respecting the
participant-level structure.

Then I'd ask whether the improvement exists at the operating
point we actually care about. Did sensitivity improve by
trading away too much specificity or precision?

I'd also check relevant subgroups and external or temporal
validation.

Finally, even if the improvement is statistically reliable,
I'd ask whether it is operationally meaningful: how many
additional true cases are caught and how many additional
false alerts are generated.

So 92 versus 88 is evidence worth investigating, but not
enough by itself to justify replacement."


======================================================
23. HARALDUR ANSWER TEMPLATE
======================================================

"I'd separate three questions.

First, is the result statistically reliable? I'd look at
uncertainty using the correct independent unit — often the
participant rather than individual wearable windows — and
compare models in a paired way.

Second, is the improvement meaningful at the intended
operating point? I'd translate it into sensitivity,
specificity, precision and ideally absolute numbers of
additional detections and false alerts.

Third, does the evidence support deployment? I'd check
relevant subgroups, calibration and robustness under
realistic shifts, and I'd want increasingly strong external
or prospective validation depending on the consequence of
the decision.

So I wouldn't ask simply whether the metric improved.
I'd ask how certain the improvement is, whether it matters,
and whether it survives the conditions where the model will
actually be used."


======================================================
ONE-LINE MEMORY
======================================================

Point estimate:
"What did I observe?"

Uncertainty:
"How sure am I?"

Independence:
"Are these really separate samples?"

Statistical significance:
"Is the difference likely to be real?"

Practical significance:
"Is the difference large enough to matter?"

External validation:
"Does it survive a different data-generating process?"

Prospective validation:
"Does the fixed system work on what happens next?"

Deployment:
"What happens to real users when the model is wrong?"

Monitoring:
"Is the system still behaving as expected?"

CORE PRINCIPLE:

A better benchmark number is the beginning of the
deployment argument, not the end.
```
