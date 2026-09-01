# On-site — Chung-Cheng: 30-minute final review

Companion to [`2026-08-27_onsite-chung-cheng.md`](2026-08-27_onsite-chung-cheng.md). Diagnose first; do not restudy A1–A7 as a list of tools.

```text
CHUNG-CHENG — 30-MINUTE FINAL REVIEW
LLM Training & Infrastructure
====================================

PURPOSE

I already know the basic definitions.

The goal of this review is to be able to reason through
training-system questions rather than list technologies.

For almost every question, use:

FAILURE
  ->
BOTTLENECK
  ->
DOMINANT TERM
  ->
INTERVENTION
  ->
TRADEOFF
  ->
MEASURE AGAIN


The major bottlenecks are:

MEMORY
COMPUTE
COMMUNICATION
DATA / I/O
SYNCHRONIZATION
OPTIMIZATION / NUMERICS


====================================
1. TRAINING MEMORY: DIAGNOSE FIRST
====================================

Training memory has four major buckets:

1. Parameters
2. Gradients
3. Optimizer states
4. Activations


PARAMETER-RELATED MEMORY

Depends on:

- number of parameters
- parameter dtype
- gradient dtype
- optimizer
- optimizer-state dtype
- whether FP32 master weights exist
- whether states are replicated or sharded


With Adam, optimizer states can be substantial because
we maintain first and second moments.

Do not memorize one universal "bytes per parameter" number.

Ask what the actual implementation stores.


ACTIVATION MEMORY

Depends strongly on:

- microbatch size
- sequence length
- hidden size
- number of layers
- attention implementation


Important diagnostic clue:

If the model fits at sequence length 2k but OOMs at 16k,
parameter count did not change.

Activations / attention are obvious suspects.


------------------------------------
WHAT SOLVES WHAT?
------------------------------------

Smaller microbatch:

reduces activation memory.


Gradient accumulation:

allows a large effective batch while keeping each
microbatch small.


Activation checkpointing:

stores fewer activations and recomputes them during
backward.

TRADEOFF:

memory down
compute up


FSDP / ZeRO:

reduces replicated model-state memory through sharding.

TRADEOFF:

memory down
communication up


IMPORTANT:

Activation checkpointing does not shard optimizer states.

FSDP does not magically solve an architecture that creates
an absurd number of tokens.


====================================
2. GLOBAL BATCH SIZE
====================================

A systems change can silently become an optimization change.

Approximately:

global batch
=
microbatch per GPU
*
data-parallel workers
*
gradient accumulation steps


Example:

microbatch = 4
8 GPUs
accumulation = 8

global batch = 256


Now increase:

8 GPUs -> 64 GPUs


If everything else remains fixed:

global batch becomes 2048.


That may require reconsidering:

- learning rate
- warmup
- number of optimizer steps
- training schedule


Therefore if scaling changes training quality, ask:

"Did we actually preserve the optimization setup?"


GRADIENT ACCUMULATION

Processes multiple microbatches sequentially before one
optimizer update.

It saves activation memory relative to processing the full
effective batch simultaneously.

But it does not provide the same throughput benefit as
processing those microbatches concurrently on additional
GPUs.


====================================
3. DDP VS FSDP / ZERO
====================================

DDP:

same model
different data


Each GPU has a model replica.

Each GPU processes a different batch.

During backward, gradients are synchronized, commonly using:

ALL-REDUCE


DDP is primarily useful for:

THROUGHPUT SCALING


But conventional DDP replicates model states.

Therefore it does not solve the fundamental problem:

"This model's training state does not fit on one GPU."


------------------------------------

ZeRO progressively removes replication.


Stage 1:

shard optimizer states


Stage 2:

shard optimizer states + gradients


Stage 3:

shard optimizer states + gradients + parameters


FSDP follows the same broad full-sharding idea:

keep parameters sharded when possible,
gather what is needed for computation,
then reshard.


The central tradeoff is:

REPLICATION
vs
COMMUNICATION


DDP:

more replication
less parameter-sharding communication


FSDP:

less replication
more communication


Therefore:

FSDP can make a model fit

AND

make training slower.


That is not contradictory.


====================================
4. THE THREE COLLECTIVES I SHOULD KNOW
====================================

ALL-REDUCE

Each worker contributes values.

They are combined.

Every worker receives the combined result.


Typical example:

DDP gradient synchronization.


------------------------------------

ALL-GATHER

Each worker owns a shard.

Gather shards to construct the full object.


Mental picture:

SHARDS -> FULL


Typical example:

gathering sharded parameters for computation.


------------------------------------

REDUCE-SCATTER

Combine distributed contributions

and leave each worker with only its resulting shard.


Mental picture:

COMBINE -> SHARDS


Typical example:

sharded gradient handling.


I do not need to recite collective algorithms.

I should understand:

what information each GPU needs
and why communication is necessary.


====================================
5. DATA, TENSOR, AND PIPELINE PARALLELISM
====================================

DATA PARALLELISM

same model
different data


Goal:

throughput.


------------------------------------

TENSOR PARALLELISM

split operations inside a layer across GPUs.


Example:

Y = XW


split W across GPUs.


Useful when individual layers are too large or expensive.

But TP introduces frequent communication inside the model.

Therefore it benefits strongly from:

fast interconnect.


------------------------------------

PIPELINE PARALLELISM

split model depth.


GPU 0:
layers 1-10

GPU 1:
layers 11-20

GPU 2:
layers 21-30


Use microbatches to keep pipeline stages busy.

Problem:

pipeline bubbles.


------------------------------------

VERY LARGE TRAINING MAY COMBINE:

TP + PP + DP


Different dimensions solve different problems:

TP:
split layers

PP:
split depth

DP:
process more data


Topology matters.

Communication-heavy TP is often best placed across GPUs
with very fast local interconnect.


====================================
6. WHY MORE GPUs STOP HELPING
====================================

Suppose:

8 GPUs  -> 1000 tokens/sec
64 GPUs -> 3000 tokens/sec


Training is faster.

But scaling efficiency is poor.


Do NOT immediately say:

"Communication overhead."


Ask what workers are waiting for.


Possible bottlenecks:

COMPUTE

COMMUNICATION

DATA LOADING

SYNCHRONIZATION

LOAD IMBALANCE


As GPU count increases:

work per GPU may decrease

while collective communication and synchronization remain
significant.


Eventually:

communication / synchronization can dominate.


Other possibilities:

- slow network
- poor topology
- dataloader starvation
- straggler workers
- very small microbatch per GPU
- pipeline bubbles


Correct response:

PROFILE FIRST.


Look at:

GPU utilization
kernel timeline
collective time
data-loading time
idle periods


Question:

"Are GPUs computing, waiting for data, or waiting for
other GPUs?"


====================================
7. STRONG VS WEAK SCALING
====================================

Easy distinction to overlook.


STRONG SCALING

Keep total workload fixed.

Add GPUs.

Ask:

"How much faster can I solve the same problem?"


WEAK SCALING

Increase workload as GPUs increase while approximately
preserving workload per GPU.


Therefore:

"How well does this system scale?"

is incomplete without specifying the experiment.


====================================
8. MFU AND GPU UTILIZATION
====================================

High GPU utilization is not automatically good.

The GPU could be efficiently doing unnecessary work.


MFU — Model FLOPs Utilization — asks approximately how much
of theoretical compute is being used for useful model
computation.


Low MFU can result from:

- communication
- memory bandwidth
- small/inefficient kernels
- synchronization
- pipeline stalls
- data starvation


But the real objective is:

USEFUL TRAINING THROUGHPUT


not maximizing a utilization statistic.


====================================
9. ATTENTION AND SEQUENCE LENGTH
====================================

Self-attention:

Q = X W_Q
K = X W_K
V = X W_V


The interaction:

Q K^T


creates a T x T score structure.


Therefore dense self-attention has quadratic interaction
cost in sequence length.


Double sequence length:

approximately 4x pairwise interactions.


This becomes particularly important for multimodal models.


Suppose:

text = 2k tokens
wearable stream = 30k tokens


Simply concatenating everything into one transformer may be
architecturally and computationally wasteful.


====================================
10. WHAT FLASHATTENTION ACTUALLY DOES
====================================

DO NOT SAY:

"FlashAttention makes attention linear."


It does not.


FlashAttention computes exact attention with a much more
I/O-efficient algorithm.

A major idea is:

avoid repeatedly moving/materializing huge intermediate
attention structures in expensive GPU memory.


It improves:

memory behavior
speed


But it does not eliminate the fundamental quadratic
interaction structure of dense attention.


Therefore:

FlashAttention is valuable

BUT

30,000 unnecessary sensor tokens may still be a bad
representation.


====================================
11. MULTIMODAL TOKEN EXPLOSION
====================================

Suppose:

PPG = 128 Hz
accelerometer = 50 Hz
heart rate = 1 Hz


Bad default:

resample everything to 128 Hz
and create one token per sample.


Problems:

- enormous token count
- redundant slow-channel values
- attention cost
- activation memory
- expensive cross-modal interaction


Better:

encode each modality at an appropriate/native rate.


Possible tools:

patching
local temporal encoders
downsampling
hierarchical encoding
latent resampling
cross-attention


Example:

20,000 sensor tokens
   ->
sensor encoder / resampler
   ->
128 latent tokens
   ->
LLM


Tradeoff:

COMPUTE ↓

but possibly:

INFORMATION ↓


So token compression itself needs validation.


====================================
12. CROSS-ATTENTION VS CONCATENATION
====================================

If I concatenate everything:

sequence length ≈ T_text + T_sensor


dense self-attention scales roughly with:

(T_text + T_sensor)^2


With cross-attention:

queries length = Tq
keys/values length = Tk


interaction cost roughly involves:

Tq * Tk


This can control multimodal interaction cost.


It also allows modalities to retain specialized encoders.


But cross-attention is not automatically better.

Architecture should follow:

- interaction needed
- token counts
- alignment
- missing modalities
- compute budget


====================================
13. PACKING VS PADDING
====================================

Suppose sequence lengths are:

100
120
150
2000


Padding everything to 2000 wastes huge amounts of compute.


PACKING:

combine shorter examples efficiently into larger sequences.


Benefit:

better token utilization.


But implementation must preserve boundaries.

Independent examples should not accidentally attend to each
other unless intentionally designed that way.


Also verify:

attention masks
loss masks


Packing bugs can silently corrupt training.


====================================
14. LOSS SPIKE / NAN: DEBUG SYSTEMATICALLY
====================================

Suppose:

training is stable until step 20,000

then loss spikes and becomes NaN.


Bad answer:

"Lower the learning rate."


Use four categories:


1. DATA

Did a bad batch appear?

Corrupt sample?

Extreme sequence length?

Invalid tokens?

Bad mask?


2. OPTIMIZATION

LR too high?

Scheduler transition?

Gradient explosion?

Effective batch changed?


3. NUMERICS

NaN/Inf activations?

FP16 overflow?

Unstable operation?


4. DISTRIBUTED / SYSTEM

One bad rank?

Synchronization problem?

Checkpoint/resume issue?

Different behavior across workers?


The most useful first question:

"WHAT CHANGED around the failure?"


Then reproduce / inspect the failing region if possible.


====================================
15. BF16 VS FP16
====================================

Both reduce memory/bandwidth compared with FP32.


FP16:

more mantissa precision

but much smaller dynamic range.


BF16:

fewer mantissa bits

but exponent range comparable to FP32.


Therefore BF16 is often easier for large-model training
because of its dynamic range.


Do NOT say:

"BF16 is more accurate."


It isn't universally.


FP16 often requires more careful loss scaling.


====================================
16. CHECKPOINTING HAS TWO MEANINGS
====================================

ACTIVATION CHECKPOINTING:

save activation memory by recomputing forward operations.


TRAINING CHECKPOINT:

save training state to disk/storage so training can resume.


Do not confuse them.


A robust training checkpoint may include:

model parameters
optimizer states
scheduler
training step
random-number state
possibly data-loader position


With distributed/sharded training, checkpointing itself can
be a distributed-systems problem.


====================================
17. RESUME BUGS ARE EASY TO MISS
====================================

Suppose weights restore correctly.

Training still diverges after resume.


Possible reasons:


OPTIMIZER STATE NOT RESTORED

Adam moments reset.


SCHEDULER NOT RESTORED

learning rate jumps.


TRAINING STEP WRONG

schedule/warmup becomes inconsistent.


DATA POSITION WRONG

examples repeat or disappear.


RNG STATE WRONG

exact reproducibility disappears.


Therefore:

"model weights loaded successfully"

does not mean:

"training resumed correctly."


====================================
18. LORA VS QLORA
====================================

LoRA:

keep base weights frozen

learn low-rank updates:

ΔW = BA


Advantages:

far fewer trainable parameters
smaller gradient/optimizer-state requirements
small adapters


But:

the base model still exists in memory and participates in
forward/backward computation.


Therefore LoRA does NOT remove all memory pressure.


QLoRA:

quantize the frozen base model

+

train LoRA adapters.


So the distinction is:


LoRA

reduces TRAINABLE STATE.


QLoRA

also reduces storage/memory for the frozen base.


====================================
19. MULTIMODAL STAGED TRAINING
====================================

Suppose:

pretrained sensor encoder
+
projector
+
pretrained LLM


One useful strategy:


STAGE 1

freeze major pretrained components

train alignment/projector.


Question:

Can the sensor representation be translated into something
the language model can use?


STAGE 2

selectively adapt:

LLM
sensor encoder
or both


using LoRA or full fine-tuning as appropriate.


Why stage?

Not because staging is always optimal.


Because it can:

- preserve pretrained capabilities
- reduce compute
- isolate failure modes


If everything is unfrozen immediately and training fails,
it is harder to determine whether the problem was:

representation
alignment
optimization
catastrophic forgetting
supervision


====================================
20. SFT: LOSS MASKING
====================================

For instruction tuning:

USER:
...

ASSISTANT:
...


we often train primarily on assistant response tokens.


Prompt/system/padding tokens can be masked from the loss.


Important distinction:

ATTENTION MASK

controls what tokens can attend to.


LOSS MASK

controls which token predictions contribute to the
training objective.


Confusing the two can create subtle bugs.


====================================
21. CASE: 30B MODEL OOMS
====================================

Do not start with:

"Use FSDP."


Start:

"Where is the memory going?"


Estimate:

parameters
gradients
optimizer states
activations


Then reason.


If activations dominate:

- smaller microbatch
- gradient accumulation
- activation checkpointing
- memory-efficient attention
- reduce unnecessary sequence length


If replicated model state dominates:

- ZeRO/FSDP


If individual layers are too large:

- tensor parallelism


If model depth must be distributed:

- pipeline parallelism


Then profile again.


Maybe I solved:

MEMORY


but created:

COMMUNICATION BOTTLENECK.


====================================
22. CASE: FSDP FITS BUT IS SLOW
====================================

This is completely plausible.


Why?

Sharded parameters may need to be all-gathered for
computation.

Gradients may require reduce-scatter.

Communication may now dominate.


Investigate:

- communication time
- network/interconnect
- sharding granularity
- FSDP configuration
- per-GPU workload
- topology


Principle:

Use the least aggressive parallelism that satisfies the
memory constraint while maintaining good throughput.


====================================
23. CASE: 8 GPUS GOOD, 64 GPUS BAD
====================================

Do not answer with one hypothesis.


Ask:

What are the extra GPUs waiting for?


PROFILE:

compute
communication
data
synchronization


Likely possibilities:

communication becomes dominant

per-GPU workload too small

stragglers

data pipeline cannot feed 64 GPUs

network topology changes across nodes


Also check:

Did global batch change?

Did optimization change?


Systems scaling and optimization scaling are separate
questions.


====================================
24. CASE: SENSOR TOKENS CAUSE OOM
====================================

Suppose adding wearable signals creates:

30,000 additional tokens.


Do not immediately:

add GPUs
use FSDP
use checkpointing


First ask:

Should there be 30,000 tokens?


Consider:

native-rate encoding
patching
local encoder
latent resampler
cross-attention


Then use infrastructure techniques on the resulting
reasonable architecture.


Important principle:

Do not solve a representation problem only with
infrastructure.


====================================
25. FINAL DIAGNOSTIC FRAMEWORK
====================================

When asked:

"Training is slow."


I ask:

Where is time going?


COMPUTE?
COMMUNICATION?
DATA?
SYNCHRONIZATION?


------------------------------------

When asked:

"Training OOMs."


I ask:

What memory dominates?


PARAMETERS?
GRADIENTS?
OPTIMIZER?
ACTIVATIONS?


------------------------------------

When asked:

"Training diverged."


I ask:

What changed?


DATA?
OPTIMIZATION?
NUMERICS?
DISTRIBUTED STATE?


------------------------------------

When asked:

"Scaling is poor."


I ask:

What are workers waiting for?


------------------------------------

Then:

choose the simplest intervention

state its tradeoff

profile again.


====================================
30-SECOND FINAL RECALL
====================================

DDP
-> throughput, replicated model


FSDP / ZeRO
-> model-state memory ↓
-> communication ↑


Activation checkpointing
-> activation memory ↓
-> recomputation ↑


Gradient accumulation
-> larger effective batch without larger microbatch


TP
-> split operations/layers
-> frequent communication


PP
-> split depth
-> pipeline bubbles


All-reduce
-> combine and give result to everyone


All-gather
-> shards to full


Reduce-scatter
-> combine and leave shards


FlashAttention
-> exact attention with much better I/O behavior
-> NOT linear attention


BF16
-> large dynamic range


LoRA
-> fewer trainable parameters


QLoRA
-> quantized frozen base + LoRA


Packing
-> reduce padding waste


Multimodal token explosion
-> question representation before scaling infrastructure


FINAL SENTENCE

Before choosing a distributed-training technique,
I want to identify whether the limiting resource is
memory, compute, communication, data throughput,
synchronization, or optimization stability.

Then I choose the simplest intervention that addresses
that bottleneck, state the tradeoff it introduces,
and measure again.
```
