# On-site — Haraldur: Evaluation, generalization, and leakage

Companion to [`2026-08-27_onsite-haraldur.md`](2026-08-27_onsite-haraldur.md), [`2026-09-01_onsite-haraldur-health-evaluation.md`](2026-09-01_onsite-haraldur-health-evaluation.md), and [`2026-09-01_onsite-haraldur-model-usability.md`](2026-09-01_onsite-haraldur-model-usability.md).

```text
HEALTH ML — LESSON 3
EVALUATION, GENERALIZATION & LEAKAGE
====================================

CORE IDEA

A model's test performance is meaningful only relative to
the GENERALIZATION CLAIM.

Before looking at a metric, ask:

"What new thing do I expect this model to generalize to?"

Examples:

- new windows from known users?
- completely new users?
- future data from the same users?
- a new hospital/site?
- a different device?
- a different population?
- real prospective deployment?

The train/test split must match that claim.


====================================
1. THE UNIT OF INDEPENDENCE
====================================

Suppose each participant contributes:

1000 wearable windows.

If I randomly split WINDOWS:

80% train
20% test

then windows from the SAME PERSON can appear in both sets.

This can make performance look much better than true
generalization to unseen users.

Why?

The model may exploit participant-specific information:

- baseline heart rate
- movement style
- physiology
- device characteristics
- daily routines
- persistent artifacts


If the deployment claim is:

"We generalize to NEW PEOPLE"

then I should usually split:

BY PARTICIPANT

not by window.


KEY PRINCIPLE:

The unit of independence in evaluation should correspond
to the generalization claim.


====================================
2. TEMPORAL LEAKAGE
====================================

Health data often has strong temporal dependence.

Suppose I want to predict:

"Will an adverse event occur in the next 24 hours?"

At prediction time t, features must contain ONLY information
available at or before t.


Correct structure:

PAST                    t              FUTURE

[ observation window ]  |  [ prediction horizon ]
                        |
                     prediction


Potential leakage:

- features computed using future measurements
- normalization using the entire trajectory
- labels influencing preprocessing
- windows overlapping the event itself
- post-event measurements entering the input
- random temporal splits when neighboring windows are
  nearly identical


QUESTION TO ASK:

"Could this feature have been computed at the moment when
the prediction would actually have been made?"


If not:

LEAKAGE.


====================================
3. OVERLAPPING WINDOWS
====================================

Suppose I create:

window 1: seconds 0-60
window 2: seconds 5-65
window 3: seconds 10-70

These examples share most of their raw observations.

If highly overlapping windows are randomly divided between
train and test, the test set is not genuinely independent.

The model may effectively see almost the same signal during
training.


Therefore:

Think about independence BEFORE window generation and
splitting.

Often:

split participants / trajectories first

THEN

construct windows within each split.


====================================
4. RANDOM SPLIT VS TEMPORAL SPLIT
====================================

A random split asks approximately:

"Can I generalize to another sample drawn from the same
distribution?"


A temporal split asks:

"Can I train on the past and generalize to the future?"


Example:

Train:
Jan 2024 - Dec 2025

Test:
Jan 2026 - Jun 2026


This may expose:

- changing user behavior
- new devices
- software changes
- seasonality
- population changes
- measurement drift


For a system deployed into the future, temporal evaluation
may be much closer to the actual use case.


====================================
5. INTERNAL VS EXTERNAL VALIDATION
====================================

INTERNAL VALIDATION:

Train and test data come from the same underlying study,
organization, population, or data-generation pipeline.

Useful, but limited.


EXTERNAL VALIDATION:

Evaluate on meaningfully different data:

- another hospital
- another geographic population
- another cohort
- another device
- another study
- another acquisition pipeline


This asks a stronger question:

"Does the result survive a realistic distribution shift?"


A model can have excellent internal validation and still
fail externally.


====================================
6. RETROSPECTIVE VS PROSPECTIVE
====================================

RETROSPECTIVE:

Evaluate using data that has already been collected.

Advantages:

- fast
- cheap
- useful for development


But the model is evaluated on an existing historical dataset.


PROSPECTIVE:

Define the model/evaluation procedure first and then evaluate
on subsequently collected data or in the intended workflow.

This is much closer to:

"What happens when we actually use this system?"


Prospective evaluation can reveal problems absent from
retrospective benchmarks:

- workflow changes
- missing data
- user behavior
- sensor failures
- prevalence changes
- feedback effects
- operational constraints


IMPORTANT:

Strong retrospective results do NOT automatically imply
deployment readiness.


====================================
7. DISTRIBUTION SHIFT
====================================

Suppose:

Train performance: strong
Test benchmark: strong
Deployment: weak


Ask:

"What changed?"


Useful categories:


A. POPULATION SHIFT

Different:

- ages
- demographics
- disease prevalence
- activity levels
- comorbidities


B. MEASUREMENT SHIFT

Different:

- sensor
- sampling rate
- firmware
- device placement
- noise
- missingness


C. BEHAVIORAL SHIFT

Different:

- when people wear device
- how frequently they wear it
- activity patterns
- adherence


D. TEMPORAL SHIFT

The world/data changes over time.


E. LABEL SHIFT / LABELING SHIFT

Disease prevalence may change.

Or:

the process used to determine the ground-truth label changes.


====================================
8. PERFORMANCE BY SUBGROUP
====================================

Aggregate performance can hide important failures.

Suppose:

Overall sensitivity = 92%


But:

Group A = 96%
Group B = 72%


The aggregate number may be misleading.


Therefore evaluate relevant slices:

- age
- sex, when relevant to the clinical problem
- device type
- activity state
- signal quality
- wear time
- missingness
- disease severity
- relevant clinical groups


IMPORTANT:

Don't just ask:

"Are subgroup metrics different?"

Also ask:

"Why?"


Possible explanations:

- smaller sample size
- different prevalence
- measurement quality
- true population shift
- model weakness
- labeling differences


====================================
9. UNCERTAINTY / CONFIDENCE INTERVALS
====================================

Suppose:

Model A sensitivity = 91%
Model B sensitivity = 93%


Is B actually better?

Not enough information.


If there are only 30 positive patients,
the uncertainty may be enormous.


Report uncertainty around metrics.

For example:

Sensitivity = 0.91
95% CI = [0.84, 0.96]


In wearable datasets, be careful about the unit used
for uncertainty estimation.


If one participant contributes 1000 correlated windows,
those are NOT equivalent to 1000 independent participants.


A useful approach:

bootstrap at the PARTICIPANT level

when participants are the independent units.


KEY IDEA:

Huge numbers of windows do not necessarily mean huge
effective sample size.


====================================
10. PREVALENCE SHIFT
====================================

Remember:

Sensitivity and specificity are conditional on actual class.

Precision depends strongly on prevalence.


Suppose:

Development prevalence = 20%

Deployment prevalence = 1%


Even if sensitivity and specificity remain similar,
precision may collapse.


Therefore:

For deployment I want to know:

"What precision should I expect at the real prevalence?"


This connects directly to Lesson 1.


====================================
11. CALIBRATION UNDER SHIFT
====================================

A model may be calibrated in development:

Predicted 80% risk
≈
80% observed event rate


But after deployment:

Predicted 80%
≈
40% observed rate


Distribution or prevalence changes can damage calibration.


Therefore:

Calibration should be evaluated in the population where
the probability will actually be interpreted.


This connects directly to Lesson 2.


====================================
12. BASELINES
====================================

A sophisticated model should not only beat weak baselines.

Useful comparisons might include:

- majority / prevalence baseline
- logistic regression
- simple summary statistics + XGBoost
- simple temporal model
- previous clinical score
- single-modality model


WHY?

Suppose:

Large multimodal foundation model: AUROC 0.91
XGBoost:                         AUROC 0.90


Then the question becomes:

"What does the large model actually buy us?"


Maybe:

- better low-label performance
- robustness
- transfer
- difficult subgroup performance
- personalization
- richer downstream tasks


Or maybe:

not enough to justify its complexity.


====================================
13. EVALUATION SHOULD FOLLOW THE CLAIM
====================================

Suppose my claim is:

"The model is robust to missing wearable data."


Then average AUROC is insufficient.

I need an evaluation specifically testing missingness:

performance at:

0% missing
20% missing
40% missing
60% missing


Or:

continuous wearers
moderate wearers
intermittent wearers


If my claim is:

"The model generalizes to new people"

I need participant-disjoint evaluation.


If my claim is:

"The model generalizes over time"

I need temporal evaluation.


If my claim is:

"The model transfers across devices"

I need device-shift evaluation.


CORE SCIENTIFIC PRINCIPLE:

DESIGN THE EVALUATION AROUND THE CLAIM.


====================================
14. HEALTH-ML FAILURE EXAMPLE
====================================

Suppose someone says:

"We trained a wearable disease detector.

We have 500 participants and millions of windows.

Random train/test split gives:

AUROC = 0.96."


My immediate questions should be:

1. Were participants shared between train and test?

2. How much do windows overlap?

3. Was the split performed before or after window generation?

4. Could preprocessing use future/test information?

5. What is the intended deployment population?

6. What is performance on completely unseen participants?

7. What is sensitivity/precision at the intended operating point?

8. What is performance across important subgroups?

9. What are the confidence intervals at the participant level?


I would NOT be impressed by "millions of samples"
until I understand how many independent units exist.


====================================
15. INTERVIEW CASE
====================================

Interviewer:

"Our wearable model gets 92% accuracy on a random test split,
but only 74% when we hold out entire participants.

What do you conclude?"


BAD ANSWER:

"The model is overfitting, so I would add regularization."


BETTER ANSWER:

"The first thing I'd conclude is that the random split was
answering an easier generalization question.

If windows from the same participant appeared in training
and test, the model may exploit participant-specific patterns.

The participant-held-out result is more relevant if the
deployment goal is generalization to new users.

I wouldn't immediately change the architecture. I'd first
quantify the gap, check for overlapping windows and other
leakage, and examine whether particular participants or
subgroups account for the degradation.

Then I'd investigate whether the model is learning
participant-specific shortcuts rather than transferable
health signals."


====================================
16. A REUSABLE EVALUATION FRAMEWORK
====================================

When someone shows me a health-model result:

CLAIM
  |
  v
WHAT GENERALIZATION DO WE CLAIM?
  |
  v
WHAT IS THE INDEPENDENT UNIT?
  |
  v
DOES THE SPLIT MATCH THAT CLAIM?
  |
  v
IS THERE LEAKAGE?
  |
  v
WHAT METRIC + OPERATING POINT?
  |
  v
WHAT SLICES / SUBGROUPS?
  |
  v
WHAT UNCERTAINTY?
  |
  v
DOES IT SURVIVE REALISTIC SHIFT?


====================================
17. HARALDUR ANSWER TEMPLATE
====================================

"I'd first define the generalization claim, because that
determines what constitutes a valid test set.

If the goal is deployment to new users, I'd want a
participant-disjoint split rather than randomly splitting
wearable windows. If the goal includes future deployment,
I'd also consider temporal validation and ideally external
or prospective validation.

I'd explicitly audit leakage, particularly overlapping
windows, preprocessing across train and test, and information
that would not have been available at prediction time.

Then I'd evaluate at the intended operating point using
sensitivity, specificity and precision at realistic
prevalence, with participant-level confidence intervals.

Finally, I'd slice performance by clinically and technically
relevant factors such as signal quality, missingness, device
and relevant user groups.

The main principle is that the evaluation design has to
match the claim we're trying to make."


====================================
ONE-LINE MEMORY
====================================

Split:
"Does my test set represent the thing I claim is new?"

Leakage:
"Did the model indirectly see information it would not have
at deployment?"

Independence:
"Millions of windows are not millions of independent people."

Shift:
"What changed between development and deployment?"

Subgroups:
"Does the aggregate hide an important failure?"

Uncertainty:
"Is the apparent difference larger than sampling uncertainty?"

Scientific rigor:
"The evaluation should be designed around the claim,
not the claim around the metric."
```
