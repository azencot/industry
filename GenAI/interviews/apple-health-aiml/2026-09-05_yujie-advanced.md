APPLE — YUJIE ADVANCED PRACTICE
Multimodal Architecture & Time-Series Encoding
=======================================================

GOAL

Assume Yujie is an expert and will not be satisfied with:

"Patch the time series and use cross-attention."

She may keep drilling until I can explain:

1. what information exists in the raw signal
2. what the representation preserves and destroys
3. why the encoder can access that information
4. why modalities should interact in a particular way
5. what the token/compute consequences are
6. how I would prove that each architectural choice helps


CORE FRAMEWORK

RAW INFORMATION
    ↓
REPRESENTATION
    ↓
TOKENIZATION / COMPRESSION
    ↓
ENCODER PRIOR
    ↓
TEMPORAL ALIGNMENT
    ↓
FUSION
    ↓
TRAINING
    ↓
EVALUATION / ABLATION


For every design choice ask:

WHAT INFORMATION AM I TRYING TO EXPOSE?

WHAT INFORMATION MIGHT I DESTROY?

WHAT INDUCTIVE BIAS AM I ADDING?

WHAT DOES IT COST?

WHAT EXPERIMENT WOULD PROVE IT WAS WORTH IT?


=======================================================
BLOCK 1 — TIME-SERIES REPRESENTATION DEEP DIVE
60 MIN
=======================================================

MAIN QUESTION

"You have raw multivariate time-series data.

How do you decide how to represent it for a multimodal model?"


DO NOT BEGIN WITH THE ARCHITECTURE.

Begin with:

"What information does the downstream task need?"


Possible information:

absolute value / scale

trend

local morphology

frequency content

phase

periodicity

cross-channel relationship

temporal ordering

recurrence

long-range dynamics

events / discontinuities

uncertainty / missingness


Then compare representations.


-------------------------------------------------------
A. RAW SAMPLE REPRESENTATION
-------------------------------------------------------

Input:

x_t ∈ R^C


Possible:

linear projection
+
time/position encoding


Advantages:

maximum direct access to native measurements

minimal handcrafted representation bias


Problems:

huge token counts at high sampling rates

noise

redundancy

poor long-context scaling


FOLLOW-UPS

"Why not just let the transformer learn everything?"

"How much data would that require?"

"What happens at 128 Hz over hours?"

"What prior does raw-sample tokenization impose?"

"When would raw tokens actually be reasonable?"


-------------------------------------------------------
B. PATCHES / WINDOWS
-------------------------------------------------------

Map:

x[t:t+P]
    ->
token z_t


Advantages:

token reduction

local pattern extraction

natural temporal inductive bias


Tradeoff:

patch size determines:

temporal resolution
token count
information loss


Larger P:

tokens ↓
compute ↓

but:

short temporal events may disappear


Smaller P:

resolution ↑

but:

sequence length ↑


IMPORTANT

Patch size should ideally reflect:

signal bandwidth
task timescale
sampling rate


Do not necessarily use the same patch duration across modalities.


FOLLOW-UPS

"Should PPG and HR have the same patch size?"

"What about patch size in samples versus seconds?"

"What if deployment changes the sampling rate?"

"Should patches overlap?"

"What does overlap buy?"

"Could learned convolution be better than hard patching?"


-------------------------------------------------------
C. FREQUENCY / TIME-FREQUENCY REPRESENTATIONS
-------------------------------------------------------

FFT:

global frequency information

but loses temporal localization.


STFT:

time + frequency localization.


Tradeoff:

window length.

Long window:

frequency resolution ↑
temporal resolution ↓


Short window:

temporal localization ↑
frequency resolution ↓


Wavelets:

multi-resolution decomposition

potentially useful for events at different timescales.


FOLLOW-UPS

"When is STFT better than raw patches?"

"Why isn't STFT universally better?"

"What if phase matters?"

"What information is lost?"

"How do you choose window size?"

"Would you learn the transform instead?"


-------------------------------------------------------
D. DELAY EMBEDDINGS
-------------------------------------------------------

Conceptually:

x_t
    ->
[x_t, x_{t-τ}, x_{t-2τ}, ...]


Then organize the embedding geometrically.


Potential benefit:

exposes recurrence
dynamical structure
trajectory geometry


Potential weakness:

absolute values / numerical scale may not be readily accessible
to a pretrained visual encoder.


IMPORTANT LESSON FROM MY OWN WORK

Delay-only numerical QA:

poor.

Chart:

much stronger.

Dual:

strongest.


Do NOT say:

"delay doesn't contain numerical information."


Better:

"The numerical information may exist in the representation,
but it is not necessarily accessible to the pretrained encoder
under our adaptation budget."


FOLLOW-UPS

"How do you choose τ?"

"How do you choose embedding dimension?"

"What happens for noisy signals?"

"What happens with irregular sampling?"

"Why should a vision encoder understand a delay embedding?"

"What does DINO pretraining buy?"

"Could enough adaptation remove the need for the chart tower?"


-------------------------------------------------------
E. CHART REPRESENTATIONS
-------------------------------------------------------

Potential advantages:

scale
amplitude
trend
human-readable geometry

plus compatibility with strong pretrained VLMs.


Weaknesses:

rendering artifacts

pixel inefficiency

visual choices matter

not native to the signal

precision may depend on resolution

potential loss of exact samples


IMPORTANT

Charts are not:

"information-preserving by definition."


They are a representation with a particular accessibility bias.


FOLLOW-UPS

"What happens if I change axis scaling?"

"How does line thickness affect the model?"

"Could the model read values from ticks instead of the signal?"

"Does rendering resolution matter?"

"Why not provide the numerical values as text?"

"What benchmark artifacts might the model exploit?"


-------------------------------------------------------
F. REPRESENTATION IS TASK-CONDITIONAL
-------------------------------------------------------

Do not ask:

"What is the best TS representation?"


Ask:

"What representation exposes the information needed for THIS objective
to THIS encoder?"


Useful conceptual equation:

utility =
f(
    raw information,
    representation,
    encoder prior,
    adaptation budget,
    downstream task
)


This is a central Yujie insight.


=======================================================
BLOCK 2 — MULTIVARIATE TIME SERIES
45 MIN
=======================================================

MAIN QUESTION

"You have 20 sensor channels. How do you encode them?"


OPTIONS


A. CHANNEL-INDEPENDENT

Each channel encoded separately.


Advantages:

parameter sharing
robust to variable channel sets
simple


Weakness:

cross-channel interaction delayed.


B. CHANNEL-MIXING PATCH

Each patch contains:

P × C

and one encoder processes all channels together.


Advantages:

early cross-channel interaction.


Weakness:

assumes fixed channel structure
more parameters
may couple heterogeneous sensors unnaturally.


C. MODALITY-SPECIFIC ENCODERS

PPG encoder

IMU encoder

ECG encoder

etc.


Advantages:

respect different statistics/sampling rates

reuse specialized pretraining.


Weakness:

more components
alignment/fusion becomes necessary.


FOLLOW-UPS

"What if channels have different units?"

"What if one channel disappears?"

"What if the number/order of channels changes?"

"What if two IMU axes are tightly coupled?"

"Would you normalize per channel?"

"Global normalization or subject-specific?"

"Could subject normalization remove health signal?"

"What about cross-channel correlations?"


=======================================================
BLOCK 3 — IRREGULAR / ASYNCHRONOUS TIME
45 MIN
=======================================================

MAIN QUESTION

"PPG is 128 Hz, IMU 50 Hz, HR 1 Hz, and sleep is event-like.

How do you put them into one model?"


BAD DEFAULT:

upsample everything to 128 Hz.


WHY BAD?

No new information.

Token explosion.

Slow modalities become repeated staircases.

May create false temporal precision.


PREFERRED DEFAULT

encode each modality at native/appropriate rate.


Preserve:

measurement value

timestamp / relative time

availability / mask


Then fuse later.


OPTIONS


1. COARSE COMMON LATENT GRID

Each modality summarizes information into a shared time grid.


2. CROSS-ATTENTION

Independent temporal tokens interact without explicit resampling.


3. EVENT-BASED TOKENS

Represent:

(value, time)

directly.


4. CONTINUOUS-TIME / TIME-DELTA ENCODING

Include:

Δt
time since previous observation
absolute/relative time


FOLLOW-UPS

"How do you compare events that are 20 ms apart?"

"How do you represent simultaneous events?"

"What happens if timestamps drift?"

"Why not interpolate?"

"When is interpolation fine?"

"What if sensor clocks aren't synchronized?"

"What if one modality's latency is systematic?"


=======================================================
BLOCK 4 — TOKEN BUDGET AS AN ARCHITECTURAL CONSTRAINT
40 MIN
=======================================================

MAIN QUESTION

"You have:

PPG 128 Hz
IMU 50 Hz
audio 16 kHz
text

for a 30-minute session.

How many tokens do you allocate to each modality?"


DO NOT GIVE A FIXED ANSWER.


Reason:

raw information rate
task relevance
redundancy
encoder compression
compute budget


Possible pipeline:

raw signal
    ↓
local encoder
    ↓
patch/local features
    ↓
latent resampler
    ↓
bounded token set


Important principle:

TOKEN COUNT IS NOT A FAIR MEASURE OF INFORMATION.

One audio token may summarize far more raw observations than one HR token.


FOLLOW-UPS

"Why give audio more tokens?"

"What if audio is only marginally useful?"

"What if rare PPG events require fine resolution?"

"What if compression removes the health event?"

"How do you know your latent bottleneck is too aggressive?"

"Would token budget be fixed or adaptive?"


ADVANCED IDEA

Adaptive token allocation:

more tokens when signal changes / uncertainty is high

fewer tokens during redundant regions.


Potential advantages:

compute efficiency.


Potential problems:

selection mechanism may discard important subtle events.

Harder training.


=======================================================
BLOCK 5 — FUSION: CONCAT VS CROSS-ATTENTION VS LATE FUSION
60 MIN
=======================================================

MAIN QUESTION

"Where should modalities interact?"


-------------------------------------------------------
A. EARLY CONCATENATION
-------------------------------------------------------

All projected tokens become one sequence.


Advantages:

maximum interaction

simple conceptual architecture.


Cost:

sequence length explosion.

All modalities participate in full self-attention.


Risk:

dominant modality overwhelms others.

Modality identity must be represented.


Best when:

token counts manageable

fine-grained interaction required.


-------------------------------------------------------
B. CROSS-ATTENTION
-------------------------------------------------------

Example:

text/fused latent = queries

sensor tokens = keys/values


Advantages:

controlled interaction

specialized encoders retained

cost ≈ Tq × Tk rather than full combined self-attention.


Risks:

modality can be ignored

choice of query direction matters

placement of cross-attention matters.


FOLLOW-UPS

"Why text as Q and sensor as KV?"

"Why not reverse it?"

"Cross-attention every layer or only several?"

"What does early vs late cross-attention change?"

"How do you prevent modality collapse?"

"Can cross-attention model sensor-sensor interactions?"


-------------------------------------------------------
C. LATE FUSION
-------------------------------------------------------

Each modality produces:

embedding / prediction

then combine.


Advantages:

simple

modular

robust to missing modalities

easy to deploy separately.


Weakness:

limited fine-grained interaction.


Best when:

modalities provide largely independent evidence.


-------------------------------------------------------
D. HIERARCHICAL FUSION
-------------------------------------------------------

First:

within-modality temporal modeling.

Then:

cross-modality interaction.


This is probably a very natural default for:

high-frequency heterogeneous sensors.


Conceptually:

raw PPG → local PPG encoder ┐
raw IMU → local IMU encoder ├→ multimodal latent model → LLM
HR      → HR encoder        ┘


This separates:

local signal processing

from:

global semantic interaction.


=======================================================
BLOCK 6 — FUSION DIRECTION / QUERY SEMANTICS
40 MIN
=======================================================

This is a good advanced topic Yujie might probe.


Cross-attention:

Q represents:

"What information am I looking for?"


K/V represents:

"What information is available?"


If text queries sensors:

text tokens ask sensors for relevant evidence.


Useful for:

question answering
language-conditioned retrieval.


But for:

sensor representation learning

there may be no text query yet.


Then use:

learned latent queries

or:

sensor-to-sensor fusion.


FOLLOW-UPS

"What if the task is classification without text?"

"What if you want a reusable foundation representation?"

"Why should text control what sensor information survives?"

"Could query-conditioned fusion destroy information needed by another task?"

"Would you fuse before or after task prompt?"


This distinction matters:

TASK-CONDITIONED REPRESENTATION

vs

TASK-GENERAL REPRESENTATION.


=======================================================
BLOCK 7 — POSITION / TIME ENCODING
35 MIN
=======================================================

MAIN QUESTION

"How do you represent time across different modalities?"


Within each stream:

local position / relative time.


Across modalities:

actual timestamps / shared temporal coordinates.


Do NOT blindly assign concatenated token positions:

1,2,3,....


Why?

Token position is not equal to physical time.


Example:

one PPG patch = 100 ms

one sleep token = 30 seconds


Their sequence index spacing has different meaning.


Possible solution:

token contains:

modality embedding
+
local positional representation
+
physical-time embedding


FOLLOW-UPS

"Can RoPE represent physical time?"

"Could you scale RoPE by timestamps?"

"What if timestamps are irregular?"

"How do you encode long gaps?"

"What if absolute time-of-day matters?"

"What about periodicity?"


Possible time features:

relative Δt

time of day

day/week periodicity

time since last sample


But avoid leaking future information.


=======================================================
BLOCK 8 — MISSING MODALITIES
45 MIN
=======================================================

MAIN QUESTION

"Most training examples do not contain every modality.

What do you do?"


DO NOT DROP THEM.


Represent:

which modalities are present.


Train across realistic modality subsets.


Useful approaches:

modality dropout

presence masks

missing-modality tokens

variable-set fusion

time-since-observation features


Important distinction:


MISSING VALUES WITHIN A STREAM

vs

ENTIRE MISSING MODALITY.


Also:

MISSINGNESS MAY BE INFORMATIVE.


Example:

watch not worn during certain activities.


FOLLOW-UPS

"What if complete examples are only 10%?"

"Should I oversample complete examples?"

"How do you prevent model from depending on PPG if PPG is frequently absent?"

"Should missingness be predicted?"

"Would you impute?"

"Why might imputation be dangerous?"

"What if one modality is available only at training time?"


ADVANCED

TRAINING MIX

should roughly reflect:

deployment modality distribution

plus deliberate dropout for robustness.


But balance matters:

too much dropout

→ model may never learn rich fusion.


too little

→ model becomes brittle.


=======================================================
BLOCK 9 — PRETRAINING AND ENCODER PRIOR
45 MIN
=======================================================

MAIN QUESTION

"You have a strong pretrained vision encoder.

Why should it work on a time-series image?"


Answer:

It may not.


Pretraining gives an inductive prior.

Whether that transfers depends on:

representation compatibility.


This is exactly what your:

Qwen-ViT vs DINO

results illustrate.


Possible cases:


A. Frozen encoder works.

Great — representation is accessible to existing prior.


B. Light adaptation works.

LoRA/projector may be sufficient.


C. Heavy adaptation needed.

Then benefits of pretraining may be smaller.


D. From-scratch encoder wins.

Representation may be too far from pretraining domain.


FOLLOW-UPS

"What does DINO know that helps DE?"

"Why might Qwen ViT prefer charts?"

"How do you distinguish representation quality from encoder prior?"

"How much adaptation is enough?"

"What if adapted DINO eventually catches up?"

"What does that imply?"


Excellent answer:

"The right object is representation × encoder × adaptation budget,
not representation alone."


=======================================================
BLOCK 10 — TRAINING STRATEGY
45 MIN
=======================================================

MAIN QUESTION

"How do you train the full multimodal system?"


Possible staged strategy:


STAGE A — ALIGN

Freeze major pretrained components.

Train:

projector / adapter / modality bridge.


Question:

Can the new modality enter the downstream representation space?


STAGE B — TASK ADAPTATION

LoRA or selective unfreeze.


STAGE C — JOINT ADAPTATION

Only if evidence shows the representation/encoder needs it.


Why stage?

cheaper diagnosis

reduced catastrophic forgetting

separates alignment from reasoning.


But do NOT say staged training is universally superior.


FOLLOW-UPS

"What if Stage A loss improves but downstream QA doesn't?"

"What objective do you use for alignment?"

"Contrastive or generative?"

"Should sensor encoder receive gradient from LM loss?"

"When do you unfreeze it?"

"What LR for encoder versus LLM?"

"What if encoder collapses?"


=======================================================
BLOCK 11 — HOW TO KNOW A MODALITY HELPS
60 MIN
=======================================================

This should be one of your strongest sections.


Suppose:

A only = 0.71

B only = 0.17

A+B = 0.79


Can I conclude:

"B provides complementary information"?

Not fully.


Alternatives:

more tokens

more capacity

regularization

different optimization

encoder differences


Useful experiments:


A ONLY

B ONLY

A+B


Then:


B SHUFFLED ACROSS EXAMPLES

Preserves:

token count / architecture

destroys:

sample-specific information.


If performance remains:

B may not carry useful conditional information.


B TEMPORALLY SHUFFLED

Preserves:

marginal values

destroys:

temporal structure.


Useful to test dynamics claim.


B MASKED / ZEROED

Tests dependence.


MATCHED TOKEN BUDGET

Controls extra tokens.


MATCHED PARAMETER BUDGET

Controls capacity.


TARGETED SLICES

If B supposedly contributes dynamics:

evaluate tasks requiring dynamics.


CORE PRINCIPLE

The ablation should attack the CLAIMED mechanism.


=======================================================
BLOCK 12 — COMPRESSION / REPRESENTATION STRESS TESTS
40 MIN
=======================================================

Question:

"How do you know patching isn't destroying the signal?"


Run performance curves versus:

patch size

sampling rate

token budget

compression ratio


Example:

PPG:

1×
2× downsample
4×
8×
16×


Evaluate:

overall

plus:

short-event / morphology slices.


Look for:

accuracy plateau

then:

failure cliff.


This finds minimum required resolution.


Better than:

choosing patch size only from compute considerations.


=======================================================
BLOCK 13 — ROBUSTNESS TO SAMPLING-RATE SHIFT
30 MIN
=======================================================

Scenario:

train:

PPG 128 Hz


new device:

PPG 100 Hz


What happens?


Bad solution:

pretend token indices represent same time.


Options:

resample carefully

physical-time-aware patches

continuous-time encodings

sampling-rate conditioning

multi-rate augmentation during training


Important:

sample count ≠ duration.


Patch size ideally has physical interpretation.


FOLLOW-UPS

"What if anti-alias filtering is needed?"

"What if frequency content changes?"

"What if sampling jitter occurs?"

"Would resampling destroy morphology?"


=======================================================
BLOCK 14 — HARD SYSTEM DESIGN CASE
60 MIN
=======================================================

CASE

Build a multimodal representation for:

PPG: 128 Hz
IMU: 50 Hz
HR: 1 Hz
sleep: sparse events
audio: 16 kHz
text: occasional


Tasks:

1. health-event detection
2. activity classification
3. longitudinal health summarization
4. question answering


CONSTRAINTS:

30-minute windows

missing modalities

limited GPU budget

event detection needs high temporal resolution

text tasks need semantic fusion


DESIGN THE SYSTEM.


Then inject:


1.

Audio causes token explosion.


2.

PPG event lasts only 200 ms.


3.

Sleep is missing 50% of examples.


4.

IMU and PPG clocks drift.


5.

New device samples PPG at 100 Hz.


6.

Cross-attention shows near-zero attention to IMU.


7.

Removing IMU barely changes average score but dramatically hurts
exercise examples.


8.

DINO encoder requires significant adaptation.


9.

Latency must decrease 5×.


For every constraint:

do not restart.

Modify the existing design.


=======================================================
BLOCK 15 — FIVE MAIN YUJIE QUESTIONS
=======================================================

These are the five questions I would expect her to drill hardest.


-------------------------------------------------------
QUESTION 1
-------------------------------------------------------

"How do you choose a time-series representation?"


FOLLOW-UPS

What information do patches lose?

Why delay embeddings?

Why STFT?

Why chart?

What does representation preserve?

What is accessible to the encoder?

What changes with task?


-------------------------------------------------------
QUESTION 2
-------------------------------------------------------

"How would you encode several sensors with very different
sampling rates?"


FOLLOW-UPS

Why not resample?

How do you align time?

Where do timestamps enter?

How do you choose token budgets?

What if sampling rates change?


-------------------------------------------------------
QUESTION 3
-------------------------------------------------------

"How do you fuse modalities?"


FOLLOW-UPS

concat vs cross-attention?

early vs late?

which modality queries which?

where should cross-attention layers go?

what if modality is ignored?

what if sensor-sensor interaction matters?


-------------------------------------------------------
QUESTION 4
-------------------------------------------------------

"How do you handle missing modalities and asynchronous observations?"


FOLLOW-UPS

impute?

mask?

modality dropout?

training mixture?

informative missingness?

what if one modality appears only rarely?


-------------------------------------------------------
QUESTION 5
-------------------------------------------------------

"How do you know the representation/fusion you chose is actually
responsible for the gain?"


FOLLOW-UPS

extra tokens?

extra parameters?

encoder prior?

shuffling tests?

targeted slices?

compression curves?

what would make you delete a tower?


=======================================================
BLOCK 16 — QUESTIONS SPECIFIC TO YOUR DUAL-TOWER WORK
=======================================================

Be ready for these.


"Why two towers instead of one?"


"Why chart + delay?"


"Why isn't chart alone enough?"


"Does 0.79 vs 0.71 prove complementarity?"


"Could additional tokens explain it?"


"What happens if you shuffle the delay tower?"


"Why DINO?"


"Why does Qwen ViT behave differently?"


"What if I give DINO 10× more adaptation compute?"


"Would you still use this design for raw PPG?"


"Would you use matplotlib for Apple Watch signals?"


Strong answer:

Not automatically.

The representation needs to be re-evaluated for:

signal
task
pretraining prior
deployment constraints.


"What experiment would convince you to remove delay entirely?"


If:

chart-only matches dual

under matched resources

across targeted dynamics tasks,

drop delay.


=======================================================
BLOCK 17 — RAPID-FIRE TECHNICAL QUESTIONS
30 MIN
=======================================================

Answer each in 30–60 seconds.


1. Patch size doubles. What changes?

2. Why overlap patches?

3. What is the downside of overlap?

4. STFT window doubles. What changes?

5. Why could interpolation be harmful?

6. When is interpolation appropriate?

7. Why use timestamps in addition to positions?

8. How does missingness become signal?

9. Why not concatenate all modalities?

10. Why could cross-attention ignore a modality?

11. How would you detect modality collapse?

12. What does modality shuffling test?

13. Why might pretrained vision features help time series?

14. When would you train a sensor encoder from scratch?

15. What if the representation contains information but the encoder
cannot access it?

16. What does a latent bottleneck buy?

17. What does it cost?

18. How do you allocate tokens between modalities?

19. Why might fixed token allocation be wrong?

20. How would you evaluate representation robustness?


=======================================================
FINAL YUJIE MENTAL MODEL
=======================================================

Do not say:

"This architecture is best."


Say:

"For this task, I need information X.

Representation A exposes X while sacrificing Y.

Encoder B has prior Z.

Compression gives token budget C.

Fusion is chosen because interaction pattern D is required.

The main failure risk is E.

I would test that with experiment F."


THE CORE CHAIN:

INFORMATION
→ REPRESENTATION
→ ACCESSIBILITY
→ TOKENS
→ TIME
→ FUSION
→ TRAINING
→ EVIDENCE


=======================================================
THE THREE ADVANCED IDEAS TO REMEMBER
=======================================================

1. INFORMATION != ACCESSIBILITY

A representation can preserve information that the selected encoder
cannot easily extract.


2. PHYSICAL TIME != TOKEN POSITION

This matters enormously when fusing different rates.


3. ABLATE THE CLAIMED MECHANISM

If I claim a modality contributes temporal dynamics,
destroy temporal dynamics while preserving other properties and see
whether the gain disappears.


=======================================================
TARGET STATE
=======================================================

After this practice, I should be comfortable if Yujie spends:

20 minutes

on ONE decision such as:

"Why delay embeddings?"

or:

"Why cross-attention?"

or:

"How should 128-Hz PPG and 1-Hz HR interact?"


I should be able to move:

high-level design
    ↓
tensor/token consequences
    ↓
information theory / representation intuition
    ↓
training implications
    ↓
specific ablation


without changing the subject.


FINAL SENTENCE

"The representation isn't merely preprocessing.

It determines what information is exposed to the encoder, the number
and geometry of tokens the model sees, which pretrained priors are
useful, and ultimately what kinds of cross-modal reasoning the
architecture can learn."
