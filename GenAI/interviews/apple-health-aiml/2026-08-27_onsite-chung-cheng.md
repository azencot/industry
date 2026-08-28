# On-site — Chung-Cheng Chiu (Wed 1:05 PDT)

Track: LLM training and infrastructure. Conf: very high.

Who (private): Principal RE, Apple AI/ML (Mountain View). AFM reports; AXLearn author (arXiv:2507.05411). Cross-org, not Health.

Hub: 2026-08-27_onsite-prep.md

Sound like: "First I'd establish whether this is a model-state memory, activation, communication, or input-throughput problem."

Not: names of four libraries, or a definition of gradient checkpointing.

Do not name AXLearn / AFM / FlashAttention papers unless he does. Do not volunteer RelCon / Watch. If he asks about a sensor encoder + LLM and throughput dies, treat it as infra (tokens, T^2, input stall) — not a health paper recap.

Your run is evidence at the end, not the lecture: two-stage, DDP, LoRA, TR kill. See 2026-08-20_training-run-drill.md

Already locked (do not restudy AdamW / clip / pack / fp16 scale): GenAI/notes/2026-08-22_llm-training-mechanics-lockin.md

7B order: LoRA, then smaller microbatch or T, then FlashAttn, then checkpoint activations (A), then DDP, then FSDP last.

AXLearn pocket (only if he goes there): production trainer; modular (swap input / ckpt / loop); heterogeneous GPU/TPU/Trainium; parallelism via compiler sharding, not "I forked DeepSpeed." You train on Slurm/DDP — honest: you have not run GSPMD on 1k chips. You have diagnosed fit vs throughput on jobs you owned.

---

## Friday Block A — cover this file today

Goal: I can reason about a large distributed training step — not become an infra specialist overnight.

Habit every answer: (1) name the constraint (memory / compute / comm / I/O / reliability); (2) decompose; (3) one tool; (4) tradeoff; (5) how you'd verify. Diagnose first, prescribe second.

Do not study: NCCL/CUDA internals, ring-allreduce proofs, InfiniBand, compiler IR, Megatron variants, AXLearn source, TPU microarch, RoPE derivation.

A1 — Memory — 50 min. Pass: for 7B / 8B / 30B, split M and say which tool hits P vs G vs O vs A.

A2 — Collectives + DDP + FSDP — 1 hour. Pass: what is replicated vs sharded; what collective fires; why not always FSDP.

A3 — Tensor + pipeline + 3D — 50 min. Pass: 128 GPUs: what each axis buys and costs.

A4 — Runtime: MFU, overlap, 8 to 64 — 50 min. Pass: step-time decomposition without spraying tools.

A5 — Flash, act-ckpt, accum, packing, input — 50 min. Pass: idle GPU vs low MFU vs padding — different levers.

A6 — Checkpoint + NaNs — 30 min. Pass: week-long run: what you save, how you resume.

A7 — 2x compute + sensor+LLM collapse — 30 min. Pass: resource judgment; infra diagnosis if he pulls sensors.

Close — 35 min full mock. Pass: one owned run + 45% util or 8-to-64 + 30B fit.

About 6.5 hours. If short: skip extra arithmetic reps in A1 and the second A7 prompt. Never skip interleaved mocks or Close. Speak answers out loud. After each mock: one sentence on what was mushy, then continue — do not open Wikipedia.

---

## A1 — Training memory

M is roughly P + G + O + A + workspace.

- P = parameters (weights)
- G = gradients
- O = optimizer state (Adam m and v)
- A = activations saved for backward
- workspace = kernels, NCCL buffers, fragmentation

Interview habit: which term is the fire, before naming a library.

P (weights): bf16 is 2 bytes per param. Hit it with FSDP / ZeRO-3 / tensor parallel, or LoRA (train fewer).

G (grads): often bf16. Hit it with FSDP / ZeRO-2/3.

O (Adam m and v): commonly fp32, so 8 bytes per param (two states times 4 bytes). Often the biggest of P, G, O. Hit it with FSDP / ZeRO, or LoRA (tiny O).

A (activations): grows with batch B, sequence length T, hidden size d, number of layers N. Hit it with activation checkpointing, or a smaller microbatch.

Attn tiles: the B x heads x T x T score matrix. Hit it with FlashAttention (not linear-time attention).

FlashAttention is still the usual softmax attention: every query attends to every key, so compute stays about T^2. It just never materializes that T x T matrix in GPU memory — tiled kernels + online softmax, less HBM traffic. Same math, cheaper memory movement.

Linear-time attention is a different algorithm. It avoids the T x T comparison, so compute and memory scale about like T (times hidden size), not T^2. Typical tricks: a kernel/feature map instead of softmax (Performer-style), a low-rank or compressed K/V (Linformer-style), a sliding window (local, not full), or a recurrent/state update (RWKV / linear RNN family). You change the model, not just the kernel. Do not say Flash is linear-time. Do not recite those paper names unless he does.

Effective batch too big to fit: gradient accumulation.

Optional: fp32 master weights on top of bf16 P (implementation-dependent).

Worked example — bf16 weights and grads, Adam m/v in fp32, ignore A:

7B: P about 14 GB (7B params times 2 bytes). G about 14 GB. O about 56 GB (7B times 8 bytes). Replicated DDP state about 84 GB before activations.

8B: P about 16 GB, G about 16 GB, O about 64 GB. Replicated about 96 GB.

30B: P about 60 GB, G about 60 GB, O about 240 GB. Replicated about 360 GB.

7B already does not comfortably fit an 80 GB GPU as a full DDP replica once A shows up. 30B cannot be replicated. That is why FSDP exists.

Do the 8B and 30B arithmetic once on paper. Then: LoRA freezes most of P — O only on adapters; that is why LoRA is first in the 7B order, FSDP last.

Attack map (say this, not ZeRO trivia):

- Parameters: shard P (FSDP-3 / TP) or don't train them (LoRA).
- Gradients: shard G.
- Optimizer: shard O or shrink the trainable set.
- Activations: checkpoint A; cut microbatch B or T.
- Attn intermediates: FlashAttention.
- Batch too small to fit: accum.

---

### Mock A1 (~8 min) — cover, then go on

1. 8B doesn't fit on one GPU. Diagnose, then propose an order.
   Target: split P+G+O+A; 8B state about 96 GB already; 7B order; do not lead with FSDP if LoRA + smaller T + Flash + checkpoint A might suffice.

   Spoken lock (2026-08-28): Check device memory first. 8B, bf16 P and G, fp32 Adam m/v is about 16+16+64 ≈ 96 GB before activations — does not fit on 80 GB as a full replica. That is optimizer state, not activations. Do not fork P vs G vs A as three equal guesses; O is ~4x P, G ≈ P, A has not shown up. If adapters are allowed: LoRA (kills most of O), then shrink T or microbatch + accum, then Flash, then checkpoint A. Do not lead with FSDP on one GPU — sharding needs a fleet. If I must train all 8B: add GPUs, FSDP last. If it later OOMs in the first forward after LoRA, then A: Flash, checkpoint, smaller T.

2. Which of those tools does not reduce optimizer memory?
   Target: FlashAttention and activation checkpointing. They hit A / attn tiles.

   Spoken lock (2026-08-28): O is AdamW m + v, usually fp32 (8 bytes/param vs 2 for bf16 P). LoRA/QLoRA cuts how many params you update, so G and O shrink with the trainable set (QLoRA also shrinks frozen P via 4-bit — that's P, not O). Flash, grad accum, and activation checkpointing do not touch O — they hit A / attn tiles / microbatch. FSDP/ZeRO does reduce per-device O (shard, not shrink the optimizer). Don't say "those tools never help memory"; they help the wrong term.

3. Follow-up: why is O often larger than P?
   Target: two fp32 moments vs one bf16 weight tensor.

   Spoken lock (2026-08-28): AdamW stores m and v, usually fp32 — 8 bytes/param vs 2 for bf16 P, so O is about 4x P. Not "more updates"; same step, fatter tensors. (fp32 master weights would be extra P storage, not O.)

---

## A2 — Collectives, DDP, FSDP

### Collectives

All-reduce: each rank starts with a full tensor, same shape. Everyone ends with the reduced tensor (sum or mean). Typical use: DDP, sync G.

All-gather: each rank starts with a shard. Everyone ends with the concatenated whole. Typical use: FSDP, materialize P for a layer.

Reduce-scatter: each rank starts with a full tensor. After reduce, each rank keeps only its shard. Typical use: FSDP, shard G after backward.

All-to-all: each rank sends a different slice to each peer; pieces get rearranged. Typical use: tensor-parallel activations.

Do not lead with "I'd use NCCL." Name what is being shipped.

### DDP

Job: more tokens/step. Model fits per GPU.

Each GPU: full P (and usually G and O) plus a different batch. Independent fwd/bwd. Then all-reduce G so every replica takes the same Adam step (mean of per-rank grads).

What moves: full G each step. What does not: parameters stay replicated.

Cheap when it fits. Fatal when it doesn't — you replicate the expensive O on every GPU.

You have run DDP. Say that. Don't pretend 128-GPU DDP is the same as 8.

### FSDP / ZeRO

Job: model-state (P, G, O) doesn't fit if replicated. Data is still data-parallel (different batches).

If asked ZeRO stages — what you shard, not a speech:

- ZeRO-1: O
- ZeRO-2: O + G
- ZeRO-3 / FSDP-full: O + G + P

Do not recite stages as the answer. If asked: stage means what you shard. Then the bottleneck.

Mental model: DDP = replicate state, all-reduce grads. FSDP = shard state, all-gather P around the layer, compute, drop, reduce-scatter G.

That per-layer all-gather is the FSDP tax.

Tradeoff: memory down, communication and complexity up. Never "FSDP is better." Say: "FSDP buys per-device state memory with extra collectives; if the model already fits, DDP is often simpler and faster."

When FSDP all-gather is worse than pipeline: slow fabric, tiny compute per layer (gather dominates), or you would rather ship activations between stages than rebuild full P every layer.

---

### Mock A2 (~10 min)

1. Walk DDP vs FSDP on 4 GPUs. What is replicated? What collective?
   Target: DDP: 4 copies of full P, all-reduce G. FSDP: each rank about 1/4 of P, G, O; all-gather P per layer; reduce-scatter G.

   Spoken lock (2026-08-28): DDP — every GPU has full P, G, O; batch is split so A is per-GPU microbatch. After backward, all-reduce G (not P) so every replica takes the same Adam step and P stays identical. Use when that replica fits. FSDP — each GPU keeps 1/n of P, G, O on the same index cuts. Before a layer, all-gather P, GEMM, drop the extra; grads reduce-scatter. Still data parallel. Peak still includes full W for the current layer. ZeRO-1/2/3 is what you shard (O, then G, then P) — don't open with the stages.

2. Why not always FSDP?
   Target: if it fits, DDP can win on comm and complexity.

   Spoken lock (2026-08-28): FSDP trades extra collectives (and complexity) for less per-device state. If the model already fits, DDP is often simpler and faster. Do not say "FSDP is better."

3. FSDP all-gather every layer — when pipeline instead?
   Target: comm-bound gathers vs shipping activations along depth; bubble vs tax.

   Spoken lock (2026-08-28): When all-gather of P dominates step time (slow fabric, fat W, skinny GEMM per layer) — FSDP tax. Pipeline instead keeps each stage's layers resident and ships activations (and backward grads) to the next stage, which can be cheaper than rebuilding full W every layer. Cost: bubble / stragglers; fill with microbatches. Not "pipeline is deeper FSDP." Profile comm vs compute first.

---

## A3 — Tensor, pipeline, 3D

One step is still fwd -> loss -> bwd -> opt. Families split different things. Hybrid is normal.

### Tensor / model parallel

Job: one matmul y = xW (one layer) doesn't fit, or you want GPUs inside the layer.

Split W into W1 and W2. GPU0 computes xW1, GPU1 computes xW2, then all-reduce or all-gather activations so the next op sees a full vector. Usual split points: QKV, MLP.

DP splits examples. TP splits the matmul. FSDP shards state and reconstructs around the layer.

Cost: collectives inside every Transformer layer; volume scales with T and hidden size. TP wants fast interconnect (typically within a node). Across nodes: DP / FSDP / pipeline first.

You have not owned Megatron TP. Honest: you know the job. No 1k-chip story.

### Pipeline

Job: depth doesn't fit: blocks 1-10 on GPU0, 11-20 on GPU1, ...

Naive: GPU1 idle until the first forward arrives = bubble. Microbatches stagger the line (1F1B-style schedules exist — do not memorize them). More microbatches -> smaller relative bubble.

What moves: activations forward and grads backward between adjacent stages — often cheaper than all-gather full P every layer.

Cost: bubble, stragglers (one slow stage stalls everyone).

### 3D / hybrid

No axis scales forever. Example 128 GPUs: tensor parallel 8 x pipeline 4 x data parallel 4.

DP / FSDP buys tokens/step, or shards state. Dies when replica memory blows up, or all-reduce / all-gather latency dominates.

TP buys layer GEMM / layer memory. Dies on intra-layer comm, especially long T.

PP buys total depth. Dies on bubbles, too few microbatches.

Choose (what doesn't fit, then interconnect):

- Fits; want tokens/step -> DDP.
- P+G+O OOM; layers themselves fit -> FSDP; checkpoint A before this.
- One matmul / layer doesn't fit -> tensor (NVLink group).
- Depth / FSDP tax -> pipeline.

Spoken: "Fit state with FSDP; if a layer still doesn't fit, tensor-split on NVLink; if depth is the issue, pipeline and fill with microbatches." Not "DeepSpeed vs Megatron."

---

### Mock A3 (~10 min)

1. 128 accelerators, 30B. How might you combine axes — and why not 128-way DP?
   Target: 30B state about 360 GB replicated; must shard and/or TP/PP; pick an example product that multiplies to 128; TP on the fast domain.

2. 2x GPUs, 1.4x speedup. Why?
   Target: Amdahl; comm fraction; smaller GEMMs; collective latency; pipeline bubble; straggler; dataloader not scaled.

3. Increase B or T?
   Target: no universal. Tokens/step = B * T * n_gpu. Attention is about O(T^2 * d). Long context is a T^2 tax; bigger B is often cheaper if the task doesn't need long T. Objective + memory decide.

---

## A4 — Runtime: compute vs communication

Step time = compute + comm + input + sync + ckpt/other.

Add GPUs -> per-device compute shrinks; comm does not vanish. Comm as a fraction of step time grows. 8 to 64 is not 8x. That is the whole 64-GPU question.

Overlap: bad = compute then a blocking collective. Better = hide all-reduce/all-gather behind backward of another layer. Goal: comm under useful FLOPs.

Throughput for training: tokens/s (not "latency of one sample"). Latency = time for one op / step.

MFU is roughly useful model FLOPs / peak hardware FLOPs. Do not memorize a formula. Low MFU is not "buy FlashAttention." It flags a regime:

- GPUs idle in waves: look at input, straggler, barrier, ckpt pause.
- Comm dominates step time: look at parallelism, topology, collective size, overlap, too-small per-GPU work.
- GPUs busy, MFU still low: kernels, tiny GEMMs, bad shapes, extra recompute (act-ckpt), unfused attn, host .item().
- Huge padding: packing / bucketing / varlen.

Diagnosis order (30B, 128 accelerators, 45% util) — say this:

1. Compute-bound vs communication-bound (MFU vs collective time).
2. Profile step breakdown (fwd / bwd / opt / wait).
3. Input (decode, H2D, host stall).
4. Collectives (FSDP tax).
5. Per-device microbatch too small.
6. Padding / real tokens (ragged T).
7. Activation checkpoint — extra compute, can look like low "useful" MFU.
8. Kernel / attention impl.
9. Host-device sync.

Compare to the 8-GPU run that was healthy. Do not spray tools until the profile names the class.

---

### Mock A4 (~10 min)

1. 8 GPUs fine; 64 GPUs about 4x not 8x. Investigate.
   Target: decompose step time; compare fractions to the 8-GPU job; then one regime.

2. 64-GPU job 30% slower than expected. First three sentences.
   Target: profile, don't prescribe; compute / comm / input / sync; compare to baseline.

3. Follow-up: GPUs busy but MFU 20%. Where do you not start?
   Target: not "add FSDP." Kernels, shapes, padding, recompute, unfused attn.

---

## A5 — Flash, checkpoint A, accum, packing, input

### Activation checkpointing is not a disk checkpoint

Normal fwd saves activations for bwd. Activation checkpointing: save a few, recompute the rest in backward. A down, compute up. Hits A, not P or O. Disk ckpt is a different word — don't mix them.

### FlashAttention

Naive attn materializes B x heads x T x T. Flash = tiled exact attn + online softmax; less HBM traffic. Compute still about O(T^2 * d). Not linear attention. Don't recite the paper.

### Gradient accumulation

Microbatch = what fits one fwd/bwd. Global batch is about microbatch * accum * data-parallel world size (tokens also times T).

Fwd/bwd times accum, then clip, then step, then zero_grad. Clip after accum (locked). Memory down per fwd (smaller A); more sequential microsteps per update.

### Variable T / padding

Attention is about O(T^2 * d). One 4000-token sequence next to 100s, pad-to-max = waste. Levers: bucketing, packing (your -100 / splice mask — else doc B in doc A's CE), varlen kernels, truncate only if the science allows.

### Data pipeline

storage -> CPU preprocess -> tokenize -> batch -> H2D -> GPU.

If the GPU waits for data, more GPUs do nothing. Offline tokenize, shard the dataset, workers, prefetch, pinned memory, async H2D, keep Python off the hot path.

If he pulls multimodal input: reading many files, resampling, STFT, augmentation, varlen, syncing modalities can stall the host. Distinguish model bottleneck vs input bottleneck. Do not volunteer Watch papers.

Your collator / packing is IC evidence for "data pipeline for packed multimodal batches."

---

### Mock A5 (~10 min)

1. Explain activation checkpointing. Cost? What memory term?
   Target: A down, compute up; not disk ckpt; not O.

2. Highly variable sequence lengths — memory and tokens/s?
   Target: T^2; pad-to-max; packing/bucketing; your -100 leak story if asked how packing fails.

3. GPUs periodically idle. First fork.
   Target: input vs straggler vs sync vs ckpt pause — not "FlashAttention."

---

## A6 — Distributed checkpointing and NaNs

A real ckpt is not "the weights file." Include: P, O, LR schedule, step, RNG, AMP scaler if used. At 128 GPUs, state is hundreds of GB.

Bad: gather everything to rank 0, write one blob. Better: sharded save (each rank writes its slice). Concerns: storage bandwidth, pause time, frequency, consistency, resume world size, recovery time.

Tradeoff: frequent ckpt -> less lost work, more I/O. A 3-day / week run that dies at 80%: resume from last consistent shard set; don't restart from scratch; val (not train loss) decides if the ckpt is worth keeping — you have this.

NaNs at 20k steps (not first-step overflow): skip "just lower LR" as the whole answer. Fork: (1) which rank / which layer / which slice of data; (2) loss scale / inf in fp16 (bf16 usually not scale); (3) bad packed labels (-100 miss -> huge CE); (4) LR / wd / clip after a schedule boundary; (5) corrupt ckpt resume; (6) a new long-T batch. Bisect step and data. You killed a TR mix when the average lied — same instinct: don't trust train NLL alone.

---

### Mock A6 (~8 min)

1. Week-long 128-GPU run. Design ckpt/recovery.
   Target: sharded; what you save; frequency vs I/O; resume; don't gather to rank 0.

2. Dies at 80%. What do you do tomorrow morning?
   Target: last good ckpt; don't re-download the world; check val; find the failing step.

3. NaNs after 20k steps.
   Target: not "FSDP." Isolate data vs numerics vs resume vs packing.

---

## A7 — 2x compute, and sensor+LLM only if pulled

2x compute: do not auto-double model size. Candidates: more tokens, better data, longer T (pay T^2), more experiments, better representation, HPO. Applied: small scaling probes -> marginal return -> then spend the big allocation. Do not scale an architecture before it is worth scaling. Your TR mix kill is the story: average up, slice down -> killed.

If he asks: 100 Hz encoder + LLM, throughput collapses. Infra tree, not RelCon:

raw rate -> encoder FLOPs -> sensor token count -> LLM T -> attn T^2 -> A up -> microbatch down -> comm/compute ratio worse -> padding / CPU preprocess / I/O.

Architectural direction: native-rate local encoder -> compress / patch -> few latents -> LLM. Do not resample every modality onto the fastest clock (Yujie sheet; don't name her).

---

### Mock A7 (~8 min)

1. 2x GPUs for a year. Model vs data vs context vs experiments?
   Target: probe first; don't double 30B by default; kill criteria.

2. Throughput collapses after adding a high-rate encoder. Diagnose.
   Target: tokens and T^2 and input stall; local encoder + patch; not "use FSDP."

---

## Close — 35 min full mock (do this last)

Play cross-org FM engineer. IC verbs. No AXLearn name-drop. No RelCon.

0-8 min: Broad: a run you owned including infra (DDP, LoRA, collator, TR kill). Evidence at the end.

8-20 min: Drill: 45% util on 30B at 128, or 8-to-64 about 4x. Diagnosis order.

20-30 min: Scenario: 30B doesn't fit — P vs A vs one layer vs depth.

30-35 min: Your Q: how they debug scaling (not "do you use AXLearn").

Strong close (memorize the shape, not the nouns):

I'd first determine where step time is going: model compute, collectives, input stalls, sync — and compare those fractions to the smaller run that worked. If comm grew dominant, I'd look at parallelism, topology, collective sizes, and overlap with backward. If GPUs are periodically idle, I'd look at input or stragglers. I wouldn't change the parallelism strategy until the profile says which regime I'm in.

---

## Predicted questions (full list)

1. 8 GPUs fine; 64 GPUs about 4x not 8x.
2. 30B, 128 acc, 45% util — diagnosis order.
3. DDP vs FSDP vs tensor vs pipeline — choose.
4. 2x GPUs, 1.4x speedup.
5. Increase B or T?
6. Model doesn't fit — attack P vs A vs a single layer.
7. FSDP all-gather every layer — when is that worse than pipeline?
8. Checkpoint/resume a multi-day run that dies at 80%.
9. Data pipeline for packed multimodal batches (your collator).
10. How do you know a ckpt is worth keeping? (val, not train loss.)
11. 8B OOM on one GPU — order of levers.
12. Variable T / padding.
13. Choose global batch vs microbatch vs accum.
14. NaNs at 20k steps.
15. 2x compute: model vs data vs context vs experiments.
16. (If pulled) high-rate encoder + LLM, throughput dies.

---

## Traps

Don't define checkpointing / ZeRO 1/2/3 as the whole answer. Classify the bottleneck, then one lever plus the tradeoff.

Don't open with "I'd use DeepSpeed / FSDP / Flash." Say what is broken: state, activations, comm, input.

Don't volunteer Health / RelCon. He is AFM. Stay on training unless he pulls sensors-as-tokens.

Don't claim 122B MoE as a result. Scale probe; letter-A bias; don't slide.

Don't recite the FlashAttention paper. Exact attn, less HBM, still T^2.

Don't mix activation ckpt with disk ckpt. A vs reliability.
