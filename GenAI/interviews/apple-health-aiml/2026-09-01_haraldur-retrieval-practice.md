# Haraldur — Retrieval practice

Companion to [`2026-08-27_onsite-haraldur.md`](2026-08-27_onsite-haraldur.md) and the Health ML lesson series dated 2026-09-01.

```text
HARALDUR — RETRIEVAL PRACTICE
Health ML Metrics, Evaluation, and Deployment Judgment
=======================================================

PURPOSE

This sheet captures the main lessons from retrieval practice.

The goal is not to memorize answers.

For each health-ML case, reason through:

1. What is the intended decision?
2. What metric actually answers the question?
3. What is the independent unit?
4. Could the evaluation be misleading?
5. How uncertain is the result?
6. What alternative explanations exist?
7. What experiment would distinguish them?


=======================================================
CASE 1 — BASIC METRICS
=======================================================

SCENARIO

2,000 people.

200 actually have the condition.

The model correctly identifies 170 of them.

Among 1,800 healthy people, it incorrectly flags 180.


CONFUSION MATRIX

TP = 170
FN = 30
FP = 180
TN = 1,620


SENSITIVITY

Among people who actually have the condition,
how many did I catch?

Sensitivity = TP / (TP + FN)

            = 170 / 200

            = 85%


SPECIFICITY

Among people who actually do not have the condition,
how many did I correctly leave negative?

Specificity = TN / (TN + FP)

            = 1620 / 1800

            = 90%


PRECISION / PPV

Among people I flagged as positive,
how many actually have the condition?

Precision = TP / (TP + FP)

          = 170 / 350

          ≈ 48.6%


IMPORTANT CORRECTION

Precision is NOT:

- false-positive rate
- how many sick people I missed


"How many sick people did I miss?" corresponds to:

False Negative Rate = FN / (TP + FN)

                    = 15%


MEMORY

Start from REALITY:

Actually sick
    -> sensitivity

Actually healthy
    -> specificity


Start from PREDICTION:

Predicted sick
    -> precision / PPV

Predicted healthy
    -> NPV


=======================================================
CASE 2 — PREVALENCE
=======================================================

QUESTION

What happens if I deploy the same classifier in a population
where the condition is much rarer?


KEY ANSWER

Precision / PPV can change dramatically.


WHY?

If disease prevalence decreases, there are many more healthy
people relative to sick people.

Even with unchanged sensitivity and specificity, false
positives can then greatly outnumber true positives.


Therefore:

Sensitivity and specificity may remain approximately stable
under pure prevalence shift.

Precision and NPV generally do not.


INTERVIEW TAKEAWAY

Never interpret precision without considering deployment
prevalence.


=======================================================
CASE 3 — CALIBRATION VS DISCRIMINATION
=======================================================

SCENARIO

Model A ranks positive cases very well.

But among people receiving approximately:

80% predicted risk

only:

40% actually experience the condition.


DIAGNOSIS

Model A has a calibration problem.

Its probabilities are overconfident.


CALIBRATION ASKS

"When the model predicts probability p,
does the event actually occur approximately p fraction
of the time?"


DISCRIMINATION ASKS

"Does the model tend to score positives higher than
negatives?"


Therefore:

A model can have:

excellent AUROC

AND

poor calibration.


WHY?

AUROC is fundamentally about ranking.

A useful intuition:

AUROC measures how likely a randomly chosen positive example
is to receive a higher score than a randomly chosen negative.


It does NOT require:

predicted 80% risk
    ->
actual event frequency 80%


=======================================================
CASE 4 — WHY BAD CALIBRATION MATTERS
=======================================================

Suppose predicted probabilities directly determine whether
a patient receives an intervention.


If:

predicted risk = 80%

but:

actual risk ≈ 40%


then decisions based on the numerical probability may be
inappropriate.


IMPORTANT CORRECTION

Poor calibration does NOT automatically imply:

"a higher false-positive rate."


False-positive rate depends on the chosen decision threshold.


The more precise statement is:

The model systematically overstates risk.

Therefore a downstream policy interpreting 0.8 as genuine
80% risk may trigger inappropriate interventions.


MEMORY

AUROC:

"Can I rank people?"


Calibration:

"Can I trust the probability?"


Threshold:

"When should I act?"


=======================================================
CASE 5 — CHOOSING A THRESHOLD
=======================================================

SCENARIO

Threshold = 0.30

Sensitivity = 97%
Specificity = 70%
Precision   = 18%


Threshold = 0.70

Sensitivity = 74%
Specificity = 95%
Precision   = 52%


This is a first-stage wearable screening system.

A positive result triggers a cheap, non-invasive
confirmatory test.


INITIAL CHOICE

Favor threshold 0.30.


WHY?

The downstream cost of a false positive is relatively low.

Meanwhile:

0.30 threshold catches 97% of positives.

0.70 threshold catches only 74%.


For screening, protecting sensitivity is often appropriate
when missing true cases is costly and false positives can be
resolved cheaply downstream.


BUT DO NOT STOP THERE.


Before choosing the operating point, ask:

1. What is the consequence of a false negative?

2. What is the deployment prevalence?

3. How many false alerts will 18% precision produce?

4. What is the burden of the confirmatory test?

5. How frequently will users receive alerts?

6. Is alarm fatigue a concern?


The threshold follows the decision problem.

It should not be chosen from AUROC or convention alone.


=======================================================
CASE 6 — RANDOM WINDOW SPLIT VS PARTICIPANT SPLIT
=======================================================

SCENARIO

Predict cardiac event within the next 24 hours.

Dataset contains many overlapping wearable windows.


Random window split:

AUROC = 0.94


Participant-disjoint split:

AUROC = 0.78


Deployment target:

new users.


WHICH NUMBER DO I TRUST?

For this deployment claim:

0.78 is much more relevant.


WHY?

The generalization claim is:

"Does the model work for unseen people?"


Therefore the evaluation should contain:

unseen people.


=======================================================
CASE 7 — WHY RANDOM WINDOW SPLITTING CAN LOOK TOO GOOD
=======================================================

Three major explanations should be considered.


1. PARTICIPANT LEAKAGE / PERSON-SPECIFIC SHORTCUTS

The same participant appears in training and testing.

The model may exploit:

- baseline physiology
- behavior
- activity patterns
- sensor characteristics
- personal routines


rather than learning something that generalizes to new users.


2. OVERLAPPING-WINDOW LEAKAGE

Suppose windows overlap heavily.

Then:

training window
    ->
[0 sec ... 60 sec]

test window
    ->
[10 sec ... 70 sec]


These windows share most of their raw signal.

Random splitting can therefore create nearly duplicated
training and testing examples.


3. TRUE BETWEEN-PARTICIPANT DISTRIBUTION SHIFT

Even without direct leakage, unseen users may differ in:

- baseline heart rate
- physiology
- activity
- adherence
- sensor quality
- disease characteristics
- demographics


Therefore new-participant generalization may simply be a
harder problem.


=======================================================
CASE 8 — PREDICTION-TIME LEAKAGE
=======================================================

Another important audit is:

"Did the model use information that would not actually be
available when the prediction must be made?"


Examples:

- future measurements
- normalization using future observations
- features collected after the event
- diagnosis-related information created after clinical
  suspicion arose


This can inflate evaluation substantially.


IMPORTANT DISTINCTION

Prediction-time leakage is an important general explanation
for unrealistically strong performance.

But it does not automatically explain the specific gap:

random split 0.94
vs
participant split 0.78


unless the evaluation pipelines differ in how that leakage
appears.


INTERVIEW PRINCIPLE

Separate:

"Why might the evaluation generally be optimistic?"

from:

"Why did THIS experimental manipulation change performance?"


=======================================================
CASE 9 — SUBGROUP PERFORMANCE
=======================================================

SCENARIO

Overall sensitivity = 92%

Under age 50:
Sensitivity = 94%

Over age 70:
Sensitivity = 78%


But the over-70 group contains only:

18 positive participants.


WHAT SHOULD I CONCLUDE?

The 78% result is a concerning signal.

It deserves investigation.

But I should NOT yet confidently conclude:

"The model performs worse for older users."


WHY?

The subgroup estimate is based on very little independent
positive data.

With 18 positive participants, a small number of people can
move sensitivity substantially.


Therefore:

effect size looks large

BUT

uncertainty may also be large.


=======================================================
CASE 10 — WHAT TO DO WITH THE SUBGROUP RESULT
=======================================================

First:

Quantify uncertainty.


For example:

participant-level confidence intervals.


Even better:

estimate uncertainty in the difference:

Sensitivity(over 70) - Sensitivity(under 50)


rather than looking only at two independent point estimates.


Second:

collect more data from the underrepresented subgroup.


Third:

look beyond sensitivity.


For example:

- specificity
- precision
- calibration
- false-alert burden


Fourth:

investigate alternative explanations.


The observed age gap could correlate with:

- signal quality
- wear time
- device generation
- missingness
- prevalence
- activity
- comorbidities
- labeling differences


Therefore do NOT jump from:

"older subgroup performs worse"

to:

"age causes model failure."


Age may be the relevant factor.

Or age may be correlated with the actual mechanism.


=======================================================
CASE 11 — SUBGROUP UNCERTAINTY
=======================================================

Weak conclusion:

"We only have 18 positive participants, so the subgroup
result is meaningless."


Also weak:

"Sensitivity is 78% versus 94%, therefore the model clearly
fails older users."


Better:

"The observed gap is large enough that I would treat it as
a warning, but the over-70 estimate is based on only 18
positive participants and is therefore likely uncertain.

I'd quantify uncertainty at the participant level, examine
the uncertainty in the performance gap, investigate
correlated factors such as signal quality and missingness,
and collect more data before making a strong subgroup
claim."


MEMORY

Small subgroup:

NOT

"ignore result."


Instead:

"warning signal + large uncertainty + collect evidence."


=======================================================
CASE 12 — WINDOWS ARE NOT PEOPLE
=======================================================

Suppose:

100 participants

each contributes:

10,000 windows.


I have:

1,000,000 windows.


Do I have one million independent samples?

NO.


Repeated measurements from the same participant are
correlated.


Therefore:

The correct independent unit may be the participant.


This affects:

- confidence intervals
- statistical tests
- bootstrapping
- model comparison
- train/test splitting


MEMORY

Millions of windows do not create millions of independent
people.


=======================================================
CASE 13 — BOOTSTRAPPING
=======================================================

If my deployment claim concerns new participants and each
participant contributes many correlated windows:

bootstrap PARTICIPANTS

rather than independently bootstrapping windows.


Conceptually:

sample participants with replacement

    ↓

include their observations

    ↓

calculate metric

    ↓

repeat


For comparing two models evaluated on the same participants:

preserve the pairing.


For every bootstrap sample:

Metric(Model B) - Metric(Model A)


This gives uncertainty on the improvement itself.


=======================================================
THE BIG INTERVIEW FRAMEWORK
=======================================================

When Haraldur gives me a health-ML result, do NOT immediately
suggest a better architecture.


Work through:


1. DECISION

What health decision is the system supporting?


2. CLAIM

What exactly are we claiming?

New windows?

New users?

Future data?

New device?

New population?


3. METRIC

Does the metric match the decision?

Screening
    -> sensitivity may dominate

Alert system
    -> precision / false-alert burden matters

Risk prediction
    -> calibration matters


4. INDEPENDENCE

What is the true independent unit?

Participant?

Episode?

Hospital?

Trajectory?


5. SPLIT

Does the train/test split match the generalization claim?


6. LEAKAGE

Could train and test share:

participants?

overlapping windows?

future information?

post-outcome information?


7. UNCERTAINTY

How many independent observations actually support the
result?

What are the confidence intervals?

How uncertain is the DIFFERENCE between models/groups?


8. ALTERNATIVE EXPLANATIONS

If performance differs between groups/settings:

What else changed?

Population?

Signal quality?

Missingness?

Device?

Prevalence?

Labels?


9. DISCRIMINATING EXPERIMENT

What experiment separates these explanations?


10. DEPLOYMENT CONSEQUENCE

Translate percentages into:

missed cases

false alerts

confirmatory tests

user burden

clinical consequences


=======================================================
COMMON TRAPS TO AVOID
=======================================================

TRAP 1

Precision = false-positive rate.

WRONG.

Precision asks:

Among predicted positives, how many are true?


-----------------------------------------------

TRAP 2

Poor calibration means high false-positive rate.

NOT NECESSARILY.

Calibration concerns probability reliability.

FPR depends on the threshold.


-----------------------------------------------

TRAP 3

AUROC is excellent, therefore the model is deployable.

WRONG.

Still need:

operating point
calibration
deployment prevalence
uncertainty
subgroups
external/generalization evidence
workflow consequences


-----------------------------------------------

TRAP 4

Tens of thousands of windows means tiny uncertainty.

WRONG if windows come from a small number of people.


-----------------------------------------------

TRAP 5

A subgroup metric is worse, therefore demographic membership
causes the failure.

WRONG.

Investigate correlated mechanisms.


-----------------------------------------------

TRAP 6

Small subgroup means ignore the result.

WRONG.

Treat it as:

potentially important signal

+

high uncertainty.


-----------------------------------------------

TRAP 7

Bad participant-disjoint performance means immediately
change the architecture.

WRONG.

First determine whether the gap comes from:

leakage
shortcuts
true distribution shift
measurement differences
missingness
other evaluation issues


=======================================================
FAST RETRIEVAL — SAY THESE WITHOUT NOTES
=======================================================

Sensitivity:

"Of the actually positive people, how many did I catch?"


Specificity:

"Of the actually negative people, how many did I correctly
leave negative?"


Precision:

"Of the people I flagged, how many were actually positive?"


Calibration:

"Can I interpret the predicted probability as risk?"


AUROC:

"How well does the model rank positives above negatives?"


Threshold:

"At what score should the system act, given the costs?"


Participant-disjoint split:

"Does it generalize to unseen people?"


Confidence interval:

"How uncertain is my estimate?"


Subgroup gap:

"Signal worth investigating; quantify uncertainty before
making a strong claim."


Prospective validation:

"Does my fixed system work on what happens next?"


=======================================================
FINAL MENTAL MODEL
=======================================================

When I see an impressive health-ML number, my first reaction
should NOT be:

"How can I improve the model?"


It should be:

"What exactly does this number allow me to claim?"


Then:

CLAIM
    ↓
DECISION
    ↓
METRIC
    ↓
INDEPENDENT UNIT
    ↓
SPLIT + LEAKAGE
    ↓
UNCERTAINTY
    ↓
ALTERNATIVE EXPLANATIONS
    ↓
DISCRIMINATING EXPERIMENT
    ↓
DEPLOYMENT CONSEQUENCE


That is the scientific-jgment loop.
```
