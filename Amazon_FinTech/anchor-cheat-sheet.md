# PS1 anchor cheat sheet — VLM time-series reasoning

**One project, three angles.** Read before PS1 intro / ML deep-dive / LP follow-ups.  
Full context: [`.cursor/skills/debrief/vlm_multimodal_project.md`](../.cursor/skills/debrief/vlm_multimodal_project.md)

North star: [TSRBench](https://tsrbench.github.io/) · Control: allcap-a5b3 (TSExam 0.854, TSRBench 0.339, TR 28.7%)

---

## Anchor A — Production ML/LLM system

| | |
|---|---|
| **Problem** | General VLMs can't do exam-grade time-series reasoning (MCQ, numbers, temporal relations). |
| **Insight** | Raw TS tokens are inefficient; dual visual encodings (chart + delay embedding) fused into one LLM. |
| **What I built** | Patched Qwen3-VL-8B & Qwen3.5-0.8B forwards; DinoVisionTower; dual-stream collator + M-RoPE tags; two-stage curriculum (Stage A: vision alignment, Stage B: LM LoRA); YAML-config sweeps (162 configs); DDP on 8× GPU via Slurm. |
| **Metrics** | **Qwen3-VL-8B** stock (0.618 / 0.402) → our stack **3ep** (0.905 / 0.452). |
| **JD map** | End-to-end ML systems; tiered eval gates; multimodal finance docs analogy. |
| **Honest limit** | TSRBench +5 pp from stock real but below frontier; hard TR ~29%; proprietary gap remains. |
| **Lesson** | Decouple *how to see* (Stage A) from *how to answer* (Stage B) — same pattern as domain alignment → task FT on finance docs. |
| **LPs** | Invent & Simplify, Deliver Results, Ownership |

**90s spoken:** **Qwen3-VL-8B** stock **0.618 / 0.402** → dual tower + curriculum → **0.905 / 0.452** (3ep).

---

## Anchor B — Eval / monitoring / gating

| | |
|---|---|
| **Problem** | Full TSRBench runs are expensive; headline accuracy hides slice regressions and parse failures. |
| **Insight** | Treat eval like a release gate — cheap sanity before north star; track **parse-miss** separately from accuracy. |
| **What I built** | Tiered eval gates (per checkpoint): **loss** (free) → **TSExam** (~35 s) → **176-item TSRBench slice** (~12 s) → **full TSRBench** (~3 min 0.8B / ~5 min 8B, 8-GPU parallel). Per-task/per-group accuracy; parse-miss logging; HF + local dataset parity. Promotion gates **−3 pp overall / −5 pp per task** (set before training). |
| **Parse-miss** | MCQ tasks expect a **single letter**; anything else (free text / empty) = format failure, not scored as wrong answer. Surfaced **NR** and **TSF** on TSRBench as mostly parse-miss while underlying reasoning was often correct — format inconsistency, not capability gap. |
| **Metrics** | **TR 26.9→21.9 (−5 pp)** on synth mix → **killed**; reas mean 29.5→31.2 (misleading alone); AR/IR **+7 pp** but gate tripped on TR. |
| **JD map** | Eval frameworks that **gate** model changes; slice by task; schema/format reliability before accuracy (→ doc type / entity in FinTech). |
| **Honest limit** | Synthetic TR path wrong lever; TR still open — task coverage audit next (Anchor C). |
| **Lesson** | More training mix ≠ better when task distribution shifts — stop and fix data generation. |
| **LPs** | Ownership, Earn Trust, Dive Deep, Have Backbone |

**90s spoken:** Gate expensive eval — loss → TSExam ~35 s → 176-item TSRBench slice ~12 s → full ~3–5 min. Parse-miss ≠ wrong answer (single-letter MCQ). TR synth → gates −3/−5 pp → **26.9→21.9** → killed despite AR/IR +7 pp.

---

## Anchor C — Ambiguity / Dive Deep (data + task diagnosis)

| | |
|---|---|
| **Problem** | Skipping Stage A left TSExam stuck at **~61.8%** (50+ IF configs); Stage B weak on TSRBench reasoning — perception strong, reasoning ~25% bracket. |
| **Insight** | Gaps were *missing operators/formats* in coverage, not volume alone — audit before stacking data. |
| **Stage A (low-label)** | No TS captions at start → LLaVA-style align. I adapted TSExam/ChatTS generators: **gold features → text** (no LLM; randomized templates). Added **CaTS** (Rose Yu group — expert-audited domains) for messy real-world signal. Mix → Stage A → TSExam **~90.5%** (recent 8B stack). |
| **Audit → fix** | Manual pass on all TSRBench reasoning tasks (AR, ER, NR, TR, …). **Three regimes:** (1) operator depth — segmentation, ordering, value extract, trend/seasonality; (2) domain knowledge — defer on 0.8B; (3) format/convention — e.g. **Goldstein scale** synthetics. Per-task TSExam generators for regimes 1+3. |
| **Metrics (0.8B prelim)** | vs `stageb-weak11k`: TSRBench **0.382→0.405 (+2.3 pp)**; reasoning **0.245→0.255 (+1.0 pp)** with new data + Stage C. 8B WIP. |
| **JD map** | Low-label synthetic + curated real captions; instrument tasks before scaling data. |
| **Honest limit** | Reasoning/TR/IR still hard; domain-knowledge regime open; Stage C early. |
| **Lesson** | When progress stalls, **instrument tasks** before adding data. |
| **LPs** | Dive Deep, Learn and Be Curious, Customer Obsession (exam/user coverage) |

**90s spoken:** No captions → IF-only stuck **61.8%** → synthetic feature captions + CaTS → Stage A → **~90.5%** TSExam. TR kill → task audit (operators · domain defer · formats) → targeted TSExam gens + Stage C → **+2.3 pp** overall / **+1.0 pp** reasoning on 0.8B (prelim).

---

## Quick numbers (memorize)

| Metric | Value |
|--------|-------|
| TSExam HF Q35 / 8B | 0.890 / 0.901 |
| TSRBench overall Q35 / 8B | 0.374 / 0.454 |
| TSRBench TR | ~29% (hard, in progress) |
| TSExam-numeric medAE | 0.14 |
| Caption attr-recovery | 0.72 |
| Configs / scripts | 162 / 125 |
| Eval gate latency | loss free · TSExam ~35 s · TSRBench slice 176 items ~12 s · full ~3 min (0.8B) / ~5 min (8B) |
| Stage A lift | IF-only TSExam **~61.8%** → post–Stage A **~90.5%** (8B recent) |
| Audit + Stage C (0.8B) | vs `stageb-weak11k`: overall **0.382→0.405** · reasoning **0.245→0.255** |

---

## FinTech one-liners (bridge any anchor)

| Research | FinTech |
|----------|---------|
| Dual chart + delay encoding | Tables + text + numbers — one view loses information |
| Stage A → B curriculum | Domain alignment → task FT on invoices / remittance |
| Tiered eval + parse-miss | Slice by doc type; schema reliability before accuracy |
| 0.8B ≈ 8B on TSExam | SLM routing when quality holds |
| Killed bad TR mixes | Don't cargo-cult data before shipping to finance users |
| Extended TSExam ops | Cover field extraction / segmentation primitives exams actually test |

---

## Supporting LP stories (not anchors)

| LP | Story | Status |
|----|-------|--------|
| Ownership | TR synth kill — [`stories/ownership_killed-tr-synthetic.md`](stories/ownership_killed-tr-synthetic.md) | Draft v2 DOC review |
| Deliver Results | VLM Anchor A — [`stories/deliver-results_dual-tower-curriculum.md`](stories/deliver-results_dual-tower-curriculum.md) | Qwen3-VL-8B → 3ep: 0.618→0.905, 0.402→0.452 |
| Invent & Simplify | ImagenTime — [`stories/invent-simplify_imagentime.md`](stories/invent-simplify_imagentime.md) | Draft v3 DOC L6 |
| Dive Deep | TSRBench reasoning audit — [`stories/dive-deep_tsrbench-reasoning-audit.md`](stories/dive-deep_tsrbench-reasoning-audit.md) | Draft v1; audit + Stage C: +2.3 pp overall / +1.0 pp reasoning (0.8B prelim) |
| Customer Obsession | **Gap** | Need stakeholder/user story |

---

## If Karan pulls a thread

| Question | Point to |
|----------|----------|
| "Walk me through architecture" | Anchor A — dual tower, Stage A/B |
| "How do you know it's ready to ship?" | Anchor B — tiered eval latencies, parse-miss, −3/−5 pp gates, TR kill |
| "What failed recently?" | Anchor B (TR mixes) + Anchor C (over-reasoning) |
| "Low labels / synthetic data?" | Anchor C — synthetic align + CaTS + quality caveats |
| "RL?" | GRPO warm-started from SFT, MCQ rewards; Stage C VRT planned |
| "Why Amazon / FinTech?" | Elevator pitch — precision, eval gates, peer scientists at scale |
