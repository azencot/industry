# On-site — Vincent Chan (Tue 9/8 4:05 PDT)

**Track:** technical leadership / system thinking + multimodal **strategy**. **Conf:** medium-high. Last of five same day — energy, not a fresh Friday morning.  
**Who (private):** Eng Manager, Health AIML. Recruits multimodal LLMs / fusion / VLMs / TS. Stats PhD (Wisconsin); menstrual-cycle patent. Thanked on TS-LLM.  
**Hub:** [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)

He cares whether you can turn an **ambiguous multimodal-health objective into a research program**, not RoPE.

IC verbs. **Not** “I’d facilitate consensus.” **Not** associate professor / my lab. Why-Apple only if pulled: [`2026-08-20_why-apple-health-drill.md`](2026-08-20_why-apple-health-drill.md) — never “impact at scale.”

---

APPLE — VINCENT PRACTICE DAY
Technical Leadership & System Thinking
=======================================

GOAL

Vincent is not primarily testing:

"Do you know architecture X?"

or:

"Can you tell me a leadership story?"


The likely question is:

Can I take an ambiguous real-world ML problem and reason about the
ENTIRE system?

Can I go wide:

population
data
legal/privacy constraints
labels
modeling
evaluation
deployment
cross-functional dependencies

while still going deep when a technical decision matters?


CORE FRAMEWORK

OBJECTIVE
→ POPULATION
→ DATA / LABELS / PERMISSIBILITY
→ BASELINE
→ REPRESENTATION / MODEL
→ EVALUATION
→ DEPLOYMENT
→ MONITORING


At every stage ask:

WHAT CAN FAIL?

WHAT INTERACTS WITH THIS DECISION?

WHAT IS THE CHEAPEST WAY TO LEARN?

WHAT TRADEOFF AM I MAKING?

WHAT EVIDENCE WOULD CHANGE MY DECISION?


APPLE EMPLOYEE SIGNALS TO KEEP IN MIND

- Include all relevant populations.
- Think about differences such as BMI / body characteristics.
- Think about different gestures / behaviors.
- Think about how data can legally be collected and used.
- L5 requires cross-functional collaboration.
- Start modeling simple; increase complexity only when justified.
- Define how the model will be evaluated.
- Show both wide and deep judgment.
- Think through deployment, not only research metrics.
- Results.
- Innovation.
- Teamwork.


============================================================
BLOCK 0 — 15 MIN
MENTAL WARM-UP
============================================================

Do NOT study.

Take one imaginary Apple health problem:

"Predict a health/fitness state from Apple Watch sensor data."


Without notes, speak through:

1. Who is the target population?
2. What decision does the prediction support?
3. What labels exist?
4. What data can actually be collected?
5. What is the simplest useful baseline?
6. What would justify a more complex model?
7. How would I evaluate it?
8. What populations/slices could fail?
9. How would it eventually be deployed?
10. Which other teams/expertise do I need?


TARGET

5–7 minute coherent answer.

Do not immediately jump to:

transformer
cross-attention
foundation model.


============================================================
BLOCK 1 — 45 MIN
QUESTION 1: DESIGN THE WHOLE HEALTH ML SYSTEM
============================================================

MAIN QUESTION

"We want to develop a model from wearable sensor data to identify or
predict a health condition.

How would you approach the problem end to end?"


THIS IS PROBABLY THE MOST IMPORTANT VINCENT QUESTION.


------------------------------------------------------------
GOOD INITIAL STRUCTURE
------------------------------------------------------------

Start with:

"I'd first define the prediction problem and population before choosing
the model."


Then:

POPULATION

Who will use this?

Age distribution?
BMI/body characteristics?
Activity level?
Health status?
Different gestures/movement patterns?
Different wear patterns?
Different device generations?
Geographies/sites if relevant?


OUTCOME / LABEL

What exactly are we predicting?

Detection?
Prediction?
Risk stratification?

How is ground truth established?

At what time is the prediction made?

What information exists at prediction time?


DATA

Which sensors?

Sampling rates?

Missingness?

Sensor quality?

How much labeled vs unlabeled data?

Can all desired data legally/permissibly be:

collected
linked
retained
used for this purpose?


BASELINE

Start simple.

Examples:

summary features
+
logistic regression / XGBoost

or:

simple unimodal temporal encoder.


MODEL COMPLEXITY

Only add complexity when there is evidence that the simpler system
cannot capture something important.

Possible progression:

classical baseline
→ unimodal temporal model
→ pretrained representation
→ multimodal model
→ larger foundation model


EVALUATION

Participant-disjoint where appropriate.

Sensitivity/specificity/precision/calibration.

Operating point tied to use case.

Subgroup performance.

Missingness robustness.

Device/site/temporal shift.

Confidence intervals at independent-unit level.


DEPLOYMENT

On-device vs cloud?

Latency?

Memory?

Battery/compute?

Missing sensors?

New device generation?

Monitoring?

Recalibration?

What happens when input quality is bad?


------------------------------------------------------------
FOLLOW-UPS VINCENT COULD ASK
------------------------------------------------------------

"Why wouldn't you start with a large foundation model?"

"What would make you move from XGBoost to a deep model?"

"What if XGBoost is almost as good?"

"What if multimodality improves AUROC by 2% but costs 10x more?"

"What if the model works for young users but performs poorly for
older users?"

"What if performance changes substantially with BMI?"

"What if a gesture produces sensor patterns similar to the health
event?"

"What if one population is poorly represented in the dataset?"

"Would you delay deployment?"

"How would you collect additional data?"

"What if legal/privacy tells you that one useful data source cannot
be used?"

"What if labels are extremely expensive?"

"What if only 2% of users have labels?"

"What should be pretrained?"

"How would you know whether another modality is actually useful?"

"What would you monitor after deployment?"


------------------------------------------------------------
WHAT HE IS TESTING
------------------------------------------------------------

Do I define the problem before modeling?

Can I reason about populations?

Do I treat data collection as part of ML system design?

Do I naturally consider legal/privacy constraints?

Do I start simple?

Can I justify complexity?

Can I connect metrics to the decision?

Can I think through deployment?


============================================================
BLOCK 2 — 45 MIN
QUESTION 2: THE MODEL WINS OVERALL BUT FAILS A POPULATION
============================================================

MAIN QUESTION

"Your new multimodal model significantly improves the overall metric.

But performance for one important population is worse than the
previous model.

What do you do?"


------------------------------------------------------------
DO NOT ANSWER IMMEDIATELY
------------------------------------------------------------

First determine:

Is the difference real?

Then:

Why might it happen?


------------------------------------------------------------
DIAGNOSTIC TREE
------------------------------------------------------------

DATA

Is this group underrepresented?

Different prevalence?

Different labels?

Different missingness?


SENSOR

Different signal quality?

Sensor-body interaction?

Wear behavior?

BMI/body characteristics?

Different movement/gestures?


REPRESENTATION

Did preprocessing discard relevant information?

Does tokenization work equally well for this population?


MODEL

Negative transfer?

Shortcut?

One modality dominates?

Insufficient capacity?

Pretraining distribution mismatch?


EVALUATION

Small sample?

Uncertainty?

Threshold inappropriate?

Calibration shift?


------------------------------------------------------------
FOLLOW-UPS
------------------------------------------------------------

"The subgroup contains only 20 positive cases. What do you conclude?"

"Would you block deployment?"

"What if the overall gain is very large?"

"What if fixing this subgroup reduces average performance?"

"What if the subgroup is only 2% of users?"

"What if you don't know why the gap exists?"

"How would you collect more evidence?"

"Would you train a separate model?"

"Would you use a different threshold?"

"How do you distinguish a physiological difference from a sensor
artifact?"

"Who would you involve in this decision?"


------------------------------------------------------------
CROSS-FUNCTIONAL COMPONENT
------------------------------------------------------------

Possible expertise needed:

health/domain experts
sensor/hardware experts
data collection
statistics
ML research
engineering
privacy/legal
product


Do not say:

"I would ask those teams what to do."


Instead:

Explain the technical uncertainty you need each team to resolve.


Example:

Sensor team:

Is the subgroup difference consistent with known changes in sensor
signal quality?


Clinical/domain team:

Is the observed failure mode clinically meaningful?


Privacy/legal:

Can additional targeted data be collected and used?


Research:

Which experiment distinguishes data coverage from representation
failure?


CORE LESSON

Population performance is not merely another metric slice.

It can expose a failure anywhere in the entire system.


============================================================
BREAK — 20–30 MIN
============================================================

Leave the desk.

No interview material.


============================================================
BLOCK 3 — 40 MIN
QUESTION 3: DATA COLLECTION + LEGAL / PRIVACY CONSTRAINT
============================================================

MAIN QUESTION

"You believe the model needs more representative data.

How would you design the next data collection?"


------------------------------------------------------------
STRUCTURE
------------------------------------------------------------

START FROM THE FAILURE.

What uncertainty are we trying to resolve?


Then define:

TARGET POPULATION

Who is missing?

Why?


OBSERVATIONS

Which sensors?

At what sampling rates?

Under which behaviors/gestures?

How long?

Naturalistic vs controlled?


LABELS

What is ground truth?

Who provides it?

How reliable is it?

Does label collection alter behavior?


COVERAGE

Age
BMI/body characteristics
activity
behavior/gestures
device
relevant health variation
other relevant deployment dimensions


PERMISSIBILITY

Before assuming data exists:

Can it be collected?

Can it be linked?

Can it be retained?

Can it be used for this model/research purpose?

What consent/permissions are required?


IMPORTANT

Do NOT pretend to know Apple's internal legal/privacy policy.

Good answer:

"I would work with the appropriate privacy/legal teams early because
the permissible data determines the feasible technical design."


Bad answer:

"Apple policy allows us to..."


------------------------------------------------------------
FOLLOW-UPS
------------------------------------------------------------

"What if legal says you cannot collect the modality you wanted?"

"What if the ideal labels are unavailable?"

"What if collecting labels costs 100x more than collecting unlabeled
sensor data?"

"What if participants behave differently because they know they are
being studied?"

"What if your dataset is representative today but the next device
generation changes the sensor?"

"How much data is enough?"

"Would you collect broadly or target failure populations?"

"How would you avoid collecting enormous amounts of unnecessary data?"

"How would you test whether BMI is actually relevant rather than just
collecting more BMI diversity?"

"What if one team wants to collect more data and another wants to
improve the model?"


------------------------------------------------------------
STRONG PRINCIPLE
------------------------------------------------------------

DATA COLLECTION IS AN EXPERIMENT.

Do not simply say:

"collect more diverse data."


Say:

"We observed failure X.

Hypotheses A/B/C could explain it.

I would collect data that distinguishes those hypotheses."


============================================================
BLOCK 4 — 45 MIN
QUESTION 4: FIXED BUDGET — WHERE DO YOU INVEST?
============================================================

MAIN QUESTION

"You have a fixed compute and engineering budget.

You can:

A. make the model 4x larger
B. train on 4x more data
C. preserve higher sensor resolution
D. add another modality

How do you decide?"


------------------------------------------------------------
KEY
------------------------------------------------------------

There is no universally correct choice.

Do NOT choose based on intuition alone.

Ask:

WHAT IS CURRENTLY LIMITING PERFORMANCE?


------------------------------------------------------------
FRAMEWORK
------------------------------------------------------------

CURRENT FAILURE

What tasks/slices fail?


HYPOTHESES

Capacity?

Data?

Representation?

Missing information?

Optimization?


CHEAP EXPERIMENTS

Small scaling curves.

Data scaling curve.

Model scaling curve.

Token/resolution ablation.

Modality ablation.

Compute-normalized comparison.


MARGINAL VALUE

For each additional unit of:

compute
data
tokens
modality complexity

how much downstream improvement do I obtain?


------------------------------------------------------------
FOLLOW-UPS
------------------------------------------------------------

"What if the larger model gives +2%?"

"What if adding a modality gives +3% but doubles deployment cost?"

"What if higher sampling rate helps one rare but important task?"

"What if more data improves average performance but not the weakest
population?"

"What if your model has not saturated with scale?"

"What if training compute is unlimited but inference compute is
strictly constrained?"

"What if the new modality is often missing?"

"What if the new modality is legally difficult to collect?"

"Would you use a teacher model during training and deploy a smaller
student?"

"How would you decide when an experiment deserves an 8B-scale run?"


------------------------------------------------------------
SYSTEMS-THINKING SIGNAL
------------------------------------------------------------

A local improvement can damage the global system.

Examples:

higher resolution
→ better information
→ more tokens
→ higher training cost
→ higher latency


new modality
→ complementary information
→ more missingness
→ additional collection/legal complexity
→ deployment dependency


larger model
→ capacity
→ compute/memory/latency
→ possibly no benefit if representation is bottleneck


CORE QUESTION

"What bottleneck am I paying to remove?"


============================================================
BREAK — 15 MIN
============================================================


============================================================
BLOCK 5 — 45 MIN
QUESTION 5: RESEARCH SYSTEM AT SCALE
============================================================

MAIN QUESTION

"Multiple researchers and engineers are working on representations,
encoders, fusion strategies and training objectives for the same
foundation model.

How would you structure the technical process so that the team knows
whether it is actually making progress?"


------------------------------------------------------------
ANSWER STRUCTURE
------------------------------------------------------------

SHARED OBJECTIVE

What downstream capabilities matter?


REFERENCE BASELINES

Simple baseline.

Current production/reference model.

Strong research baseline.


STANDARDIZED DATA

Versioned datasets.

Fixed splits.

Population coverage.

Leakage controls.


STANDARDIZED EVALUATION

Primary metrics.

Critical slices.

Subgroup floors.

Missingness robustness.

Compute/latency metrics.


EXPERIMENT HIERARCHY

CHEAP PROBE
→ INTERMEDIATE EXPERIMENT
→ EXPENSIVE CONFIRMATION


Do not run every idea at 8B scale.


REGRESSION GATES

Define before expensive experiments:

what must improve?

what cannot regress?

what causes us to kill the intervention?


REPRODUCIBILITY

Code/configuration.

Dataset version.

Checkpoint.

Seeds where meaningful.

Training/evaluation metadata.


------------------------------------------------------------
FOLLOW-UPS
------------------------------------------------------------

"What if researchers optimize only for the benchmark?"

"What if one model improves 8 tasks and hurts 2?"

"What if two teams disagree about which metric matters?"

"What if an innovative idea is initially worse?"

"How do you avoid killing risky research too early?"

"How do you decide who owns a technical decision?"

"What if a collaborator strongly disagrees with you?"

"What if you have enough compute to run everything?"

"How do you prevent duplicated work?"

"How do you communicate negative results?"

"How do you make decisions when evidence is incomplete?"


------------------------------------------------------------
USE REAL STORIES
------------------------------------------------------------

IMAGENTIME

Representation disagreement.

Cheap tests before expensive scale.


TSRBENCH

0.8B probe before 8B.


TEMPORAL-RELATIONS MIX

Predefined regression gates.

Killed despite improvements elsewhere.


These show:

technical leadership

through:

EXPERIMENT DESIGN

rather than:

AUTHORITY.


============================================================
BLOCK 6 — 35 MIN
CROSS-FUNCTIONAL LEADERSHIP
============================================================

MAIN QUESTION

"Tell me about a project where working with people from another
discipline changed your technical approach."


PRIMARY STORY

BOSCH.


------------------------------------------------------------
STRUCTURE
------------------------------------------------------------

PROBLEM

Modality translation on industrial sensor data.


INITIAL MODELING ASSUMPTION

Clean:

A → B


REALITY EXPOSED BY BOSCH

irregular sampling
noise
partial observations
imperfect alignment


TECHNICAL CHANGE

Reformulate:

partial/noisy/irregular A
→ useful B


YOUR CONTRIBUTION

Translate real sensor/pipeline observations into:

modeling assumptions
experiments
robustness requirements


BOSCH CONTRIBUTION

Industrial sensor/data-collection expertise.

Real failure modes.


RESULT

Stronger behavior on realistic data / strong internal research
baseline.

Do NOT claim a shipped product if there wasn't one.


------------------------------------------------------------
FOLLOW-UPS
------------------------------------------------------------

"What did YOU personally do?"

"What did Bosch know that you didn't?"

"What did you know that they didn't?"

"Where did you disagree?"

"How did their input change the model?"

"What if their preferred solution contradicted your research
intuition?"

"How did you communicate technical tradeoffs?"

"How did you decide which assumptions from the benchmark had to be
abandoned?"

"What was the measurable result?"

"What would you do differently?"


------------------------------------------------------------
L5 SIGNAL
------------------------------------------------------------

Not:

"I directed the collaborators."


Instead:

"I owned an important technical part, integrated expertise that I
didn't have myself, and used it to change the technical solution."


============================================================
BLOCK 7 — 30 MIN
DEPLOYMENT CASE
============================================================

MAIN QUESTION

"Your research model is performing well enough to consider deployment.

What happens next?"


------------------------------------------------------------
DO NOT SAY
------------------------------------------------------------

"Hand it to engineering."


------------------------------------------------------------
THINK THROUGH
------------------------------------------------------------

QUALITY

Does retrospective performance survive realistic deployment
conditions?


OPERATING POINT

What threshold?

What FP/FN tradeoff?


CALIBRATION

Do probabilities mean what we think they mean?


POPULATIONS

Any unacceptable subgroup failures?


ROBUSTNESS

Missing sensors?

Corrupted sensor?

Movement?

New hardware?


SYSTEM

Latency?

Memory?

Battery?

Cloud vs device?


FAILURE BEHAVIOR

What happens when:

input is missing
confidence is low
distribution shifts?


MONITORING

Input quality.

Missingness.

Score distribution.

Alert rate.

Subgroup behavior where measurable/permissible.

Labels/outcomes when eventually available.


------------------------------------------------------------
FOLLOW-UPS
------------------------------------------------------------

"Would you deploy a model with better AUROC but worse calibration?"

"What if the cloud model is much better than the on-device model?"

"What if inference takes 10 seconds?"

"What if a sensor disappears?"

"What if the model sees a new device generation?"

"What metrics do you monitor?"

"What triggers rollback?"

"How do you distinguish model drift from sensor drift?"

"What if you cannot obtain labels quickly after deployment?"

"Who needs to be involved before launch?"


CORE LESSON

A research metric is the BEGINNING of the deployment argument,

not the end.


============================================================
BLOCK 8 — 20 MIN
RAPID-FIRE VINCENT QUESTIONS
============================================================

Answer each in:

30–60 seconds.


1.

When should you prefer a simple model over a foundation model?


2.

When is adding another modality NOT worthwhile?


3.

How do you decide whether a subgroup regression is real?


4.

What makes a good technical baseline?


5.

When should an experiment be killed?


6.

When should a failed experiment be given more resources?


7.

How do you distinguish a data problem from a model problem?


8.

How do you decide what data to collect next?


9.

What do you do when legal/privacy constraints eliminate the most
obvious technical solution?


10.

How do you measure whether a cross-functional collaboration is
working?


11.

What if an engineer wants the simplest deployable solution while a
researcher wants a substantially more complex architecture?


12.

What if your best offline model cannot meet latency requirements?


13.

What if adding data improves average performance but hurts an
important population?


14.

How do you decide whether to increase:

data
model size
input resolution
or modalities?


15.

How do you know when research is ready for deployment?


============================================================
BLOCK 9 — 15 MIN
APPLE L5 SELF-CHECK
============================================================

For every major answer ask:

RESULTS

Did I explain what measurable outcome mattered?


INNOVATION

Did I demonstrate non-obvious technical judgment rather than simply
following standard practice?


TEAMWORK

Did I show how expertise from other people/functions affected the
technical result?


And:

DID I PERSONALLY DO SOMETHING TECHNICAL?


Avoid answers where:

"I coordinated..."
"I asked the team..."
"I assigned..."
"I aligned stakeholders..."

is the main action.


Prefer:

"I formulated..."
"I designed..."
"I implemented..."
"I analyzed..."
"I found..."
"I changed..."
"I proposed..."
"I tested..."


============================================================
THE FIVE QUESTIONS TO REMEMBER
============================================================

If I remember nothing else, remember these five.


QUESTION 1

"Design the health ML system end to end."

Tests:

wide system judgment.


QUESTION 2

"Overall performance improves, but an important population gets
worse. What do you do?"

Tests:

population awareness + diagnosis + judgment.


QUESTION 3

"You need more/better data. How do you collect it given real-world
and legal/privacy constraints?"

Tests:

data-system thinking + cross-functional work.


QUESTION 4

"With a fixed budget, do you spend it on model size, data,
resolution or another modality?"

Tests:

technical prioritization + interactions + evidence.


QUESTION 5

"How do you organize experimentation across a large research effort so
that you know you're making progress?"

Tests:

technical leadership + research systems thinking.


============================================================
VINCENT'S MENTAL MODEL
============================================================

Do not optimize a component in isolation.

Think:

OBJECTIVE
      ↓
POPULATION
      ↓
DATA / LABELS
      ↓
REPRESENTATION
      ↓
MODEL
      ↓
TRAINING
      ↓
EVALUATION
      ↓
DEPLOYMENT
      ↓
MONITORING


A change anywhere can propagate through the whole system.


Higher sensor resolution:

information ↑
tokens ↑
compute ↑
latency ↑


New modality:

information ↑
missingness ↑
collection complexity ↑
legal/privacy dependencies ↑


Larger model:

capacity ↑
training cost ↑
deployment cost ↑

but:

zero benefit if the real bottleneck is data/representation.


More data:

coverage ↑

but potentially:

collection cost ↑
label cost ↑

and:

doesn't necessarily fix the population that actually fails.


============================================================
FINAL VINCENT PRINCIPLE
============================================================

WIDE:

Can I see the whole system?


DEEP:

Can I identify the technical bottleneck and reason precisely about it?


SCIENTIFIC:

Can I design an experiment that tells me what to do?


PRACTICAL:

Can this actually be collected, evaluated and deployed?


L5:

Can I make these decisions while working effectively across people
with expertise I do not have?


The answer should rarely be:

"Use architecture X."


The answer should usually sound like:

"Here is the decision we need to make, here are the competing
hypotheses and constraints, here is the cheapest evidence I would
collect, and here is how that evidence changes the system design."

---

Stories (Blocks 5–6): [`2026-08-30_behavioral-stories.md`](2026-08-30_behavioral-stories.md) · Hub: [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md) · Mock log: [`2026-09-03_onsite-vincent-practice.md`](2026-09-03_onsite-vincent-practice.md)
