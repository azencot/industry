# Prep — Apple Health AIML virtual on-site (hub)

**Status:** Active. Live **Tue 2026-09-08** (Jonathan 11:05 → Yujie 1:05 → Chung-Cheng 2:05 → Haraldur 3:05 → Vincent 4:05). Same five. **Jaya dropped.** Rescheduled 2026-09-02 (sick).  
**Invite:** [`2026-08-26_virtual-onsite-invite.md`](2026-08-26_virtual-onsite-invite.md) (updated 2026-09-02)

**Biggest adjustment:** less LLaVA/Flamingo review, more **wearable tokens + infra diagnosis**. Screen already covered attn, KV cache, concat vs xattn.

**Goal:** own a run, bake off representations on *their* signals, kill what fails, impose 3-month slices. IC verbs.

---

## Sheets (practice these, not Tyler’s theme list)

| When | Person | Sheet |
|------|--------|--------|
| Tue 11:05 | **Jonathan Bourim** | [`2026-08-27_onsite-jonathan.md`](2026-08-27_onsite-jonathan.md) — **opens**. Primary map: **research depth + rigor**; small pad contingency. Tue 9/1 mock: [`2026-09-01_onsite-jonathan-research-rigor.md`](2026-09-01_onsite-jonathan-research-rigor.md) (Q5 missed: degrees of freedom) |
| Tue 1:05 | **Yujie Li** | [`2026-08-27_onsite-yujie.md`](2026-08-27_onsite-yujie.md) — four modules: encode TS → multimodal arch → clocks → diagnose / bakeoff |
| Tue 2:05 | **Chung-Cheng Chiu** | [`2026-08-27_onsite-chung-cheng.md`](2026-08-27_onsite-chung-cheng.md) — parallelism + profiling. **Largest study delta**. Tue 9/1 30-min: [`2026-09-01_onsite-chung-cheng-training-infra.md`](2026-09-01_onsite-chung-cheng-training-infra.md) · challenging mock: [`2026-09-01_onsite-chung-cheng-challenging-practice.md`](2026-09-01_onsite-chung-cheng-challenging-practice.md) (Q5 missed: global batch) |
| Tue 3:05 | **Haraldur Hallgrímsson** | [`2026-08-27_onsite-haraldur.md`](2026-08-27_onsite-haraldur.md) — most Apple-Health-specific. **Do not assume DL wins** |
| Tue 4:05 | **Vincent Chan** | [`2026-08-27_onsite-vincent.md`](2026-08-27_onsite-vincent.md) — 6-month program, discriminating experiments. Last of five. Stories: [`2026-08-30_behavioral-stories.md`](2026-08-30_behavioral-stories.md) |

**Jaya** was Fri 10:05 — **dropped**. No prep sheet.

First two minutes override the map. After lunch, **15 min** between Yujie / Chung-Cheng / Haraldur / Vincent — no new material in those gaps. Eat 11:50–1:05.

---

## Calendar

Bosch is **done**. Do not mix Sunnyvale scripts.

| When | Block | Hours |
|------|-------|-------|
| **Thu PM** (if energy) | skipped / leftover — full Block A is **today** | — |
| **Fri 8/28** | **A** entire Chung-Cheng path **A1–A7 + Close** | ~6.5. Sheet has mocks every block. Compress: skip extra A1 arithmetic + second A7; **never skip Close** |
| **Sat 8/29** | **B** Yujie + Haraldur: wearable **design problems** | ~4. Yujie leftover: **Module 1 encodings** (3 encodings × 4 questions). Haraldur leftover: Module 2 case + Module 4 ship. Abstracts only. **Do not name-drop** |
| **Sun 8/30** | **D** two-project hostile defense | ~4 |
| **Mon 8/31** | **C** Vincent: 5-min structured answers | ~3 |
| **Tue 9/1** | Repair + Chung-Cheng **30-min final review** + mocks (done) | Logged. Q5s still to speak once before live |
| **Wed 9/2** | **Rest** (sick). Confirm the reschedule email | No new bootcamp |
| **Thu 9/3 – Fri 9/4** | Recovery + leftover Q5s only if energy | Chung-Cheng global batch; Jonathan degrees of freedom. Light |
| **Sat 9/5** | **Live-order mocks**: Jonathan (30) → Yujie → Chung-Cheng | ~4. Stop by 7. Do not run five full 45s |
| **Sun 9/6** | Haraldur + Vincent mock | ~3. Stories once |
| **Mon 9/7** | Community talk day. **Light only** — 20-min skim, early bed | Do not cram. Talk: [`talks/ts-vlm/`](../../../talks/ts-vlm/) |
| **Tue 9/8** | **LIVE** 11:05 / 1:05 / 2:05 / 3:05 / 4:05 | Join after 10:55, 12:55, 1:55, 2:55, 3:55. Eat in the **lunch** gap (11:50–1:05) |

**Compress:** leftover Q5s + live-order mocks beat a new study block. Cut a fourth 45 if behind — keep Jonathan at 30 min.

**Effort:** Chung-Cheng ~30% · Yujie+Haraldur ~40% · Jonathan (rigor; small pad contingency) ~15% · Vincent ~15%.

Skip unless a mock fails: RoPE derivation, RMSNorm, FlashAttention internals, RelCon cover-to-cover, LeetCode.

**Coding contingency** (do not replace person mocks): [`coding/`](coding/) — 6 high-ROI primitives (alignment, patchify, xattn, trie, sliding stats, XGBoost features). Open the problem file only; `*_solution.py` after. Not LeetCode.

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

Teach the day’s **new** material, then mock in that person’s voice.

**Fri:** open [`2026-08-27_onsite-chung-cheng.md`](2026-08-27_onsite-chung-cheng.md) at **Friday Block A**. Do A1→Close in order. Speak every mock. Not RoPE.

**Before Tue 9/8:** speak Chung-Cheng Q5 once (global batch 128→1024) and Jonathan Q5 once (pre-specified hypothesis / kill criteria, not “many datasets”). Live-order mocks Sat: Jonathan first. Reason, do not recap tool names.

---

## After live day

Tue night: `2026-09-08_onsite-debrief.md`.

## Hand-off

```
@GenAI/interviews/apple-health-aiml/2026-08-27_onsite-prep.md
@GenAI/interviews/apple-health-aiml/2026-08-27_onsite-jonathan.md
Apple onsite is Tue 2026-09-08. Rest today. Confirm the reschedule email. Live order: Jonathan 11:05 → Yujie 1:05 → Chung-Cheng 2:05 → Haraldur 3:05 → Vincent 4:05. Speak leftover Q5s when energy returns. Do not start a new bootcamp.
```
