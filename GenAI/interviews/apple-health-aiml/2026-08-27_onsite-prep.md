# Prep — Apple Health AIML virtual on-site (hub)

**Status:** Active. Live **Tue 2026-09-08** (Jonathan 11:05 → Yujie 1:05 → Chung-Cheng 2:05 → Haraldur 3:05 → Vincent 4:05). Same five. **Jaya dropped.** Rescheduled 2026-09-02 (sick).  
**This week:** [`2026-09-03_four-day-final-plan.md`](2026-09-03_four-day-final-plan.md) (second cycle — transfer, not recall).  
**Invite:** [`2026-08-26_virtual-onsite-invite.md`](2026-08-26_virtual-onsite-invite.md) (updated 2026-09-02)

**Biggest adjustment:** less LLaVA/Flamingo review, more **wearable tokens + infra diagnosis**. Screen already covered attn, KV cache, concat vs xattn.

**Goal:** own a run, bake off representations on *their* signals, kill what fails, impose 3-month slices. IC verbs.

---

## Sheets (practice these, not Tyler’s theme list)

| When | Person | Sheet |
|------|--------|--------|
| Tue 11:05 | **Jonathan Bourim** | [`2026-08-27_onsite-jonathan.md`](2026-08-27_onsite-jonathan.md) — **opens**. Primary map: **research depth + rigor**; small pad contingency. Tue 9/1 mock: [`2026-09-01_onsite-jonathan-research-rigor.md`](2026-09-01_onsite-jonathan-research-rigor.md) (Q5 missed: degrees of freedom) |
| Tue 1:05 | **Yujie Li** | [`2026-08-27_onsite-yujie.md`](2026-08-27_onsite-yujie.md) — four modules: encode TS → multimodal arch → clocks → diagnose / bakeoff. Second cycle: [`2026-09-05_yujie-advanced.md`](2026-09-05_yujie-advanced.md). Fri 9/4 mock: [`2026-09-04_onsite-second-cycle-mocks.md`](2026-09-04_onsite-second-cycle-mocks.md) |
| Tue 2:05 | **Chung-Cheng Chiu** | [`2026-08-27_onsite-chung-cheng.md`](2026-08-27_onsite-chung-cheng.md) — parallelism + profiling. **Largest study delta**. Tue 9/1 30-min: [`2026-09-01_onsite-chung-cheng-training-infra.md`](2026-09-01_onsite-chung-cheng-training-infra.md) · challenging mock: [`2026-09-01_onsite-chung-cheng-challenging-practice.md`](2026-09-01_onsite-chung-cheng-challenging-practice.md) (Q5 missed: global batch) |
| Tue 3:05 | **Haraldur Hallgrímsson** | [`2026-08-27_onsite-haraldur.md`](2026-08-27_onsite-haraldur.md) — most Apple-Health-specific. **Do not assume DL wins**. Fri 9/4 Lesson 1 mock: [`2026-09-04_onsite-second-cycle-mocks.md`](2026-09-04_onsite-second-cycle-mocks.md) |
| Tue 4:05 | **Vincent Chan** | [`2026-08-27_onsite-vincent.md`](2026-08-27_onsite-vincent.md) — **practice day** (Blocks 0–9). Mock log (in progress): [`2026-09-03_onsite-vincent-practice.md`](2026-09-03_onsite-vincent-practice.md) — Block 0 spoken. Last of five. Stories: [`2026-08-30_behavioral-stories.md`](2026-08-30_behavioral-stories.md) |

**Jaya** was Fri 10:05 — **dropped**. No prep sheet.

First two minutes override the map. After lunch, **15 min** between Yujie / Chung-Cheng / Haraldur / Vincent — no new material in those gaps. Eat 11:50–1:05.

---

## Calendar

Bosch is **done**. Do not mix Sunnyvale scripts.

**Second cycle (this week):** [`2026-09-03_four-day-final-plan.md`](2026-09-03_four-day-final-plan.md). Do **not** restart first-cycle Block A–D.

| When | Block | Hours |
|------|-------|-------|
| **Fri 9/4** | Chung-Cheng + Haraldur advanced + coding #7 | 5–6. [`chung-cheng`](2026-09-04_chung-cheng-advanced.md) · [`haraldur`](2026-09-04_haraldur-advanced.md) · [`coding/07_merge_intervals.py`](coding/07_merge_intervals.py). **Mock log:** [`2026-09-04_onsite-second-cycle-mocks.md`](2026-09-04_onsite-second-cycle-mocks.md) |
| **Sat 9/5** | Vincent constraint-injection + Yujie edge cases + coding #8 | 5–6. [`yujie advanced`](2026-09-05_yujie-advanced.md). Do **not** continue Vincent sheet Blocks 1–9 |
| **Sun 9/6** | Jonathan 3-claim defense + mixed mock + stories A/B | 4.5–5.5. Speak the 9/1 degrees-of-freedom miss |
| **Mon 9/7** | Retrieval + mini-loop + **stop** | **≤4**. Also TS-VLM community talk — do not full-cram both |
| **Tue 9/8** | **LIVE** 11:05 / 1:05 / 2:05 / 3:05 / 4:05 | Join after 10:55, 12:55, 1:55, 2:55, 3:55. Eat in the **lunch** gap (11:50–1:05) |

**Compress:** leftover Q5s are inside Friday Q3 (global batch) and Sunday Block 3 (hill-climbing). Do not reread the 9/1 writeups first.

**Effort this cycle:** Chung-Cheng + Haraldur Fri · Vincent + Yujie Sat · Jonathan + mixed Sun · retrieval Mon.

Skip unless a mock fails: RoPE derivation, RMSNorm, FlashAttention internals, RelCon cover-to-cover, LeetCode.

**Coding contingency** (do not replace person mocks): [`coding/`](coding/) — 8 primitives. Open the problem file only; `*_solution.py` after. #7 Fri, #8 Sat. Not LeetCode.

**Abstracts only** (method-level; no recap on loop): [`papers/README.md`](papers/README.md) + [Beyond Sensor Data](https://machinelearning.apple.com/research/beyond-sensor). Cultural signal: this team will use **SSL FMs and GBDT** when the latter is more robust.

---

## Hard rules

| Skip | Why |
|------|-----|
| “What is gradient checkpointing?” as the whole answer | Chung-Cheng wants diagnosis order |
| Transformer + multimodal LLM as first sentence to Haraldur | He published GBDT > deep TS under missingness shift |
| Matplotlib on PPG / force VLM images | Yujie: behavioral tokens + native clocks |
| Name-drop RelCon, WBM, periodicity, AXLearn, hypertension posts | Quiz |
| PI / students / impact at scale | HM + prior loops |
| Treat Jonathan as Jaya | Jaya **dropped**. Tue 11:05 is Jonathan |
| Email interviewers | Tyler owns process |

---

## How to practice

**This week:** follow [`2026-09-03_four-day-final-plan.md`](2026-09-03_four-day-final-plan.md). Teach only the day’s **new** failure modes, then mock.

**Fri:** open [`2026-09-04_chung-cheng-advanced.md`](2026-09-04_chung-cheng-advanced.md) Learning → Mock, then Haraldur advanced, then coding #7. Do not open A1–A7.

**Before Tue 9/8:** Friday mock Q3 *is* the global-batch miss; Sunday Block 3 *is* degrees of freedom. Speak them in those slots. Reason, do not recap tool names.

---

## After live day

Tue night: `2026-09-08_onsite-debrief.md`.

## Hand-off

```
@GenAI/interviews/apple-health-aiml/2026-09-03_four-day-final-plan.md
Second cycle. Next = Friday Block 1: 2026-09-04_chung-cheng-advanced.md Learning (75 min). Do not reread A1–A7 or Vincent Blocks 1–9.
```
