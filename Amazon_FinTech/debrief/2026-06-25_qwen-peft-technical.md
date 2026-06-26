# Debrief — 2026-06-25 — Qwen (HF) + PEFT/LoRA technical depth

## Session

- **Type:** exploration — repo walkthrough + interview framing (Cursor Q&A)
- **Duration:** ~30 min (end of Wed 25 prep day)
- **Prior context:** [`vlm_multimodal_project.md`](vlm_multimodal_project.md) (architecture); [`2026-06-25_anchor-bc-lp-debrief.md`](2026-06-25_anchor-bc-lp-debrief.md) (Anchor B/C same day)

## Conclusions

### Qwen from Hugging Face / Transformers

The repo uses **Qwen as a pinned local Hugging Face model snapshot** loaded through `transformers`.

**Paths**

- Config: `"${QTSX_ROOT}/models/base/Qwen3.5-0.8B"`
- Heavy weights redirected via `src/paths.py` → `$QTSX_ARTIFACT_ROOT/models/base/Qwen3.5-0.8B` (outside git on artifact filesystem)

**Load API**

```python
AutoModelForImageTextToText.from_pretrained(model_path)
AutoProcessor.from_pretrained(model_path)
```

The **processor matters as much as the model**: tokenizer, chat template, image/video special tokens, multimodal formatting.

**Not plain text** — `src/model_patch_q35.py` loads Qwen3.5, keeps native vision tower for matplotlib chart images, attaches **DINO tower** as second “video” stream for delay-embedding time-series images; rest of Qwen forward path reused.

**Key integration files**

| File | Role |
|------|------|
| `configs/dual_q35_*.yaml` | model_path, data, adapters, hyperparams |
| `src/model_patch_q35.py` | load Qwen + processor; dual visual setup |
| `src/unified_collator.py` | time-series examples → Qwen-compatible multimodal batches |
| `src/train_q35.py` | train with Qwen as base runtime |
| `src/eval_q35_vision.py` / `src/eval_q35_tsrbench.py` | reload Qwen + adapter chains for eval |

### PEFT and LoRA on the model

**PEFT** adapts Qwen without full fine-tuning. Base Qwen weights stay **frozen**; training writes small adapter checkpoints under `$QTSX_ARTIFACT_ROOT/checkpoints/<run>/best`.

**LoRA targets**

- `q_proj`, `k_proj`, `v_proj`, `o_proj` — full-attention token mixing
- `gate_proj`, `up_proj`, `down_proj` — MLP feature transforms
- Embeddings, norms, most base weights stay frozen

**Qwen3.5-0.8B hybrid nuance**

Many layers are **linear_attention / DeltaNet**; only periodic layers are **full attention**.

- Attention LoRA hits **only full-attention layers**
- DeltaNet projections (`in_proj_qkv`, `in_proj_z`, `in_proj_b`, `in_proj_a`, `out_proj`) are **not** adapted
- MLP LoRA hits **every layer**
- `visual_dino.merger` can be full-weight saved via `modules_to_save` when configured

**Effective PEFT setup**

- Sparse attention adaptation
- Dense MLP adaptation
- No DeltaNet mixer adaptation
- Optional full-weight merger save on visual/DINO side

**Stage pattern**

```
base Qwen → Stage A adapter / merger prior → Stage B LoRA adapter → eval
```

- **Stage A:** usually visual/DINO side
- **Stage B:** usually language model side
- **Eval:** adapter **order matters** — forgetting Stage A prior means Stage B is applied to wrong base state

### Interview one-liner (memorize)

> My repo uses Qwen as a pinned local Hugging Face/Transformers snapshot, loaded with `AutoModelForImageTextToText` and `AutoProcessor`. Around that base, the repo adds a dual visual path for time-series inputs and uses PEFT/LoRA to fine-tune small adapter deltas instead of the full model. LoRA targets attention and MLP projections, but because Qwen3.5 is hybrid, the attention LoRA only touches full-attention layers while MLP LoRA touches all layers. Evaluation must reconstruct the same base-plus-adapter chain used in training.

### Karan follow-up hooks

- Why LoRA on MLP everywhere but sparse on attention? (hybrid architecture)
- What stays frozen vs `modules_to_save` on merger?
- How eval reload differs from train (adapter chain order)
- Processor/chat template — what breaks if you swap tokenizer?

## Decisions / artifacts updated

- [x] [`Amazon_FinTech/prep-plan.md`](../prep-plan.md) — Wed 25 VLM item
- [x] This debrief
- [ ] `vlm_multimodal_project.md` — already has high-level PEFT; no change unless drilling file-level detail

## Open questions

- None blocking; optional: spoken 2-min version of one-liner under mock grill

## Next session (one prompt for session B)

> Read `@Files Amazon_FinTech/debrief/2026-06-25_qwen-peft-technical.md` and `@Files .cursor/skills/debrief/vlm_multimodal_project.md`. Run a 5-min Karan follow-up drill: ablations, config sweeps, and “what would you change for proprietary finance TS?”
