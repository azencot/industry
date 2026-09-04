# Friday — Chung-Cheng advanced (second cycle)

**When:** Fri 2026-09-04 · Block 1 (75 min) + Block 2 (45 min)  
**Plan:** [`2026-09-03_four-day-final-plan.md`](2026-09-03_four-day-final-plan.md)  
**Do not open first:** the person sheet A1–A7, the 30-min review, or the 9/1 challenging writeup.

You already have: P/G/O/A, DDP vs FSDP collectives, TP wants NVLink, step time = compute+comm+input+sync, 8→64 can silently 8× global batch.

This file is **transfer**: why the system behaves that way, and how you diagnose it.

---

## How to use

1. Read **Learning A–F** once. Speak the one-line lock at the end of each section.  
2. Stop. Do **Mock Q1–Q5** with notes closed. For each: bottleneck → competing explanations → measure → intervene → tradeoff.  
3. Then open **Keys**. Restitch only the worst miss.

---

# Learning (75 min)

## A. Communication vs compute

Scaling is not “more GPUs.” It is whether **added compute** pays for **added communication and sync**.

Per step, roughly:

```
step_time ≈ max(compute, comm)   if they overlap
          + uncovered comm
          + input / straggler / checkpoint
```

If compute per GPU is large and comm is hidden, GPUs scale. If you shard so aggressively that each unit’s GEMM is tiny, **launch + all-gather latency** dominates and you see: GPUs alternate compute and idle.

### Volume vs latency

- **Volume:** bytes moved. FSDP all-gather of a unit ≈ size of that unit’s parameters (bf16: 2 bytes × params). DDP all-reduce of grads ≈ size of the replica’s gradients. TP activation all-reduce scales with `B · T · d`.  
- **Latency:** time to start and synchronize a collective, even for small tensors. Many tiny collectives lose to one large one.  
- **Topology:** intra-node NVLink / NVSwitch is high bandwidth, low latency. Inter-node (IB / Ethernet / whatever the cluster actually is) is slower, often by a large factor. A collective that **crosses nodes** is a different problem than one that stays on NVLink.

### Why tensor parallelism is topology-sensitive

TP puts a collective **inside every layer**, on the critical path of the GEMM. That only works if that collective is cheap. Typical placement: TP **within a node** (NVLink domain), FSDP / DP **across nodes**.

You have not owned Megatron TP. Honest line: *I know the job of TP (split a matmul that does not fit, or keep a layer’s GEMM on fast links). I would not design a 1k-chip map from experience. I would ask what the node’s NVLink domain is and keep TP inside it.*

### Single-node vs multi-node

Same 8 GPUs on one node vs 8 GPUs as 2×4 across nodes is not the same FSDP. Cross-node all-gather of the same parameter unit can turn a memory win into a throughput loss.

**Lock:** *I scale until the uncovered comm and sync eat the extra compute. TP stays on the fast domain. FSDP/DP can cross nodes. If GPUs idle between GEMMs, I profile comm vs compute before I add ranks.*

---

## B. FSDP prefetch / sharding intuition

Do not memorize flags. Track **when a parameter must be whole** and **when it can be a shard**.

Forward, for unit (often a Transformer block):

1. Rank holds a shard of W.  
2. **All-gather** → full W for that unit.  
3. GEMM.  
4. **Reshard / free** the extra copies if you need the memory.  
5. Repeat for the next unit.

Backward needs W again (and produces full grads, then **reduce-scatter** to a grad shard). So aggressive free-after-forward means you **all-gather twice** (fwd + bwd) unless you keep W.

**Prefetch:** all-gather unit i+1 **while** computing unit i. That is overlap. If prefetch is off or the unit is too small, you see: compute, wait, compute, wait.

**Why aggressive sharding saves memory but can stall**

- Memory: each rank stores ~1/N of P, G, O, plus **one** gathered unit at a time (plus activations).  
- Stall: more ranks → more all-gather participants; smaller compute per unit if you also wrap too finely; cross-node tax.  
- Peak still includes the **currently gathered** W. Sharding does not make a 70B layer free during its GEMM.

If FSDP “solved OOM” and step time jumped, first suspects: overlap failure, unit too small, fabric crossed a topology boundary — not “FSDP is slow.”

**Lock:** *FSDP buys per-device state memory with extra all-gather/reduce-scatter. Prefetch is how you hide that tax. If I still stall, I coarsen the wrap or keep TP/FSDP on the right side of the node boundary — I do not turn prefetch flags at random.*

---

## C. Large-batch training

This is the 9/1 miss. Internalize the identities, then transfer.

```
global_batch    = microbatch_per_gpu × accum × data_parallel_world
tokens_per_step = global_batch × seq_len   (ignore padding for a second)
steps           = total_tokens / tokens_per_step
```

Scale 8 → 64 GPUs, **same microbatch, accum=1, same T**: global batch ×8, steps ÷8, **same token budget ≠ same optimization**.

Fewer Adam steps → less noise in the updates, different implicit regularization. Validation can get worse while training loss looks fine or even better.

### LR and warmup

Linear scaling rule (classic, not a law): `η ∝ global_batch`, **with warmup**, because early large-LR steps on an untrained net diverge.

**Warmup in steps vs tokens**

If warmup is 2,000 **steps**, 8× batch means 8× tokens before you reach peak LR. If warmup is 2B **tokens**, the schedule is comparable across batch sizes.

Same tokens through the model is not the same trajectory unless step count, LR, warmup unit, and (often) weight decay / dropout interaction are accounted for.

You can keep global batch **constant** when adding GPUs: shrink microbatch or raise accum. That is a legitimate choice when the goal is speed at matched optimization.

**Lock:** *When GPU count changes I compute global_batch and steps at fixed tokens before I talk about generalization. Same tokens is not the same run. Warmup unit is part of the schedule, not a footnote.*

---

## D. Training throughput

These are not synonyms.

| Metric | What it is | Lies when |
|--------|------------|-----------|
| **Step time** | Wall clock per optimizer update | You changed accum or global batch and still compare “steps/sec” |
| **Samples/sec** | global_batch / step_time | Sequence length changed; a “sample” is a different token count |
| **Tokens/sec** | non-pad tokens / wall clock | The number you want for LLM pretrain; packing vs padding matters |
| **GPU utilization** (smi) | SM busy-ish | Can be high during NCCL wait or memory-bound kernels. Not MFU. |
| **MFU** | achieved FLOPs / peak FLOPs | Dense-transformer 6ND-per-token is an approximation; MoE / sparsity / recompute change the numerator |

Idle GPU + low smi → often **input** or **straggler** (nothing to run).  
High smi + low MFU → often **memory-bound, tiny GEMMs, or comm mapped as busy**.  
Tokens/sec down after you double T even if MFU looks similar → **T² attention / memory** tax.

For multimodal: tokens/sec on the **LLM backbone** can collapse because the vision/sensor encoder or collate path cannot feed it. That is an **input / encoder stall**, not “the LLM is slow.”

**Lock:** *I say which clock I mean. Utilization is not MFU. Tokens/sec is not samples/sec. If T or padding changed, I refuse a samples/sec comparison.*

---

## E. Checkpointing at scale

A checkpoint is not “save the weights.”

Typical bulk:

- Parameters (bf16: ~2 bytes × N)  
- Optimizer (Adam m, v often fp32: ~8 bytes × N trainable)  
- Optional: scheduler, AMP scaler, RNG, sampler epoch, step index  

Optimizer often **dominates** the file. FSDP **sharded** ckpt: each rank writes ~1/N. **Full** state dict: someone gathers — memory and time spike.

**Storage bandwidth:** `size / write_bandwidth`. 80 GB at 2 GB/s is 40 s of stall if you block the step. Shared filesystems contend when 64 ranks flush at once.

**Restart cost:** load shards + rebuild process groups + maybe warm allocator. If world size changed, you must **reshard**, not blindly map rank i → file i.

**Atomic / incomplete:** crash mid-write → unreadable or silently truncated optimizer on one rank. Write to tmp + rename, keep last-K, never load a ckpt that did not finish on **all** ranks.

A run that was stable, then **resume**, then diverges **hundreds of steps later** is usually not “the first step is NaN.” More often: missing scaler / RNG / sampler, LR schedule in the wrong unit, or a quietly wrong optimizer shard that takes time to show.

**Lock:** *I checkpoint enough to restart the same trajectory: weights, optimizer, schedule, scaler, RNG, data position. I treat incomplete shards as poison. Divergence after resume is a state bug until proven otherwise.*

---

## F. Determinism vs reproducibility

**Bitwise determinism** (same bits on the same hardware): RNG seeds **per rank**, dataloader worker seeds, operator determinism (some CUDA kernels are not), same kernel algorithm (FlashAttention has variants), same reduction trees.

**Scientific reproducibility** (same conclusion, not same bits): same data recipe, same global batch and schedule **in tokens**, same eval protocol. This is what papers and production gates actually need.

Distributed topology changes bitwise results even with a seed: all-reduce tree, TF32/atomicAdd order, different DP degree.

Data **order** is part of the algorithm. Restoring weights but not sampler state is a different run.

You will not get bitwise identity across a cluster change. Do not promise it. Do promise: I can restore the training **state** and the **data position**, and I eval with a frozen protocol.

**Lock:** *I distinguish bitwise determinism from reproducibility of the scientific claim. Seeds without sampler and topology are theater. I restore the trajectory, then I re-run eval — I do not claim bit equality after 64-GPU NCCL.*

---

# Mock (45 min) — do not read keys yet

Speak. No definitions. Combine failure modes.

**Q1.** FSDP solves OOM, but training is 30% slower. Profiling shows GPUs alternate between compute and idle. What do you inspect?

**Q2.** You double context length and halve batch size. Peak memory still increases substantially. Why?

**Q3.** 64 GPUs train faster but validation is worse. Total tokens unchanged. What changed?

**Q4.** Training is stable until a checkpoint resume, then divergence starts ~500 steps later.

**Q5.** Two ranks consistently arrive late at every collective. What could cause it and how do you isolate it?

For every answer: bottleneck → competitors → measurement → intervene → tradeoff.

---

# Keys (after speaking)

## Q1 — FSDP OOM-fixed, 30% slower, compute/idle alternation

**Bottleneck:** uncovered **communication** (or a too-small compute unit), not “FSDP is slower than DDP” as a slogan.

**Competitors**

- Prefetch off / not overlapping all-gather with GEMM  
- Wrap too fine: many tiny all-gathers, latency-bound  
- FSDP group crossed **nodes**; NVLink would have hidden it, IB does not  
- Input stall that *looks* like comm idle (next batch not ready)  
- Activation checkpointing: extra recompute, different idle pattern (usually compute-heavy, not wait-for-NCCL)

**Measure**

- Step-time split: compute vs NCCL vs H2D vs CPU  
- Whether idle lines up with all-gather (NCCL trace) vs dataloader  
- Unit size (params all-gathered per wait)  
- Intra-node vs inter-node placement of the FSDP group

**Intervene (after the trace)**

- Enable / increase prefetch so gather i+1 overlaps compute i  
- Coarser wrap (block, not submodule)  
- Keep FSDP/DP across nodes, TP inside the node — or *less* shard if memory now has slack  
- If it was input: workers, packing, prefetch of batches — not more FSDP flags

**Tradeoff:** overlap and coarser wrap use more peak memory (you hold an extra gathered unit, or a larger unit). That is acceptable if you are no longer OOM.

**Miss if:** you said “switch to DDP” without checking whether the replica still fits, or you named a library.

---

## Q2 — 2× context, ½ batch, peak memory still up

**Bottleneck:** **activation / attention** memory, not parameter memory. Model size did not change.

**Arithmetic to say aloud**

Naive attention memory / compute ~ `B · T²`.  
New: `B' = B/2`, `T' = 2T` → `B' · (T')² = (B/2) · 4 T² = 2 · B T²`.

Halving batch **does not cancel** doubling T for the quadratic term. Linear-in-T activation terms (`B · T · layers · d`) stay about flat: `(B/2)·(2T) = B T`. So the increase is the **quadratic (or KV/recompute peak)** piece, plus allocator fragmentation from larger tensors.

FlashAttention lowers the *naive* T² *materialized* scores; you can still grow: longer KV during training, checkpoint recompute peaks, larger activation tensors per layer, sequence-parallel not used.

**Competitors:** leak (keeping full activations despite checkpoint), extra KV from a longer cache in a hybrid train/infer path, packing changed so “halved batch” still has the same token count *and* longer max T.

**Measure:** memory snapshot by bucket (P/G/O vs activations). Compare at T vs 2T with **matched tokens per step**, not matched batch.

**Intervene:** activation checkpointing, sequence parallel / context parallel if you have it, smaller microbatch + accum to keep tokens/step, last-resort shorter context or sliding windows. **Not** “more FSDP” — P did not grow.

**Tradeoff:** checkpointing trades memory for extra compute; smaller microbatch can hurt MFU.

---

## Q3 — 64 GPUs faster, val worse, tokens unchanged

**Bottleneck:** **optimization trajectory**, not hardware. This is the 9/1 miss in a new wrapping.

**What almost certainly changed if microbatch was held fixed**

- `global_batch` ×8 (if 8→64 data parallel)  
- Optimizer steps ÷8  
- Noise per update down  
- If LR was not scaled (or was scaled without warmup): either too small a step or early divergence/instability  
- If warmup is in **steps**, warmup now covers 8× tokens  

**Competitors (still say them)**

- Different data order / fewer epochs through a shuffle (same tokens can mean a different mix if packing changed)  
- Eval bug (different batching, different prompt packing)  
- Precision / accum numerical differences  
- Overfitting to a smaller number of noisier… no: *fewer* noisy steps often **hurts** generalization — don’t invert this

**Measure:** print `global_batch`, steps, LR schedule **in tokens**, train loss vs val. Compare to an 8-GPU run with **matched global batch** (accum or smaller microbatch).

**Intervene:** match global batch first (accum). If you *want* large batch, scale LR with warmup in **tokens**, and re-tune. Do not “add dropout” as the first move.

**Tradeoff:** matching batch keeps the trajectory and may leave some GPU memory idle; large batch is faster per token but is a different scientific run.

---

## Q4 — Stable, resume, diverge ~500 steps later

**Bottleneck:** **incomplete restored state**, not “the model forgot how to train.” Immediate NaNs would be a load/shape bug. **Delayed** divergence smells like scheduler, scaler, RNG, or data position.

**Competitors**

- Optimizer shards incomplete / wrong rank map after world-size change  
- AMP grad-scaler not restored (loss scale walks, then a late overflow/underflow pattern)  
- LR scheduler restored as *step=0* or as step index when the recipe is token-based  
- Dataloader / sampler not restored: repeated data then a later shift, or skipped shard  
- RNG (dropout, shuffle) reset — usually noisier, not a slow divergence by itself  
- One rank’s shard silently truncated; others fine — that *can* take time if the bad slice is a rare layer

**Measure**

- Diff: step, LR, scaler, optimizer moment norms, pre-resume vs post-resume **immediately** (not 500 steps later)  
- Whether world size matched  
- Whether every rank finished the write (manifest / last-K)

**Intervene:** restore the full trajectory; if the ckpt cannot, rewind to last known-good complete ckpt. Do not keep training on a “weights-only” resume and hope.

**Tradeoff:** fuller checkpoints are larger and slower to write. Worth it. Weights-only is for export, not for crash recovery of a long run.

---

## Q5 — Two ranks always late to every collective

**Bottleneck:** **persistent stragglers** on those ranks, not random jitter and not “NCCL is broken” globally.

**Competitors**

- **Data skew:** those ranks drew longer sequences / heavier multimodal examples every step (collate waits)  
- **Input:** those ranks’ dataloader workers / disk / NUMA are slower  
- **Compute:** thermal throttle, a slower GPU, ECC, different clock  
- **Network:** those ranks’ NIC / PCIe / a specific switch hop  
- **CPU overlap:** logging `.item()`, eval, tokenizer on those ranks only (bad rank-local extra work)  
- Same two **physical hosts** after a restart → hardware; same two **ranks** after host swap → data partition

**Isolate (order)**

1. Dummy equal-length batches: if the lag **vanishes**, it was data/input.  
2. Swap those ranks onto other hosts (or swap data shards): does the slowness **follow the rank id** or the **machine**?  
3. NCCL tests / a compute-only GEMM loop on those GPUs.  
4. Profile those two: H2D vs GEMM vs tokenizer vs disk.

**Intervene** on the measured cause: length-bucketing / packing so every rank sees similar T; fix the host; stop rank-0-only work that accidentally became rank-17-only; last: exclude the sick GPU.

**Tradeoff:** packing/bucketing changes the batch mix (a mild trajectory change). Hardware isolation costs a rank. Both beat syncing 62 GPUs to 2 slow ones every step.

---

## Self-score

- [ ] Named a bottleneck before a tool  
- [ ] Gave at least one competing explanation per question  
- [ ] Q2 had B·T² arithmetic aloud  
- [ ] Q3 said global_batch and steps, not “overfitting”  
- [ ] Q4 treated delayed divergence as state, not “learning rate too high” as the first guess  
- [ ] Q5 split data-skew vs host vs network with a swap test
