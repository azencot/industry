# Ownership: Killed synthetic TR mix — per-task gates before promote

**Leadership Principle:** Ownership  
**Project:** Time-series VLM — TSRBench reasoning gap (Anchor B)  
**Status:** Draft v2 — DOC L6 (post AI review)  
**Target length:** ~750 words (body) · **~8 min spoken** (descriptive primary) · table for prep only

---

## Title

I set slice-level promotion gates — and killed a mix when the target task regressed exactly five points

## Outline

Our benchmark had plateaued near **46%** while **reasoning** sat near **29%**. I targeted **temporal relations**, built tiered synthetic exam data, and set **−3 pp overall / −5 pp per-task** gates **before** training — then **killed** the recipe when **TR fell 26.9% → 21.9%** despite a better reasoning average and **+7 pp** wins on other tasks.

## Ecosystem

At Ben-Gurion University I lead the **evaluation and training-direction** workstream on a time-series **vision-language** reasoning project. My formal goal was to improve reasoning scores on **TSRBench**; I also took responsibility for **promotion criteria** because the lab had no reliable way to stop slice regressions from hiding inside average gains. The team included me, a student who ran larger **8B** training jobs from my recipe, and lab members who used my readouts to decide which recipes earned the next **GPU** cycle. I recommend what ships, what dies, and what needs more study before we spend eight-GPU weeks again.

## Issue

Overall **TSRBench** had **plateaued near ~46%**. Proprietary systems sit in a **46–55%** band with a much stronger **reasoning** category — we were near **29%** on reasoning tasks. The risk was not “we need more data.” The risk was promoting a recipe because the **average** moved while the **target slice** got worse — wasting the next GPU cycle and eroding trust in our eval process. I manually reviewed reasoning items and chose **temporal relations (TR)**: weak scores, but the operations looked addressable — **segmentation**, **ordering**, **multi-hop** layouts over many segments.

## Objectives

**Goal:** Improve reasoning starting with **TR**, using tiered synthetic training examples (simple seg/ordering → complex multi-hop), not another blind data bucket.

**Guardrails (set before training):**

- **−3 pp** on **TSRBench overall** vs current best → do not promote.
- **−5 pp** on **any reasoning subtask** → do not promote.

**Execution:** I train **0.8B** validation; student runs **8B** on my recipe; **I** own the per-task readout and promote/kill recommendation.

## Actions

I designed two phases of **synthetic exam-style** data: phase one taught basic **segmentation and ordering**; phase two added **multiple hops** and ordering across **eight or more segments**. I wrote the failure gates **before** anyone launched the large run so we could not talk ourselves into a bad promote afterward.

I trained the **0.8B** model myself, then had a student run **8B** using my exact data recipe. I remained accountable for evaluation. I added a **per-task reasoning table** to the promotion readout — overall score and reasoning average were no longer enough to approve a mix.

The difficult part came after eval. The **reasoning average** rose **29.5% → 31.2%**. Two tasks gained about **seven points** each — the kind of headline that makes a recipe look ready for the next cycle, especially after **8B** GPU time was already spent. In lab review, that aggregate could have passed as progress. But **TR** — the task we designed the data for — dropped **26.9% → 21.9%**, **minus five points exactly**, hitting the gate I had set. **Numeric reasoning** also fell **3.4 points**. I recommended **against promotion** and stopped this synthetic path so we would not spend another large run on a recipe that had already damaged the target behavior.

## Results

**Prep table (do not read aloud in interview):**

| Task | Control | + synth | Δ (pp) |
|------|---------|---------|--------|
| reas avg | 29.5 | 31.2 | +1.7 |
| **TR** | **26.9** | **21.9** | **−5.0** |
| NR | 35.2 | 31.8 | −3.4 |
| AR / IR | — | — | +7.3 / +7.0 |

**Spoken summary:** Reasoning average **+1.8 pp**; two tasks **~+7 pp**; **TR −5.0 pp** (gate fired); **NR −3.4 pp**.

- Mix **not promoted** — avoided committing the **next GPU cycle** to a failing recipe.
- I updated the lab’s evaluation template: every reasoning experiment now reports **overall, reasoning average, and each subtask** against **pre-declared gates** — not aggregate movement alone.
- **TR remains open**; this synthetic lever was wrong, not the ambition. Deeper task-coverage work followed (separate Dive Deep story).

## Learnings and Improvements

Define **slice-level floors before training** and treat a **target-task regression** as a failed experiment even when the average improves. Targeted synthetic data can boost unrelated tasks while hurting the slice you aimed at — that is distribution shift. The durable outcome was the **promotion process**, not a TR win on this run.

---

## Interview notes

### Role & accountability (say early if probed)

Formal: improve VLM reasoning on TSRBench. I also owned promotion criteria and kill recommendations. Student ran 8B; I ran 0.8B and the per-task eval.

### Kill gate (memorize)

**TR 26.9 → 21.9 (−5.0 pp)**. Reasoning avg +1.8 pp + AR/IR ~+7 pp = **still kill**.

### IC proof

- Pre-declared gates (−3 / −5 pp).
- Per-task promotion table (lab template).
- Tiered synthetic generators; kill recommendation in lab review.

### Spoken script (~8 min) — **use this in interview**

At Ben-Gurion University I lead the evaluation and training-direction workstream on a time-series vision-language reasoning project. My formal assignment was to improve reasoning scores on TSRBench — a multi-task benchmark that spans perception, forecasting, decision-making, and reasoning across thousands of problems. But I also took on something the lab had not formalized: promotion criteria. We had been making GPU-heavy training decisions from headline benchmark movement, and I had seen how an average score could tick up while an important slice got worse. So I made myself accountable not just for running experiments, but for recommending what ships, what dies, and what needs deeper study before we commit another eight-GPU week.

When I looked at where we stood, the picture was clear but uncomfortable. Overall TSRBench had plateaued near forty-six percent on our best dual-tower stack — competitive on perception and forecasting in places, but not where proprietary systems were pulling ahead. Proprietary VLMs sat in a forty-six to fifty-five percent band, and they were meaningfully stronger in the reasoning category — where we were only around twenty-nine percent on the reasoning bracket average. That gap was the bottleneck, not raw perception. I had already delivered headline lifts on TSExam and overall TSRBench in the architecture story; this chapter was specifically about whether we could close reasoning without breaking the evaluation discipline that got us there.

The failure mode I cared about was not “we need more data.” It was promoting a recipe because the reasoning average moved, or because two unrelated tasks jumped, while the slice we had actually targeted regressed. That would waste the next GPU cycle — an eight-GPU week is not a free experiment in our lab — and teach stakeholders to trust the wrong signal in the weekly readout.

I did not pick the target task from a spreadsheet. I manually reviewed reasoning items on the benchmark — read the questions, traced what operation the model had to perform, and compared error patterns across subtasks. I chose temporal relations — TR — as the first lever. TR was weak, around twenty-seven percent on our control model, but when I read the items, the underlying operations looked bridgeable: find segments in a time series, put them in order, handle multi-hop layouts where you reason across eight or more segments. Numeric reasoning and interval reasoning were also weak, but TR had the clearest path through synthetic exam-style data. That was a hypothesis I could test with a tiered generator rather than another blind data bucket.

Before anyone launched a large run, I wrote two guardrails into the experiment plan. No more than a three-point drop on overall TSRBench versus our current best — do not promote. No more than a five-point drop on any individual reasoning subtask — do not promote. I designed the synthetic data in two phases on purpose. Phase one taught basic segmentation and ordering with simpler exam-style examples. Phase two added multiple hops and ordering across longer segment chains. The idea was tiered curriculum, not dumping synthetic volume and hoping the average moved.

I trained the smaller zero-point-eight-billion validation model myself. That let me iterate quickly on the data recipe before we spent real GPU budget. Then I had a student run the eight-billion model using my exact recipe — same phases, same mix — and I remained accountable for the evaluation readout and the promote-or-kill recommendation. I also changed what “evaluation” meant for this line of work. I added a per-task reasoning table to the promotion artifact. Overall TSRBench and the reasoning average were still reported, but they were no longer sufficient to approve a mix.

When results came back, the headline numbers looked like progress — and that is exactly why the gates mattered. The reasoning average improved from twenty-nine-point-five to thirty-one-point-two percent. Two tasks — arithmetic reasoning and interval reasoning — jumped about seven percentage points each. After an eight-billion run that had already consumed GPU time, that is an easy story for a lab update: average up, big wins on two slices, ready for the next cycle.

But TR — the task we had designed the synthetic data for — went from twenty-six-point-nine to twenty-one-point-nine. Minus five points exactly. That fired the gate I had written before training, not after. Numeric reasoning also fell three-point-four points. In lab review, I recommended against promotion. The difficult part was not the arithmetic. It was that without the per-task table, the average gain and the seven-point wins on AR and IR would likely have made this mix look viable for another large run. We would have spent more GPU time reinforcing a recipe that had already damaged the behavior we were trying to fix.

The mix was not promoted. That avoided committing the next GPU cycle to a failing path. More durably, I updated the lab’s evaluation template so every later reasoning experiment reports overall score, reasoning average, and each subtask against those pre-declared floors — not aggregate movement alone. TR remains an open problem; this synthetic lever was wrong, not the ambition. We redirected to deeper task-coverage analysis, which is a separate story.

The lesson I took forward is direct: define slice-level floors before training, and treat a target-task regression as a failed experiment even when the average improves. Targeted synthetic data can boost unrelated tasks — arithmetic and interval reasoning in this run — while hurting the slice you aimed at. That is distribution shift in practice, not a mysterious benchmark quirk. The durable outcome was the promotion process, not a TR win on this run. Temporal relations stayed on the roadmap, but with a different diagnosis: we needed task coverage and alignment analysis, not more of the same synthetic recipe.

### Short version (~90 sec)

Benchmark ~46%, reasoning ~29%. I targeted TR, set −3/−5 pp gates before training, built tiered synthetic data. TR went 26.9 → 21.9 (−5 pp); average and two tasks looked better. I killed promotion, saved the next GPU cycle, made per-task gates the lab default.

### Likely follow-ups

- Why kill if average went up?
- Pressure to promote after 8B spend?
- What happened next? → Anchor C coverage audit (brief pointer only)
- Student vs your role?

### Weak spots / facts to verify

- [ ] “Updated lab template” — confirm adoption wording (every later experiment vs most).
- [ ] 8B vs 0.8B — same TR regression on both?

### FinTech bridge (only if asked)

Per-slice floors before promote — same as not shipping when one doc-type metric drops five points.

### Related stories

- **Deliver Results:** architecture + 0.618→0.905 — don’t repeat here.
- **Dive Deep:** post-mortem task audit — [`dive-deep_tsrbench-reasoning-audit.md`](dive-deep_tsrbench-reasoning-audit.md).
