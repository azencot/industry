# On-site — Chung-Cheng: challenging practice mock (Tue 9/1)

Companion to [`2026-08-27_onsite-chung-cheng.md`](2026-08-27_onsite-chung-cheng.md) and [`2026-09-01_onsite-chung-cheng-training-infra.md`](2026-09-01_onsite-chung-cheng-training-infra.md).

**Outcome:** Q1–Q4 spoken. **Q5 not answered live** — global batch 128→1024 and ~8× fewer optimizer updates at a fixed token budget. Q2 correction: same per-GPU microbatch means wait-time (comm / data / stragglers), not “less compute per GPU.”

```text
CHUNG-CHENG — CHALLENGING PRACTICE
LLM Training & Infrastructure
=================================

PURPOSE

These questions test diagnosis rather than terminology.

For each systems problem:

1. Identify what changed.
2. Locate the likely bottleneck.
3. Gather evidence before intervening.
4. Choose the intervention that attacks that bottleneck.
5. State the new tradeoff introduced.


============================================================
QUESTION 1 — LONG-SEQUENCE OOM
============================================================

SCENARIO

Train a 13B transformer with AdamW on:

8 x 80 GB GPUs

using FSDP.


At sequence length:

2,048

microbatch 4/GPU works.


Change ONLY sequence length to:

16,384


Even:

microbatch 1/GPU

OOMs.


An engineer proposes:

"Move from 8 GPUs to 16 GPUs and use more aggressive
parameter sharding."


QUESTION

What is likely happening?

What evidence would confirm it?

What changes should I try, and in what order?

Does adding/sharding across more GPUs attack the likely
bottleneck?


------------------------------------------------------------
MY REASONING
------------------------------------------------------------

For a 13B model, model-state memory is substantial.

Roughly:

parameters
gradients
optimizer states


With BF16 parameters:

13B * 2 bytes ≈ 26 GB parameters


But exact training-state memory depends on:

- gradient dtype
- optimizer-state dtype
- FP32 master weights
- implementation
- sharding strategy


The important observation is:

MODEL SIZE DID NOT CHANGE.

Only:

SEQUENCE LENGTH

changed.


Therefore the first suspect should be:

ACTIVATION / ATTENTION MEMORY


rather than:

parameter / optimizer memory.


Going:

2k -> 16k

dramatically increases activation memory.

For naive dense attention, the attention interaction also
grows quadratically with sequence length.


------------------------------------------------------------
HOW TO CONFIRM
------------------------------------------------------------

Profile peak memory while varying sequence length:

2k
4k
8k
16k


Also determine WHERE OOM occurs:

forward attention?

backward?

optimizer step?


Compare memory with and without:

FlashAttention
activation checkpointing


If model-state memory remains roughly constant while peak
memory explodes with T:

activation / attention memory is implicated.


------------------------------------------------------------
INTERVENTION ORDER
------------------------------------------------------------

1. FlashAttention / memory-efficient attention

Avoid materializing enormous attention intermediates and
improve attention I/O behavior.


2. Activation checkpointing

Store fewer activations and recompute them during backward.

Tradeoff:

memory ↓
compute ↑


3. Reduce microbatch

Already at 1 in this example.


4. Recover desired effective/global batch with gradient
   accumulation if necessary.


5. Only then consider additional GPUs / more aggressive
   sharding if model-state memory remains an important
   constraint.


------------------------------------------------------------
IMPORTANT NUANCE
------------------------------------------------------------

More GPUs can reduce per-rank MODEL-STATE memory if additional
sharding is possible.

But they do not directly solve the fundamental problem:

one extremely long sequence creates enormous activation and
attention memory on the rank processing it.


CORE LESSON

If changing only sequence length causes OOM:

do not immediately attack parameter memory.


============================================================
QUESTION 2 — POOR SCALING
============================================================

SCENARIO

Train a 7B model.


8 GPUs:

throughput = 1,000 tokens/sec
GPU utilization = 93%


64 GPUs:

throughput = 3,200 tokens/sec
GPU utilization = 48%


Per-GPU microbatch is unchanged.


QUESTION

What are the top hypotheses?

How do I distinguish:

1. communication bottleneck
2. data-pipeline starvation
3. load imbalance / stragglers?


------------------------------------------------------------
INITIAL REASONING
------------------------------------------------------------

The system became faster overall:

1000 -> 3200 tokens/sec


but nowhere near ideal scaling.


GPU utilization:

93% -> 48%


suggests GPUs spend much more time waiting.


An Amdahl-style view is useful:

parallel compute may scale

while:

communication
input
synchronization
checkpointing
other serial/system costs

do not scale similarly and may even increase.


IMPORTANT CORRECTION:

Because PER-GPU microbatch is unchanged, each GPU still has
roughly similar local compute work per step.

Therefore:

"there is much less compute per GPU"

is not the strongest first explanation here.


Instead, increasing GPU count may have greatly increased:

communication
synchronization
cross-node overhead


especially if 64 GPUs cross machine/node boundaries.


------------------------------------------------------------
DIAGNOSIS
------------------------------------------------------------

PROFILE STEP TIME INTO:

COMPUTE
COMMUNICATION
INPUT
IDLE / SYNCHRONIZATION


Ask:

What are GPUs waiting for?


------------------------------------------------------------
COMMUNICATION BOTTLENECK
------------------------------------------------------------

Evidence:

large fraction of step time inside collectives.


Inspect:

all-reduce
all-gather
reduce-scatter


Compare:

intra-node scaling
vs
inter-node scaling


Possible experiments:

- fewer ranks
- different sharding configuration
- DDP vs FSDP configuration where appropriate
- topology-aware placement


If collective time dominates:

communication/network/topology is implicated.


------------------------------------------------------------
DATA PIPELINE STARVATION
------------------------------------------------------------

Excellent diagnostic experiment:

REAL DATA

vs

SYNTHETIC / DUMMY BATCHES


If dummy batches restore high GPU utilization:

the input pipeline is likely the bottleneck.


Possible causes:

disk/network storage
tokenization
CPU preprocessing
dataloader workers
prefetching


------------------------------------------------------------
STRAGGLERS
------------------------------------------------------------

Inspect:

per-rank step times
when each rank reaches synchronization points


Pattern:

most ranks finish computation

then wait

because one/few ranks consistently arrive late.


Possible causes:

uneven batches
hardware issue
data processing variation
network issue
load imbalance


CORE ANSWER

"At 64 GPUs, 48% utilization tells me the GPUs are spending
much more time waiting. I'd profile step time into compute,
collectives, input and idle. If dummy batches restore
utilization, it's the data path. If collective time
dominates, it's communication/topology. If some ranks
consistently enter collectives late, it's load imbalance or
stragglers."


============================================================
QUESTION 3 — BAD CHECKPOINT RESUME
============================================================

SCENARIO

Train for:

40,000 steps.


Job is preempted.


Restore:

MODEL WEIGHTS


but accidentally do NOT restore:

OPTIMIZER STATE
SCHEDULER STATE


Loss initially looks normal.

After a few hundred steps:

performance becomes noticeably worse than an uninterrupted
run.


QUESTION

Why?

What exactly is missing?

What must be checkpointed for a trustworthy resume?


------------------------------------------------------------
OPTIMIZER STATE
------------------------------------------------------------

AdamW maintains state including:

first moment m

second moment v


At step 40k these statistics contain substantial history.


If they are reset:

the optimizer behaves partly like a fresh optimizer operating
on already-trained model weights.


This changes the effective preconditioning / update dynamics.


So it is stronger to say:

"optimizer geometry changed"

rather than merely:

"gradients became noisier."


------------------------------------------------------------
SCHEDULER STATE
------------------------------------------------------------

Suppose training uses:

warmup
+
cosine decay


At step 40k the LR may be relatively small.


If scheduler state is reset:

LR might:

jump upward
restart warmup
follow the wrong point in the schedule


That can substantially change optimization.


------------------------------------------------------------
ROBUST CHECKPOINT CONTENT
------------------------------------------------------------

Save/restore:

MODEL PARAMETERS

OPTIMIZER STATE
- Adam moments

SCHEDULER STATE

GLOBAL / OPTIMIZER STEP

RNG STATES

SAMPLER / DATA POSITION
- important for deterministic continuation

AMP GRADIENT SCALER
- if relevant, especially FP16 training


------------------------------------------------------------
FSDP NUANCE
------------------------------------------------------------

Do not categorically say:

"checkpoint must be per-rank."


Depending on the checkpoint strategy, state may be stored:

sharded

or

gathered/full.


The important requirement is:

distributed/sharded state and associated metadata must be
restored consistently across ranks.


------------------------------------------------------------
GOOD VERIFICATION
------------------------------------------------------------

After resume:

verify LR

verify global step

verify optimizer state exists

verify data position if required


For high-confidence reproducibility:

compare a few resumed steps against an uninterrupted
reference run.


CORE LESSON

"Model weights loaded"

does NOT imply:

"training resumed correctly."


============================================================
QUESTION 4 — MULTIMODAL TOKEN EXPLOSION
============================================================

SCENARIO

Add wearable data to a pretrained 8B LLM.


For each 10-minute example:

PPG = 128 Hz

IMU = 50 Hz

heart rate = 1 Hz

text ≈ 1,500 tokens


First implementation:

project EVERY raw sensor sample into an LLM token

concatenate all modalities

dense self-attention


Training:

extremely slow

OOMs even with:

FlashAttention
FSDP


Someone says:

"We have 4x more GPUs."


QUESTION

What should I change?

Separate:

REPRESENTATION / ARCHITECTURE

from:

INFRASTRUCTURE


What information might I lose?


------------------------------------------------------------
FIRST: CALCULATE THE SCALE
------------------------------------------------------------

10 minutes = 600 seconds.


PPG:

128 * 600 = 76,800 samples


IMU:

50 * 600 = 30,000 samples


HR:

1 * 600 = 600 samples


Total sensor samples:

107,400


plus:

~1,500 text tokens.


This is a representation problem before it is an
infrastructure problem.


------------------------------------------------------------
WHY CONCATENATION IS BAD HERE
------------------------------------------------------------

Dense self-attention sees approximately:

109k tokens.


Pairwise interaction grows quadratically with sequence
length.


FlashAttention improves:

memory behavior
I/O efficiency


but does NOT make dense attention linear.


FSDP reduces:

replicated model-state memory


but does NOT solve:

107k sensor tokens.


Adding GPUs does not make this representation sensible.


------------------------------------------------------------
REPRESENTATION FIX
------------------------------------------------------------

Prefer something like:

RAW SIGNALS AT NATIVE RATES

        ↓

MODALITY-SPECIFIC PATCHING / LOCAL ENCODERS

        ↓

BOUNDED TOKEN SET PER MODALITY

        ↓

MULTIMODAL FUSION


Do NOT necessarily use the same patch duration for every
modality.


PPG and IMU:

may require relatively fine local temporal resolution.


Heart rate:

may support much stronger temporal compression.


Possible tools:

patching
local temporal encoders
downsampling
hierarchical encoders
latent resampling


Example:

107k raw samples

    ↓

few hundred / ~1000 meaningful modality tokens


Exact token budget should be experimentally determined.


------------------------------------------------------------
CROSS-ATTENTION
------------------------------------------------------------

Instead of putting every token into one giant
self-attention sequence:

use specialized modality representations and controlled
cross-attention.


Self-attention over concatenation:

approximately

(T_text + T_sensor)^2


Cross-attention interaction:

approximately

T_query * T_key/value


But:

cross-attention to 107k raw K/V tokens is STILL expensive.


Therefore:

COMPRESS FIRST

then:

CROSS-ATTEND.


Example:

107k sensor samples

    ↓

modality encoders / resampler

    ↓

128–1000 sensor latent tokens

    ↓

cross-attention with text/model representation


------------------------------------------------------------
WHAT INFORMATION MAY BE LOST?
------------------------------------------------------------

Compression can destroy:

short transients
high-frequency morphology
local temporal events
motion artifacts that are diagnostically useful
precise temporal relationships


For example:

aggressive PPG pooling could erase a short arrhythmic
pattern.


Therefore do not simply:

"compress as much as possible."


Instead evaluate performance versus:

patch size
token budget
sampling/compression level


especially on tasks/slices requiring high temporal
resolution.


------------------------------------------------------------
OTHER ARCHITECTURAL RISK
------------------------------------------------------------

Cross-attention does not guarantee the LLM uses the wearable
information.

The model may ignore the modality.


Test with:

modality ablation
shuffling
masking
targeted tasks/slices


------------------------------------------------------------
INFRASTRUCTURE AFTER ARCHITECTURE
------------------------------------------------------------

Once tokenization is reasonable:

profile again.


Then possibly use:

FlashAttention
activation checkpointing
FSDP
gradient accumulation
more GPUs


depending on the remaining bottleneck.


Microbatch 1 can reduce activation memory compared with a
larger microbatch.

But if one example itself contains a pathological sequence
length:

microbatch reduction cannot fix the fundamental design.


CORE LESSON

Do not solve a representation problem only with
infrastructure.


============================================================
QUESTION 5 — OPTIMIZATION × SYSTEMS
NOT ANSWERED DURING PRACTICE
============================================================

SCENARIO

Scale an 8B model from:

8 GPUs

to:

64 GPUs.


Keep:

per-GPU microbatch = 2

gradient accumulation = 8

learning-rate schedule unchanged

same TOTAL number of training tokens


Training becomes faster.


But:

final validation quality is noticeably worse.


Nothing is obviously broken numerically.


QUESTION

What are the top hypotheses?

What should I change first?


------------------------------------------------------------
HOW TO REASON ABOUT IT
------------------------------------------------------------

The first thing to calculate is:

GLOBAL BATCH SIZE.


Approximately:

global batch
=
microbatch/GPU
*
number of data-parallel workers
*
gradient accumulation


Assuming all GPUs participate in data parallelism:


8 GPUs:

2 * 8 * 8 = 128


64 GPUs:

2 * 64 * 8 = 1024


Therefore global batch increased:

8x.


This is NOT merely a systems change.


The optimization problem changed.


------------------------------------------------------------
SAME TOTAL TOKENS, FEWER OPTIMIZER UPDATES
------------------------------------------------------------

If total training tokens remain fixed while global batch
increases 8x:

the 64-GPU run performs roughly 1/8 as many optimizer
updates.


Therefore:

same number of training tokens

does NOT mean:

same optimization trajectory.


This is a major candidate explanation for worse validation.


------------------------------------------------------------
LEARNING-RATE SCHEDULE
------------------------------------------------------------

"Learning-rate schedule unchanged" is ambiguous and
potentially problematic.


Ask:

Is schedule defined in:

optimizer steps?

tokens?

examples?


If it is step-based:

the new run may traverse a very different fraction of the
schedule because it performs far fewer optimizer steps.


Warmup can also become inconsistent.


Example:

same 1000 warmup steps

with an 8x larger global batch

means warmup now consumes approximately 8x more training
tokens.


So always relate scheduling to:

effective batch
optimizer steps
training tokens.


------------------------------------------------------------
LARGE-BATCH OPTIMIZATION
------------------------------------------------------------

Even if LR/schedule are adjusted:

very large batches can change optimization behavior.


Potential effects:

less stochastic gradient noise
fewer parameter updates
different convergence/generalization behavior


Do not assume:

8x batch
+
8x LR

will perfectly reproduce the smaller-batch run.


Linear LR scaling is a heuristic, not a law.


------------------------------------------------------------
TOP HYPOTHESES
------------------------------------------------------------

1. GLOBAL BATCH CHANGED

128 -> 1024.


2. NUMBER OF OPTIMIZER STEPS CHANGED

Same total tokens with 8x batch means far fewer updates.


3. LR / WARMUP / SCHEDULE NO LONGER MATCH TRAINING REGIME

Especially if schedule is step-based.


4. LARGE-BATCH GENERALIZATION / OPTIMIZATION CHANGED

Even after simple LR adjustment.


5. POSSIBLE SYSTEMS EFFECTS

Still check:

data ordering
distributed sampler
effective batch calculation
loss normalization
gradient accumulation semantics


But given the scenario:

optimization change is the first suspect.


------------------------------------------------------------
FIRST EXPERIMENT
------------------------------------------------------------

The cleanest first comparison is to preserve the original
effective global batch if practical.


For example, when increasing GPU count:

reduce gradient accumulation

and/or

per-GPU microbatch


so global batch stays approximately fixed.


Then compare:

training loss
validation
throughput


If quality returns:

the issue was strongly associated with the optimization
change caused by scaling.


------------------------------------------------------------
IF I WANT THE 1024 GLOBAL BATCH
------------------------------------------------------------

Then deliberately retune the training regime.


Consider:

learning rate
warmup
schedule
number of optimizer updates
training duration


Potentially compare schedules defined relative to:

tokens processed

rather than blindly preserving step counts.


Then empirically test whether large-batch training reaches
the desired quality/compute tradeoff.


------------------------------------------------------------
STRONG INTERVIEW ANSWER
------------------------------------------------------------

"The first thing I'd notice is that we did not actually
preserve the training setup.

With microbatch 2 and accumulation 8, moving from 8 to 64
data-parallel GPUs increases global batch from 128 to 1024.

If total training tokens stay fixed, we now make roughly
eight times fewer optimizer updates. An unchanged
step-based LR and warmup schedule therefore represents a
very different optimization trajectory.

My first controlled experiment would preserve the original
global batch while scaling the infrastructure. If quality
recovers, I've separated a systems-scaling problem from a
large-batch optimization problem.

If we intentionally want the larger batch for throughput,
I'd then retune LR, warmup and schedule and determine whether
the reduced update count or large-batch regime itself is
hurting validation.

The important point is that scaling the number of
data-parallel workers can silently change the optimization
problem."


============================================================
WHAT THESE FIVE QUESTIONS WERE REALLY TESTING
============================================================

Q1 — OOM

Can I distinguish:

MODEL-STATE MEMORY

from:

ACTIVATION / SEQUENCE MEMORY?


------------------------------------

Q2 — SCALING

Can I distinguish:

COMPUTE

COMMUNICATION

DATA

STRAGGLERS / SYNCHRONIZATION?


------------------------------------

Q3 — CHECKPOINTING

Do I understand that training state is more than model
weights?


------------------------------------

Q4 — MULTIMODAL SYSTEM

Will I recognize when an infrastructure problem is actually
an architecture / representation problem?


------------------------------------

Q5 — DISTRIBUTED OPTIMIZATION

Will I recognize when an infrastructure scaling change has
silently changed:

GLOBAL BATCH

OPTIMIZER-STEP COUNT

LR SCHEDULE

and therefore the optimization problem?


============================================================
FINAL 60-SECOND RECALL
============================================================

OOM after increasing sequence length:

suspect activations/attention before parameters.


Poor multi-GPU scaling:

profile what GPUs are waiting for.


Checkpoint resume:

weights alone are insufficient.


Huge multimodal sequence:

fix representation before throwing GPUs at it.


More data-parallel GPUs:

always recalculate global batch and optimizer-step count.


And for every systems intervention ask:

WHAT BOTTLENECK DOES THIS ACTUALLY FIX?

WHAT NEW COST DOES IT INTRODUCE?

HOW WOULD I VERIFY THAT MY DIAGNOSIS WAS RIGHT?
```
