# Apple Health virtual on-site — 4-day final practice

**Status:** Second cycle. Live **Tue 2026-09-08**.  
**Do not** restart [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md) Block A–D. Foundations are done.  
**Hub still owns:** hard rules, people map, invite. **This file owns:** Fri 9/4 → Mon 9/7.

| Day | Date | Focus | Hours | Materials |
|-----|------|-------|-------|-----------|
| Fri | 9/4 | Deepen risk: Chung-Cheng + Haraldur + coding #7 | 5–6 | [`2026-09-04_chung-cheng-advanced.md`](2026-09-04_chung-cheng-advanced.md) · [`2026-09-04_haraldur-advanced.md`](2026-09-04_haraldur-advanced.md) · [`coding/07_merge_intervals.py`](coding/07_merge_intervals.py) |
| Sat | 9/5 | Whole-system: Vincent + Yujie + coding #8 | 5–6 | Vincent sheet for the *framework only* · Yujie sheet Module 3–4 · [`coding/08_topk_window.py`](coding/08_topk_window.py) |
| Sun | 9/6 | Jonathan defense + mixed mock + backup cards | 4.5–5.5 | Jonathan sheet + [`2026-09-01_onsite-jonathan-research-rigor.md`](2026-09-01_onsite-jonathan-research-rigor.md) Q5 · stories |
| Mon | 9/7 | Retrieval + mini-loop + stop | **≤4** | Headings only. No new concepts. |

---

## Goal

Transfer, not recall.

Interviewer changes one assumption → you notice what changes downstream.

Not “what is FSDP?” → “FSDP fitted the model, throughput dropped 40%. Why?”  
Not “how do you evaluate a wearable classifier?” → “AUROC up, PPV collapsed, older subgroup has 18 positives. What do you conclude?”

---

## Adjustments (do not skip)

The plan as written is the right second cycle. Four changes from this week’s artifacts:

1. **Do not continue first-cycle Vincent Blocks 1–9.** Thu 9/3 already started that sheet. Saturday Case #1 is a *new* cardiac-detection design with constraint injection. Keep the framework (objective → … → monitoring). Keep the Thu locks (near-chance does not license a bigger model; n=20 is uncertainty not shift). Do not restudy the sheet.

2. **Friday Chung-Cheng Q3 is the 9/1 miss, on purpose.** Global batch / fewer optimizer steps at fixed tokens. Speak it under a new wrapping. Do not reread the 9/1 writeup first.

3. **Sunday Jonathan Block 3 is the other 9/1 miss.** Researcher degrees of freedom / “how do I know you aren’t hill-climbing?” Speak it. Do not pretend every hypothesis was pre-registered.

4. **Monday is also the TS-VLM community talk** ([`talks/ts-vlm/`](../../../talks/ts-vlm/)). Do not do a full Apple day *and* a talk rewrite. If the talk happens: Apple mini-loop in the morning, then talk, then **stop**. If it can move, move it. Five sessions Tuesday; energy is the scarce resource.

---

## What changes vs first cycle

| First cycle | This cycle |
|-------------|------------|
| Learn concepts, build frameworks, standard questions | One assumption changes; trace the downstream |
| Chung-Cheng A1–A7 definitions | Diagnose stalls, topology, same-tokens ≠ same trajectory |
| Haraldur metrics / PPV primer | Labels, selection, decision utility |
| Vincent 6-month FM script then whole-system sheet | Constraint injection on a live design; do not restart |
| Jonathan claim–evidence | Hostile alternatives + hill-climbing answer |
| 6 coding primitives | +2 (intervals, streaming top-k). Stop. |

**Still true:** no paper recaps, no name-drop, no matplotlib-on-PPG, IC verbs, no PI/student stories as the plot.

---

## Interview map (unchanged)

| Person | Dimension | Risk |
|--------|-----------|------|
| Chung-Cheng | LLM training & infrastructure | **1 — highest** |
| Haraldur | Health domain & applied ML judgment | **2** |
| Vincent | Technical leadership & system thinking | **3** |
| Jonathan | Research depth & scientific rigor | **4** |
| Yujie | Multimodal architecture & time-series encoding | **5 — strongest; edge cases only** |

Do not spend four days only on 1–2. By Sunday/Monday the work is mixed mocks, context switching, retrieval, communication.

---

## Answer shape (every technical question)

1. Identify the likely bottleneck / failure class  
2. Name competing explanations  
3. Propose a measurement that discriminates  
4. Intervene on the measured thing  
5. State the new tradeoff  

If you skip to a tool name, interrupt yourself.

---

## Friday 9/4 — deepen the two biggest risks (~5–6 h)

| Block | Min | Do |
|-------|-----|-----|
| 1 Chung-Cheng advanced | 75 | Open [`2026-09-04_chung-cheng-advanced.md`](2026-09-04_chung-cheng-advanced.md) **Learning**. Do **not** reread DDP/FSDP definitions or the 30-min review. |
| 2 Chung-Cheng hard mock | 45 | Same file, **Mock**. 5 questions. Speak. Then keys. |
| Break | 20–30 | |
| 3 Haraldur advanced | 60 | [`2026-09-04_haraldur-advanced.md`](2026-09-04_haraldur-advanced.md) **Learning**. Skip Lesson 1 metrics. |
| 4 Haraldur cases | 45 | Same file, **Cases**. 4 integrated. |
| 5 Coding #7 | 45–60 | [`coding/07_merge_intervals.py`](coding/07_merge_intervals.py) from blank. Talk aloud. |

**Do not:** open [`2026-09-01_onsite-chung-cheng-challenging-practice.md`](2026-09-01_onsite-chung-cheng-challenging-practice.md) before the mock. **Do not:** reread Haraldur Lesson 1.

---

## Saturday 9/5 — system design (~5–6 h)

| Block | Min | Do |
|-------|-----|-----|
| 1 Vincent Case #1 | 60 | Cardiac early-detection, **broad population**. Framework: objective → population → data → labels → baseline → model → eval → deploy → monitor. Inject one constraint every 5–10 min. **Modify, do not restart.** |
| 2 Vincent Case #2 | 45 | Fixed annual compute/data budget. Choose among 4× model, 4× data, higher sensor rate, new modality, better labels. Marginal value. |
| 3 Vincent leadership | 35 | Cards 1, 4, 3, 5. Compression. “What did YOU do?” Do not rewrite stories. |
| Break | 20–30 | |
| 4 Yujie architecture | 60 | PPG 128 / IMU 50 / HR 1 / sleep events / occasional text / workout audio. Then inject A–H. Each change: information → tokens → alignment → fusion → training → evidence. |
| 5 Yujie ablation | 40 | “How do you know?” Matched token budget, shuffle, corrupt, missingness curves. |
| 6 Coding #8 | 30 | [`coding/08_topk_window.py`](coding/08_topk_window.py) from blank. |

### Saturday Case #1 injections (in order)

1. BMI-related performance gap.  
2. Gestures resemble pathological patterns.  
3. Legal/privacy blocks one linked dataset.  
4. XGBoost within 1.5 points of the deep model.  
5. Multimodal helps average, hurts one subgroup.  
6. Deployment latency too high.  
7. New device generation changes the signal.

### Saturday Case #2 force

Scaling curves, simple probes, deployment cost, legal/data constraints. Say what you measure *before* you spend the 4×.

### Yujie injections (A–H)

Audio dominates tokens · PPG short transients · async clocks · modality drop · missingness informative · new sampling rates at deploy · one modality dominates xattn · sensor-encoder pretrain does not transfer.

**Do not** open Yujie Module 1 encoding menu. That is first-cycle.

Run Saturday mocks in-session (`/follow-up-mock` Vincent then Yujie) rather than reading a key.

---

## Sunday 9/6 — rigor + context switch (~4.5–5.5 h)

| Block | Min | Do |
|-------|-----|-----|
| 1 ImagenFew defense | 60 | **Three claims only.** Each: claim → evidence → alternative → discriminating experiment → limitation. Then attack. |
| 2 Multimodal defense | 60 | Delay vs chart, dual-tower, DINO vs Qwen, adaptation budget. Falsify the preferred explanation. |
| 3 Degrees of freedom | 30 | **Speak the 9/1 miss.** “How do I know you aren’t benchmark hill-climbing?” Exploratory vs confirmatory. Held-out confirmation. Kill criteria. Negative results. Do not fake pre-registration. |
| Break | 20 | |
| 4 Mixed interviewer | 60 | Do **not** know who it is. One question at a time. Infer the dimension. Five sessions Tuesday are the same day. |
| 5 Behavioral maintenance | 30 | Cards 1–5, one minute each, then a random follow-up. Backup A/B if pulled. |

### Three ImagenFew claims (do not add a fourth)

1. Image-space formulation is effective under data scarcity.  
2. Representation choice matters *within* image-space modeling.  
3. The advantage persists across scarcity regimes / sequence lengths / datasets.

Attack: compute, architecture, sampling, leakage, where it stops generalizing.

### Mixed-mock example sequence (reorder on the day)

1. 8B regresses after scaling to 64 GPUs.  
2. Health model AUROC 0.95, PPV 0.08.  
3. Why should I believe the second modality adds information?  
4. Best architecture is too expensive to deploy.  
5. Bosch: your benchmark does not resemble production data.

---

## Monday 9/7 — retrieval, then stop (≤4 h)

This is **not** a learning day.

| Block | Min | Do |
|-------|-----|-----|
| 1 Five-interviewer retrieval | 45 | No notes. Write the headings below. ~8 min each. Then check notes **only** for holes. |
| 2 Mini-loop | 2 h | 5 × ~20 min + 5-min breaks. **Random order.** One main Q + 2–3 follow-ups. Stop. |
| 3 Behavioral rapid fire | 30 | Hear the prompt, *then* pick the story. Tests selection, not memorization. |
| 4 Weakness patch | 30 | Only what failed in the mini-loop. No new concepts. |
| Stop | — | Computer, Webex, charger, water, food, quiet room. No evening cram. |

### Retrieval headings (write from memory)

| Person | Headings |
|--------|----------|
| Chung-Cheng | memory · distributed · scaling · training failures · multimodal efficiency |
| Yujie | information · tokens · alignment · fusion · training · evidence |
| Jonathan | claim · evidence · alternative · experiment · limitation |
| Vincent | objective · population · data · baseline · model · evaluation · deployment · teamwork |
| Haraldur | decision · metrics · calibration · evaluation · uncertainty · deployment |

Example mini-loop order (shuffle): Haraldur → Chung-Cheng → Vincent → Jonathan → Yujie.

---

## Behavioral

Five cards are enough: [`2026-08-30_behavioral-stories.md`](2026-08-30_behavioral-stories.md).

Two **60-second backups** added to that file (not full 90s docs):

- **A** Mentorship / helping someone succeed — technical unblock, they keep ownership. **Not** “I supervised my student.”  
- **B** Deadline / execution under pressure — prioritization, what you cut, quality bar.

Sunday: speak A and B once. Monday rapid fire may pull them.

---

## Coding

| # | Problem | When |
|---|---------|------|
| 1–6 | Already done | Do not redo unless a mock fails |
| 7 | Interval / event merging | **Friday** |
| 8 | Streaming top-k in a time window | **Saturday** |
| LRU | Optional only if 7/8 feel shaky | Skip by default |

Talk while coding. Edge cases. Complexity. Stop adding problems.

---

## What not to do

- Read more papers cover-to-cover  
- Learn obscure transformer variants  
- Add a new story set  
- Memorize Apple policy  
- Pretend clinical facts  
- Grind generic LeetCode  
- Rewrite strong stories  
- Run full five-hour loops every day  
- Continue Vincent sheet Blocks 1–9  
- Reread Chung-Cheng A1–A7 or Haraldur Lesson 1  

---

## Monday-night target

| Person | Target state |
|--------|----------------|
| Chung-Cheng | Diagnose systems problems without throwing technology names |
| Yujie | Design a multimodal temporal architecture from first principles and defend every tradeoff |
| Jonathan | Know exactly what the evidence establishes and where the claim stops |
| Vincent | Reason across population, data, model, eval, deploy, and cross-functional constraints, and still go deep |
| Haraldur | Turn a metric into a judgment: valid, useful, deployable? |
| Behavioral | Five strong + two backups; choose without sounding rehearsed |
| Coding | Sequence/data-structure primitives, narrated |

Do not try to out-know every interviewer. Robust expertise: understand the problem, name the uncertainty, reason from first principles, make the tradeoff explicit, design the next experiment, speak clearly.
