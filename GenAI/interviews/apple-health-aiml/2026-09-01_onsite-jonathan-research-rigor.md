# On-site — Jonathan: research depth & scientific rigor mock (Tue 9/1)

Companion to [`2026-08-27_onsite-jonathan.md`](2026-08-27_onsite-jonathan.md).

**Outcome:** Q1–Q4 spoken. **Q5 not answered live** — researcher degrees of freedom / pre-specified hypothesis vs post-hoc story. Recalc: claim → evidence → alternative → discriminating experiment → narrow the claim.

```text
JONATHAN — RESEARCH DEPTH & SCIENTIFIC RIGOR MOCK
=================================================

PURPOSE

This mock focused less on whether the methods work and more on:

CLAIM
→ EVIDENCE
→ ALTERNATIVE EXPLANATION
→ DISCRIMINATING EXPERIMENT
→ LIMITATION
→ NARROW/REVISE CLAIM

The central theme was:
Do the experiments actually support the strength and mechanism of the scientific claim?


============================================================
QUESTION 1 — WHAT ACTUALLY CAUSED THE GAIN?
============================================================

SCENARIO

ImagenFew shows that an image-based diffusion approach substantially
outperforms strong time-series baselines in the low-data regime.

CHALLENGE

"You claim the image representation is responsible for the data
efficiency, but you changed several things at once. You introduced a
2D representation, a vision-oriented diffusion architecture, and
potentially different optimization/training choices.

Your result only shows that the complete system is better.

Why should I believe your explanation for WHY it is better?

What experiment would provide the strongest evidence for or against
your claim?"


------------------------------------------------------------
MY ANSWER
------------------------------------------------------------

For each change, I ablated the change with the best and closest
baseline to show that the advantages were real.

First, I ablated the time-series representation.

I considered:

- delay embeddings
- STFT
- charts
- Gramian angular fields

Charts are particularly interesting because they are similar in spirit
to the plain time-series representation.

Across the tests, DE and STFT were consistently best in generative
quality across:

- multiple sequence lengths
- multiple datasets
- multiple metrics

I also compared the complete system with the strongest available 1D
system on the same benchmark while controlling parameter count and
training budget.

The method achieved state-of-the-art unconditional generation across
multiple metrics.

The robustness across multiple sequence lengths, datasets/tasks,
metrics and competing methods gives evidence that the result is not
specific to a single benchmark configuration.


------------------------------------------------------------
IMPORTANT PUSHBACK
------------------------------------------------------------

A completely factorial experiment such as:

1D representation + 1D architecture
1D representation + 2D architecture
2D representation + 1D architecture
2D representation + 2D architecture

is not really well-defined.

A native 1D architecture cannot simply accept a 2D representation
without changing the architecture and violating the intended
representation/architecture assumptions.

The reverse is also true.

The representation and architecture are partially coupled.


------------------------------------------------------------
BETTER SCIENTIFIC CLAIM
------------------------------------------------------------

Do NOT overclaim:

"The 2D representation alone causally produces the improvement."


Instead distinguish two levels of evidence.


LEVEL 1 — WITHIN THE 2D FRAMEWORK

Hold the image-space modeling framework approximately fixed and compare:

delay embedding
STFT
line chart
Gramian angular field


This tests:

Given an image-space framework, does representation choice matter?


The line-chart control is particularly useful.

It is approximately:

"show the original trajectory as an image"

without introducing the same structural transformation as DE/STFT.


If:

DE/STFT > line charts/GAF

consistently, then:

the result is not merely caused by converting anything into an image.


LEVEL 2 — ACROSS MODELING FAMILIES

Compare:

best 2D representation + image diffusion

against:

strongest native 1D generative model


under as well matched conditions as reasonably possible:

- training data
- parameter count
- training budget
- evaluation protocol


This tests the COMPLETE modeling formulation.


------------------------------------------------------------
STRONG INTERVIEW FORMULATION
------------------------------------------------------------

"I don't think representation and architecture are completely
separable here.

A delay embedding is intrinsically 2D while the native baseline is
intrinsically 1D, so forcing either through the wrong architecture
would create an artificial control.

I therefore use two levels of evidence.

Within the image framework, I hold the diffusion architecture fixed
and change the representation: delay, STFT, line plots and Gramian
fields.

Delay and STFT consistently perform best, and line plots are a useful
control because they're essentially the raw trajectory rendered in 2D.
That tells me the gain isn't simply 'anything converted to an image.'

Separately, I compare the best image-space system with strong native
1D models under matched parameter and training budgets.

So I would not claim that I've identified the causal effect of
representation independently of architecture.

The stronger claim is that the representation-architecture combination
changes the low-data problem favorably, while the within-2D ablations
show that representation choice is an important part of that
combination."


CORE LESSON

Do not invent an artificial ablation merely because it would make the
causal table cleaner.

When representation and architecture are structurally coupled:

acknowledge the coupling
+
design the closest meaningful controls
+
narrow the causal claim.


============================================================
QUESTION 2 — DATA EFFICIENCY OR JUST MORE COMPUTE?
============================================================

CHALLENGE

"Fine. But even with matched parameter count, your 2D method may spend
substantially more FLOPs per example.

With only 5% of the training data, you're effectively buying more
computation per observation.

Why should I call that DATA EFFICIENCY rather than simply MORE COMPUTE
PER DATUM?"


------------------------------------------------------------
MY ANSWER
------------------------------------------------------------

I disagree that greater compute invalidates the data-efficiency claim.

If training is restricted to the same 5% of the dataset, and my method
gets better results from those observations, then it is more effective
at using the available data.

It may use more compute, but:

DATA EFFICIENCY

and

COMPUTE EFFICIENCY

are different properties.


Compute can be controlled separately.

For example:

run both systems under a fixed total FLOP budget

and compare their performance.


In my experience, competing methods also tended to flatten at some
point even when additional compute was available.


------------------------------------------------------------
REFINED INTERPRETATION
------------------------------------------------------------

Two complementary experiments answer two different questions.


FIXED DATA

Give every method:

1%
5%
10%
25%
etc.

of the training observations.

Measure performance.

This tests:

DATA EFFICIENCY.


FIXED COMPUTE

Give every method the same:

total FLOPs / training compute budget.

Measure performance.

This tests:

COMPUTE EFFICIENCY.


Ideally report both:

performance vs amount of data

and

performance vs compute.


------------------------------------------------------------
IMPORTANT CLAIM BOUNDARY
------------------------------------------------------------

If the image method wins at fixed data but requires more compute:

reasonable claim:

"more data efficient"


NOT automatically:

"more compute efficient."


If competing methods saturate despite receiving additional compute,
that is stronger evidence that the result cannot simply be explained
as:

"the image method trained harder."


------------------------------------------------------------
STRONG INTERVIEW FORMULATION
------------------------------------------------------------

"I would separate data efficiency from compute efficiency.

If both methods see the same 5% of the dataset and mine generalizes
better, that's evidence of greater data efficiency even if it uses
more FLOPs.

But I agree that compute is an important practical confound, so I'd
report a second controlled experiment at fixed total FLOPs.

An important observation in our experiments was that competing methods
tended to saturate; additional compute did not necessarily close the
gap.

So I wouldn't claim we're more compute-efficient unless the
fixed-compute experiment supports it.

I'd claim we're more effective at learning from limited observations."


CORE LESSON

Scarce data and scarce compute are different constraints.

Be explicit about which efficiency claim the experiment supports.


============================================================
QUESTION 3 — DOES THE FEW-SHOT SPLIT SUPPORT THE CLAIM?
============================================================

SCENARIO

ImagenFew gets a large improvement using only 5% training data.


CHALLENGE

"How exactly did you construct the 5% subset?

If these are time-series windows originating from longer trajectories,
random subsampling can leave highly correlated or overlapping windows
in train and test.

Your apparent few-shot performance could partly be leakage.

And even without literal overlap, perhaps your 5% subset happens to
cover essentially all subjects or trajectories, so this isn't really
the kind of data scarcity you imply."


QUESTION

How would you determine whether this criticism applies?

What different claims can you make if you subsample:

- windows
- trajectories
- subjects?


------------------------------------------------------------
MY ANSWER
------------------------------------------------------------

First, all competing methods had access to exactly the same data and
subsampling.

Specifically, in ImagenFew I sampled non-overlapping windows randomly.

In a later study, I extended the sampling procedure to be more coherent
with realistic scenarios such as sensor defects.

Even if some leakage existed, competing methods could exploit the same
information.

However, this really raises a question about the EVALUATION SETTING and
the GENERALIZATION CLAIM.

Those should be made explicit.


------------------------------------------------------------
IMPORTANT DISTINCTION
------------------------------------------------------------

FAIR COMPARISON

is not the same as:

VALID GENERALIZATION CLAIM.


Giving every method the same split makes the comparison between methods
fair.

But if the split leaks subject or trajectory identity, it does not
justify claiming generalization to unseen subjects.


------------------------------------------------------------
DIFFERENT SPLITS SUPPORT DIFFERENT CLAIMS
------------------------------------------------------------

WINDOW-LEVEL SCARCITY

Train on a small number of non-overlapping windows.

Supports something like:

learning from few observed segments drawn from a similar underlying
population/process.

It may largely test interpolation/generalization within a familiar
trajectory/subject distribution.


TRAJECTORY-LEVEL SCARCITY

Hold out complete trajectories.

Supports:

generalization to unseen trajectories.

Depending on the dataset, these trajectories may still originate from
subjects seen during training.


SUBJECT-LEVEL SCARCITY

Hold out complete people.

Supports:

generalization to unseen subjects.

This is a substantially stronger claim and particularly important in
health applications.


TEMPORAL-BLOCK / STRUCTURED SCARCITY

Train/test using coherent temporal regions rather than random windows.

Examples:

sensor outage
contiguous missing intervals
early period -> later period

This can better reflect realistic deployment scarcity or temporal
distribution shift.


------------------------------------------------------------
STRONG INTERVIEW FORMULATION
------------------------------------------------------------

"I'd separate fairness from validity.

Giving every baseline the same 5% subset makes the model comparison
fair, but it doesn't by itself validate the generalization claim.

In ImagenFew we used randomly sampled non-overlapping windows, so the
supported claim is about learning effectively from a small number of
observed segments under that sampling regime—not necessarily
new-subject generalization.

In later work I used more structured scarcity patterns, such as
contiguous missing regions or sensor-defect-like sampling, to better
match realistic scenarios.

If I wanted a stronger health claim, I'd explicitly evaluate
window-level, trajectory-level, subject-level and temporal-block
scarcity.

Each answers a different scientific question, and I'd label the claim
accordingly."


CORE LESSON

Always ask:

WHAT IS THE INDEPENDENT UNIT?

and:

WHAT GENERALIZATION CLAIM DOES THIS SPLIT ACTUALLY SUPPORT?


============================================================
QUESTION 4 — REPRESENTATION FAILURE OR ENCODER MISMATCH?
============================================================

SCENARIO

In the multimodal project:

delay-only performs poorly on numerical QA.

chart-only is substantially stronger.

dual-tower is strongest.


INTERPRETATION MIGHT BE:

delay embedding exposes dynamics/topology

while:

chart representation exposes scale/amplitude.


CHALLENGE

"Maybe the delay representation is perfectly adequate and your encoder
is simply badly matched to it.

In fact, your own Qwen-vs-DINO result seems to support that.

Why should I believe the failure is about the representation at all?"


QUESTION

How do you distinguish:

REPRESENTATION LIMITATION

from:

ENCODER-REPRESENTATION MISMATCH?


------------------------------------------------------------
MY ANSWER
------------------------------------------------------------

Importantly:

Qwen-ViT was pretrained through Qwen's process.

DINO was pretrained on natural images.

Neither encoder had seen delay-embedding images before my Stage A.


To test whether encoder mismatch was responsible:

I directly fine-tuned DINO on delay-embedding images.


RESULT

Numerical performance improved.

But:

it did not improve enough to make the chart tower unnecessary.


This means encoder mismatch explains PART of the original result.

It does not explain all of it.


------------------------------------------------------------
CLAIM SHOULD CHANGE
------------------------------------------------------------

Do NOT conclude:

"delay embeddings intrinsically lack numerical information."


The evidence supports a more nuanced claim.


Information may be PRESENT in the representation

without being:

ACCESSIBLE TO THE PRETRAINED ENCODER.


Under a constrained adaptation/training budget:

the dual representation is more effective because each tower exposes
information in a form that the pretrained system can access.


When additional adaptation compute is given:

the gap shrinks.


That is evidence that part of the dual-tower advantage comes from:

PRETRAINING / REPRESENTATION COMPATIBILITY

rather than intrinsic information content alone.


------------------------------------------------------------
ADDITIONAL EXPERIMENTS
------------------------------------------------------------

I also tried multiple representations with the DINO tower:

- STFT
- charts
- wavelet-based representations
- delay embeddings


Results were mixed.

Empirically, Qwen's ViT was strongest with no or minimal additional
training.


These experiments provide supporting evidence about representation /
encoder interaction.


------------------------------------------------------------
CLEANER DISCRIMINATING EXPERIMENT
------------------------------------------------------------

Keep:

REPRESENTATION FIXED

ENCODER FIXED


Then vary:

ADAPTATION DATA / COMPUTE.


For example:

delay + DINO

at increasing levels of adaptation.


Plot:

numerical performance

vs

adaptation compute/data.


Possible outcomes:


CASE A

Delay+DINO approaches chart/dual performance as adaptation increases.

Evidence favors:

ENCODER MISMATCH.


CASE B

Delay+DINO improves initially but consistently plateaus substantially
below the chart/dual system despite sufficient adaptation.

Evidence for:

REPRESENTATION/TASK MISMATCH

becomes stronger.


------------------------------------------------------------
STRONG INTERVIEW FORMULATION
------------------------------------------------------------

"I don't think the original result lets me conclude that delay
embeddings intrinsically lack numerical information.

There are at least two hypotheses: representation limitation and
encoder-representation mismatch.

We have evidence for the second because directly adapting DINO on
delay embeddings improves numerical performance, even though DINO was
originally pretrained on natural images.

But that adaptation doesn't close the gap to the dual system, so
encoder mismatch isn't the entire explanation.

I therefore narrow the claim.

Under a limited adaptation budget, the dual representation is
substantially more effective because each tower exposes information in
a form that the pretrained encoders can access.

With more adaptation the gap shrinks, which tells me that part of the
original advantage comes from compatibility with the pretrained
representation rather than intrinsic information content."


KEY SENTENCE

"The information may be present in the representation without being
accessible to the pretrained encoder."


CORE LESSON

CONTAINED INFORMATION

is not the same thing as:

ACCESSIBLE INFORMATION

under a particular architecture/pretraining/adaptation budget.


============================================================
QUESTION 5 — RESEARCHER DEGREES OF FREEDOM
NOT ANSWERED DURING THE MOCK
============================================================

SCENARIO

You have now shown:

- multiple datasets
- multiple representations
- multiple encoders
- multiple metrics
- multiple ablations
- multiple training budgets
- negative results


CHALLENGE

"This worries me for a different reason.

With enough experiments, you can eventually find a configuration that
wins.

How do I know your conclusions aren't the result of researcher degrees
of freedom—trying many representations, architectures, hyperparameters
and evaluation slices and then constructing the scientific story after
seeing the results?"


QUESTION

How would you convince me that your experimental process distinguishes:

HYPOTHESIS-DRIVEN SCIENCE

from:

SOPHISTICATED BENCHMARK HILL-CLIMBING?


------------------------------------------------------------
POINTS TO THINK ABOUT LATER
------------------------------------------------------------

Do not merely answer:

"We evaluated on many datasets."

The challenge is specifically about whether the hypothesis and success
criteria were determined BEFORE or AFTER observing results.


Useful dimensions to consider:

1. PRE-SPECIFIED HYPOTHESIS

What did I believe before running the experiment?

What observation would have falsified it?


2. PRE-SPECIFIED SUCCESS / KILL CRITERIA

Can I define beforehand:

what improvement matters?

what regression is unacceptable?

what result causes me to abandon the approach?


3. CHEAP DISCRIMINATING EXPERIMENTS

Instead of large hyperparameter searches:

design the smallest experiment that distinguishes competing
explanations.


4. HELD-OUT CONFIRMATION

After selecting an approach:

does it survive evaluation on data/tasks/settings that were not used
to choose it?


5. NEGATIVE RESULTS

Can I point to cases where:

an experiment contradicted my hypothesis

and I changed/killed the method

rather than changing the story?


6. CLAIM DISCIPLINE

When the experiment only supports:

A + B works

do not retrospectively claim:

A causes the improvement.


7. EXPLORATION VS CONFIRMATION

Exploratory experimentation is legitimate.

But distinguish:

experiments used to GENERATE the hypothesis

from:

experiments used to TEST the hypothesis.


============================================================
MOCK TAKEAWAYS
============================================================

1. ROBUSTNESS IS NOT CAUSAL IDENTIFICATION

Winning across many datasets and metrics makes the empirical result
more robust.

It does not automatically identify WHY the method wins.


2. SOME REPRESENTATION/ARCHITECTURE VARIABLES CANNOT BE CLEANLY
   SEPARATED

Do not create meaningless controls merely to make a factorial table.

Use the closest scientifically meaningful controls and narrow the
claim.


3. DATA EFFICIENCY != COMPUTE EFFICIENCY

Measure both when relevant.


4. FAIR BENCHMARK != VALID GENERALIZATION CLAIM

All methods can receive the same split and still all be evaluated under
an unrealistic generalization regime.


5. REPRESENTATION INFORMATION != ENCODER ACCESSIBILITY

A representation can contain information that a pretrained encoder
cannot readily extract.


6. WHEN ALTERNATIVE EXPLANATIONS SURVIVE, NARROW THE CLAIM

This is a strength, not a weakness.


7. THE JONATHAN MINDSET

For essentially every result, ask:

WHAT EXACTLY AM I CLAIMING?

WHAT EVIDENCE SUPPORTS THAT CLAIM?

WHAT ELSE COULD EXPLAIN THE RESULT?

WHAT EXPERIMENT WOULD DISTINGUISH THE EXPLANATIONS?

WHAT WOULD MAKE ME CHANGE MY MIND?

WHAT IS THE NARROWEST CLAIM THE EVIDENCE ACTUALLY SUPPORTS?
```
