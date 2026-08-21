# Notes — 2026-08-20 — LLM training judgments (not the VLM project)

**Type:** Extra spoken drills after the Apple training-run walkthrough  
**Use:** later **tech screen** / on-site LLM-training interview — **not** the Fri HM skim  
**Apple HM spoken spine:** [`../interviews/apple-health-aiml/2026-08-20_training-run-drill.md`](../interviews/apple-health-aiml/2026-08-20_training-run-drill.md)  
**Follow-on:** [`2026-08-21_sft-starting-pitfalls.md`](2026-08-21_sft-starting-pitfalls.md) — first-SFT pitfalls (template, data, LoRA, eval, RL too early)

---

## What broke in the room (keep these)

| Symptom | Junior move | IC move |
|---------|-------------|---------|
| Train + held-out **NLL ↓**, task flat | Sweep LoRA rank | Mixture NLL ≠ the task. Frozen-base eval check; NLL on **task strings**; original instruct suite if forgetting |
| Train NLL **stalled** | Raise LR **and** train longer; never unfreeze | Split: bug / dead cosine / high floor after LR sweep → rank → unfreeze. Don’t add data if you can’t fit the current set |
| Unfreeze at **LoRA LR** (3e-4) + LoRA steps | Replay pretrain data | That recipe **wrecks** the base and OOMs plain DDP. Retune LR, shorter run, partial unfreeze, shard; replay after it’s stable |
| Pack 8k; sources uniform; A=200 tok, B=6k | “Padding / mask loss” | Packing ≠ padding. Uniform **files** ≠ uniform **tokens**. 1×6k ≈ 30×200. Set a **token budget**; don’t pack A+B into one token-mean CE unless you mean to |
| Keep **best** ckpt on the reported eval | “I verified eval” | You chose **stopping time** on the published number (winner’s curse). Select on val/proxy; report test **once** |
| Grad accum of 8, copy paper LR + clip 1.0 | Skip accum | Clip **after** accum. Mean vs sum of micro-losses; match **tokens**/step not just sequences |
| SFT: all-tokens vs completion-only | All-tokens when the answer is a letter (more signal) | **Completion-only** for instruct SFT. Short answers are why you **mask the prompt** (else the question owns CE). Imbalance → rebalance or longer completion, not prompt loss. All-tokens = domain pretrain. Same FLOPs either way |

---

## Three sentences

> Mixture NLL is not the task. Train NLL tells you whether you are underfitting before you touch rank. Equal file counts is not a mix if one source is thirty times longer.
