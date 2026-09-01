# On-site — Haraldur: Model usability

Companion to [`2026-08-27_onsite-haraldur.md`](2026-08-27_onsite-haraldur.md) and [`2026-09-01_onsite-haraldur-health-evaluation.md`](2026-09-01_onsite-haraldur-health-evaluation.md).

```text
HEALTH ML — LESSON 2
CALIBRATION, THRESHOLDS, ROC & PRECISION–RECALL
=================================================

Suppose a model outputs:

P(AFib | x) = 0.80


There are THREE separate questions:

1. DISCRIMINATION
   Can the model rank high-risk people above low-risk people?

2. CALIBRATION
   Does "80%" actually mean approximately 80% risk?

3. DECISION / THRESHOLD
   At what probability should we take an action?


These are NOT the same thing.


=================================================
1. DISCRIMINATION
=================================================

Imagine two people:

Alice actually has AFib.
Bob does not.

Model predicts:

Alice: 0.80
Bob:   0.20


The ranking is correct.


A model has good discrimination if positive cases tend to
receive higher scores than negative cases.


It does NOT require the probabilities themselves to be correct.


For example:

Model A:

AFib patients:       ~0.90
non-AFib patients:   ~0.60


This could have excellent discrimination:

positives > negatives


but terrible calibration.

A prediction of 0.90 may not actually correspond to a
90% probability of AFib.


=================================================
2. CALIBRATION
=================================================

QUESTION:

When the model predicts approximately 80% risk,
does the event actually occur approximately 80% of the time?


Example:

Take 1000 predictions around:

0.80


If roughly:

800 actually have the condition

then the model is well calibrated around that score.


If only:

300 actually have it

then the model is strongly overconfident.


INTUITION:

DISCRIMINATION asks:

"Did I rank people correctly?"


CALIBRATION asks:

"Do my probabilities mean what they say?"


=================================================
3. WHY CALIBRATION MATTERS IN HEALTH
=================================================

Suppose:

Patient A: predicted risk 5%
Patient B: predicted risk 30%
Patient C: predicted risk 80%


If clinicians or downstream systems use these probabilities
to make decisions, their numerical meaning matters.

A model that ranks patients correctly but systematically says
80% when the real probability is 30% can lead to bad decisions.


Therefore:

GOOD AUROC DOES NOT IMPLY GOOD CALIBRATION.


=================================================
4. HOW TO CHECK CALIBRATION
=================================================

A common approach is a reliability diagram.

Group predictions into bins:

0.0 - 0.1
0.1 - 0.2
...
0.9 - 1.0


For each bin compare:

average predicted probability

versus

observed event frequency.


Perfect calibration would approximately follow:

predicted 10% -> observed ~10%
predicted 40% -> observed ~40%
predicted 80% -> observed ~80%


Another useful metric:

Brier score

= mean squared error between probability and outcome.


Lower is better.


=================================================
5. THRESHOLDS
=================================================

The model produces a score:

p = P(condition | x)


To make a binary decision:

if p >= threshold:
    positive
else:
    negative


Example:

threshold = 0.50


But 0.50 is NOT automatically the correct threshold.


=================================================
6. WHAT HAPPENS WHEN THRESHOLD CHANGES?
=================================================

LOWER THRESHOLD:

More people become positive.

Typically:

Sensitivity ↑
False positives ↑
Specificity ↓
Precision often ↓


HIGHER THRESHOLD:

Fewer people become positive.

Typically:

Sensitivity ↓
False positives ↓
Specificity ↑
Precision often ↑


So threshold selection is a TRADEOFF.


=================================================
7. HEALTH EXAMPLE
=================================================

Suppose the model is a first-stage wearable screening system.

An alert says:

"We detected something unusual.
Consider taking an ECG."


The downstream action is:

cheap
non-invasive
low risk


You may choose a relatively LOW threshold.

Why?

You prefer catching more possible cases.

Sensitivity matters strongly.


Now imagine instead that a positive prediction automatically
triggers an expensive or invasive procedure.


Then false positives are much more costly.

You may require:

higher specificity
higher precision
and potentially a higher threshold.


KEY PRINCIPLE:

THE THRESHOLD SHOULD FOLLOW THE DECISION COST,
NOT CONVENTION.


=================================================
8. ROC CURVE
=================================================

Every possible threshold produces:

Sensitivity = TP / (TP + FN)

and:

False Positive Rate = FP / (FP + TN)

                           = 1 - Specificity


The ROC curve plots:

Y axis:
Sensitivity / True Positive Rate

X axis:
False Positive Rate


as the threshold changes.


Low threshold:

catch many positives
but generate more false positives.


High threshold:

fewer false positives
but miss more positives.


=================================================
9. AUROC
=================================================

AUROC summarizes discrimination across thresholds.


INTUITIVE INTERPRETATION:

Take:

one randomly selected positive patient

and

one randomly selected negative patient.


AUROC is related to the probability that the model assigns
the positive patient a higher score than the negative patient.


AUROC = 0.5

roughly random ranking.


AUROC = 1.0

perfect ranking.


IMPORTANT:

AUROC tells you about RANKING.

It does NOT tell you:

- whether probabilities are calibrated
- which threshold to use
- what precision will be in deployment
- whether the model is clinically useful


=================================================
10. WHY AUROC CAN BE MISLEADING FOR RARE CONDITIONS
=================================================

Suppose:

10 positive patients
990 negative patients


There are many negatives.

A classifier can maintain a relatively low false-positive RATE
while still generating a substantial number of false-positive
ALERTS.


Therefore, for rare positive events, I also want to examine
precision and recall directly.


=================================================
11. PRECISION-RECALL CURVE
=================================================

PR curve plots:

Precision

versus

Recall / Sensitivity


as the threshold changes.


Recall asks:

"How many true cases did I catch?"


Precision asks:

"How many of my alerts were real?"


This makes PR curves particularly informative when:

- the positive class is rare
- false alarms matter
- we care strongly about detecting the positive class


=================================================
12. AUROC VS PR-AUC
=================================================

AUROC:

"How well does the model rank positives above negatives?"


PR-AUC:

"What precision/recall tradeoff do I obtain while trying
to find the positive class?"


For highly imbalanced health problems:

PR-AUC is often especially informative.


But neither metric alone determines deployment readiness.


=================================================
13. PREVALENCE AGAIN
=================================================

Precision depends strongly on prevalence.

Therefore:

PR curves / precision measured in one population may not
directly describe what happens in another population with
very different prevalence.


This is why deployment population matters.


=================================================
14. OPERATING POINT
=================================================

In practice, I usually care about a particular point on these
curves.


For example:

"We require at least 95% sensitivity."


Then among thresholds satisfying that requirement, I might ask:

Which gives the best specificity?

What precision does that produce at deployment prevalence?

How many false alerts per 1000 users?

Is that operationally acceptable?


This is much more meaningful than simply saying:

"AUROC = 0.94."


=================================================
15. CALIBRATION CAN CHANGE
=================================================

Even if a model was calibrated during development,
calibration can degrade under distribution shift.


Examples:

different population
different prevalence
different device
different measurement process
different age distribution
different deployment environment


Therefore calibration should be checked on the population
where the model will actually be used.


=================================================
16. INTERVIEW QUESTION
=================================================

Interviewer:

"Our AFib model has AUROC = 0.94.
Is it ready to deploy?"


WEAK ANSWER:

"0.94 is very good, so probably yes."


STRONG ANSWER:

"Not from AUROC alone.

AUROC tells me that discrimination is strong, but I would want
to evaluate the model at the intended operating point.

For the deployment population, I'd look at sensitivity,
specificity, and especially precision given the expected
prevalence.

I'd choose the threshold based on the consequences of false
positives and false negatives in the actual workflow.

I'd also check whether the predicted probabilities are
calibrated, and whether performance and calibration remain
stable across relevant subgroups and deployment conditions."


=================================================
17. INTERVIEW FRAMEWORK
=================================================

When someone gives you a health-model score, ask:

1. WHAT IS THE TASK?

   screening?
   diagnosis?
   risk estimation?


2. WHAT DOES THE SCORE MEAN?

   ranking score?
   calibrated probability?


3. WHAT IS THE PREVALENCE?


4. WHAT ARE THE COSTS?

   false positive?
   false negative?


5. WHAT OPERATING POINT DO WE NEED?

   required sensitivity?
   required specificity?


6. WHAT HAPPENS AT THAT THRESHOLD?

   sensitivity
   specificity
   precision
   false alerts / user


7. IS THE MODEL CALIBRATED?


8. DOES THIS HOLD IN THE DEPLOYMENT POPULATION?


=================================================
ONE-LINE MEMORY
=================================================

Discrimination:
"Do I rank the risky people above the non-risky people?"

Calibration:
"When I say 80%, does it really mean 80%?"

Threshold:
"At what score should I act?"

ROC:
"How does sensitivity trade against false-positive rate?"

PR:
"How does catching more true cases trade against trustworthy alerts?"

Deployment:
"Choose the operating point based on the real cost of FP and FN,
not because 0.5 is a convenient threshold."
```
