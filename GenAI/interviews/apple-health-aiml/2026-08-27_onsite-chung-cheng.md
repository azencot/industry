# On-site — Chung-Cheng Chiu (Wed 1:05 PDT)

**Track:** LLM training & infrastructure. **Conf:** very high.  
**Who (private):** Principal RE, Apple AI/ML (Mountain View). AFM reports; **AXLearn** author ([arXiv:2507.05411](https://arxiv.org/abs/2507.05411)). Cross-org, **not** Health.  
**Hub:** [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)

**Sound like:** “First I’d establish whether this is a **model-state memory**, **activation**, **communication**, or **input-throughput** problem.”  
**Not:** names of four libraries, or a definition of gradient checkpointing.

Do **not** name AXLearn / AFM / FlashAttention papers unless he does. Do **not** volunteer RelCon / Watch. If he asks about a sensor encoder + LLM and throughput dies, treat it as **infra** (tokens, \(T^2\), input stall) — not a health paper recap.

Your run is **evidence at the end**, not the lecture: two-stage, DDP, LoRA, TR kill. [`2026-08-20_training-run-drill.md`](2026-08-20_training-run-drill.md)

**Already locked** (do not restudy AdamW / clip / pack / fp16 scale): [`../../notes/2026-08-22_llm-training-mechanics-lockin.md`](../../notes/2026-08-22_llm-training-mechanics-lockin.md). **7B order:** LoRA → microbatch/\(T\) → FlashAttn → **checkpoint \(A\)** → DDP → **FSDP last**.

**AXLearn pocket (only if he goes there):** production trainer; **modular** (swap input / ckpt / loop); **heterogeneous** GPU/TPU/Trainium; parallelism via **compiler sharding**, not “I forked DeepSpeed.” You train on Slurm/DDP — honest: you have not run GSPMD on 1k chips. You **have** diagnosed fit vs throughput on jobs you owned.

---

## Friday Block A — cover this file today

Goal: *I can reason about a large distributed training step* — not become an infra specialist overnight.

**Habit every answer:** (1) name the **constraint** (memory / compute / comm / I/O / reliability) → (2) **decompose** → (3) **one** tool → (4) **tradeoff** → (5) **how you’d verify**. Diagnose first, prescribe second.

Do **not** study: NCCL/CUDA internals, ring-allreduce proofs, InfiniBand, compiler IR, Megatron variants, AXLearn source, TPU microarch, RoPE derivation.

| Slot | Section | ~h | Pass when you can |
|------|---------|----|-------------------|
| **A1** | Memory | 0:50 | For 7B / 8B / 30B, split \(M\) and say which tool hits \(P\) vs \(G\) vs \(O\) vs \(A\) |
| **A2** | Collectives + DDP + FSDP | 1:00 | What is replicated vs sharded; what collective fires; why not always FSDP |
| **A3** | Tensor + pipeline + 3D | 0:50 | 128 GPUs: what each axis buys and costs |
| **A4** | Runtime: MFU, overlap, 8→64 | 0:50 | Step-time decomposition without spraying tools |
| **A5** | Flash, act-ckpt, accum, packing, input | 0:50 | Idle GPU vs low MFU vs padding — different levers |
| **A6** | Checkpoint + NaNs | 0:30 | Week-long run: what you save, how you resume |
| **A7** | 2× compute + sensor+LLM collapse | 0:30 | Resource judgment; infra diagnosis if he pulls sensors |
| **Close** | 35 min full mock | 0:35 | One owned run + 45% util **or** 8→64 + 30B fit |

**~6.5 h.** If short: skip extra arithmetic reps in A1 and the second A7 prompt. **Never skip interleaved mocks or Close.** Speak answers out loud. After each mock: one sentence on what was mushy, then continue — do not open Wikipedia.

---

## A1 — Training memory

\[
M \approx P + G + O + A + \text{workspace}
\]

Workspace = kernels, NCCL buffers, fragmentation. Interview habit: **which term is the fire** before naming a library.

| Term | What | Typical dtype | Hits it |
|------|------|---------------|---------|
| \(P\) | weights | bf16 → 2 B/param | FSDP / ZeRO-3 / tensor / LoRA (train fewer) |
| \(G\) | grads | often bf16 | FSDP / ZeRO-2/3 |
| \(O\) | Adam \(m,v\) | commonly **fp32** → **8 B/param** (\(2\times 4\)) | FSDP / ZeRO / LoRA (tiny \(O\)) |
| \(A\) | saved for backward | grows with \(B,T,d,N\) | **activation checkpointing**; smaller microbatch |
| Attn tiles | \(B,H,T,T\) scores | — | **FlashAttention** (not linear-time) |
| Effective batch | want large \(B\) but \(A\) OOM | — | **gradient accumulation** |

Optional: fp32 **master** weights on top of bf16 \(P\) (implementation-dependent).

**Worked bf16 + Adam fp32 \(m,v\), ignore \(A\):**

| Model | \(P\) | \(G\) | \(O=m{+}v\) | Replicated state (DDP) |
|-------|------|------|-------------|------------------------|
| **7B** | \(7\text{e}9\times 2 \approx 14\) GB | ~14 GB | \(7\text{e}9\times 8 \approx 56\) GB | **~84 GB** before activations |
| **8B** | ~16 GB | ~16 GB | ~64 GB | **~96 GB** |
| **30B** | ~60 GB | ~60 GB | ~240 GB | **~360 GB** |

7B already **does not comfortably fit** an 80 GB GPU as a full DDP replica once \(A\) shows up. 30B **cannot** be replicated. That is why FSDP exists.

Do the 8B and 30B arithmetic once on paper. Then: LoRA freezes most of \(P\) — \(O\) only on adapters; that is why LoRA is **first** in the 7B order, FSDP **last**.

**Attack map (say this, not ZeRO trivia):**

| Problem | First lever |
|---------|-------------|
| Parameters | shard \(P\) (FSDP-3 / TP) or don’t train them (LoRA) |
| Gradients | shard \(G\) |
| Optimizer | shard \(O\) or shrink trainable set |
| Activations | checkpoint \(A\); cut microbatch \(B\) or \(T\) |
| Attn intermediates | FlashAttention |
| Batch too small to fit | accum |

---

### Mock A1 (~8 min) — cover, then go on

1. *8B doesn’t fit on one GPU. Diagnose, then propose an order.*  
   **Target:** split \(P+G+O+A\); 8B state ~96 GB already; 7B order; do **not** lead with FSDP if LoRA + smaller \(T\) + Flash + checkpoint \(A\) might suffice.  
2. *Which of those tools does **not** reduce optimizer memory?*  
   **Target:** FlashAttention and activation checkpointing. They hit \(A\) / attn tiles.  
3. *Follow-up:* why is \(O\) often larger than \(P\)?  
   **Target:** two fp32 moments vs one bf16 weight tensor.

---

## A2 — Collectives, DDP, FSDP

### Collectives

| Op | Starts with | Ends with | Typical use |
|----|-------------|-----------|-------------|
| **All-reduce** | Full tensor, same shape on every rank | **Reduced** (sum/mean) on **every** rank | DDP: sync \(G\) |
| **All-gather** | A **shard** | **Concatenated whole** on every rank | FSDP: materialize \(P\) for a layer |
| **Reduce-scatter** | Full tensor | Reduced, each rank keeps **its shard** | FSDP: shard \(G\) after backward |
| **All-to-all** | Each rank sends a **different** slice to each peer | Pieces **rearranged** | Tensor-parallel activations |

Do not lead with “I’d use NCCL.” Name **what is being shipped**.

### DDP

**Job:** more **tokens/step**. Model **fits** per GPU.

Each GPU: **full** \(P\) (and usually \(G,O\)) + a **different** batch. Independent fwd/bwd. Then **all-reduce** \(G\) so every replica takes the **same** Adam step (mean of per-rank grads).

What moves: full \(G\) each step. What does **not**: parameters stay replicated.

**Cheap when it fits. Fatal when it doesn’t** — you replicate the expensive \(O\) \(N\) times.

You **have** run DDP. Say that. Don’t pretend 128-GPU DDP is the same as 8.

### FSDP / ZeRO

**Job:** **model-state** (\(P,G,O\)) doesn’t fit if replicated. Data is **still** DP (different batches).

| Stage (if asked) | What you shard |
|------------------|----------------|
| ZeRO-1 | \(O\) |
| ZeRO-2 | \(O+G\) |
| ZeRO-3 / FSDP-full | \(O+G+P\) |

Do **not** recite stages as the answer. If asked: stage ≈ *what you shard*. Then the bottleneck.

**Mental model:** DDP = replicate state, all-reduce grads. FSDP = **shard** state, **all-gather \(P\)** around the layer, compute, drop, **reduce-scatter \(G\)**.

That per-layer all-gather is the **FSDP tax**.

**Tradeoff:** memory ↓, **communication and complexity** ↑. Never “FSDP is better.” Say: *“FSDP buys per-device state memory with extra collectives; if the model already fits, DDP is often simpler and faster.”*

**When FSDP all-gather is worse than pipeline:** slow fabric, tiny compute per layer (gather dominates), or you would rather ship **activations between stages** than rebuild **full \(P\)** every layer.

---

### Mock A2 (~10 min)

1. *Walk DDP vs FSDP on 4 GPUs. What is replicated? What collective?*  
   **Target:** DDP: 4× full \(P\), all-reduce \(G\). FSDP: each rank ~\(1/4\) of \(P,G,O\); all-gather \(P\) per layer; reduce-scatter \(G\).  
2. *Why not always FSDP?*  
   **Target:** fits → DDP can win on comm + complexity.  
3. *FSDP all-gather every layer — when pipeline instead?*  
   **Target:** comm-bound gathers vs shipping activations along depth; bubble vs tax.

---

## A3 — Tensor, pipeline, 3D

One step is still fwd → loss → bwd → opt. Families split **different** things. Hybrid is normal.

### Tensor / model parallel

**Job:** **one** matmul \(y=xW\) (one layer) doesn’t fit, or you want GPUs **inside** the layer.

Split \(W=[W_1\mid W_2]\). GPU0: \(xW_1\), GPU1: \(xW_2\), then **all-reduce / all-gather activations** so the next op sees a full vector. Usual split points: QKV, MLP.

**DP splits examples. TP splits the matmul. FSDP shards state and reconstructs around the layer.**

Cost: collectives **inside** every Transformer layer; volume scales with \(T\) and hidden size. TP wants **fast** interconnect (typically **within a node**). Across nodes: DP / FSDP / pipeline first.

You have **not** owned Megatron TP. Honest: you know the job. No 1k-chip story.

### Pipeline

**Job:** **depth** doesn’t fit: blocks 1–10 on GPU0, 11–20 on GPU1, …

Naive: GPU1 idle until the first forward arrives = **bubble**. **Microbatches** stagger the line (1F1B-style schedules exist — do not memorize them). More microbatches → smaller **relative** bubble.

What moves: activations fwd and grads bwd **between adjacent stages** — often cheaper than all-gather full \(P\) every layer.

Cost: bubble, stragglers (one slow stage stalls everyone).

### 3D / hybrid

No axis scales forever. Example **128 GPUs:** TP=8 × PP=4 × DP=4.

| Axis | Buys | Dies when |
|------|------|-----------|
| DP / FSDP | tokens/step, or shard state | replica memory, or all-reduce/all-gather latency |
| TP | layer GEMM / layer memory | intra-layer comm, long \(T\) |
| PP | total depth | bubbles, too few microbatches |

**Choose (what doesn’t fit, then interconnect):**

| Symptom | First family |
|---------|----------------|
| Fits; want tokens/step | **DDP** |
| \(P{+}G{+}O\) OOM; layers fit | **FSDP**; checkpoint \(A\) **before** this |
| One matmul / layer | **Tensor** (NVLink group) |
| Depth / FSDP tax | **Pipeline** |

Spoken: *“Fit state with FSDP; if a layer still doesn’t fit, tensor-split on NVLink; if depth is the issue, pipeline and fill with microbatches.”* Not “DeepSpeed vs Megatron.”

---

### Mock A3 (~10 min)

1. *128 accelerators, 30B. How might you combine axes — and why not 128-way DP?*  
   **Target:** 30B state ~360 GB replicated; must shard and/or TP/PP; pick an example product that multiplies to 128; TP on the fast domain.  
2. *2× GPUs, 1.4× speedup. Why?*  
   **Target:** Amdahl; comm fraction; smaller GEMMs; collective latency; pipeline bubble; straggler; dataloader not scaled.  
3. *Increase \(B\) or \(T\)?*  
   **Target:** no universal. \(\text{tokens/step}=B\times T\times n\). Attn \(\mathcal{O}(T^2 d)\). Long context is a **\(T^2\)** tax; bigger \(B\) often cheaper **if the task doesn’t need long \(T\)**. Objective + memory decide.

---

## A4 — Runtime: compute vs communication

\[
T_{\text{step}} = T_{\text{compute}} + T_{\text{comm}} + T_{\text{input}} + T_{\text{sync}} + \text{ckpt/other}
\]

Add GPUs → **per-device compute shrinks**; **comm does not vanish**. \(T_{\text{comm}}/T_{\text{step}}\) grows. **8 → 64 is not 8×.** That is the whole 64-GPU question.

**Overlap:** bad = compute then a blocking collective. Better = hide all-reduce/all-gather **behind** backward of another layer. Goal: comm under useful FLOPs.

**Throughput** for training: **tokens/s** (not “latency of one sample”). **Latency** = time for one op / step.

**MFU** ≈ useful model FLOPs / peak hardware FLOPs. Do not memorize a formula. Low MFU ≠ “buy FlashAttention.” It **flags** a regime:

| Observation | Look at |
|-------------|---------|
| GPUs **idle** in waves | input, straggler, barrier, ckpt pause |
| Comm **dominates** step time | parallelism, topology, collective size, overlap, **too-small** per-GPU work |
| GPUs **busy**, MFU still low | kernels, tiny GEMMs, bad shapes, extra recompute (act-ckpt), unfused attn, host `.item()` |
| Huge **padding** | packing / bucketing / varlen |

**Diagnosis order (30B · 128 acc · 45% util) — say this:**

1. Compute-bound vs **communication-bound** (MFU vs collective time).  
2. Profile **step breakdown** (fwd / bwd / opt / wait).  
3. **Input** (decode, H2D, host stall).  
4. Collectives (FSDP tax).  
5. Per-device microbatch too small.  
6. **Padding** / real tokens (ragged \(T\)).  
7. Activation checkpoint — extra compute, can look like low “useful” MFU.  
8. Kernel / attention impl.  
9. Host–device sync.

Compare to the **8-GPU** run that was healthy. Do not spray tools until the profile names the class.

---

### Mock A4 (~10 min)

1. *8 GPUs fine; 64 GPUs ~4× not 8×. Investigate.*  
   **Target:** decompose \(T_{\text{step}}\); compare fractions to the 8-GPU job; then **one** regime.  
2. *64-GPU job 30% slower than expected. First three sentences.*  
   **Target:** profile, don’t prescribe; compute / comm / input / sync; compare to baseline.  
3. *Follow-up:* GPUs busy but MFU 20%. Where do you **not** start?  
   **Target:** not “add FSDP.” Kernels, shapes, padding, recompute, unfused attn.

---

## A5 — Flash, checkpoint-\(A\), accum, packing, input

### Activation checkpointing ≠ disk checkpoint

Normal fwd **saves** activations for bwd. **Activation checkpointing:** save a few, **recompute** the rest in backward. \(A\) ↓, compute ↑. Hits **\(A\)**, not \(P\) or \(O\). Disk ckpt is a different word — don’t mix them.

### FlashAttention

Naive attn materializes \(B,H,T,T\). Flash = tiled exact attn + online softmax; **less HBM traffic**. Compute still \(\approx \mathcal{O}(T^2 d)\). **Not** linear attention. Don’t recite the paper.

### Gradient accumulation

Microbatch = what **fits** one fwd/bwd. Global batch ≈ \(\text{microbatch} \times \text{accum} \times \text{DP world size}\) (tokens also \(\times T\)).

Fwd/bwd × accum, **then** clip → `step` → `zero_grad`. Clip **after** accum (locked). Memory ↓ per fwd (smaller \(A\)); more sequential microsteps per update.

### Variable \(T\) / padding

Attn \(\mathcal{O}(T^2 d)\). One 4000-token sequence next to 100s, pad-to-max = **waste**. Levers: **bucketing**, **packing** (your `-100` / splice mask — else doc B in doc A’s CE), varlen kernels, truncate only if the **science** allows.

### Data pipeline

storage → CPU preprocess → tokenize → batch → **H2D** → GPU.

If the GPU **waits for data**, more GPUs do nothing. Offline tokenize, shard the dataset, workers, prefetch, pinned memory, async H2D, keep Python off the hot path.

**If he pulls multimodal input:** reading many files, resampling, STFT, augmentation, varlen, syncing modalities can stall the **host**. Distinguish **model** bottleneck vs **input** bottleneck. Do not volunteer Watch papers.

Your collator / packing is **IC evidence** for “data pipeline for packed multimodal batches.”

---

### Mock A5 (~10 min)

1. *Explain activation checkpointing. Cost? What memory term?*  
   **Target:** \(A\) ↓, compute ↑; not disk ckpt; not \(O\).  
2. *Highly variable sequence lengths — memory and tokens/s?*  
   **Target:** \(T^2\); pad-to-max; packing/bucketing; your `-100` leak story if asked how packing fails.  
3. *GPUs periodically idle. First fork.*  
   **Target:** input vs straggler vs sync vs ckpt pause — not “FlashAttention.”

---

## A6 — Distributed checkpointing and NaNs

A real ckpt is not “the weights file.” Include: \(P\), \(O\), LR schedule, **step**, **RNG**, AMP scaler if used. At 128 GPUs, state is **hundreds of GB**.

**Bad:** gather everything to rank 0, write one blob. **Better:** **sharded** save (each rank writes its slice). Concerns: storage bandwidth, pause time, frequency, consistency, **resume world size**, recovery time.

Tradeoff: frequent ckpt → less lost work, more I/O. A 3-day / week run that dies at 80%: resume from last **consistent** shard set; don’t restart from scratch; val (not train loss) decides if the ckpt is **worth keeping** — you have this.

**NaNs at 20k steps (not first-step overflow):** skip “just lower LR” as the whole answer. Fork: (1) which rank / which layer / which **slice** of data; (2) loss scale / inf in fp16 (bf16 usually not scale); (3) bad packed labels (`-100` miss → huge CE); (4) LR / wd / clip after a schedule boundary; (5) corrupt ckpt resume; (6) a new long-\(T\) batch. Bisect step and **data**. You killed a TR mix when the average lied — same instinct: don’t trust train NLL alone.

---

### Mock A6 (~8 min)

1. *Week-long 128-GPU run. Design ckpt/recovery.*  
   **Target:** sharded; what you save; frequency vs I/O; resume; don’t gather to rank 0.  
2. *Dies at 80%. What do you do tomorrow morning?*  
   **Target:** last good ckpt; don’t re-download the world; check val; find the failing step.  
3. *NaNs after 20k steps.*  
   **Target:** not “FSDP.” Isolate data vs numerics vs resume vs packing.

---

## A7 — 2× compute, and sensor+LLM only if pulled

**2× compute:** do **not** auto-double model size. Candidates: more tokens, better data, longer \(T\) (pay \(T^2\)), more **experiments**, better representation, HPO. Applied: small scaling probes → marginal return → then spend the big allocation. **Do not scale an architecture before it is worth scaling.** Your TR mix kill is the story: average up, slice down → **killed**.

**If he asks:** *100 Hz encoder + LLM, throughput collapses.* Infra tree, not RelCon:

raw rate → encoder FLOPs → **sensor token count** → LLM \(T\) → attn \(T^2\) → \(A\) up → microbatch down → comm/compute ratio worse → padding / CPU preprocess / I/O.

Architectural direction: native-rate **local** encoder → **compress / patch** → few latents → LLM. **Do not** resample every modality onto the fastest clock (Yujie sheet; don’t name her).

---

### Mock A7 (~8 min)

1. *2× GPUs for a year. Model vs data vs context vs experiments?*  
   **Target:** probe first; don’t double 30B by default; kill criteria.  
2. *Throughput collapses after adding a high-rate encoder. Diagnose.*  
   **Target:** tokens and \(T^2\) and input stall; local encoder + patch; not “use FSDP.”

---

## Close — 35 min full mock (do this last)

Play **cross-org FM engineer**. IC verbs. No AXLearn name-drop. No RelCon.

| Min | Prompt |
|-----|--------|
| 0–8 | Broad: a **run you owned** including infra (DDP, LoRA, collator, TR kill). Evidence at the **end**. |
| 8–20 | Drill: **45% util on 30B @ 128** **or** **8→64 ~4×**. Diagnosis order. |
| 20–30 | Scenario: **30B doesn’t fit** — \(P\) vs \(A\) vs one layer vs depth. |
| 30–35 | Your Q: how **they** debug scaling (not “do you use AXLearn”). |

**Strong close (memorize the shape, not the nouns):**

> I’d first determine where step time is going: model compute, collectives, input stalls, sync — and compare those fractions to the smaller run that worked. If comm grew dominant, I’d look at parallelism, topology, collective sizes, and overlap with backward. If GPUs are periodically idle, I’d look at input or stragglers. I wouldn’t change the parallelism strategy until the profile says which regime I’m in.

---

## Predicted questions (full list)

1. 8 GPUs fine; 64 GPUs ~4× not 8×.  
2. 30B, 128 acc, 45% util — diagnosis order.  
3. DDP vs FSDP vs tensor vs pipeline — **choose**.  
4. 2× GPUs, 1.4× speedup.  
5. Increase \(B\) or \(T\)?  
6. Model doesn’t fit — attack \(P\) vs \(A\) vs a single layer.  
7. FSDP all-gather every layer — when is that worse than pipeline?  
8. Checkpoint/resume a multi-day run that dies at 80%.  
9. Data pipeline for packed multimodal batches (your collator).  
10. How do you know a ckpt is worth keeping? (val, not train loss.)  
11. 8B OOM on one GPU — order of levers.  
12. Variable \(T\) / padding.  
13. Choose global batch vs microbatch vs accum.  
14. NaNs at 20k steps.  
15. 2× compute: model vs data vs context vs experiments.  
16. *(If pulled)* high-rate encoder + LLM, throughput dies.

---

## Traps

| Trap | Do instead |
|------|------------|
| Define checkpointing / ZeRO 1/2/3 | Classify bottleneck, then one lever + tradeoff |
| “I’d use DeepSpeed / FSDP / Flash” as sentence one | What is broken: state, activations, comm, input |
| Health / RelCon | He is AFM. Stay on training unless **he** pulls sensors-as-tokens |
| Claim 122B MoE as a result | Scale probe; letter-A bias; don’t slide |
| Recite FlashAttention paper | Exact attn, less HBM, still \(T^2\) |
| Mix activation ckpt with disk ckpt | \(A\) vs reliability |
