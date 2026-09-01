# On-site — Haraldur: Health-system evaluation

Companion to [`2026-08-27_onsite-haraldur.md`](2026-08-27_onsite-haraldur.md).

```text
HEALTH ML — LESSON 1
SENSITIVITY, SPECIFICITY, PRECISION & PREVALENCE
=================================================

CORE SETUP

For binary classification:

                         ACTUAL
                    Positive   Negative
                  -----------------------
Predicted Positive |   TP    |   FP
Predicted Negative |   FN    |   TN


The easiest way to remember the metrics is to ask:

"Which population am I starting from?"


=================================================
1. SENSITIVITY / RECALL
=================================================

QUESTION:

Of the people who ACTUALLY HAVE the condition,
how many did I catch?

Sensitivity = TP / (TP + FN)


INTUITION:

Start with the sick population.

Among them:
    how many did the model find?


HIGH SENSITIVITY = FEW FALSE NEGATIVES.


Memory:

SENSITIVITY = "Don't miss disease."


Example:

100 people actually have AFib.
Model identifies 90.

Sensitivity = 90 / 100 = 90%


The remaining 10 are false negatives.


WHEN IT MATTERS:

Often especially important for screening.

If missing a condition is dangerous, we may tolerate
more false positives in exchange for higher sensitivity.


=================================================
2. SPECIFICITY
=================================================

QUESTION:

Of the people who ACTUALLY DO NOT HAVE the condition,
how many did I correctly leave negative?

Specificity = TN / (TN + FP)


INTUITION:

Start with the healthy population.

Among them:
    how many did the model correctly leave alone?


HIGH SPECIFICITY = FEW FALSE POSITIVES.


Memory:

SPECIFICITY = "Don't falsely diagnose healthy people."


Example:

900 people do not have AFib.

720 correctly test negative.
180 incorrectly test positive.

Specificity = 720 / 900 = 80%


=================================================
3. PRECISION / POSITIVE PREDICTIVE VALUE (PPV)
=================================================

QUESTION:

Of everyone THE MODEL CALLED POSITIVE,
how many actually have the condition?

Precision = TP / (TP + FP)


INTUITION:

Start with the model's alarms.

Among all alarms:
    how many were real?


Memory:

PRECISION = "When I raise an alarm, how much should you trust it?"


Example:

Model raises 280 AFib alerts.

90 are real AFib.
190 would be false positives.

Precision = 90 / 280 = 32.1%


So roughly:

1 in 3 alerts is correct.


=================================================
THE MOST IMPORTANT DISTINCTION
=================================================

SENSITIVITY:

    Start from REALITY.

    "Of the sick people, how many did I find?"


PRECISION:

    Start from PREDICTIONS.

    "Of the people I called sick, how many really are?"


SPECIFICITY:

    Start from REALITY.

    "Of the healthy people, how many did I correctly leave alone?"


A useful mental diagram:


                    ACTUAL POSITIVE
                         |
                         v
                   SENSITIVITY
                  "Did I catch it?"


PREDICTED POSITIVE ---> PRECISION
                       "Was my alarm right?"


                    ACTUAL NEGATIVE
                         |
                         v
                    SPECIFICITY
                  "Did I leave it alone?"


=================================================
4. NEGATIVE PREDICTIVE VALUE (NPV)
=================================================

QUESTION:

Of everyone the model calls negative,
how many actually are negative?

NPV = TN / (TN + FN)


Memory:

"When I give the all-clear, how trustworthy is it?"


=================================================
5. PREVALENCE
=================================================

Prevalence means:

How common is the condition in the population?

Prevalence = number with condition / total population


This is extremely important because:

PRECISION DEPENDS ON PREVALENCE.


Example:

Suppose a model has:

Sensitivity = 90%
Specificity = 90%


POPULATION A:

50% have the disease.

Out of 1000:

500 sick:
    450 TP
    50 FN

500 healthy:
    450 TN
    50 FP

Precision:

450 / (450 + 50)
= 90%


Now deploy THE SAME MODEL in a population where
only 1% have the disease.


Out of 10,000:

100 sick:
    90 TP
    10 FN

9,900 healthy:
    9,900 * 10% = 990 FP


Precision:

90 / (90 + 990)
≈ 8.3%


Same:

Sensitivity = 90%
Specificity = 90%


But precision fell:

90% -> 8.3%


WHY?

Because when disease is rare, even a relatively small
false-positive RATE can produce many false positives.


=================================================
6. ACCURACY CAN BE MISLEADING
=================================================

Accuracy:

(TP + TN) / total


Suppose disease prevalence is 1%.

A useless model says:

"healthy"

for everyone.


Then:

Accuracy = 99%


but:

Sensitivity = 0%


It catches nobody.


Therefore:

High accuracy does NOT necessarily imply a useful
health classifier.


=================================================
7. F1
=================================================

F1 combines precision and recall:

F1 = 2 * Precision * Recall
         ------------------
         Precision + Recall


Useful when:

- positive class matters
- classes are imbalanced
- both precision and recall matter


But:

F1 ignores true negatives.

So it is NOT automatically the right health metric.


=================================================
8. SCREENING VS CONFIRMATION
=================================================

SCREENING:

Often prioritize sensitivity.

Goal:

Don't miss people who might have the condition.

It may be acceptable to generate some false positives
if they receive a cheap/non-invasive confirmatory test.


CONFIRMATORY / EXPENSIVE INTERVENTION:

Specificity and/or precision may become much more important.

If a positive result triggers:

- expensive testing
- anxiety
- medication
- invasive intervention

false positives can be costly.


There is no universally correct metric.

The right metric depends on:

"What happens when the model is wrong?"


=================================================
9. INTERVIEW FRAMEWORK
=================================================

When given a health classifier, ask:

1. What is the positive event?

2. What is the prevalence?

3. What is worse:
       false positive
   or
       false negative?

4. Is this:
       screening
   or
       diagnosis / intervention?

5. What are:
       sensitivity
       specificity
       precision?

6. What happens downstream after an alert?

7. Are these numbers measured in the actual
   deployment population?


=================================================
INTERVIEW ANSWER TEMPLATE
=================================================

"I wouldn't choose the metric without understanding the
clinical workflow.

If this is a first-stage screening system, I would generally
care strongly about sensitivity because I don't want to miss
true cases.

But I would also examine precision because a high false-alarm
burden may make the system unusable.

And because precision depends on prevalence, I would want to
evaluate it at the prevalence expected in the deployment
population rather than relying only on the benchmark."


=================================================
ONE-LINE MEMORY
=================================================

Sensitivity:
"Of the sick, how many did I catch?"

Specificity:
"Of the healthy, how many did I leave alone?"

Precision:
"Of my alarms, how many were real?"

NPV:
"Of my all-clears, how many were correct?"

Prevalence:
"How common is the condition?"

Health-ML judgment:
"The right metric depends on the cost of being wrong."
```
