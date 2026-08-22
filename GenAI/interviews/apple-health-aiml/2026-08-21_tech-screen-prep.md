# Prep — Apple Health AIML tech screen (45 min)

**Status:** **Scheduled — Tue 2026-08-25, 1:35–2:20 PM PDT**, Webex. Interviewer **Feng Zhu**.  
**Format (Tyler 2026-08-21, locked):** **45 min** spoken **depth check** on **LLM training** + **multimodality fundamentals**.  
**Coding:** **No.** Invite lists CoderPad — **ignore** (same HM template). Don’t grind LeetCode.  
**Confirm:** reply to Tyler that you are available — template in [`2026-08-21_tech-screen-invite.md`](2026-08-21_tech-screen-invite.md).  
**Group PDFs:** [`papers/README.md`](papers/README.md) — skim **Feng’s periodicity** paper; TS-LLM only for the bakeoff. Do not name-drop.  
**Invite / reply:** [`2026-08-21_tech-screen-invite.md`](2026-08-21_tech-screen-invite.md)  
**HM debrief (what she already heard):** [`2026-08-21_hm-screen-debrief.md`](2026-08-21_hm-screen-debrief.md)

**Your goal:** They leave thinking you can **own an LLM training run and a representation bakeoff** — IC verbs, a kill, transfer to *their* signals without reprinting matplotlib on PPG.

This is **not** a second why-Apple chat. Locked 50s stays in the pocket. Lead with training + encodings.

---

## What already happened (don’t replay the HM)

Shirley already got: 2–3 min multimodal; three encodings (text / patched / images) + bet; three evals; TSRBench (finance question; you blanked on sensors); two-stage + gates; Bosch / no product ship; ImagenFew; “impact at scale”; Seattle.

**Tech screen = one layer down.** Same topics are allowed. Repeating the same 2–3 min without a **number, a kill, or a counterfactual** is a miss.

---

## Two pillars (Tyler)

### 1. LLM training (half the hour if they drive it)

**Project run (must be a run, not a lab tour):** [`2026-08-20_training-run-drill.md`](2026-08-20_training-run-drill.md) · [`2026-08-12_hm-3c-training-run.md`](2026-08-12_hm-3c-training-run.md)

Say if they didn’t hear it on HM:

> Two-stage: A = see (vision, LM frozen), B = answer (LM LoRA). I don’t promote on loss. Cheap TSExam → TSRBench slice → full north star. Gates **−3 pp overall / −5 pp slice** set before the run. Synthetic TR mix: average looked up, TR **26.9 → 21.9**, I **killed it**. 8B stock **0.62 → ~0.90** TSExam, TSRBench **~0.40 → ~0.45**.

**General LLM judgments (not the VLM story):** [`../../notes/2026-08-20_llm-training-judgments.md`](../../notes/2026-08-20_llm-training-judgments.md) · [`../../notes/2026-08-21_sft-starting-pitfalls.md`](../../notes/2026-08-21_sft-starting-pitfalls.md)

If they leave the project: mixture NLL ≠ task; packing ≠ padding; completion-only SFT; chat template (Qwen ChatML / thinking); LoRA vs unfreeze LR; select ckpt on val, report test once. Don’t jump to RL.

### 2. Multimodal fundamentals (the other half)

Three encodings you already listed — now with **failure modes** and **what you’d do on wearables**.

| Approach | When it works | Failure |
|----------|---------------|---------|
| **TS as text** | Tiny series, scale as numbers in the prompt | Burns context; weak perception; her paper’s named failure too |
| **Patched native encoder → LLM** | Honest bias if you have the data (this is **her** TS-LLM shape) | You must train the encoder; patch rate / multivariate layout matter |
| **TS as images** | Steal a visual prior; dual views beat one | One view **loses** information (delay-only ChatTS num **~0.17** vs chart **~0.71** vs dual **~0.79**). **Do not** say “images keep all information.” **Do not** reprint charts on PPG |

Bakeoff line (30s):

> Text dumps lose structure. A patched encoder is the more honest bias if you have the data — I’d bake that off. Images were a stolen visual prior, not the true object of a series. I used two views because one loses information. Year one on this team: same eval gate, compare encoder families on *your* IMU/PPG/longitudinal signals. I would not port matplotlib onto PPG.

Group facts if they go there (don’t volunteer papers): [`2026-08-20_shirley-group-briefing.md`](2026-08-20_shirley-group-briefing.md). RelCon **~3.9M params**, 1B **segments**. LLM seat = **language layer**.

**Feng Zhu angle:** his public paper with this group is multimodal wearable streams + **naturalistic missingness** + periodicity vs a deep TS model. If he pulls “your benches aren’t Watch data,” land on missingness / longitudinal / don’t reprint charts on PPG — not a paper recap of his mood work.

---

## Pockets from the HM (they may re-ask)

**TSRBench ≠ finance.** 4,125 / 15 tasks / 14 domains. Healthcare is in it (**ECG-QA**, **PTB-XL** on decision-making). Also industrial / river sensors / weather / energy. Honest: public ECG ≠ Watch PPG/IMU.

**Product:** still **no consumer ship**. Bosch irregular/noisy → generative adaptation (**ImagenFew** / irregular sampling), not a Watch feature. **Guillermo (private — do not cite):** team is applied ML with a **~1 year product** target. If Feng asks research vs product:

> Research toward a defined product target — advanced ML that has to land in about a year, not an open-ended FM lab. I pick a representation, gate it, kill what doesn’t transfer. I have not shipped a Watch feature; the industry pressure I have felt is messy data changing the model.

**Why this seat (only if asked):** locked 50s in [`2026-08-20_why-apple-health-drill.md`](2026-08-20_why-apple-health-drill.md). **Never** “impact at scale.”

**Intro:** IC first. Not associate professor.

**Success bar she named:** curious + **breadth** — show a kill, not a paper list. Work mode: **~3-month concrete slices** of a large problem.

---

## What not to do

| Skip | Why |
|------|-----|
| Full 5-interview on-site bank | Tyler: this screen is the next gate |
| LeetCode / HF-stack tourism | Not briefed. Study code is **nanoGPT-scale** + a toy multimodal forward, then **speak** |
| RelCon / Workout Buddy / Feng’s mood paper name-drop | HM didn’t go there; don’t start a paper quiz |
| PI / “my students” / associate professor lead | Prior loop + this HM open |
| “Images keep all information” | Contradicts your ablation |
| Mixing Bosch Watch scripts | Separate track; Sunnyvale reloc vs Seattle on-site |

---

## Practice plan — 3-day bootcamp (Fri night → Mon), Tue = retrieval

Tyler locked a **45 min spoken** screen: LLM training + multimodality fundamentals. **No pad.** Code is how you *learn* tensor shapes; you will not type in Webex.

**Study object:** equations ↔ architecture ↔ training decision ↔ a small implementation. **Your VLM run is evidence**, mapped at the end of a block — not the textbook. Do **not** open ImagenFew / OpenTSLM / TSEXAMPP / Bosch / RelCon cover-to-cover / LeetCode.

**Calendar (today is Fri 2026-08-21):**

| When | ChatGPT day | Hours | Mix |
|------|-------------|-------|-----|
| **Fri night** | Day 1A — pipeline + attention | ~2 | **Pipeline locked** (tokenizer vs `E`, RoPE ≠ `M`, parallel CE, AdamW). Attn: \(Y=AV\) locked; **implement** [`code/day1_attention.py`](code/day1_attention.py) `FromMemory` if continuing. Debrief: [`../../notes/2026-08-21_llm-pipeline-attn-lockin.md`](../../notes/2026-08-21_llm-pipeline-attn-lockin.md) |
| **Sat** | Day 1B — training mechanics + nanoGPT | ~4 | **Mostly locked** — \(\eta\) vs \(\lambda\); \(m\)/\(v\); fp16 scale; pack `-100`. Re-say \(\beta_1,\beta_2\) + 7B order if needed. Debrief: [`../../notes/2026-08-22_llm-training-mechanics-lockin.md`](../../notes/2026-08-22_llm-training-mechanics-lockin.md) |
| **Sun** | Day 2 — multimodal | ~5 | **Partial (Sat):** families + labels + concat-vs-xattn locked. Left: CLIP \(s_{ij}\), toy `MultiModalLM`, wearables Q12. Debrief: [`../../notes/2026-08-22_multimodal-fusion-lockin.md`](../../notes/2026-08-22_multimodal-fusion-lockin.md) |
| **Mon** | Day 3 — SFT + debug + mock | ~4 | `-100` labels, broken Attention, **12 questions aloud** |
| **Tue AM** | retrieval only | 15 min | Q1, Q6, Q10, Q12; then stop |

Skip: RLHF/DPO internals, obscure Transformer variants, scaling-law papers. SentencePiece = **2 min** of tradeoffs, not a tokenizer paper.

SFT judgment notes (Day 3): [`../../notes/2026-08-20_llm-training-judgments.md`](../../notes/2026-08-20_llm-training-judgments.md) · [`../../notes/2026-08-21_sft-starting-pitfalls.md`](../../notes/2026-08-21_sft-starting-pitfalls.md)

**Pass a block when:** you can name every tensor shape, say why the design exists, and name the failure if you drop it.

---

### Day 1 — LLM training end-to-end

**Goal:** raw text → updated parameter, with shapes.

#### 1A (Fri) — reconstruct the pipeline, no notes after the first pass

```
text → tokenizer (BPE) → input_ids [B, T]
     → token emb + position (learned or RoPE on Q/K)
     → N × (pre-norm → MHA → residual → pre-norm → SwiGLU FFN → residual)
     → final RMSNorm → lm_head → logits [B, T, V]
     → shift: predict token t+1 from t
     → CE → backward → AdamW
```

Must be able to **say**, not recite a list: BPE vs char (compression vs messy splits); embeddings + **RoPE on Q/K** (not a 3rd add in modern LLMs); Q/K/V; **1/√d_k**; causal mask **M**; softmax; multi-head (several subspaces, concat, `W_O`); pre-norm vs post-norm (trainability); LayerNorm vs **RMSNorm** (no mean-center, scale only — LLaMA/Qwen); FFN vs **SwiGLU**; residuals; tied embeddings (lm_head = emb.T, optional); next-token CE.

**Attention (derive on paper):**

\[
Q=XW_Q,\; K=XW_K,\; V=XW_V,\quad
A=\mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}+M\right),\quad Y=AV
\]

| Term | Why it exists |
|------|----------------|
| \(1/\sqrt{d_k}\) | Dot products grow like \(d_k\); without it softmax saturates, gradients die |
| \(M\) (causal) | Upper triangle \(-\infty\) so token \(t\) cannot see \(>t\). **This is what makes it a LM**, not a bidirectional encoder |
| softmax | Turns scores into a distribution over keys; one token can mix many |
| heads | Each head is \(d_k=d/h\); concat → \(W_O\). Different heads specialize |
| RoPE | Rotate Q/K by position so \(q_i^\top k_j\) depends on \(i-j\); relative, extrapolates better than learned abs pos |

Memory: attention maps are \(\mathcal{O}(B H T^2)\) (or \(\mathcal{O}(BT^2)\) if you materialize). **Compute still \(\mathcal{O}(T^2 d)\)** even with FlashAttention (IO-aware tiling; does not change the asymptotic). Long context is expensive because of **T²**, not because of V.

**Code (Fri + Sat):** [karpathy/nanoGPT `model.py`](https://github.com/karpathy/nanoGPT/blob/master/model.py) — `CausalSelfAttention` + `GPT.forward` loss. Local: [`code/day1_attention.py`](code/day1_attention.py). Trace:

```
input_ids [B,T] → wte → [B,T,C] → blocks → ln_f → lm_head → logits [B,T,V]
loss = CE(logits[:, :-1], targets[:, 1:])   # or labels = ids[:, 1:], logits[:, :-1]
```

Implement `CausalSelfAttention.forward` from memory (QKV reshape, scale, causal mask, softmax, concat). Explain every shape. Close the file and redraw.

#### 1B (Sat) — training mechanics (~2h) then speak (~30 min)

Know **what it does to the update**, not the PyTorch flag list:

| Knob | Interview sentence |
|------|-------------------|
| AdamW + weight decay | Decoupled decay on weights (not Adam’s L2-in-m). Bias/norm often no decay |
| warmup + cosine | First steps would spike if LR is full; cosine → near-zero. Too high LR = loss spike / collapse |
| grad accum | Fake larger batch: sum (or mean-consistent) grads over micro-steps, then step. Clip **after** accum |
| grad clip | Global-norm cap; NaN/explode defense |
| bf16 vs fp16 vs fp32 | bf16 = fp32 range, less precision; no loss-scale. fp16 needs **loss scaling**. fp32 wasteful. Qwen-class expects **bf16** |
| batch vs T | Memory ~ activations; T² attention. Tokens/step = B × T × world |
| pad vs pack | Pad = mask pads in attn + labels `-100`. Pack = concat docs; **block the boundary** or doc B is in doc A’s loss. Files ≠ tokens |
| DDP / FSDP / ZeRO | DDP = replica + allreduce grads. FSDP/ZeRO = shard params/grads/opt. 7B doesn’t fit → bf16 + LoRA / checkpointing / shard / smaller T |
| ckpt vs grad ckpt | Save weights vs recompute activations in backward (save memory, extra compute) |
| FlashAttention | Same math, better HBM traffic; still T² compute |

**Sat speak (timer, no notes):** Why causal mask? Why bf16? LR too high? Why warmup? 7B doesn’t fit one GPU? Train ↓ val ↑ — what do you look at?

---

### Day 2 (Sun) — multimodality

Largest fraction of prep. Canonical drawing:

```
signal/image → modality encoder → projector → modality tokens ─┐
text → tokenizer → embeddings ─────────────────────────────────┴→ LLM → out
```

**Three families:**

1. **Encoder + projector + concat (LLaVA).** \(z_v\in\mathbb{R}^{d_v}\mapsto Wz_v\in\mathbb{R}^{d_{\mathrm{LLM}}}\), scatter/concat into the LM sequence. Projector exists because **dims and spaces differ**. Frozen encoder + train projector = Stage 1; then LM LoRA = Stage 2.
2. **Cross-attention (Flamingo).** \(Q=X_{\text{text}}W_Q\), \(K,V=X_{\text{mod}}W_{K,V}\). Text length stays T; cost \(\mathcal{O}(T\cdot T_{\text{mod}})\) per layer instead of \(\mathcal{O}((T+T_{\text{mod}})^2)\). Better when the second stream is long or you want a **bottleneck**. Worse: extra params, modality can be ignored if gates collapse.
3. **Unified tokens.** Patch/quantize the signal so it is the same Transformer. Honest if you have the data; you **train the encoder**.

**Training strategies to speak:** frozen vs joint encoder; frozen LLM; LoRA; staged align → instruct; **CLIP contrastive** \(s_{ij}=z_i^{\text{img}}\cdot z_j^{\text{txt}}/\tau\) + in-batch negatives (alignment, **no decoder**); SFT on chats; modality imbalance; missing modalities; paired vs unpaired.

**Code:** [`code/day2_multimodal.py`](code/day2_multimodal.py) (write Sun). Interrogate: shapes; where RoPE/positions go; attn mask; do image tokens attend to future text?; **labels after inserting vision tokens** (vision positions `-100`); multi-image; freeze encoder; LoRA LLM; where grad flows.

**Apple translation (do not skip):** PPG/ECG/IMU/sleep/text, **asynchronous, irregular, missing**. Concat vs cross-attn vs native TS encoder — bake off under **one eval gate**. Do **not** reprint matplotlib on PPG. This is Q12.

CLIP math: [transformers `clip_loss`](https://github.com/huggingface/transformers/blob/v4.51.3/src/transformers/models/clip/modeling_clip.py). Concat scatter: [LLaVA `modeling_llava.py`](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llava/modeling_llava.py). Skim Feng PDF abstract only if Q12 is already clean.

---

### Day 3 (Mon) — SFT + debug + mock

**Stack:** pretrain → (domain CPT) → instruction SFT → (preference) → deploy/eval. **Do not** jump to RL.

Chat → loss: template (Qwen ChatML) then `labels = -100` on user/system, values on assistant (+ EOS). Why: otherwise the **question owns CE**.

Review: LoRA/QLoRA; forgetting; mix/replay; contamination; “loss fine, decode garbage” → **diff train tokens vs inference template** (BOS/EOS, thinking, padding, masking, tokenizer, LR, `do_sample`).

**Debug (~1h):** broken Attention (no scale, no causal, not multi-head); wrong pad mask; SFT labels; off-by-one CE; detached vision; accidentally frozen; NaNs; train/eval mismatch. [`code/day3_broken_attention.py`](code/day3_broken_attention.py) (write Mon).

**Mock 2–3h, no notes — 12 questions:**

1. Transformer LLM from raw text.
2. Derive scaled dot-product; each term.
3. Why RoPE and RMSNorm.
4. 8B, not enough GPU memory.
5. Pretrain vs SFT.
6. Add images to a pretrained LM.
7. Concat tokens vs cross-attention.
8. Align two independently pretrained modalities.
9. Text gets better, second modality ignored. Why.
10. Continuous sensor into an LLM.
11. Multimodal loss NaN — debug.
12. ECG, PPG, IMU, sleep, text; **most examples are a subset**. Training strategy. **Spend real time.** Missingness + mix + health.

Your run (kill, gates, 0.62→0.90) is **one example inside Q1/Q5**, not a separate lecture. Pockets (TSRBench, why-Apple) only if pulled.

**Questions to ask him (pick 2):** (1) first 3-month gate — bakeoff vs harness vs language prototype? (2) what wearable failure kills a model if a public bench moved?

### Tue morning — 15 min, then stop

Say Q1 spine, Q6 concat, Q10 sensor, Q12 missingness. Join Webex **after 1:25 PM PDT**. Fallback: **425-606-7471**.

---

## Local code (study, not the screen)

| File | Day |
|------|-----|
| [`code/day1_attention.py`](code/day1_attention.py) | 1 — causal MHA + CE shift |
| [`code/day2_multimodal.py`](code/day2_multimodal.py) | 2 — projector concat (Sun) |
| [`code/day3_broken_attention.py`](code/day3_broken_attention.py) | 3 — find the bugs (Mon) |

External: [nanoGPT `model.py`](https://github.com/karpathy/nanoGPT/blob/master/model.py) (read Sat, don’t vendor HF).

---

## How to practice (method)

- Close the notes and **speak**. If you cannot say the shape, you did not finish.
- Code until you can **interrogate** it (mask, labels, freeze). Then stop coding.
- Map your numbers **last**.
- Timed drills with me: I play Feng on the 12 questions. Day 2–3. Tonight is 1A, not a mock.

---

## After the call

Write `YYYY-MM-DD_tech-screen-debrief.md` (use the actual date). Update [`README.md`](README.md). Do not email Shirley.
