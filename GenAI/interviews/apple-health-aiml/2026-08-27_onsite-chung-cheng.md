# On-site — Chung-Cheng Chiu (Wed 1:05 PDT)

Track: LLM training and infrastructure. Conf: very high.

Who (private): Principal RE, Apple AI/ML (Mountain View). AFM reports; AXLearn author (arXiv:2507.05411). Cross-org, not Health.

Hub: 2026-08-27_onsite-prep.md

Tue 9/1 30-min review: [`2026-09-01_onsite-chung-cheng-training-infra.md`](2026-09-01_onsite-chung-cheng-training-infra.md) — failure → bottleneck → dominant term → intervention → tradeoff → measure again. Not a restudy of A1–A7.

Tue 9/1 challenging mock: [`2026-09-01_onsite-chung-cheng-challenging-practice.md`](2026-09-01_onsite-chung-cheng-challenging-practice.md) — Q1–Q4 spoken. **Q5 missed live:** 8→64 GPUs with fixed microbatch/accum/token budget silently 8×s global batch and cuts optimizer updates. Recalc global batch before blaming the network. Q2: same per-GPU microbatch → wait-time, not “less compute per GPU.”

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

   Spoken lock (2026-08-28): 30B is about 360 GB of P+G+O before A, so DDP on 80 GB is out. Shard with FSDP 8- or 16-way (~45 or ~22 GB state per GPU) and check shards + A + one gathered layer W still fit — not "all layers at once." Do not 128-way DP/FSDP: replica doesn't fit, and 128-way collectives + tiny batches dominate. If one layer still doesn't fit, TP on NVLink (e.g. TP 8 x FSDP 16 = 128, or TP 4 x PP 4 x FSDP 8). Fast interconnect is placement, not the reason for TP. Pipeline if depth or FSDP gather tax dominates; fill with microbatches.

2. 2x GPUs, 1.4x speedup. Why?
   Target: Amdahl; comm fraction; smaller GEMMs; collective latency; pipeline bubble; straggler; dataloader not scaled.

   Spoken lock (2026-08-28): Amdahl — serial / sync / input / bubble don't shrink 2x. Compute per GPU drops; comm does not vanish and often **grows** (more ranks, longer collectives, maybe crossing nodes) — not "comm stays the same." Smaller per-GPU GEMMs (worse MFU); collective **latency**; pipeline bubble; straggler; dataloader not scaled. Profile step time: compute vs comm vs input vs sync. Don't prescribe FSDP.

   Amdahl (don't call the fraction P — that's weights): f = parallel share of 1-GPU time T. T(N) = T * ((1-f) + f/N). Speedup S(N) = 1 / ((1-f) + f/N). Ceiling S → 1/(1-f). Comm/input/sync sit in (1-f); adding ranks can **raise** that bucket.

3. Increase B or T?
   Target: no universal. Tokens/step = B * T * n_gpu. Attention is about O(T^2 * d). Long context is a T^2 tax; bigger B is often cheaper if the task doesn't need long T. Objective + memory decide.

   Spoken lock (2026-08-28): No universal — objective first. Tokens/step = B * T * n_gpu. Attention compute (and naive attn memory) is ~T^2; B is roughly linear in A and splits cleanly with DDP. If the task does not need longer context, raise B (or accum). If it does (long docs / long history), you pay the T^2 tax; packing/bucketing before padding. A still grows with B, so linear is not "free." Don't raise T just to look like a long-context model.

---

## A4 — Runtime: compute vs communication

A training step is one optimizer update: forward, backward, (maybe accum), clip, Adam, zero. Wall-clock for that step is not "the GEMMs." Split it:

Step time = compute + comm + input + sync + ckpt/other.

- Compute: GPU math — mainly GEMMs (xW, attention). This is what MFU is trying to capture.
- Comm: NCCL collectives — DDP all-reduce G, FSDP all-gather P / reduce-scatter G, TP activation all-reduce. Waiting for a collective counts here even if the SM looks "busy."
- Input: CPU decode, collate, copy host-to-device. GPU sits idle if the next batch is not there.
- Sync: barriers, logging that pulls a scalar to CPU (.item()), stragglers (fast ranks wait for the slow one).
- Ckpt/other: pausing to write shards, allocator stalls, fragmentation.

You do not need a profiler dump in the interview. You need to name which bucket you would look at first.

### Why 8 GPUs fine, 64 GPUs not 8x

On one GPU, almost all of step time can be compute. Add data-parallel ranks: each GPU gets a smaller slice of the global batch (or you keep per-GPU batch and grow global batch — different choice). Per-GPU GEMM shrinks. Collectives do not go away: you still all-reduce a full G (DDP) or all-gather each layer (FSDP). More ranks -> longer rings/trees, more chance you leave NVLink and hit the network. Comm's share of the step grows. That is Amdahl: f (parallel GEMMs) / N drops; (1-f) (comm, input, sync) does not shrink the same way and can get worse.

So "64 GPUs, about 4x not 8x" is the default physics, not a mysterious bug. Investigate where the extra time went vs the 8-GPU run (same model, same per-GPU batch if you can). Don't open with "I'd switch to FSDP."

2x GPUs -> 1.4x is the same story at small N (Mock A3 Q2).

### Overlap (hiding comm)

Bad schedule: finish all compute, then a blocking all-reduce. Step time = compute + comm, added.

Better: start communicating G for layer i+1 while you still compute backward of layer i (DDP bucketing / async all-reduce). FSDP can overlap all-gather of the next unit with compute of the current one, if the implementation allows it.

Goal: comm under useful FLOPs so wall-clock is about max(compute, comm), not the sum. If overlap is broken, you pay both. You would not claim you implemented this at 128 GPUs; you would ask for the profile: wait time vs kernel time.

### Throughput vs latency vs utilization vs MFU

Don't mix these four.

- Latency: time for one step (or one collective). Users care in serving; in training the product metric is usually tokens/s (samples/s times T, or packed tokens).
- Throughput: tokens/s (or samples/s). Scale-out should raise this; if it doesn't, something in the split above ate the win.
- GPU utilization (nvidia-smi / "45% util"): fraction of time the chip is doing something. Idle waves -> input, straggler, barrier, ckpt. High util + bad training is possible: the GPU is busy copying, waiting on NCCL, or running tiny kernels.
- MFU (model FLOPs utilization) is about (FLOPs the model should need for those tokens) / (peak GPU FLOPs times time). Do not memorize a paper formula. It asks: of the chip's math peak, how much was useful Transformer work? 20-40% is common at small scale; 45% util in the drill is "the job looks sick," not a magic constant.

Low MFU is a flag, not a prescription. FlashAttention can raise MFU if the problem was unfused T x T attn. It does nothing if the GPU is waiting on the dataloader.

### Four regimes (read the symptom, then the bucket)

GPUs idle in waves (util drops to 0, then spikes): not a weak GEMM. Input (workers, H2D, tokenize), straggler, barrier, ckpt pause. More GPUs make this worse if the host pipeline wasn't scaled.

Comm dominates step time (NCCL wait much larger than GEMM): parallelism choice (FSDP tax every layer, TP across slow links, 128-way DP), topology, huge collectives, no overlap, per-GPU batch too small (all-reduce of G costs the same, compute vanished). This is the 8-to-64 question.

GPUs busy, MFU still low: the chip is working but not on fat model FLOPs — tiny GEMMs (small B or T), bad shapes, padding (compute on pad tokens), extra recompute from activation checkpointing, naive attn, Python .item() every step. Not "add FSDP."

Huge padding: lengths 100, 120, 4000 padded to 4000. You pay T^2 on garbage. Packing / bucketing / varlen. Your -100 collator story if he asks how packing fails.

### Diagnosis order (30B, 128 acc, 45% util) — say this

Compare to a healthy smaller run (8 GPU) when you have one. Same global recipe if possible.

1. Compute-bound vs communication-bound. Look at MFU vs time in collectives. Names the fork.
2. Profile step breakdown: fwd vs bwd vs opt vs wait. Wait is the tell.
3. Input: decode, H2D, host stall — idle waves.
4. Collectives: FSDP all-gather tax, DDP all-reduce size, TP on the wrong domain.
5. Per-device microbatch too small — Amdahl + tiny GEMMs.
6. Padding / real tokens per step (ragged T).
7. Activation checkpoint — extra compute; can lower MFU while saving A. Don't confuse with "slow comm."
8. Kernel / attention: fused vs materializing T x T.
9. Host-device sync (.item(), logging).

Do not spray tools until the profile names the class. Your evidence at the end: you have diagnosed fit vs throughput on jobs you owned (DDP, LoRA), not 128-GPU FSDP.

---

### Mock A4 (~10 min)

1. 8 GPUs fine; 64 GPUs about 4x not 8x. Investigate.
   Target: decompose step time; compare fractions to the 8-GPU job; then one regime.

2. 64-GPU job 30% slower than expected. First three sentences.
   Target: profile, don't prescribe; compute / comm / input / sync; compare to baseline.

3. Follow-up: GPUs busy but MFU 20%. Where do you not start?
   Target: not "add FSDP." Kernels, shapes, padding, recompute, unfused attn.

### Spoken integrated incident (2026-08-30)

Prompt: full-fine-tune a 30B Transformer with AdamW in bf16 on 8 x 80 GB GPUs. It OOMs before the first step. Account for memory, decide whether 8 GPUs are enough, choose parallelism, then diagnose why 8 -> 64 GPUs gives only 4x throughput at fixed global tokens/step.

First take: 30B needs P 60 GB + G 60 GB + O 240 GB = 360 GB before A. Eight GPUs may be enough depending on the bottleneck. Proposed LoRA if allowed, otherwise FSDP / ZeRO; proposed smaller B/T, accumulation, Flash, checkpointing, then FSDP / ZeRO on A. Estimated A as B x H x d_h x T^2 and concluded 45 GB sharded state + 16 GB A fits. Recalled all-gather for P but not reduce-scatter for G; said the highest FSDP level shards A. For scaling, decomposed step time into GEMM + communication + input + sync + checkpoint, but preferred TP unless non-GEMM time dominated.

Factual correction: FSDP does not shard activations. It shards P/G/O. Around a layer it all-gathers that layer's P, computes, releases the full copy, and reduce-scatters G; O remains sharded. Peak also contains the gathered layer, A, and temporary buffers. B x H x d_h x T^2 is not total activation memory; FlashAttention does not materialize the T x T score matrix. H=8 and d_h=64 implies d=512, not a plausible 30B model.

Missing decision: LoRA was forbidden by full FT. With fixed global tokens, 64 GPUs get less local work, so GEMMs shrink and MFU can fall while FSDP collectives cross more ranks / nodes. Profile compute, FSDP all-gather / reduce-scatter, input / H2D, synchronization / stragglers, and checkpoint pauses before changing parallelism. TP only if a layer does not fit, usually inside NVLink. Pipeline if depth or repeated FSDP gather traffic dominates and shipping activations is cheaper.

Spoken lock: The 30B state is about 360 GB, so eight-way FSDP leaves roughly 45 GB per GPU before activations. Around each layer, FSDP all-gathers that layer's parameters, computes, releases the full copy, and reduce-scatters its gradients; optimizer state remains sharded. It does not shard activations. At 64 GPUs with fixed global tokens, I would profile compute, communication, input, and waiting separately. Smaller local work can lower MFU while cross-node all-gathers and reduce-scatters become more expensive. I add TP only if a layer does not fit; I consider pipeline if depth or FSDP gather traffic dominates.

Spoken follow-up mock (2026-08-31), 15 min, mid-conversation. Already treated as covered: owned run, 8B replica (~96 GB before activations), DDP vs FSDP as a named fork, LoRA then shorter T then Flash then activation checkpointing. Prompt: same 30B FSDP job is fine on 8 GPUs; at 64 GPUs, tokens/s is about 4x not 8x; global token budget held fixed. Where is the extra step time, and what is the first measurement?

First take: Amdahl; each GPU gets less work so utilization can fall; GEMM down, communication / input / sync / checkpoint can rise; first look at nvidia-smi for periodic drops (input or checkpoint); then sync (pipeline bubble, ranks waiting); communication last, including tensor / pipeline split.

Follow-up: why communication's share rises even though each all-gather still rebuilds the same layer W; first plot MFU versus time in collectives, or smi percent? First take: 64-way all-gather is more NCCL work than 8-way; MFU vs collectives is a useful 8-vs-64 comparison; asked whether smi is just an app that shows MFU.

Follow-up: collective time much larger than GEMM, MFU down, GPUs not idle; first lever, and do you add tensor parallel? First take: add tensor parallel, ablate 2 / 4 / 8, drive collective time toward GEMM time, target MFU near 1 with high smi.

Miss: nvidia-smi utilization is not MFU. smi is the fraction of time the chip is occupied (including NCCL, copies, and tiny kernels); MFU is the Transformer FLOPs this step should have needed, divided by peak FLOPs times wall time. High smi with a slow job is possible. Idle waves (input, straggler, checkpoint pause) are a different failure from 4x instead of 8x. The all-gather payload is still that layer's W; communication's share rises because local GEMM shrank about 8x, because more ranks add latency and often leave the node, and because a skinny GEMM no longer overlaps the collective. Tensor parallel is for a layer that does not fit; it adds activation collectives and is the wrong change on a communication-bound FSDP job. MFU near 1 is not a realistic target; 20–40% is a common live range at this scale.

Spoken lock: I would compare the 64-GPU step to the 8-GPU run that was healthy, splitting wall time into compute, collectives, input, and waiting. nvidia-smi utilization only tells me whether the GPU was occupied; it counts NCCL, copies, and tiny kernels as busy. Model FLOPs utilization is the FLOPs the Transformer should have needed for those tokens, divided by the chip's peak times wall time. I would not treat those as the same number, and I would not try to push MFU to 1; 20 to 40 percent is a common live range here. With the global token count held fixed, 64 GPUs do about eight times less local work than 8, so GEMMs get smaller. Each FSDP all-gather still reconstructs the same layer weights; the tensor is not larger. Communication still takes a larger share of the step because there is less compute to hide it, because the collective now involves more ranks and often crosses nodes, and because a skinny GEMM no longer covers the all-gather. If collectives dominate, the GPUs are not idle, and MFU has dropped, I would not add tensor parallel. Tensor parallel is for a layer that does not fit, usually on NVLink, and it adds more collectives. The first change is to give each GPU more local work: keep FSDP at a degree that still fits — eight-way is about 45 GB of sharded state before activations, sixteen-way about 22 GB — and use the extra GPUs as additional data-parallel replicas, and check that all-gather is overlapped with compute. I would consider pipeline parallelism only if the per-layer all-gather itself is the tax and shipping activations along depth would be cheaper. Periodic idle waves are a different problem: the host pipeline, a straggler, a host sync such as pulling a scalar to CPU, or a checkpoint pause.

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

storage -> CPU preprocess -> tokenize -> batch -> H2D (host to device copy) -> GPU.

If the GPU waits for data, more GPUs do nothing. Offline tokenize, shard the dataset, workers, prefetch, pinned memory, async H2D, keep Python off the hot path.

If he pulls multimodal input: reading many files, resampling, STFT, augmentation, varlen, syncing modalities can stall the host. Distinguish model bottleneck vs input bottleneck. Do not volunteer Watch papers.

Your collator / packing is IC evidence for "data pipeline for packed multimodal batches."

---

### Mock A5 (~10 min)

1. Explain activation checkpointing. Cost? What memory term?
   Target: A down, compute up; not disk ckpt; not O.

   Spoken lock (2026-08-28): Save a few activations (often the input to a block / every k layers), recompute the rest in backward. A down, compute up. P, G, O unchanged. Not a disk checkpoint. Can look like lower MFU because extra FLOPs are real work, just not "more model."

2. Highly variable sequence lengths — memory and tokens/s?
   Target: T^2; pad-to-max; packing/bucketing; your -100 leak story if asked how packing fails.

   Spoken lock (2026-08-28): Pad-to-max is the wrong default — attention is ~T^2, so one long sequence next to shorts blows A and tokens/s (you compute on pad). Prefer bucketing, packing, varlen kernels; trim T only if the science allows. Packing: labels -100 / splice mask or doc B leaks into doc A's CE (collator you owned).

3. GPUs periodically idle. First fork.
   Target: input vs straggler vs sync vs ckpt pause — not "FlashAttention."

   Spoken lock (2026-08-28): Idle waves are not a weak GEMM and not FlashAttention. Fork: input (CPU / H2D), straggler (fast ranks wait), sync (.item() / barrier), disk ckpt pause. If the GPU waits for data or disk, more GPUs do not help — scale the host pipeline or shard ckpt. Then profile; don't prescribe FSDP.

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

   Spoken lock (2026-08-28): State is hundreds of GB because O is fat — do not gather to rank 0. Each rank writes its shard (P, O, step, RNG, scheduler, scaler). Watch pause time, disk bandwidth, capacity. Frequency: lose hours not days on a crash, without making I/O the job — 8-12/day is a plausible order, not a law. Two copies: rolling last-consistent shards to **resume** (even if val dipped); a separate **best-val** keep for selection. Don't resume from "best val" if that skips steps. Resume world size may differ — say you'd check the format.

2. Dies at 80%. What do you do tomorrow morning?
   Target: last good ckpt; don't re-download the world; check val; find the failing step.

   Spoken lock (2026-08-28): Resume the last **consistent** shard set, not best-val. Don't restart from step 0. Then diagnose the crash: data (new long T, pad/pack, -100 miss) vs numerics (fp16 loss scale; bf16 usually no scale) vs infra (disk, NCCL, OOM, corrupt ckpt). Find the failing step / rank / batch. Val on the resumed ckpt tells if the run was already sick.

3. NaNs after 20k steps.
   Target: not "FSDP." Isolate data vs numerics vs resume vs packing.

   Spoken lock (2026-08-28): Not first-step overflow, not "I'd use FSDP." Isolate: which rank / layer / shard; data (longer T, different mix, -100 miss -> huge CE); fp16 loss scale (bf16 usually skip); LR / wd / clip after a schedule boundary; corrupt resume. Bisect step and the batch. Same instinct as TR mix: don't trust train NLL alone.

### Spoken incident continuation (2026-08-30)

Prompt: rank 37 reports NaNs at step 20,143. Sharded checkpoints exist every two hours plus a separate best-validation checkpoint. Choose a resume point, verify consistency, reproduce the failure, and find the earliest corruption.

First take: resume last consistent, not best-val, to continue the run rather than skip steps. Verify by recovering eval and checking non-NaN P/G/A. Check data by replaying batches / outliers / normalization; numerics by fp16 loss scale and overflow; optimizer by warmup / schedule; distributed by network / communication. Inspect in that order.

Follow-up first take: recompute A in a forward pass as a consistency test; save another checkpoint at the failing step and use saved RNG to reproduce; inspect batch -> forward -> loss -> backward for first NaN; finite loss + non-finite G suggests a bad backward component, perhaps division by zero in normalization.

Factual correction: a checkpoint consistency test asks whether the save is transactionally complete, not whether the loaded model produces finite activations. Verify every expected rank shard exists, all shards report the same global step / world size, sizes and checksums pass, optimizer / scheduler / RNG metadata agree, and an atomic completion manifest exists. Do not save a new recovery checkpoint after state becomes non-finite.

Missing decision: restore the last completed checkpoint, RNG, and sampler state; log batch IDs and replay to the failing step. Running the step twice is comparable only after resetting to the same state and deterministic execution. Instrument input -> activations -> logits -> loss -> gradients -> optimizer update. If forward and loss are finite but layer 42 first emits a non-finite gradient, focus on its incoming gradient, saved / recomputed activations, backward op, mixed-precision scaling / unscale order, and fused kernels. LayerNorm has epsilon; do not jump to division by zero. Network faults usually produce errors / hangs, not silently valid NaNs.

Spoken lock: I resume the last atomically completed shard set, not best-validation. I verify all shards share the same step and metadata and pass the checkpoint manifest. Then I restore RNG and sampler state and replay while logging batch IDs. I instrument input, activations, logits, loss, gradients, and the optimizer update to find the first non-finite tensor. If forward and loss are finite but layer 42 first produces a non-finite gradient, I focus on that backward operation, its incoming gradient and saved activations, mixed-precision scaling, and any fused kernel — not immediately on the LR or network.

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

---

## LLM training (spoken; Day 1B still the lock)

Source for knobs: GenAI/notes/2026-08-22_llm-training-mechanics-lockin.md. Do not restudy RoPE. Infra (DDP/FSDP/TP) is A1-A6 above. This section is the **optimizer / data / SFT** layer if he leaves systems.

### A. One step

raw text -> tokenize -> pack/batch -> input_ids [B, T] -> Transformer -> logits [B, T, V] -> next-token CE -> backward -> accum -> clip (after accum) -> AdamW -> LR schedule -> val -> ckpt.

Training computes all positions in the packed window in parallel. Causal mask blocks future tokens. Loss:

L = - sum over t of log p(x_{t+1} | x_<=t)

tokens/step = microbatch * accum * T * n_gpu (DP world).

### B. AdamW

m = beta1 * m + (1-beta1) * g     (beta1 ~ 0.9; most weight on the past — do not flip 1-beta)

v = beta2 * v + (1-beta2) * g^2   (beta2 ~ 0.999)

Then bias-correct to m_hat, v_hat. Update (sketch):

theta <- theta - lr * m_hat / (sqrt(v_hat) + eps) - lr * lambda * theta

Weight decay is **decoupled**: the lambda * theta term is **outside** m, v. Not a per-sample loss weight. No decay on bias / RMSNorm.

Why AdamW: adaptive per-param scale + momentum; Transformers have heterogeneous gradient sizes. SGD can work; AdamW is the reliable default. v is **not** SGD velocity.

O is these m, v (usually fp32) — that is why O ~ 4x bf16 P.

### C. Warmup

Warmup **is** eta(t) ramping from ~0 to peak, then usually cosine decay. Not "tune the weights until a scheduler starts."

Why: early g, m, v are garbage; full LR wrecks the first steps.

Mental model: warmup = stability, peak LR = fast learning, decay = refine.

Early loss spike: LR too high, too little warmup, init, numerics, a bad batch, grad norm. Not "FSDP."

Cosine is common, not uniquely optimal. Don't overclaim.

### D. Accum and clip

Microbatch = what fits one fwd/bwd. Global batch ~ microbatch * accum * DP world size.

Clip **after** accum, before step — global grad norm: if ||g|| > c, rescale to c. Spikes and catastrophic steps. Not a substitute for bad LR / bad data / broken loss.

DDP follow-up: you can skip all-reduce on intermediate microbatches (no_sync) and sync once around the step — fewer collectives. Huge accum: tiny GEMMs, more sequential microsteps, fewer Adam steps for a fixed token budget if you define the run that way. Accum cuts peak **A**, not total FLOPs, and not O.

Do not automatically maximize global batch: less noise, maybe higher LR, fewer updates per token budget; too large can hurt. Objective decides (same as B vs T).

### E. bf16 / fp16 / loss scale

bf16: exponent like fp32 (wide range), skinny mantissa. Preferred on modern GPUs. Usually **no** loss scale.

fp16: small exponent — grads underflow to 0. Loss scale: L' = S * L, backward, **unscale** in fp32, then Adam. Inf/NaN => S too big, skip, cut S. fp16 exponent is 5 **bits**, not "5 digits."

Optional fp32 master: one Adam step; bf16 P is a cast for GEMMs so tiny updates don't vanish in the mantissa. Many bf16 stacks skip the master and keep O in fp32.

### F. Packing vs padding

Pad: rectangular batch. Attn mask: don't attend to pad. Loss mask: don't CE on invalid tokens (labels -100).

Pack: concat shorts to fill T. **EOS alone does not isolate docs.** Need -100 and/or **block attention at the splice** or doc B is in doc A's CE. Files != tokens. Your collator.

T^2: doubling T is much more expensive than doubling B. Longer T also grows A and padding sensitivity.

### G. Mix, quality, SFT

The optimizer sees E_{x ~ p_train}[loss]. Sampling weights **are** the objective. A small high-quality domain that boosts one bench and hurts general: lower its sample weight, replay general data, fewer steps / smaller LR, LoRA, mixture schedule.

More tokens != better: dups, bad synth, eval contamination, formatting that dominates SFT.

Pretrain / continued pretrain / SFT: same autoregressive CE. Different data shape, mask, LR, duration. Do not say SFT is a different LM loss.

Completion-only: attend to the prompt; CE only on assistant tokens (prompt labels -100). Attend != loss.

Chat template wrong: train NLL can look fine, generation dies. Debug: raw -> template -> tokens -> labels -> decode the training sample.

EOS: when to stop. Packing + bad EOS => endless gen or leak into the next sample.

### H. LoRA / QLoRA / forgetting

W = W0 + B A, W0 frozen, A/B low rank. Hits trainable P, G, and especially O.

QLoRA: frozen base in 4-bit (P storage on forward); adapters higher precision. 4-bit is a **P** win; O shrinks because you still only train adapters.

Catastrophic forgetting: smaller LR, fewer steps, replay, LoRA, freeze, broader mix.

### I. What to trust

Don't pick the ckpt on train NLL. Val (and task metrics). Hold out test. Train down / val up: **eval bug or mix first**, then overfit. Too-high LR usually wrecks **train** too. Task flat + NLL down = mixture NLL is not the task (your 27B vs TSRBench story).

NaNs / spikes: first non-finite — data batch, acts, logits, loss, grads, then the update. Same fork as Mock A6 Q3.

Track tokens/s, step time, grad norm, LR, stalls — not only loss. Numerically healthy and system-efficient.

### J. Follow-ups to drill (after Close)

Why warmup / AdamW / bf16 / clip. Why not max batch. Context doubles. Loss up, eval down. Bad mix. LoRA vs full FT. Unstable only after 20k steps. What you checkpoint. Optimization vs infra bottleneck.

Depth example — why accum? Desired global batch didn't fit. Does it cut total compute? No; peak A. Comm? DDP can delay all-reduce until the step. Huge accum? Tiny kernels, longer step, fewer updates per token budget.

Your run as evidence at the end: two-stage, DDP, LoRA, pack -100, TR kill on val/slice not train average.
