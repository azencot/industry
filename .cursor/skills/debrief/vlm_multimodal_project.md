# Time-Series Vision-Language Models — project summary

**Long-lived reference.** Extend this file as the project evolves — new results, problems solved, ablations, interview angles.  
**Interview cheat sheet:** [`Amazon_FinTech/anchor-cheat-sheet.md`](../anchor-cheat-sheet.md)  
**Experience profile (broader arc):** [`omri_azencot_experience.md`](omri_azencot_experience.md)  
**Talk map:** [`talks/ts-vlm/README.md`](../../../talks/ts-vlm/README.md)

**Source of truth for numbers:** private repo [`azencot-group/TSLMTSEXAM`](https://github.com/azencot-group/TSLMTSEXAM) branch **`grpo`**, `RUN_SUMMARY.md` through **§28 (2026-08-10)**. Do **not** quote `main` (frozen 2026-06-30) or mix unlabeled campaigns.

Last updated: 2026-08-27

---

## Overview

**Goal:** Teach general-purpose VLMs to reason over univariate and multivariate time series — not just classify UCR shapes, but answer exam-style questions, explain temporal relations, and generate structured captions. If there is “prediction,” it is choose-the-answer, not a forecast head.

**Which scale to quote (lock):**

| Role | Model | Use in a talk |
|------|--------|----------------|
| **TSExam / TSRBench ceiling** | Qwen3-VL-**8B** dual | Headline three-bench results |
| **ChatTS ceiling** | Qwen3.5-**27B** dual (thinking OFF) | Beats ChatTS-14B paper on cat |
| **Stage C / serving** | Qwen3.5-**9B** dual | TSExam **0.9316** after C-RS; vLLM port |
| **Recipe screen** | Qwen3.5-**0.8B** | Fast pilots; not the external hook |
| **Scale probe, not a result** | Qwen3.5-**122B-A10B** MoE | Trained; FT letter-A bias — do not slide |

**North star:** [TSRBench](https://tsrbench.github.io/) — 15 tasks, 4 dimensions, **4,125** problems, official protocol. Paper open ceiling: Qwen3-VL-32B **44.9%** overall; closed: GPT-5 (T+V) **55.6%**.

**Supporting benches:** TSExam HF (`AutonLab/TimeSeriesExam1`, n=746) · ChatTS official A/B · TSExam-numeric · captions · ICL-UCR · CaTS-Bench. The 12-task JSONL is a **training gate**, not the SOTA claim.

**Intellectual lineage:** ImagenTime (NeurIPS 2024) — TS-as-image for *generation*; this project is *reasoning* via a VLM with two live towers.

---

## Core insight (measured, not a hunch)

LLMs do not use raw numeric tokens well. **One rendering loses information.**

| Encoding | Captures | Route | Failure mode if used alone |
|----------|----------|-------|----------------------------|
| **Line chart** (matplotlib) | Amplitude, trend, axes | Frozen native Qwen ViT (`visual`) | Weaker on anomaly / causality |
| **Delay-embedding** | Shape / recurrence; **scale-invariant** | DINOv3 + merger (`visual_dino`) | **ChatTS numerical collapses** (~0.17–0.35 vs ~0.71 matplotlib) |

**Dual tower** feeds both in parallel. Empirically: dual 8B **beats every 32B single-tower** on TSExam-full (0.886 vs 0.849); dual ChatTS numerical **matches ChatTS-14B paper** (0.787). Native ViT **cannot** be LoRA’d into a delay encoder (`qwendelay` 0.601 vs DINO 0.831). Complementary by TSExam category: delay wins anomaly + causality; chart wins noise + pattern.

**Implementation note (Q&A, not a title):** DINOv3 rides Qwen’s video stream (`t=1`); native ViT stays on the image stream and is never LoRA’d.

**DINO objective (lock — missed on Bosch 2026-08-27):** Self-distillation, not SimCLR. Two views; student vs **EMA teacher**; CE on softmax (teacher centered/sharpened); no labels. DINOv3 = that family. You **load pretrained**, then Stage A **LoRA on delay images**. “Zero-shot” = SSL init, not “the tower is never trained.” Image → tokens: patches → ViT tokens → merger/projector → LLM.

**Design principle:** Decouple *how to see* from *how to answer* — Stage A captions transfer to Stage B QA.

---

## Architecture

```
Time series input
    ├── line chart ──────────→ Qwen native ViT (frozen) ──→ projector ──┐
    │                                                                    ├──→ LLM (LoRA in Stage B)
    └── delay-embedding image → DINOv3 + merger (LoRA in Stage A) ──→ projector ──┘
```

**Personal ownership:** patched Qwen3-VL-8B / Qwen3.5 0.8B / 9B / 27B / 122B-A10B forwards; `DinoVisionTower`; dual-stream collator (M-RoPE); adapter merge/resume A→B; **vLLM out-of-tree dual plugin** (9B, 100/100 TSExam-gate parity vs HF).

**Scale strategy:** validate the recipe on 0.8B/8B; 9B/27B for ChatTS + native thinking + serving; do **not** assume bigger is better on TSRBench (it isn’t, yet).

---

## Training curriculum

| Stage | What trains | LLM updates? | Status |
|-------|-------------|--------------|--------|
| **A** | DINO LoRA + merger on caption/align | **No** | Locked. LLM frozen. Perception: what a series is + components. |
| **B** | Merge A; LM LoRA; merger often frozen | **Yes** | Locked. QA + traces. |
| **C** | C-RS (SFT on **gold** TR rationales) then C-RL2 (GRPO) | LoRA | **Working recipe on 9B.** Early letter-GRPO on saturated SFT was a **no-op**. |

### Stage C — what actually happened (`grpo` §7, §27–28)

- Letter GRPO on new-ds SFT: **0.795 vs SFT 0.796** — 90% of groups had zero reward-std.
- Reasoning-format GRPO: **regressed 11 pp** (confident wrong chains).
- Fresh GRPO from bare base: learned **format**, not correctness (~zero-shot).
- **C-RS → C-RL2** on a rationale-free 9B letters base: TSExam **0.9316** (all-time), box/fmt 1.0, TSRBench inline **40.7** (+1.2).
- Think-base + RL: **format only**, accuracy-neutral (third confirmation).

Talk: in progress / upweight good answers — don’t say “GRPO is how we got SOTA.” Gold traces then RL moved TSExam; TSRBench barely moved.

### Stage A data (evolution)

0. Instruction-only: **50+ configs**, TSExam stuck **~61.8%**.
1. Synthetic captions from **per-series gold features** (template + randomization; no LLM labeler).
2. **CaTS** (~16K) for messy real signal.
3. Mix → 8B TSExam **~90.5%+**; full-B ep10 **0.926**.

### Stage B mix

TSExam MCQ, ChatTS SFT/IFT, TSExam-numeric, optional caption holdout, TR-20k / **TR-v2** operator families. **ICL-UCR raises ICL and costs TSRBench pred/decision** — TSRBench champ is **no-ICL**.

**Control (Jun 2025):** `allcap-a5b3` — TSExam 0.854, TSRBench 0.339, TR 28.7%.

---

## Technical scope — what I built

| Area | Details |
|------|---------|
| **Training** | PyTorch DDP; LoRA/PEFT; YAML-config-first (**162+ configs**); stratified samplers; warm-restart `continue_adapter` (fresh cosine — naive `--resume` froze LR) |
| **Data** | Unified loaders: TSExam / numeric / caption / ChatTS / ICL-UCR / CaTS / TSRBench / TR-v2 (named series, up to 8 ch, series-as-options) |
| **Eval** | Loss → TSExam HF → TSRBench slice → full n=4125. Parse-miss ≠ accuracy. Official ChatTS rule-based cat/num/reason. Thinking ON/OFF + EOS `<\|im_end\|>` (two bugs caught — see log) |
| **RL** | Stage C: STaR/vLLM gen, C-RS, C-RL2 GRPO (per-chunk backward, 4096 completions); **not** the failed letter-GRPO on new-ds |
| **Serving** | vLLM 0.25.1 dual plugin; bake merged 9B; **100/100** greedy parity vs HF on a local TSExam gate (~30 GPU-min for the port) |
| **Scale** | 122B-A10B ZeRO-3 (attention + shared-expert LoRA; don’t LoRA 256 routed experts). FT MC collapsed to letter-A — adapter regime, not a published win |

---

## Results (official protocols)

*TSExam = HF n=746. TSRBench = official overall n=4125. ChatTS = paper A/B cat/num. Label the campaign when you speak.*

### Headline three-bench (talk contribution 4)

| Bench | Best we report | Vs published | Note |
|-------|----------------|--------------|------|
| **TSExam HF** | **0.926** 8B full-B ep10; **0.9316** 9B after C-RS | No public dual-tower posting this on HF TSExam | 0.901 unified a4b10 is the earlier specialist champ |
| **ChatTS** | Dual 8B **matches 14B paper numerical** (0.787); **27B cat 0.92 / 0.90** beats paper 0.889 / 0.862 | ChatTS-14B paper A 0.889/0.788, B 0.862/0.787; GPT-4o vision much lower | Official ChatTS metrics, not HiTSR |
| **TSRBench overall** | **0.4565** 8B no-ICL 4ep; **0.454** capnumicl-a8b4; TR-v2 8B **44.7** | Paper: Qwen3-VL-32B **44.9**, TimeOmni-1-7B **36.7**, ChatTS-14B **33.5**, GPT-5 T+V **55.6** | **SOTA or on par among open**; still behind proprietary. First known stack at/near SOTA on **all three** public protocols |

Do **not** say 9B/27B beat 8B on TSRBench (they don’t: ~0.41–0.43). Do **not** treat TimeOmni **49.4** as overall — that is the **EP** column; overall is **36.7**.

### Scale snapshot (don’t mix unlabeled)

| Model | TSExam HF | TSRBench overall | ChatTS (best cells) |
|-------|-----------|------------------|---------------------|
| 8B dual Stage B | **0.926** full-B ep10 | **0.4565** no-ICL 4ep | B 0.901 / 0.847 (single-cosine) |
| 9B dual Stage B | 0.883 (10ep) | ~0.41–0.43 | 9B-4ep ~0.91 / 0.87 |
| 9B + C-RS/C-RL2 | **0.9316** | inline 40.7 | C-RL2 board ~0.89/0.82/0.90/0.86 |
| 27B dual OFF | **0.921** | (re-runs @2048) | **A 0.92 / B 0.90 cat** |
| 0.8B Q35 | 0.890 v2 | 0.405 audit path | — |
| 122B zs / FT | zs **0.731** (best zs) / FT 0.47 letter-A | zs 41.6 | FT ChatTS 0.86; MC broken |

### Other (backup, not spine)

| Bench | Best | Notes |
|-------|------|-------|
| TSExam-numeric medAE | **0.14** (unified3 0.8B) | Six-order GT range — report medAE |
| Caption 9-field | **0.72** | Attr-recovery |
| ICL-UCR | micro **0.688**, 90/90 beats-chance | Fourth bench; trades off TSRBench pred/decision |

**Spoken headline:** Official protocol on TSExam, ChatTS, and TSRBench — SOTA or on par; TSRBench is where closed models still win. 8B is the TSRBench/TSExam Stage-B ceiling; 27B is the ChatTS ceiling.

---

## Negative results (show rigor)

### TR / reasoning bucket mixes regressed

Blind TR mixes **hurt** the hard slice. Stopped stacking buckets; audited primitives; rebuilt generators (TR-v2). Extra full-B epochs: TSExam climbs, **TSRBench saturates ~0.44 from ep3**, reasoning group stuck ~0.27–0.30.

### Mixed multivariate schemas (ravel as univariate)

ChatTS student path stores `timeseries` as `[C, T]` and splits **per channel**. TSExam used named 1-D fields (`ts` / `ts1` / `ts2`). Loaders that `.ravel()` a 2-D `ts` **concatenate channels in time** — one fake univariate; delay geometry is garbage. Dual collator is **N series → N markers → N chart + N delay**. Talk: slide 13, not a fifth contribution.

### Early GRPO did not beat SFT

Letter GRPO no-op; reasoning GRPO regressed. Binary correctness on saturated MCQ has no group variance.

### Native thinking

Zero-shot thinking **destroys** TSRBench (9B **0.166** ON vs **0.417** OFF). Fine-tuned: thinking-OFF is the fair best after two eval bugs (thinking never engaged; wrong EOS → runaway). Don’t claim CoT as a free win.

### 122B FT

Attention-only LoRA: TSExam 0.43→0.47 with letter-A bias (508/746). Capability is there (zs 0.73, ChatTS 0.86); **adapter regime** is not a three-bench result.

### Single-cosine vs warm-restart

One 11-ep cosine **does not** reproduce full-B TSExam 0.926 (best 0.902); it **wins ChatTS**. Don’t treat schedule as a footnote.

---

## Problems solved — detailed log

*Add new entries at the top.*

### 2026-08 — Stage C2/C3 + TR-v2 + 122B (`grpo` §27–28)

**Problem:** Letter GRPO on a format-saturated base is a no-op; TSRBench reasoning still missing operator families (NR rate-conversion, two-event localization).

**Action:** C-RS gold-rationale SFT → C-RL2; TR-v2 20k / 7 families; 122B ZeRO-3 dual chain.

**Result:** 9B TSExam **0.9316**; TR-v2 8B TSRBench **44.7** (IR/CD/ER gains; NR still recites units and fails conversion). 122B FT not usable for MC.

### 2026-07 — Qwen3.5 9B/27B + thinking/EOS eval bugs (`iucc_cluster` / `grpo` §23–25)

**Problem:** Dual eval never set `enable_thinking`; then thinking-ON ran away on wrong EOS.

**Action:** Collator toggle; stop on `<|im_end|>`; first-answer extract; MNT 2048 on TSRBench.

**Result:** 27B TSExam **0.921**; 27B ChatTS cat above ChatTS-14B; 8B still leads TSRBench.

### 2026-07 — vLLM dual-tower port (`grpo` §26)

**Action:** Out-of-tree plugin + bake; skip video re-norm / extra timestamp tokens.

**Result:** 100/100 answer parity vs HF on a 100-item greedy gate. 8B deepstack not ported.

### 2026-06 — TSRBench task audit + Stage C (0.8B)

**Problem:** Blind TR mixes regressed TR (−5 pp).

**Action:** Task audit → three regimes; extended TSExam ops; VRT/GRPO on 0.8B.

**Result:** 0.8B TSRBench **0.382→0.405**; reasoning **0.245→0.255**.

### 2026-06 — Captions too basic / scarce

Synthetic gold-feature captions, then **CaTS** in Stage A. LOO: **dropping** a caption bucket **+3 pp TSExam** — mix quality > more buckets.

---

## FinTech bridges

| Research concept | FinTech parallel |
|------------------|------------------|
| Dual chart + delay | Tables + text + numbers; one view loses information |
| A then B | Domain alignment → task FT |
| Caption 9-field 0.72 | Field extraction |
| TSExam-numeric medAE 0.14 | Numeric correctness |
| Parse-miss vs accuracy | Schema reliability before accuracy |
| 0.8B near 8B on TSExam | SLM routing when quality holds |
| GRPO no-op on saturated MCQ | Reward design before “just add RL” |
| vLLM dual parity gate | Serve the same model you trained |

### Production bridge (not yet built)

> Shadow eval before promote; abstain on parse-miss spikes; slice regressions; human queue; corrections → golden set → gated retrain.

---

## PS1 / Bosch interview hooks

| Anchor | Theme | Lead with |
|--------|-------|-----------|
| **A** | Production ML | Dual tower **measured** (numerical collapse + qwendelay control); DDP; vLLM 9B parity |
| **B** | Eval | Official three-bench protocol; parse-miss; thinking/EOS bugs caught; killed TR mixes |
| **C** | Dive Deep | Caption + TSRBench ops audit; TR-v2; Stage C = gold traces not letter-GRPO |

**5–7 min order:** problem → two geometries (evidence) → I built towers/collator/eval → **8B ~45.6% TSRBench / 0.926 TSExam / ChatTS on par with 14B; 27B wins ChatTS cat** → TR saturates / GRPO no-op → transfer = frozen suite + vLLM, not 122B.

**Anti-patterns:** Don’t lead with 9B/27B as the better model. Don’t say first dual-view in the universe (LLaTiSA is plot+table on **HiTSR**). Don’t say 122B worked. Don’t say Stage C GRPO is the SOTA.

---

## Stack

Python 3.11 · PyTorch · Transformers · PEFT/LoRA · TRL · DeepSpeed ZeRO-3 · vLLM (9B dual plugin) · HF datasets · Slurm DDP  
**Models:** Qwen3-VL-8B (north-star champ) · Qwen3.5 0.8B / 9B / 27B · 122B-A10B (infra only)

---

## Open questions

- [x] TSRBench 8B vs paper table — **0.4565** vs Qwen3-VL-32B 44.9 / GPT-5 55.6 (open on par; closed ahead)
- [ ] 27B dual TSRBench at MNT 2048 — still in-flight in §23
- [ ] NR operator coverage in TR-v2 (rate conversion, two-event localization)
- [ ] 122B shared-expert MLP LoRA retrain (pending a healthy Stage B)
- [ ] vLLM: 8B deepstack + ChatTS/ICL paths

---

## Changelog

| Date | Change |
|------|--------|
| 2026-08-19 | Synced to **`grpo` §21–28**. 8B is TSExam/TSRBench ceiling; 27B ChatTS; Stage C = C-RS not letter-GRPO; vLLM; 122B caveat. Dual-tower evidence (numerical collapse, qwendelay). |
| 2026-08-12 | Current models → 9B / 27B (overstated — 8B still north-star) |
| 2026-06-21 | Initial extended summary |
