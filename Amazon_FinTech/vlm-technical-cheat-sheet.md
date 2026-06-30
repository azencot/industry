# VLM Technical Cheat Sheet — Time-Series QA

Purpose: one technical pull-thread page for Karan. Use `anchor-cheat-sheet.md` for the 90s story; use this page only when he asks for architecture, ablations, bugs, or results.

## Canonical Numbers

Use these as the stable PS1 headline numbers.

| Metric | Headline | Use when |
|--------|----------|----------|
| 8B stock baseline | TSExam / TSRBench **0.618 / 0.402** | "before" number |
| 8B best TSExam | **0.901** unified dual-tower | architecture / training win |
| 8B TSRBench north star | **0.454** (`8b-capnumicl`) | external benchmark |
| 0.8B TSExam | **0.890** vs 8B **0.897** specialist | SLM / routing angle |
| TR slice | **26.9 → 21.9** on bad synthetic mix | negative result / Ownership |

Do not recite every checkpoint. If asked for lineage: dual 8B hit **0.886** before unified **0.9008/0.901**; recent 3-epoch stack is roughly **0.905** TSExam and **0.452** TSRBench.

## Karan Pull Threads

| If he asks | Lead with | Number | Then say |
|------------|-----------|--------|----------|
| Why dual tower? | Renderer tradeoff: chart preserves amplitude; delay embedding preserves shape/topology | DINO+delay collapses on ChatTS numerical **0.17/0.22** vs matplotlib **0.71/0.71** | Dual gets amplitude + shape; not one view for all tasks |
| Proof the extra tower works? | Same train/eval harness, same data budget, compare single-tower vs dual | 8B dual **0.886** TSExam, best 32B **0.849** | Complexity justified by gated eval, not intuition |
| Why DINO for delay images? | Native ViT was not the right encoder for delay plots | `qwendelay-8b` **0.601** vs DINO delay **0.798** TSExam | Right routing is native Qwen ViT for charts, DINOv3 for delay |
| Biggest engineering debug? | Eval adapter-chain bug | misleading **0.469 → 0.601** (+13 pp) | Always reconstruct train-time adapter chain at eval |
| Biggest training data failure? | TR synthetic kill | TR **26.9 → 21.9** despite AR/IR **+7 pp** | Killed because it regressed the exact target slice |
| 0.8B vs 8B? | Size penalty is task-shape dependent | 0.8B **0.890** vs 8B **0.897** on TSExam | Route categorical/simple tasks to SLM when eval holds |
| Batch / memory? | Effective global batch ≈ **64**; micro-batch varies by run | 8B: pdtb **2**/accum **4** early, **1**/accum **8** later | Constraint = visual-token activations, not dataset; DDP replica per GPU, no ZeRO |
| LoRA / adapter chain? | Stage A merged before Stage B; eval must reconstruct chain | eval bug **+13 pp** if chain wrong | peft rank 16/α 32; LLM frozen + LoRA only |
| Batch / memory? | Effective global batch ~**64**; micro-batch tuned to fit dual visual tokens | early 8B **pdtb=2, accum=4**; later unified **pdtb=1, accum=8** | Constraint is activation memory, not dataset size |
| Distributed? | HF Trainer + Accelerate **DDP**; one full replica per GPU | sampler bug trained **1/8** data | No FSDP/DeepSpeed/ZeRO; fix `num_samples=len(w)` + shared seed |
| Eval decode? | **Greedy** (`do_sample=False`); MCQ parse-miss tracked separately | adapter-chain eval bug **+13 pp** | Always reconstruct Stage A→B adapter chain at eval |

## 30-Second Opener

We turn a numeric time series into images and feed it to a vision-language model. The core insight is that *how* you draw the series matters: a line chart preserves axes and amplitude, while a delay embedding preserves shape/topology but loses scale. Neither alone is enough, so I built a dual vision-tower model: frozen Qwen ViT on the chart, DINOv3 on the delay image, then fuse both into the LLM. The dual 8B beat the original 32B configurations, and the 0.8B model landed within 0.7 points of the 8B on categorical TSExam, which is the routing/SLM lesson. A lot of the work was not just architecture but debugging eval and training: adapter-chain reconstruction, distributed sampler correctness, and renderer precision.

## Core Idea

General-purpose LLMs are inefficient on raw numeric time-series tokens. Specialist time-series models like Chronos are strong for forecasting, but not designed for natural-language reasoning and MCQ-style explanations. VLMs give access to strong visual reasoning, but a single rendering loses information.

Two renderers:

| Renderer | Keeps | Loses / risk |
|----------|-------|--------------|
| Matplotlib line chart | axes, amplitude, local shape, trend | may miss topological / recurrence structure |
| Delay embedding / recurrence-style image | shape, recurrence, dynamical structure | scale-invariant; loses absolute amplitude |

The empirical finding: delay embeddings can be competitive on categorical/pattern questions, but collapse on numerical questions because they cannot see amplitude. The dual tower gives both views.

## Architecture

Each series becomes two images and two visual-token streams:

| Stream | Image | Encoder | Trained? |
|--------|-------|---------|----------|
| image | matplotlib chart | native Qwen ViT (`visual`) | frozen |
| video / delay path | delay-embedding image | DINOv3 ViT-L/16 | LoRA optional |
| merger/projector | DINO tokens → LLM token space | DINO projector / merger | full weights in Stage A; usually frozen in Stage B |
| LLM | fused visual tokens + prompt | Qwen LLM | LoRA in Stage B |

Implementation phrasing: do **not** say "hijacked video stream" in the interview. Say:

> I reused Qwen3-VL's video/visual-token pathway with `t=1` for the delay image, so the existing masks, M-RoPE/type tags, and merge logic routed both visual streams without a separate forward path.

DINOv3 config: `PIA-SPACE-LAB/dinov3-vitl-pretrain-lvd1689m`, `image_size=256`, `patch_size=16`, `spatial_merge_size=2`, deepstack taps `[6, 12, 18]`.

## Training

All adaptation is LoRA SFT unless otherwise noted.

| Stage | What trains | LLM updates? | Purpose |
|-------|-------------|--------------|---------|
| Stage A | DINOv3 LoRA + projector/merger | no | align visual delay stream; learn how to see |
| Stage B | fresh LoRA on LM + optional DINO LoRA; merger often frozen | yes | learn how to answer MCQ/QA/regression |

Default LoRA: rank 16, alpha 32, dropout 0.05, targets `q/k/v/o/gate/up/down_proj`.

LR sensitivity from sweep: **3e-4 best (0.875)**, 1e-4 solid (0.821), 3e-5 underfit (0.768), **1e-3 diverged near chance (0.40)**.

## Training / Systems Engineering

Grounded config for Karan low-level probes. **Do not recite verbatim** — lead with the principle, cite numbers when pressed.

### Hardware & precision

| | 8B (historical) | 0.8B (recent) |
|--|-----------------|---------------|
| **GPUs** | mostly **8× A100** | **8× RTX Pro 6000** (~96 GB); fallback 3× RTX 4090 |
| **Precision** | **bf16** train + eval (`load_model(dtype=torch.bfloat16)`) | same |
| **TF32** | not explicitly set → PyTorch defaults | same |
| **Sharding** | **DDP** — one full replica per GPU; no FSDP / DeepSpeed / ZeRO | same |
| **Peak memory** | not logged; fits comfortably with LoRA + grad-checkpointing + bf16 | same |

### Trainable parameters

| Stage | Trains | Frozen |
|-------|--------|--------|
| **A** | DINOv3 LoRA + merger/projector (full via `modules_to_save`) | LLM (no LoRA), native Qwen ViT |
| **B** | LM LoRA + DINO LoRA + merger (full unless `dino_freeze_merger: true`) | native Qwen ViT always frozen |

Counts: **0.8B** ≈ **28.1M / 1.2B = 2.33%** trainable. **8B** Stage B dual ≈ **141M** trainable (≈ **51M** with frozen merger, **−64%**). LLM base is frozen LoRA-only; DINO backbone frozen + LoRA; merger full-trained in A.

### Batch size (effective global ≈ 64)

| Config | per-device | grad accum | GPUs | effective global |
|--------|------------|------------|------|------------------|
| **8B early dual** | **2** | **4** | 8 | **64** |
| **8B unified / capnum / a4b10** | **1** | **8** | 8 | **64** |
| **0.8B v2 A/B** | **4** | **2** | 8 | **64** |

Interview line: *"We kept effective global batch around 64. Earlier 8B runs used pdtb=2/accum=4; later unified runs used pdtb=1/accum=8 to fit longer dual-tower examples. Constraint is activation + visual-token memory, not dataset size."*

### Token budget

- **max_length:** 8192 (8B), 4096 (0.8B v2).
- **Chart:** matplotlib `figsize=(6,2)` JPEG; ≈ **114 visual tokens** per full-res TSExam chart (processor-dependent; dual collator shrinks multi-series ICL charts to fit `max_length`).
- **Delay:** 256×256 → 16×16 patches → spatial_merge 2 → **64 tokens** (`patches` mode; 65 `cls_patches`, 1 `cls_only`).
- Dual tower ≈ **doubles visual tokens per series** (chart span + delay span).

### Optimizer & LR schedule

- **Optimizer:** AdamW (`adamw_torch`, HF defaults): `weight_decay=0`, `betas=(0.9,0.999)`, `eps=1e-8`, `max_grad_norm=1.0` — none overridden.
- **LR:** Stage A **1e-4**; Stage B **3e-4** (8B and 0.8B v2). Scheduler **cosine**, `warmup_ratio=0.05`.
- **Epochs (champion):** 8B unified **A 4 / B 10**; 0.8B v2 **A 1 / B 2** (~27× larger data). Other rungs: a3b6, a5b15, a8b25, a20b120…
- **LR sweep (32B, 25-ep Stage B):** 3e-5=0.768, 1e-4=0.821, **3e-4=0.875 best**, 1e-3=0.40 (chance).

### PEFT / LoRA stack

- **Package:** HuggingFace **peft** (`LoraConfig` / `get_peft_model`); pinned version not in configs (0.8B env: transformers 5.10.2 / torch 2.11).
- **Config:** rank **16**, α **32**, dropout **0.05**, `bias="none"`, `task_type=CAUSAL_LM`.
- **LLM targets:** `q/k/v/o_proj`, `gate/up/down_proj` (full-attention + MLPs; 0.8B DeltaNet `in_proj_*/out_proj` **not** targeted).
- **DINO targets:** same module list, scoped via regex; native ViT excluded (`.*\.visual\..*`); LM excluded when `dino_lora_on_lm: false`.
- **Adapter chain:** separate adapters per stage. Stage A **merged** (`merge_and_unload`) before Stage B trains fresh adapter. At eval: reconstruct chain (`--prior-adapter` merged, then `--adapter`) — the **+13 pp eval bug** fix.

### Distributed & throughput

- **Stack:** HF `Trainer`/`SFTTrainer` + **Accelerate DDP**. No FSDP / DeepSpeed / ZeRO.
- **Sampler bug:** `WeightedRandomSampler(num_samples=N//world_size)` re-sharded by `BatchSamplerShard` → each rank saw **1/8** data. Fix: `num_samples=len(w)` + shared seed across ranks.
- **Grad checkpointing:** ON. **Attention:** 8B `flash_attention_2`; 0.8B `sdpa`. **0.8B only:** `flash-linear-attention` + `causal-conv1d` → ~**6×** step speedup.
- **Dataloader:** charts + delay images rendered on the fly in collator (no disk cache); `num_workers` 4 (8B) / 0 (0.8B).

### Pretrained weights

| Component | Checkpoint |
|-----------|------------|
| **8B** | `Qwen3-VL-8B-Instruct` (local `models/base/`); original primary was Qwen3-VL-32B-Instruct |
| **0.8B** | `Qwen3.5-0.8B` |
| **DINOv3** | `PIA-SPACE-LAB/dinov3-vitl-pretrain-lvd1689m` (ViT-L/16, 256px); older 8B refs `facebook/dinov3-vitl16-pretrain-lvd1689m` |
| **Processor** | `AutoProcessor.from_pretrained(model_path)` — shared Qwen3VLProcessor / Qwen2VL image processor |

Custom config: `vision_config.out_hidden_size=1024`, deepstack `[6,12,18]` (8B) / `[]` (0.8B), `patch_size=16`, `spatial_merge_size=2`, `image_size=256`; `get_image_features` / `get_video_features` monkey-patched for delay path.

### Eval decode & parse

- **Decode:** greedy (`do_sample=False`, `num_beams=1`); no temperature / top-p.
- **max_new_tokens:** default 64; TSRBench MCQ **16**, caption **96**, numeric **64**, thinking **512**.
- **MCQ parse:** regex cascade in `utils.extract_letter` (leading letter → "answer is X" → "X)" → JSON → standalone letter, validated vs option count). TSRBench JSON uses `extract_letter_from_json`.
- **Parse-miss:** `pred is None` → logged in `parse_misses` + `<out>_parse_misses.jsonl`; scores as wrong for accuracy.

### Caveats (say if pressed)

- Peak GPU memory per stage **not logged** in repo.
- Exact **peft** pinned version not in configs.
- Chart token count (~114) is **processor-dependent**, not a fixed constant.

## Evaluation

| Benchmark | Task | Size | Metric |
|-----------|------|------|--------|
| TSExam HF | categorical MCQ | 746 | accuracy |
| TSExam-numeric | single-float regression | 660 test | R2, MAE, medAE |
| TSExam-caption | caption → attribute recovery | 1,926 test | macro attribute accuracy |
| ChatTS | free-text QA | A=159 / B=400 | cat / num / reason |
| ICL-UCR | k=1 UCR classification | 90 subsets, n=4,378 | micro acc, balanced acc |
| TSRBench | north-star MCQ | full 12-task subset | greedy single-letter accuracy |

Eval gate principle: track format/schema reliability separately from accuracy. For MCQ, parse-miss is a format failure, not simply a wrong answer.

## Results

### 8B

| Milestone | Config | Result |
|-----------|--------|--------|
| zero-shot | native ViT + matplotlib | TSExam **0.618** |
| single-tower SFT | matplotlib or DINO+delay | TSExam ~**0.79-0.80** |
| dual-tower | native + DINOv3, matplotlib + delay | TSExam **0.886** |
| unified dual-tower | co-trained TSExam + ICL | TSExam **0.9008 / 0.901** |
| north star | `8b-capnumicl` | TSRBench **0.454** |

Renderer tradeoff on ChatTS numerical:

| Config | Numerical A / B |
|--------|-----------------|
| 8B DINO+delay | **0.17 / 0.22** |
| 8B matplotlib | **0.71 / 0.71** |
| 8B dual-tower | **0.787 / 0.787** |

Numerical regression: TSExam-numeric zero-shot R2 **0.125** → trained specialist **0.941**; median relative error **39% → 4.5%**.

### 0.8B

Qwen3.5-0.8B VLM: ~853M params, hybrid Gated-DeltaNet + Mamba SSM LM. Same processor / visual-token conventions as 8B, so the dual-tower pipeline transferred with small compatibility changes.

| Benchmark | 0.8B trained | 8B specialist | Lesson |
|-----------|--------------|----------------|--------|
| TSExam categorical | **0.890** | **0.897** | near-tie; great SLM routing candidate |
| TSExam-numeric R2 | **0.75** specialist | **0.941** | wide-range regression needs capacity/calibration |
| ChatTS A cat/num | **0.774 / 0.708** | **0.840 / 0.756** | moderate free-text gap |
| ICL-UCR micro | **0.31** undertrained | **0.633** | small-data / format mismatch hurt |

0.8B note: installing `flash-linear-attention` + `causal-conv1d` gave about **6x faster training** (roughly 7-9 s/step → 1.0-1.2 s/step).

## Ablations And Debug Findings

| Finding | Number | Interview point |
|---------|--------|-----------------|
| Eval adapter-chain bug | misleading **0.469 → 0.601** (+13 pp) | Stage B LoRA was trained on base + Stage A; eval loaded only Stage B against bare base. Always reconstruct train-time adapter chain. |
| Sampler under-training bug | balanced runs trained on **1/8** intended data | `num_samples=N//world_size` got divided again by Accelerate per rank. Distributed correctness matters. |
| Delay uint8 round-trip | **+3-4 pp** on 8B DINO (0.798 → 0.831) | lossy renderer cast burned signal; float32 [0,1] fixed it. |
| LR sensitivity | **3e-4** best; **1e-3** chance | architecture robust, optimizer window narrow. |
| Subset-balanced sampler | **0.331 → 0.633** on ICL-UCR | sampler, not 3.3x data, taught generic in-context matching. |
| Freeze-merger Stage B | helps only overfit runs | +3.6 pp on overfit long run, -2.8 pp on Pareto run; reduces trainable params ~64%. |
| CLS token compression | small drop | `cls_only` 64x token compression only about -6 pp; patches carry most signal. |
| GRPO over SFT | **0.795 vs 0.796** | no net gain; reward std near zero in saturated groups, binary correctness reward hides reasoning quality. |
| Synthetic-only longer training | **0.826 → 0.714** real generalization | eval loss looked good because validation shared generator; masked overfit. |
| DINOv3 category profile | DINO wins anomaly/causality; matplotlib wins noise/pattern | complementary by category; supports dual tower. |

## Failure Story: TR Synthetic Kill

Use this when asked about negative results or Ownership.

We had around **46%** overall TSRBench on the 8B path, but broad data additions stopped moving the benchmark. I sliced by task and found reasoning weak, especially TR at **26.9%**. I generated about **6K** temporal-relation examples from TSExam-style primitives: segmentation, value extraction, segment categorization, and ordering.

Before training, I set gates: no more than **-3 pp** overall reasoning and **-5 pp** on any reasoning task. The short FT failed. The Stage B retrain improved some tasks, including AR/IR around **+7 pp**, but TR fell **26.9 → 21.9**, exactly hitting the kill gate. I killed the data path because it regressed the exact slice it was supposed to fix.

Lesson:

> More synthetic data is not better if it shifts the task distribution. Synthetic labels can be correct by construction and still wrong for the target distribution.

## Synthetic Data Quality

TSExam synthetic generation was structured around a feature dictionary and compositional time-series patterns. The label was known by construction: the generator emitted JSON with gold trend, seasonality, segment, value, and relation fields before rendering the series.

Controls:

- construction-time validation that template metadata and generated signal agree
- post-generation feature-recovery verifiers as sanity checks (not gold)
- real / curated data mixed in via CaTS when synthetic captions were too simple
- tiered eval on TSExam and TSRBench slices to catch generator overfit

Finance transfer:

> Use synthetic data for controlled coverage and rare cases, but gate on audited real documents. Synthetic expands coverage; it does not replace real-world eval.

## Phrases To Use

- "I don't claim one component explains the whole gain. The strongest claim is that dual-view representation plus Stage A-to-B curriculum beats instruction-only and single-view baselines under the same eval harness."
- "The extra tower roughly doubles visual-token cost per series, so I justified it with ablations, not intuition."
- "The 0.8B result shows the size penalty is task-shape dependent; categorical routing can go small when eval holds."
- "I killed the TR mix not because the average was bad, but because it regressed the exact slice it was supposed to fix."

## Phrases To Avoid

- "Hijacked the video stream" → say "reused the video/visual-token pathway."
- "Free architectural win" → say "higher visual-token cost, justified by ablations."
- "Synthetic data is gold" without caveat → say "labels are known by construction, but distribution can still be wrong."
- Dumping every result. Lead with one metric and wait for pull threads.
