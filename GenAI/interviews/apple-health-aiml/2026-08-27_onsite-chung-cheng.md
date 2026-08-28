# On-site — Chung-Cheng Chiu (Wed 1:05 PDT)

**Track:** LLM training & infrastructure. **Conf:** very high.  
**Who (private):** Principal RE, Apple AI/ML (Mountain View). AFM reports; **AXLearn** author ([arXiv:2507.05411](https://arxiv.org/abs/2507.05411)). Cross-org, **not** Health.  
**Hub:** [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)

**Sound like:** “First I’d establish whether this is a **model-state memory**, **activation**, **communication**, or **input-throughput** problem.”  
**Not:** names of four libraries, or a definition of gradient checkpointing.

Do **not** name AXLearn / AFM / FlashAttention papers unless he does. Do **not** volunteer wearables.

Your run is **evidence at the end**, not the lecture: two-stage, DDP, LoRA, TR kill. [`2026-08-20_training-run-drill.md`](2026-08-20_training-run-drill.md)

---

## Already locked (don’t restudy)

\(M=P+G+O+A\); AdamW; clip-after-accum; bf16 vs fp16 scale; pack `-100`; 7B order: LoRA → microbatch/\(T\) → FlashAttn → **checkpoint A** → DDP → **FSDP last**.  
[`../../notes/2026-08-22_llm-training-mechanics-lockin.md`](../../notes/2026-08-22_llm-training-mechanics-lockin.md)

---

## Parallelism (say the *job*, then the tool)

| Family | What moves | When |
|--------|------------|------|
| **DP / DDP** | Different samples; **replicated** \(P\); all-reduce \(G\) | Model fits per device; want tokens/step |
| **FSDP / ZeRO** | Shard \(P,G,O\); all-gather \(P\) around the layer | Model-state memory; still data-parallel samples |
| **Tensor / model** | Split **one** matmul: \(W=[W_1,\ldots,W_n]\) | A **layer** doesn’t fit; extra all-to-all / all-gather on activations |
| **Pipeline** | Blocks 1–10 on GPU0, 11–20 on GPU1, … | Depth too big for one device; **bubbles** unless microbatches |

Hybrid is normal (DP × TP × PP). Decision: **what doesn’t fit** (state vs activation vs layer) **and** what the interconnect can hide.

\[
\text{step time} = \text{compute} + \text{comm} + \text{input} + \text{sync}
\]

Scale 8 → 64: per-device compute shrinks; **comm fraction grows**. Not linear.

**AXLearn pocket (if he goes there):** production trainer; **modular** (swap input / ckpt / loop); **heterogeneous** GPU/TPU/Trainium; parallelism via compiler sharding, not “I forked DeepSpeed.” You train on Slurm/DDP — honest: you have not run GSPMD on 1k chips. You **have** diagnosed fit vs throughput on the jobs you owned.

---

## Diagnose 30B · 128 acc · 45% util (say this order)

1. Compute-bound vs **communication-bound** (MFU vs NCCL/collective time).  
2. Profile **step breakdown** (fwd / bwd / opt / wait).  
3. **Input** pipeline (decode, H2D, host stall).  
4. Collectives / all-reduce / all-gather (FSDP tax).  
5. Per-device batch / microbatch too small.  
6. **Padding** / real tokens per step (ragged \(T\)).  
7. Activation checkpoint — extra compute, can look like low “useful” MFU.  
8. Kernel / attention impl (not fused, no Flash).  
9. Host–device sync (`.item()`, logging).

Do not spray tools. Name the **class** of problem first.

**2× GPUs → 1.4× faster:** Amdahl; comm; smaller GEMMs; collective latency; pipeline bubble; straggler; data loader not scaled.

**Batch vs \(T\):** no universal. \(\text{tokens/step}=B\times T\times n\). Attention \(\mathcal{O}(T^2 d)\). Long context is a **T²** tax; bigger \(B\) is often cheaper tokens if the task doesn’t need long \(T\). Objective + memory decide.

---

## Predicted questions

1. 8 GPUs fine; 64 GPUs ~4× not 8× — investigate.  
2. 30B, 128 acc, 45% util — diagnosis order.  
3. DP vs FSDP vs tensor vs pipeline — how do you **choose**?  
4. 2× GPUs, 1.4× speedup — why.  
5. Increase \(B\) or \(T\)?  
6. Model doesn’t fit — attack \(P\) vs \(A\) vs a single layer.  
7. FSDP all-gather every layer — when is that worse than pipeline?  
8. Checkpoint/resume a 3-day run that dies at 80%.  
9. Data pipeline for packed multimodal batches (your collator).  
10. How do you know a ckpt is worth keeping? (val, not train loss — you have this)

---

## Traps

| Trap | Do instead |
|------|------------|
| Define checkpointing / ZeRO 1/2/3 | Classify bottleneck, then one lever |
| “I’d use DeepSpeed” | What is broken: state, activations, comm, input |
| Health / RelCon | He is AFM. Stay on training |
| Claim 122B MoE as a result | Scale probe; letter-A bias; don’t slide |

**Mock (35 min):** play cross-org FM engineer. Broad: a run you owned including infra. Drill: 45% util **or** 8→64. Scenario: 30B fit. Your Q: how they debug scaling (not “do you use AXLearn”).
