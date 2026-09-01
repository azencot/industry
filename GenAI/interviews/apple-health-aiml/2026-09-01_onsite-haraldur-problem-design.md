# On-site — Haraldur: Health study and prediction-problem design

Companion to [`2026-08-27_onsite-haraldur.md`](2026-08-27_onsite-haraldur.md), [`2026-09-01_onsite-haraldur-health-evaluation.md`](2026-09-01_onsite-haraldur-health-evaluation.md), [`2026-09-01_onsite-haraldur-model-usability.md`](2026-09-01_onsite-haraldur-model-usability.md), and [`2026-09-01_onsite-haraldur-generalization-leakage.md`](2026-09-01_onsite-haraldur-generalization-leakage.md).

```text
HEALTH ML — LESSON 4
HEALTH STUDY & PREDICTION-PROBLEM DESIGN
========================================

CORE IDEA

Before asking:

"What model should I use?"

ask:

"What exactly am I trying to predict,
for whom,
using what information,
at what time,
and for what decision?"


Many health-ML failures are not architecture failures.

They come from incorrectly defining:

- population
- outcome / label
- observation window
- prediction time
- prediction horizon
- available inputs
- clinical/use-case action


A useful framework:

POPULATION
    ↓
OUTCOME / LABEL
    ↓
OBSERVATION WINDOW
    ↓
PREDICTION TIME
    ↓
PREDICTION HORIZON
    ↓
AVAILABLE INPUTS
    ↓
DECISION / ACTION
    ↓
EVALUATION


========================================
1. START WITH THE DECISION, NOT THE MODEL
========================================

Suppose someone says:

"We want to predict atrial fibrillation from Apple Watch data."


That is NOT yet a well-defined ML problem.


Possible tasks include:


A. DETECTION

"Is AFib happening right now?"


B. NEAR-TERM PREDICTION

"Will AFib occur in the next 24 hours?"


C. RISK STRATIFICATION

"Is this person at elevated risk of AFib over the
next 6 months?"


D. SCREENING

"Should this person receive additional testing?"


These may use similar data but are fundamentally
different problems.


They have different:

- labels
- observation windows
- prediction horizons
- acceptable errors
- evaluation metrics
- deployment workflows


FIRST QUESTION:

"What decision will this prediction support?"


========================================
2. DEFINE THE TARGET POPULATION
========================================

Ask:

"Who will this model be used for?"


Examples:

- general population
- people with known cardiovascular disease
- people above a certain age
- existing Watch users
- people referred for monitoring
- people with previous symptoms


Why does this matter?


Because population determines:

- prevalence
- available data
- expected signal quality
- baseline risk
- acceptable tradeoffs
- generalization requirements


Example:

A model evaluated in a high-risk cardiology cohort
may have very different precision when deployed to
millions of generally healthy users.


Therefore:

DEVELOPMENT POPULATION ≠ DEPLOYMENT POPULATION

can be a major problem.


========================================
3. DEFINE THE OUTCOME / LABEL
========================================

"What exactly counts as positive?"


Suppose the task is AFib.

Possible ground truth could come from:

- clinical ECG
- physician diagnosis
- medical record code
- self-report
- another wearable algorithm


These labels do NOT have equal validity.


A medical record code might mean:

"The patient was previously diagnosed with AFib"

rather than:

"AFib was occurring during this wearable window."


That difference completely changes the task.


KEY QUESTION:

"What biological or clinical event does the label
actually represent?"


========================================
4. LABEL QUALITY
========================================

Health labels are often noisy.

Sources of noise include:

- imperfect diagnostic tests
- inconsistent physician labeling
- billing codes
- self-report
- delayed diagnosis
- incomplete medical records


Suppose:

y = 0

Does that mean:

"The patient definitely does not have the disease"?

Or:

"We did not observe a diagnosis"?


Those are very different.


IMPORTANT DISTINCTION:

NEGATIVE LABEL

does not necessarily mean

CONFIRMED NEGATIVE.


========================================
5. LABEL TIMING
========================================

The timing of the label relative to the input matters.


Suppose:

Watch data:
Monday → Friday

Diagnosis:
Thursday


And the task is:

"Predict diagnosis by Friday."


If Thursday's physiological consequences of the disease
are already in the input, the model may actually be
DETECTING the existing condition rather than predicting it.


Therefore define:


OBSERVATION WINDOW

        ↓

PREDICTION TIME

        ↓

PREDICTION HORIZON


Example:


past 7 days              next 24 hours
<----------->|<---------------->
             t
        prediction


Only information available before t should be used.


========================================
6. OBSERVATION WINDOW
========================================

The observation window answers:

"How much history can the model see?"


Examples:

past 30 seconds
past hour
past 24 hours
past week
past month


Longer is not automatically better.


Long windows:

+ more context
+ long-term trends

but:

- more missingness
- greater compute
- greater opportunity for leakage
- potentially stale information


The appropriate window depends on the mechanism
and use case.


========================================
7. PREDICTION HORIZON
========================================

The prediction horizon asks:

"How far into the future are we predicting?"


Examples:

next 5 minutes
next 24 hours
next week
next year


Usually:

farther horizon
→ weaker immediate signal
→ harder prediction


But there is another important issue:

ACTIONABILITY.


Suppose I predict an adverse event with excellent accuracy
only 30 seconds before it happens.

That may be scientifically interesting but operationally
useless if intervention requires 30 minutes.


Therefore:

The prediction horizon should reflect the time needed
for the prediction to be useful.


========================================
8. DETECTION VS PREDICTION
========================================

This is an important health-ML distinction.


DETECTION:

"Is the condition present now?"


PREDICTION:

"Will the condition occur later?"


A model claimed to predict disease might actually detect
early manifestations already present in its input.


That isn't necessarily bad.

But it is a DIFFERENT CLAIM.


Ask:

"At prediction time, has the event already begun biologically
or clinically?"


========================================
9. WHAT INFORMATION EXISTS AT PREDICTION TIME?
========================================

For every feature ask:

"Would I actually know this at inference time?"


Potential inputs:

- heart rate
- PPG
- accelerometer
- sleep
- medications
- demographics
- previous diagnoses
- user-entered symptoms


Potential problem:

A feature may technically precede the label in the database
while still not have been available when the real-world
prediction would have occurred.


This creates leakage.


RULE:

Reconstruct the information state at prediction time.


========================================
10. LABEL LEAKAGE / SHORTCUTS
========================================

Suppose we predict:

"Will this patient receive an AFib diagnosis?"


The model uses:

- Watch signals
- number of cardiology visits
- ECG orders


The model performs extremely well.


Why?


Maybe ECG ordering is essentially a proxy for:

"A clinician already suspects AFib."


The model may predict the healthcare process rather than
the underlying health state.


This can happen with wearable data too.


Examples:

- user starts monitoring because symptoms began
- medication change reveals diagnosis
- device usage changes after physician advice
- missingness correlates with clinical intervention


Always ask:

"Could the model solve this using a shortcut unrelated to
the physiological mechanism I care about?"


========================================
11. MISSINGNESS IS PART OF THE PROBLEM
========================================

Suppose we require:

7 days of Watch history.


But many users only have:

2 days of measurements.


Options include:

- exclude them
- impute
- use masks
- use variable-length models
- require minimum coverage


But exclusion changes the target population.


If intermittent users are systematically different,
requiring complete data introduces selection bias.


Therefore ask:

"Who disappears from my dataset when I impose this
data-quality requirement?"


This connects directly to distribution shift.


========================================
12. CHOOSE THE SIMPLEST MEANINGFUL BASELINE
========================================

Before a foundation model, ask:

"What would a simple solution do?"


Possible baselines:

- prevalence / majority prediction
- logistic regression
- simple clinical variables
- rolling statistics + XGBoost
- single-modality model
- existing clinical score


Why?


Suppose:

Multimodal Transformer AUROC = 0.91
XGBoost                  = 0.90


Then ask:

"What does the Transformer buy?"


Potential answers:

- transfer
- robustness
- low-label performance
- personalization
- richer temporal reasoning
- better difficult slices


Or perhaps:

not enough.


A strong architecture is not automatically a useful system.


========================================
13. MULTIMODALITY SHOULD HAVE A REASON
========================================

Suppose we have:

PPG
accelerometer
heart rate
sleep
audio
text


Do NOT automatically use all modalities.


For each modality ask:

"What information should this contribute?"


Example:

PPG:
cardiovascular waveform information

Accelerometer:
motion/activity context and artifact information

Heart rate:
coarse cardiac dynamics

Sleep:
longer-term behavioral/physiological state


Then test:

Does each modality actually contribute the capability
we expected?


A+B outperforming A does not automatically establish WHY.


========================================
14. DEFINE SUCCESS BEFORE TRAINING
========================================

Don't wait for results and then choose the metric
that looks best.


Before training ask:

"What would make this model useful?"


Example:

For screening:

Sensitivity must be >= 95%

and perhaps:

false alerts must remain below an acceptable burden.


Or:

Model must improve sensitivity over baseline without
degrading specificity below an operational requirement.


This prevents:

"AUROC improved, therefore success."


Predefine:

- primary metric
- important secondary metrics
- critical subgroup floors
- operating point
- failure criteria


========================================
15. MATCH METRIC TO USE CASE
========================================

SCREENING:

often emphasize sensitivity.


ALERT SYSTEM:

precision / false-alert burden becomes important.


RISK ESTIMATION:

calibration becomes especially important.


RARE CONDITION:

precision-recall behavior becomes important.


POPULATION DEPLOYMENT:

subgroup and external generalization become important.


No metric is universally correct.


The metric follows the decision.


========================================
16. DESIGN THE SPLIT FROM THE CLAIM
========================================

Suppose deployment is:

new Watch users.


Then:

participant-disjoint evaluation.


Suppose deployment is:

future behavior.


Then consider:

temporal split.


Suppose deployment includes:

different hardware generations.


Then evaluate:

device shift.


Suppose deployment is broad population.


Then consider:

external population validation.


This connects directly to Lesson 3.


========================================
17. CASE STUDY
========================================

INTERVIEWER:

"We have heart rate, accelerometer and sleep data from
Apple Watch users.

We want to predict whether someone will develop a cardiac
condition.

How would you approach it?"


WEAK ANSWER:

"I would patch each signal, use modality-specific encoders,
and fuse them with cross-attention."


WHY WEAK?

We don't even know what the prediction problem is yet.


STRONGER ANSWER:

"Before choosing the architecture, I'd define the prediction
problem precisely.

First, what population are we targeting and what clinical
decision should the prediction support?

Second, I'd define the outcome and its ground truth. Does
'develop the condition' mean physician diagnosis, ECG-confirmed
onset, or something else?

Then I'd define the observation window and prediction horizon.
For example, perhaps we use the previous seven days of wearable
data to predict an event in the following 24 hours.

I'd make sure every input is genuinely available at prediction
time and audit potential leakage or shortcuts.

I'd then characterize missingness and determine whether our
data requirements systematically exclude certain users.

Before using a complex multimodal architecture, I'd establish
simple clinical and classical ML baselines.

Finally, I'd define success based on the intended workflow —
for example sensitivity at an acceptable false-alert burden —
and evaluate on participant-disjoint data with relevant
subgroup and robustness analyses.

Only after defining those pieces would I decide what
architecture is appropriate."


========================================
18. ANOTHER CASE: PREDICTING FALLS
========================================

TASK:

"Predict falls using wearable sensors."


Questions BEFORE modeling:


POPULATION

Older adults?
General population?
People with previous falls?


LABEL

What constitutes a fall?

Self-report?
Clinical record?
Sensor-confirmed?


OBSERVATION WINDOW

Last hour?
Last day?
Last week?


HORIZON

Next 5 minutes?
Next day?
Next month?


ACTION

Warn user?
Notify caregiver?
Recommend intervention?


FALSE NEGATIVE COST

Missed fall risk.


FALSE POSITIVE COST

Alarm fatigue / unnecessary intervention.


MISSINGNESS

Do high-risk people wear the device differently?


BASELINE

Age + previous falls + simple activity statistics?


Only after answering these questions should architecture
become the central discussion.


========================================
19. MODEL PERFORMANCE VS CLINICAL UTILITY
========================================

A model can be statistically strong but operationally weak.


Example:

AUROC = 0.95


But perhaps:

- prediction comes too late
- precision is too low
- alerts are too frequent
- high-risk subgroup performs poorly
- required sensor is often unavailable
- probability is badly calibrated
- improvement over simple baseline is tiny


Therefore:

MODEL QUALITY

is not identical to

USEFUL HEALTH SYSTEM.


========================================
20. REUSABLE FRAMEWORK
========================================

When given a vague health-ML problem, walk through:


1. POPULATION

Who are we predicting for?


2. OUTCOME

What exactly is the label?

How trustworthy is it?


3. OBSERVATION WINDOW

What historical data can we use?


4. PREDICTION TIME

At what exact moment is the prediction made?


5. PREDICTION HORIZON

What future interval are we predicting?


6. AVAILABLE INFORMATION

What genuinely exists at prediction time?


7. DECISION

What happens because of the prediction?


8. ERRORS

What are the costs of FP and FN?


9. BASELINE

What simple approach should we beat?


10. EVALUATION

What split, metrics, slices and operating point match
the deployment claim?


Only then:

11. MODEL

What architecture best fits the resulting problem?


========================================
HARALDUR ANSWER TEMPLATE
========================================

"I'd resist choosing the model initially and first formulate
the health problem precisely.

I'd define the target population, the outcome and how reliable
its ground truth is, the observation window, and the prediction
horizon.

I'd then reconstruct exactly what information would be
available at prediction time, because health datasets can
contain subtle temporal leakage and shortcuts.

I'd characterize missingness and selection effects, establish
simple clinical or classical ML baselines, and define success
based on the downstream decision and relative costs of false
positives and false negatives.

Then I'd design an evaluation that matches the intended
generalization — for example participant-disjoint and temporal
validation.

Once those pieces are fixed, I'd choose the model architecture.

The architecture should follow the prediction problem rather
than define it."


========================================
ONE-LINE MEMORY
========================================

Population:
"Who will actually use this?"

Label:
"What exactly does positive mean, and do I trust it?"

Observation:
"What history can I see?"

Prediction time:
"What do I genuinely know at this moment?"

Horizon:
"How far ahead am I predicting, and is that actionable?"

Decision:
"What happens when the model says positive?"

Baseline:
"Does complexity actually buy something?"

Evaluation:
"Does my experiment reproduce the intended deployment?"

Core principle:
"Define the health decision first; choose the model second."
```
