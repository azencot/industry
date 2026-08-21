# Notes — 2026-08-21 — Common pitfalls when starting SFT (e.g. Qwen)

**Type:** Depth note after a “what goes wrong on first SFT” discussion  
**Use:** later **tech screen** / on-site LLM-training — not the Fri HM skim  
**Related:** [`2026-08-20_llm-training-judgments.md`](2026-08-20_llm-training-judgments.md) (NLL vs task, packing, completion-only, ckpt selection)

The failures that kill a first SFT run are almost never “wrong optimizer.” They are **format, labels, and eval**. The model learns whatever you actually put in the loss — including your chat template, truncated answers, and noisy “gold.”

---

## 1. Data is the model

- **Garbage in, fluent garbage out.** SFT is imitation. Inconsistent labels, mixed styles, and wrong “gold” CoT get copied faithfully.
- **Too little diversity, too many epochs.** A few thousand near-duplicates + 5 epochs looks like training loss going to zero and a model that only works on that phrasing.
- **Train/eval leakage.** Same questions rewritten, templates copied from the test set, or synthetic data generated from the eval distribution. You “beat the bench” without learning the task.
- **Wrong target for the product.** Training long CoT when prod wants a short JSON field; training letter answers when you later score free-form. Letter-level GRPO on a saturated SFT is a no-op if the imitation objective is already maxed.
- **No replay of general instruction data.** Task-only SFT on an instruct checkpoint often wrecks chat, refusal, and formatting that you still need at inference.

Rule: start with a **small, inspected, format-consistent** set. Read 50–100 examples. If you would not want the model to say that, do not train on it.

---

## 2. Chat template and loss masking (the Qwen killer)

Most common “I followed a blog and it is broken” class.

- **Not using the model’s chat template.** Qwen is ChatML-style (`<|im_start|>` / `<|im_end|>`). Training on Alpaca `"### Instruction"` or a Llama template produces a model that is incoherent under the real tokenizer template.
- **Qwen2.5 vs Qwen3.** Qwen3 adds thinking / `<think>` behavior. Mixing templates, or training with `enable_thinking` on and serving with it off (or the reverse), looks like “SFT did nothing.”
- **Loss on the full sequence.** If you do not **mask user/system tokens**, the model spends capacity predicting the prompt. Always SFT on **assistant tokens only**.
- **Missing EOS / stop tokens.** Model never learns to stop; you get run-on answers or the next fake turn.
- **Packing without boundaries.** Concatenating examples without blocking attention/loss across documents leaks the next sample into this one. (Packing ≠ padding; uniform files ≠ uniform tokens — see the 08-20 judgments note.)
- **Truncation of the answer.** `max_length` cuts the completion; the model learns to stop mid-JSON. Check how many train rows hit the length cap.

If train loss is healthy but greedy decode is garbage, dump one tokenized train example and one inference prompt and **diff the special tokens**.

---

## 3. Starting from the wrong checkpoint

- **Base vs Instruct.** Task SFT almost always starts from **Instruct**. Base needs a real instruction-tuning mix first; a few thousand task pairs will not invent a chat model.
- **Full FT when LoRA is enough (and the reverse).** Full FT of 7B–32B on a small set is an expensive way to forget English. LoRA (or QLoRA) is the default for “adapt to my problem.” Full FT belongs to large, diverse, multi-epoch recipes or when you must change the whole distribution.
- **Wrong modules in LoRA.** On Qwen, target **q/k/v/o plus MLP (gate/up/down)**. Attention-only LoRA often underfits format-heavy tasks.
- **Continuing from a mid-run adapter** with a new template or tokenizer. Silent mismatch.

---

## 4. Optimization that looks like “SFT is unstable”

- **LR too high** (especially full FT): loss spikes, repetitive collapse, or the model becomes a single-style parrot.
- **LR too low / too few steps:** train loss barely moves; people then “fix” it by adding RL.
- **One huge epoch vs many tiny ones.** Prefer **~1–3 epochs**, early-stop on a **held-out task metric**, not train loss.
- **Unstable batch / packing.** Effective tokens/step jumping around; packing + variable packing efficiency without adjusting LR.
- **bf16 vs fp16.** Qwen-class models expect **bf16**. fp16 on Ampere/Hopper is a common NaN source.
- **Gradient accumulation + LoRA + tiny LoRA LR copied from full-FT recipes.** Scale LR to effective batch size; do not copy a 32B full-FT LR onto 8B LoRA.

---

## 5. Eval that cannot tell you if SFT worked

- **No frozen baseline.** You need zero-shot / few-shot of the **same** Instruct model, same template, same decode settings.
- **Train loss as the KPI.** It will fall even while the product metric is flat or down (forgetting, format drift). Mixture NLL is not the task.
- **Decode mismatch.** Trained at temp 0 / greedy; demoed at temp 0.8 with a different system prompt.
- **Offline metric ≠ serving constraint.** Exact-match on a letter vs calibrated probability vs latency. SFT can win the letter and lose the thing you ship.
- **Slicing.** Macro score up, worst customer slice down. In health / finance this is the actual failure.

---

## 6. Process pitfalls (especially after a first green run)

- **Jumping to RL too early.** If SFT is saturated or the reward has ~0 variance across samples, GRPO/PPO will not move the metric. Fix the data or the reward, not the RL code.
- **Synthetic data without a filter.** Teacher-model CoT that is wrong-but-fluent is worse than short correct answers.
- **Mixing incompatible objectives** in one run (tools + CoT + JSON + chat) without mixture weights or staged curriculum.
- **Tokenizer / special-token edits** (adding `<tool>`, `<ts>`) without resizing embeddings correctly and checking unused-token init.
- **Saving/loading:** adapter not merged, or merged into the wrong base; tokenizer not saved; `pad_token = eos` causing training/inference divergence.

---

## Practical first-run checklist (Qwen)

1. Instruct checkpoint, official chat template, assistant-only loss, EOS on every target.
2. 100-row **spotless** set; confirm tokenization and that answers are not truncated.
3. LoRA on attn+MLP, bf16, 1–2 epochs, held-out **task** metric vs the untuned Instruct model.
4. Keep a slice of general instruction data if you still need a general assistant.
5. Only then scale data, then full FT, then RL.
