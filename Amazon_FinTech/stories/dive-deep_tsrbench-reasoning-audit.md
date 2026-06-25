# Dive Deep: TSRBench reasoning audit — three regimes, targeted coverage

**Leadership Principle:** Dive Deep  
**Project:** Time-series VLM — reasoning gap diagnosis (Anchor C)  
**Status:** Draft v1 — DOC L6  
**Target length:** ~800 words (body) · **~8 min spoken** (descriptive primary)

---

## Title

I audited every TSRBench reasoning task — and rebuilt training around three failure regimes instead of more data volume

## Outline

After operator-based synthetic data **regressed TR by five points** (see Ownership story), I stopped stacking buckets and **audited all reasoning tasks** on TSRBench. I classified gaps into **domain knowledge**, **operator depth**, and **task-specific formats** — then ran a two-track fix (ops + format conventions) that shows **~+5 pp** preliminary lift on **0.8B** with cleaner per-task error patterns.

## Ecosystem

At Ben-Gurion University I am **project lead** on a multimodal vision-language system for time-series reasoning — chart and delay-embedding inputs fused into one LLM that answers exam-style questions with text. Our north-star benchmark is **TSRBench**: thousands of problems across **perception, reasoning, forecasting, and decision-making** in fourteen domains including finance. Perception and headline scores had moved with the dual-tower stack (see Deliver Results); **reasoning** remained the weak bracket — roughly high twenties to low thirties percent while proprietary systems were stronger. I owned the diagnosis: which reasoning failures were fixable with training coverage versus which required domain knowledge a small model cannot carry.

## Issue

The obvious lever was more synthetic reasoning data. I had already mapped **seven or eight shared operators** — value extraction, segmentation, ordering, multi-hop layouts, trend and seasonality reads, and related primitives — that appeared across multiple TSRBench reasoning tasks. If I could generate exam-style examples for those operators at increasing difficulty, I expected a broad lift. I trained on that augmented mix and hit the **pre-declared gates** from our eval protocol: **temporal relations (TR) dropped more than five points** versus control. The reasoning average looked better on some slices; the target task got worse. I **did not ship** that mix (Ownership story) — but killing a bad recipe is not a diagnosis. The real question was *why* some tasks improved while TR regressed, and what we were actually missing across **numeric reasoning, entity reasoning, arithmetic reasoning, temporal relations**, and the rest of the reasoning bracket.

## Objectives

1. **Taxonomize failures:** Audit every reasoning task on TSRBench and classify gaps — not “add more data.”
2. **Step 1 — operator depth:** Extend synthetic coverage for the **seven–eight operators** already identified, with harder compositions.
3. **Step 2 — format and conventions:** Build synthetic data that teaches **task-specific formats** the model had never seen in TSExam (expected highest ROI).
4. **Step 3 — domain knowledge:** Incorporate domain context where a **0.8B** model can realistically absorb it; defer seismology-style background gaps.
5. **Validate on 0.8B first;** 8B runs in progress; per-task error analysis, not headline average alone.

## Actions

I spent several days on a **manual task audit** — read items task by task, tagged what operation the model had to perform, and compared error patterns to our training coverage in TSExam. That work split failures into **three regimes**.

**Regime 1 — missing domain knowledge:** Some tasks assume background the model does not have — seismology is a concrete example. A zero-point-eight-billion model will not reliably learn Richter-scale intuition from a few synthetic plots. I flagged these as **out of scope for Step 1–2** and reserved them for Step 3 or larger models.

**Regime 2 — operator depth:** Many tasks are compositions of primitives I had already named — simple segmentation and value reads scaling to harder multi-hop ordering. Failures here looked like **insufficient span and difficulty** in training, not missing perception. Our model already handled basic perception — extraction, segmentation, trend and seasonality reads — but stumbled when reasoning chains got longer.

**Regime 3 — unique formats and conventions:** Some tasks fail because the model does not know the **notation or scale** the question uses — for example the **Goldstein scale** in earthquake-intensity style items. That is not a bigger U-Net problem; it is a **coverage gap** — the format never appeared in training.

Before building more data, I wrote down what I believed was already solved: **perception-level time-series understanding** was largely in place from Stage A and TSExam perception slices. What remained was **reasoning composition, format literacy, and selective domain context** — not another blind multiplier on training volume.

I executed **Step 1 and Step 2** first because I expected format-and-convention coverage to be the best ROI — teach the model scales, labels, and answer templates it would see on TSRBench but not in our legacy exam mix. Step 1 deepened operator generators; Step 2 added synthetic items that introduced those missing formats explicitly. I held Step 3 for domains where a small model could not close the gap from data alone.

I trained the **0.8B** validation model on the new recipe and pulled **per-task** readouts the same way I had for the killed mix — so I could see whether we fixed the right failure modes.

## Results

**Preliminary (0.8B vs `stageb-weak11k` control):**

| Metric | Control (`reason-sbmix-weak11k`) | + audit data + Stage C | Δ |
|--------|----------------------------------|------------------------|---|
| TSRBench overall | **0.382** | **0.405** | **+2.3 pp** |
| TSRBench reasoning | **0.245** | **0.255** | **+1.0 pp** |

- **8B evaluation still running** — not claiming north-star promotion yet.
- **Per-task error analysis:** “Missing operation” failures dropped to a **minimum** on several slices; remaining errors look like **wrong reasoning on correctly parsed items** — closer to the control’s failure mode on hard items, not random format collapse.

**Diagnosis outcome (durable):**

- Three-regime taxonomy now drives what we generate — not “more reasoning bucket.”
- Step 2 (formats/conventions) prioritized over blind operator volume after the TR regression lesson.
- **Next:** widen span and coverage of the Step 1–2 generators; explore **Step 3** domain packs and **Stage C** gold-level **VRT** reinforcement where we have reliable labels.

## Learnings and Improvements

When progress stalls on a benchmark bracket, **instrument the tasks before adding data**. Headline reasoning average and bucket mixes hid a TR regression; the audit showed **three different failure types** that need **three different fixes**. Operator generators alone are not enough if the model has never seen the task’s format. I still treat **domain knowledge** as a separate lane — honest scope for model size matters. Same habit I would use on finance docs: slice errors by **field type, format, and domain** before scaling synthetic extraction.

---

## Interview notes

### Handoff from Ownership (one sentence only)

“I killed the first synthetic mix when TR regressed five points — this story is what I did next.”

### Three regimes (memorize)

1. Domain knowledge (seismology — defer on 0.8B)  
2. Operator depth (7–8 shared primitives, harder compositions)  
3. Format/convention (Goldstein scale — Step 2 ROI)

### IC proof

- Full TSRBench reasoning task audit (manual taxonomy).
- Seven–eight operator map shared across tasks.
- Step 1 operator generators + Step 2 format/convention synthetics.
- Per-task error tagging (missing-op vs reasoning error).

### Spoken script (~8 min)

I am project lead on a multimodal time-series reasoning project at Ben-Gurion University. We teach a vision-language model to answer exam-style questions about plots and delay-embedding views of time series — not just classify shapes. Our north-star benchmark is TSRBench: thousands of problems across perception, reasoning, forecasting, and decision-making, spanning fourteen domains including finance. By the time I focused this story, we had already lifted headline scores with the dual-tower architecture — TSExam and overall TSRBench moved on stock Qwen3-VL-8B. The bracket that was still weak was reasoning — high twenties to low thirties percent on the reasoning tasks, while stronger proprietary systems were ahead. I decided to concentrate there because that was where the north star would break or hold for real exam-grade use.

My first attempt was the natural one: I had identified seven or eight operators that kept showing up across reasoning tasks — value extraction, segmentation, ordering, multi-hop layouts over segments, trend and seasonality reads, and a few related primitives. The hypothesis was simple. If I generate synthetic exam-style data that exercises those operators at increasing difficulty, I should lift multiple tasks at once. I built that augmented reasoning mix and ran it through the same eval discipline we use for promotion — per-task tables, not just averages. The mix failed a hard gate: temporal relations dropped more than five points versus control. I killed that recipe — that is the Ownership story — but the Dive Deep question was what to do after the kill. A negative result without diagnosis would just send us to another blind bucket.

So I stopped generating and audited. I went through the reasoning tasks on TSRBench systematically — numeric reasoning, entity reasoning, arithmetic reasoning, temporal relations, and the rest of the bracket. I read the items, tagged the operation each one required, and compared that to what our TSExam training mix actually covered. That took several days, but it changed the plan. Failures were not one thing. They fell into three regimes.

First, missing domain knowledge. Some tasks assume background a small model will not pick up from a few synthetic charts — seismology is the example I use in interviews. You are not going to teach Richter-scale intuition to a zero-point-eight-billion model with a handful of plots. I marked those for a separate Step 3 or for larger models, not for operator spam.

Second, operator depth. A large share of tasks are compositions of the primitives I had already named — start with simple segmentation and value reads, scale to harder multi-hop ordering. Here the model was not missing perception. We already had decent value extraction, segmentation, and basic trend and seasonality reads from earlier curriculum work — caption alignment, CaTS, TSExam perception slices. It failed when the reasoning chain got longer or the composition got harder — a coverage span problem, not a vision problem. That is an important distinction I only got by reading errors item by item: the chart was often parsed correctly; the chain broke on step three or four.

Third, unique formats and conventions. Some items fail because the model has never seen the notation the question uses — the Goldstein scale in earthquake-intensity style tasks is the concrete example. The model might segment the series fine and still pick the wrong answer because it treats the scale as arbitrary numbers. That is not fixed by training a bigger custom stack. It is fixed by putting that format into synthetic training data explicitly — teach the convention, not just more plots. That was my bet for the best return on investment after the TR regression showed that operator volume alone can lift the wrong tasks.

From that taxonomy I split the work into three tracks. Step one: deepen the operator generators I already had — more span, harder compositions. Step two: synthetic data that introduces missing formats and conventions — scales, labels, answer templates that appear on TSRBench but not in our legacy exam mix. Step three: domain-specific knowledge where a small model can realistically absorb it. I executed step one and step two first because I expected format literacy to be the highest-ROI fix after the TR regression taught us that operator volume alone can help the wrong tasks.

I trained the zero-point-eight-billion validation model on the new recipe and evaluated the same way I had on the killed mix — per task, with error patterns tagged, not just accuracy. Results are still preliminary, but directionally encouraging. On zero-point-eight-B versus `stageb-weak11k` control I am seeing **plus two-point-three points** on TSRBench overall (**0.382 to 0.405**) and **plus one point** on the reasoning bracket (**0.245 to 0.255**). Eight-billion runs are still in progress — I am not claiming north-star promotion yet. What matters more at this stage is the per-task shape of errors. I tag whether a miss is a missing operation — the model never attempted the right primitive — versus a reasoning error on a parsed item. On several slices, missing-operation failures dropped to a minimum compared to control. Remaining errors look more like the model reasoning incorrectly on items it at least parsed — closer to the control’s failure mode on hard questions, not random format collapse. That is the signal I was diving for: we are finally training on the right gaps.

Next steps are to widen span and coverage in the step one and step two generators, then selectively pursue step three domain packs and Stage C gold-level VRT reinforcement where we have reliable labels. The durable outcome is not just the preliminary two-point-three overall lift — it is that we diagnose before we scale. When a benchmark bracket stalls, I instrument the tasks, classify the failure regime, and match the data fix to the gap. Operator buckets, format conventions, and domain knowledge are different levers. Same discipline I would use on payment or filing extraction: do not cargo-cult volume until you know whether the miss is format, field coverage, or domain context.

### Short version (~90 sec)

Reasoning weak on TSRBench. Operator-based synthetic mix regressed TR five points — killed. I audited every reasoning task; three regimes: domain knowledge, operator depth, format/convention. Step 1 deepened operators; Step 2 added missing formats like Goldstein scale. Preliminary **+2.3 pp** overall / **+1.0 pp** reasoning on 0.8B vs `stageb-weak11k`; 8B WIP. Per-task misses from missing ops near zero; errors now look like reasoning, not format collapse. Lesson: instrument tasks before scaling data.

### Likely follow-ups

- Examples of the seven–eight operators?
- Why Step 2 over Step 3 first?
- Goldstein scale — what did you generate?
- How is this different from the Ownership kill?
- 8B results when ready?

### Weak spots / facts to verify

- [x] Exact reasoning bracket before/after (0.8B): **0.245→0.255 (+1.0 pp)**; overall **0.382→0.405 (+2.3 pp)** vs `stageb-weak11k`.
- [ ] Which tasks moved most in preliminary per-task table?
- [ ] Goldstein scale — correct task/domain label on TSRBench?
- [ ] Step 3 domain packs — any started or still planned?
- [ ] 8B results when ready?

### FinTech bridge (only if asked)

Slice audit by field type, format convention, and domain — same as TSRBench reasoning taxonomy before scaling synthetic extraction on invoices.

### Related stories

- **Ownership:** TR kill and gates — one-sentence handoff only.
- **Deliver Results:** architecture and headline lifts — do not re-explain dual tower.
- **Learn and Be Curious:** optional alt on same arc (pivot after negative result).
