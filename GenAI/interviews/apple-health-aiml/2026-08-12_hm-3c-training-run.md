# 3C — Most impactful LLM training run (detail)

**Resume (2026-08-12):** read through **§3 Architecture**. Next pass starts at **§4 Curriculum**. Do not restart from §1 unless the spoken paragraph is cold.

**For:** HM screen with Shirley Ren · Fri 2026-08-21  
**Spoken 2–3 min lives in** [`2026-08-12_hm-screen-prep.md`](2026-08-12_hm-screen-prep.md) §3C. **This file is the pull-thread.**  
**Sources:** [`Amazon_FinTech/vlm-technical-cheat-sheet.md`](../../../Amazon_FinTech/vlm-technical-cheat-sheet.md), [`Amazon_FinTech/anchor-cheat-sheet.md`](../../../Amazon_FinTech/anchor-cheat-sheet.md), [`.cursor/skills/debrief/vlm_multimodal_project.md`](../../../.cursor/skills/debrief/vlm_multimodal_project.md), repo `azencot-group/TSLMTSEXAM` branch **`iucc_cluster`** (as of 2026-08-12).  
**Do not** lead with FinTech bridges. Frame: **representing time series so an LLM can use them.**

**Honesty first:** this is a **multimodal fine-tune / curriculum** you owned (LoRA, DDP, eval gates) — not pretrain-from-scratch. Two campaigns; do not mix numbers.

| Campaign | Models | Role in the story |
|----------|--------|-------------------|
| **Current (lead)** | Qwen3.5 **9B** and **27B** (bf16), dual tower, native `<think>` | What you are running now on IUCC / Nebius **B200**s |
| **Measured champion (cite)** | Qwen3-VL-**8B** (+ 0.8B Q35) | Where the recipe and most ablations were proven |

---

## 1. Spoken 2–3 min (memorize this, not the tables)

> The problem I actually train on is that an LLM does not *see* a time series if you dump numbers into context. I represent each series two ways — a line chart for trend and amplitude, and a delay-embedding image for dynamical structure — and fuse both into the LLM. Training is two-stage: Stage A aligns vision with the language model frozen; Stage B teaches the LM to answer. All of it is LoRA on multi-GPU DDP, config-first sweeps, gated by a cheap eval before the expensive north star. I proved the recipe on Qwen3-VL-8B — stock **0.62 → ~0.90** on TSExam, TSRBench **~0.40 → ~0.45**. Current runs are Qwen3.5 **9B and 27B** with the same stack; 27B fine-tune lands **~0.92** TSExam, near the 8B champion. When a synthetic mix was supposed to fix temporal reasoning and instead dropped TR **26.9 → 21.9**, I killed it and went back to data generation. The lesson I would bring: architecture plus data plus an honest gate beat more GPU hours on a bad mix.

Then stop. Let her pull.

---

## 2. Problem and insight

**Problem.** General VLMs fail exam-grade time-series reasoning (MCQ, numbers, temporal relations, captions). Raw numeric tokens waste context and miss structure. Specialist forecasters (Chronos-class) are not built for language reasoning.

**Insight.** *How you draw the series matters.* One rendering loses information.

| Encoding | Keeps | Loses | Route |
|----------|-------|-------|--------|
| Matplotlib **line chart** | axes, amplitude, local shape, trend | topological / recurrence structure | Frozen native Qwen ViT (`visual` / image stream) |
| **Delay-embedding** image (256×256 recurrence-style) | shape, recurrence, dynamical structure | absolute amplitude (scale-invariant) | DINOv3 ViT-L/16 + trainable merger (`visual_dino`, reused video/visual-token path with `t=1`) |

**Empirical proof the split is real (ChatTS numerical A/B):**

| Config | Numerical |
|--------|-----------|
| 8B DINO + delay only | **0.17 / 0.22** |
| 8B matplotlib only | **0.71 / 0.71** |
| 8B dual tower | **0.787 / 0.787** |

Delay is competitive on categorical/pattern; it collapses on numbers. Dual gets both. Native ViT **cannot** be LoRA’d into a delay encoder: `qwendelay-8b` **0.601** TSExam vs DINO-on-delay **0.798**. Routing is the architecture: native ViT on charts, DINOv3 on delay.

**Design principle:** decouple *how to see* (Stage A) from *how to answer* (Stage B).

**Say:** “I reused Qwen’s video/visual-token pathway with `t=1` for the delay image so masks, M-RoPE/type tags, and merge logic routed both streams.” **Never say** “hijacked the video stream.”

---

## 3. Architecture (what you built)

```
Time series
  ├── line chart ──→ Qwen native ViT (frozen) ──→ projector ──┐
  │                                                            ├──→ LLM (LoRA in Stage B)
  └── delay image ─→ DINOv3 + merger (LoRA in Stage A) ───→ projector ──┘
```

**Personal ownership**

- Patched forwards: **Qwen3.5 9B / 27B** (`src/model_patch_q35.py`) and earlier **Qwen3-VL-8B** / **Qwen3.5-0.8B**
- Custom **DinoVisionTower** (`src/dino_vision_tower.py`)
- **UnifiedDualCollator** — on-the-fly chart + delay render; `mm_token_type_ids` for Qwen3.5 M-RoPE (0 text / 1 image-pad / 2 video-pad)
- Adapter **merge / resume** across stages; eval must reconstruct the same chain (`--prior-adapter`)

**DINOv3:** `PIA-SPACE-LAB/dinov3-vitl-pretrain-lvd1689m`, `image_size=256`, `patch_size=16`, `spatial_merge_size=2`. Deepstack `[6,12,18]` on 8B; **`[]` on Q35 9B/27B**. Token mode default `patches` (64 tokens); `cls_only` is ~64× compression at about −6 pp.

**Token budget (order of magnitude):** chart ~114 visual tokens (processor-dependent); delay 64 tokens; dual ≈ doubles visual tokens per series. Q35 train `max_length: 16384` (model default 262144 — too big to train).

**Extra tower cost:** ~2× visual tokens. Justified by ablations, not intuition.

---

## 4. Curriculum

| Stage | What trains | LLM updates? | Purpose |
|-------|-------------|--------------|---------|
| **A** | DINOv3 LoRA + merger/projector on **captions / alignment** | **No** | Learn *how to see* |
| **B** | Merge Stage A; fresh LM LoRA (+ optional DINO LoRA); merger often frozen | **Yes** | Learn *how to answer* |
| **C** | GRPO / VRT on SFT adapters (tried; not the headline) | RL on LoRA | Gold MCQ / CoT rewards |

**Stage A sources (champion “capall” recipe, 9B/27B YAML):** CaTS-Bench train + ChatTS-align captions (cap 32k) + TSExam captions; `weighted_even` (~1/3 each); **per-series** delay norm (`dino_global_norm: false`); 4 epochs; LR **1e-4**.

**Stage B sources (9B/27B unified YAML):** ChatTS ift (6,373) + sft (44,802) + TSExam large (20,640 MCQ) + TSExam-numeric (11,000) + TR reasoning subset (`target_format: think`, 3,684 TR); `weighted_even_src`; LR **3e-4**; 4 epochs (9B also 10-ep ladder).

**Baseline failure:** instruction-following only, no captions — **50+ configs**, TSExam stuck **~61.8%**. After Stage A caption prior → **~90.5%** on recent 8B stack.

**Qwen3.5 native thinking:** Stage B uses `target_format: think` (`<think>…</think>` then the letter). Value is **trained-in**: destructive zero-shot; converges toward OFF-parity with enough epochs; slightly helps the best-trained 9B-10ep. Two eval bugs once made “thinking” look useless — see §9.

---

## 5. Current 9B / 27B campaign (`iucc_cluster`)

**Cluster:** IUCC / Nebius **B200**, Slurm account `cycle2_bgu_azencot_prj`. Two venvs: 8B (`torch 2.7+cu128`, Blackwell) vs Q35 (`torch 2.11+cu128`). Jobs default `HF_HUB_OFFLINE=1`. Preemption: SIGTERM → full checkpoint (model+opt+sched+RNG) → requeue `--resume` (`src/preemption.py`).

**9B Stage A/B (from YAML):** 8-GPU DDP, bf16, grad checkpoint, SDPA. Stage A: pdtb **6** / accum **2** → eff **96**. Stage B: same. LoRA r16/α32. 27B: pdtb **4** / accum **3** → same eff **96**; ~79% VRAM worst-case, **plain DDP, no ZeRO** (54GB bf16 base fits). FP8 27B **cannot train** (transformers blocks quantized FP8 training) — eval-only.

**Zero-shot TSExam (vision, matplotlib, n=746):** 9B off **0.708** · 27B-bf16 **0.709** · 27B-FP8 **0.712**. Refs: 8B-VL **0.618**, 32B-VL **0.712**. Qwen3.5-9B matches 3.5×-larger VL-32B. Thinking **hurts** zero-shot (9B 0.708→0.673).

**Fine-tuned dual (after thinking/EOS eval fixes):**

| Model | TSExam (best OFF unless noted) | Notes |
|-------|--------------------------------|-------|
| 9B-4ep | ~0.87 OFF; ON 0.81 | Under-trained: thinking still misleads |
| 9B-10ep | **0.883** OFF; **0.890** ON | Thinking becomes useful |
| 9B r64 ep4 | **0.886** OFF (best 9B-dual TSExam) | ChatTS-B **0.92 / 0.87** beats 8B champion cat/num |
| 27B-4ep | **0.921** OFF (ON 0.88) | ≈ 8B champion **0.926** |
| 8B champion (cite) | **0.926** ep10 | Longer recipe, different arch |

**TSRBench caveat (important):** zero-shot 27B-bf16 **0.446 ≈ 8B champion 0.445**. Fine-tuning **trades reasoning/prediction for perception** (perception 58–68 → 84–87; reasoning 36 → ~28). Do not claim 9B/27B FT “won TSRBench.” 9B-10ep TSRBench @2048 ≈ **0.41**.

**ChatTS:** 27B FT dual is the **best ChatTS** in the project (A cat **0.92** / B cat **0.90**), above 8B champion ~0.88/0.87.

**LoRA rank:** 8B r16 champion vs r128 vs r256 at matched ep4 — **r128 sweet spot** (TSExam ties champion .894, wins ChatTS, small TSRBench cost); r256 overshoots. 9B **r64** is the analogue sweet spot. More rank helps ChatTS, hurts TSExam/TSRBench.

---

## 6. 8B / 0.8B campaign (where most ablations live)

**Headline vs stock Qwen3-VL-8B:** TSExam **0.618 → 0.905** (3ep) / **0.926** (full-B ep10); TSRBench **0.402 → 0.452** (3ep) / **~0.445** (full-B). Dual 8B beat every 32B single-tower config on TSExam-full (**0.886** vs best-32B **0.849**) before the later champion.

**0.8B Q35:** TSExam **0.890** vs 8B specialist **0.897** — size penalty is task-shape dependent (SLM routing lesson). Numeric R² 0.75 vs 8B 0.941 — regression still wants capacity. `flash-linear-attention` + `causal-conv1d` → ~**6×** step speedup on 0.8B.

**Hardware (historical 8B):** 8× A100, then 8× RTX Pro 6000; now B200. Effective global batch **~64** on 8B (later unified pdtb=1/accum=8); Q35 9B/27B configs target **96**. Constraint = visual-token activations + (on Q35) 248k-vocab logits, not dataset size. No FSDP/ZeRO on Q35 9B/27B; 8B on B200 can use DeepSpeed ZeRO-3.

**Default LoRA:** r16, α32, dropout 0.05, targets `q/k/v/o/gate/up/down_proj`. Qwen3.5 hybrid: attention LoRA hits **full-attention layers only**; DeltaNet `in_proj_*` **not** adapted; MLP LoRA hits every layer.

**LR sweep (32B, 25-ep Stage B):** 3e-5=0.768, 1e-4=0.821, **3e-4=0.875 best**, **1e-3≈0.40 chance**.

**Epochs:** 8B unified champion historically A4/B10; 0.8B v2 A1/B2; 9B/27B YAML A4/B4 (+ 9B 10-ep).

---

## 7. Data and eval

| Benchmark | What | Headline metric | Size |
|-----------|------|-----------------|------|
| **TSExam HF** | Categorical MCQ | accuracy | n=746 (`AutonLab/TimeSeriesExam1`) — **the** TSExam number |
| TSExam-numeric | Regression | medAE (also R², MAE) | 11k train / 660 test; best medAE **0.14** |
| TSExam-caption | Caption → 9-field attr recovery | macro acc | 7.7k train; specialist **0.72** |
| ChatTS A/B | Free-text QA | cat / num / reason-rule | A=159 / B=400 |
| ICL-UCR | k=1 in-context classification | micro / balanced acc | 90 subsets |
| **TSRBench** | North-star MCQ | overall + groups (perception / reasoning / prediction / decision) | 12-task subset, n=4125 |

**Tiered gate (per checkpoint):** loss (free) → TSExam (~35 s) → 176-item TSRBench slice (~12 s) → full TSRBench (~3 min 0.8B / ~5 min 8B, 8-GPU). **Parse-miss ≠ accuracy:** MCQ wants a single letter; free text / empty is format failure. Surfaced NR/TSF as mostly parse-miss.

**Pilot harness:** capped ~10k / 2 epochs on a frozen caption prior, LM-only LoRA, ~15 min on Q35. Noise floors (5-bucket calibration): TSExam ±**0.3 pp**, TSRBench overall ±**2.2 pp**. Pilot captures ~70–87% of full gain on TSExam; **does not** move TSRBench reasoning — use full run for that.

**Promotion gates (set before training):** −**3 pp** overall / −**5 pp** any reasoning task → do not promote.

**Decode:** greedy. `max_new_tokens` 16–64 MCQ; TSRBench thinking runs needed **2048** (1024 truncated chains → understated scores).

---

## 8. Kill decision (the hard call)

TSRBench overall had plateaued ~**46%**; reasoning ~**29%**. Targeted **TR**. Built ~6k (later TR-20k) synthetic temporal-relation exams. Gates **before** the run.

| Slice | Control | + synth | Δ |
|-------|---------|---------|---|
| Reasoning avg | 29.5 | 31.2 | +1.7 |
| AR / IR | — | — | ~+7 |
| **TR** | **26.9** | **21.9** | **−5.0** (gate) |
| NR | 35.2 | 31.8 | −3.4 |

**Killed** the mix: it regressed the exact slice it was supposed to fix. Average looked like a win. Then **task audit** (operator depth · domain-knowledge defer · format/convention) → targeted generators, not more buckets. Later full-B + TR-CoT: TSExam climbed to **0.926**; **reasoning stayed capped ~0.27–0.30** — more epochs + 3.7k TR-CoT did **not** move reasoning.

> More synthetic data is not better if it shifts the task distribution. Labels can be correct by construction and still wrong for the target.

---

## 9. Bugs you owned (infra / eval — she may probe DDP)

| Bug | What happened | Fix / number |
|-----|----------------|--------------|
| **Adapter-chain eval** | Stage B LoRA trained on base+Stage A; eval loaded Stage B on bare base | Reconstruct chain; **0.469 → 0.601 (+13 pp)** on qwendelay |
| **Distributed sampler** | `num_samples=N//world_size` re-sharded → each rank saw **1/8** data | `num_samples=len(w)` + shared seed |
| **Delay uint8 round-trip** | Lossy cast | float32 [0,1]; DINO 8B **0.798 → 0.831** |
| **Thinking never on (Q35)** | Collator read a train-only field; eval `enable_thinking` always false | Commit `6425c00`; ON==OFF was an artifact |
| **EOS mismatch (Q35)** | Model emits `<\|im_end\|>` (248046); config `eos_token_id=248044` → generate never stopped | Stop on `<\|im_end\|>` + first-answer extract; **no retrain** |
| **Warm-restart cosine** | HF `--resume` + more epochs left LR ~0 | `continue_adapter`: merge prior, attach Stage-B LoRA, **fresh** optimizer/cosine |
| **ICL unbalanced sampler** | Cap-100 without balancing = cap-30 | Balanced sampler **0.331 → 0.633** micro; 3.3× data did nothing |

**GRPO:** no net gain over SFT on saturated MCQ (0.795 vs 0.796); reward std ~0 in most groups; reasoning-format GRPO **regressed** 11 pp (confident wrong chains).

**Synthetic-only longer train:** 0.826 → **0.714** on real TSExam; val loss looked great because val shared the generator.

---

## 10. Probe bank (20–40s)

| Probe | Answer |
|-------|--------|
| Why two encoders? | Complementary failure modes. Chart = amplitude; delay = structure. ChatTS numerical 0.17 vs 0.71 vs dual 0.79. |
| Why not text-only TS? | Perception bottleneck; tokens wasteful; images steal a visual prior. Would compare to a native TS encoder on *their* signals — not married to matplotlib. |
| Why DINO for delay? | Native ViT on delay = 0.601; DINO on delay = 0.798. Right routing, not one tower for both. |
| LoRA vs full FT? | Iteration speed. r16 default; 9B r64 / 8B r128 sweet spots; r256 hurt TSExam. Unfreeze if LoRA ceiling is the bottleneck. |
| DDP / infra? | Sampler 1/8 data; adapter-chain +13 pp; Q35 EOS/thinking eval bugs; B200 preemption checkpoints. |
| How do you know it generalized? | Held-out HF TSExam + TSRBench; pilots with noise floors; kill on slice gates; parse-miss tracked separately. |
| Pretrain honesty? | Fine-tune / adapter / curriculum at 9B–27B. Not GPT-scale pretrain. |
| 9B/27B vs 8B champion? | 27B FT TSExam **0.921 ≈ 0.926**. 8B still leads some TSRBench perception. Zero-shot 27B TSRBench **ties** the 8B champion — FT is not a free win. |
| 27B on-device? | 9B/27B were iteration and ceiling, not a Watch proposal. Then freeze / probe / distill. |
| Isn’t images a hack? | Bet on a visual prior. If a native TS encoder wins on their series, that’s the same scientific question. |
| Year-one on health signals? | Learn *their* series and eval. Compare encoder families. Don’t port matplotlib. |

---

## 11. Phrases

**Use**

- “I don’t claim one component explains the whole gain. Dual-view plus Stage A→B beats single-view under the same harness.”
- “I killed the TR mix because it regressed the exact slice it was supposed to fix.”
- “Synthetic labels can be correct by construction and still wrong for the target distribution.”
- “Fine-tuning traded TSRBench reasoning/prediction for perception — I won’t hide that.”

**Avoid**

- “Hijacked the video stream”
- “Free architectural win” (2× visual tokens)
- “We pretrained a foundation model”
- Mixing 0.8B / 8B / 9B / 27B numbers in one sentence
- Claiming 9B/27B beat the 8B champion on TSRBench
- FinTech / TTD / forecasting as the lead

---

## 12. What *you* personally owned (IC)

Architecture (dual routing, DinoVisionTower, collator, Qwen patches) · curriculum (Stage A/B, caption prior, thinking format) · YAML experiment matrix (100+ configs/scripts) · tiered eval + parse-miss + pilot noise floors · promote/kill on pre-declared slice gates · eval-chain and distributed-sampler fixes · Q35 thinking/EOS eval diagnosis · cluster port (B200 venvs, preemption resume). Collaborators run Slurm jobs; **you** own the recipe and the gate.
