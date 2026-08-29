# Prep — Apple Health AIML virtual on-site (hub)

**Status:** Active. Live **Wed 2026-09-02** (Yujie 10:05 → Chung-Cheng 1:05 → **Jonathan 2:05** → Haraldur 3:05) + **Fri 2026-09-04 Vincent 11:05 only**. **Jaya dropped.**  
**Invite:** [`2026-08-26_virtual-onsite-invite.md`](2026-08-26_virtual-onsite-invite.md) (updated 2026-08-27)

**Biggest adjustment:** less LLaVA/Flamingo review, more **wearable tokens + infra diagnosis**. Screen already covered attn, KV cache, concat vs xattn.

**Goal:** own a run, bake off representations on *their* signals, kill what fails, impose 3-month slices. IC verbs.

---

## Sheets (practice these, not Tyler’s theme list)

| When | Person | Sheet |
|------|--------|--------|
| Wed 10:05 | **Yujie Li** | [`2026-08-27_onsite-yujie.md`](2026-08-27_onsite-yujie.md) — behavioral tokens, timescales |
| Wed 1:05 | **Chung-Cheng Chiu** | [`2026-08-27_onsite-chung-cheng.md`](2026-08-27_onsite-chung-cheng.md) — parallelism + profiling. **Largest study delta** |
| Wed **2:05** | **Jonathan Bourim** | [`2026-08-27_onsite-jonathan.md`](2026-08-27_onsite-jonathan.md) — SWE/ARE; most plausible **pad** + rigor leftover |
| Wed 3:05 | **Haraldur Hallgrímsson** | [`2026-08-27_onsite-haraldur.md`](2026-08-27_onsite-haraldur.md) — most Apple-Health-specific. **Do not assume DL wins** |
| Fri 11:05 | **Vincent Chan** | [`2026-08-27_onsite-vincent.md`](2026-08-27_onsite-vincent.md) — 6-month program, discriminating experiments |

**Jaya** was Fri 10:05 — **dropped**. No prep sheet.

First two minutes override the map. Wed afternoon is **15 min** between Chung-Cheng / Jonathan / Haraldur — no new material in those gaps.

---

## Calendar

Bosch is **done**. Do not mix Sunnyvale scripts.

| When | Block | Hours |
|------|-------|-------|
| **Thu PM** (if energy) | skipped / leftover — full Block A is **today** | — |
| **Fri 8/28** | **A** entire Chung-Cheng path **A1–A7 + Close** | ~6.5. Sheet has mocks every block. Compress: skip extra A1 arithmetic + second A7; **never skip Close** |
| **Sat 8/29** | **B** Yujie + Haraldur: wearable **design problems** | ~4. Yujie timescales; Haraldur **four modules** (problem → representation → evidence → decision). Today leftover: Module 2 case + Module 4 ship. Abstracts only. **Do not name-drop** |
| **Sun 8/30** | **D** two-project hostile defense | ~4 |
| **Mon 8/31** | **C** Vincent: 5-min structured answers | ~3 |
| **Tue 9/1** | Repair + **Wed-order mocks**: Yujie → Chung-Cheng → Jonathan (30 min) → Haraldur | ~4. Stop by 7. Do not run four full 45s |
| **Wed 9/2** | **LIVE** 10:05 / 1:05 / **2:05** / 3:05 | Join after 9:55, 12:55, 1:55, 2:55. Eat in the **morning** gap |
| **Thu 9/3** | **Vincent mock** only | ~2 |
| **Fri 9/4** | **LIVE** Vincent 11:05 | Join after 10:55 |

**Compress:** never skip Fri **Close** mock (35 min) or Tuesday’s Wed-order mocks. Cut a fourth 45 if behind — keep Jonathan at 30 min.

**Effort:** Chung-Cheng ~30% · Yujie+Haraldur ~40% · Jonathan (rigor/pad) ~15% · Vincent ~15%.

Skip unless a mock fails: RoPE derivation, RMSNorm, FlashAttention internals, RelCon cover-to-cover, LeetCode.

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
| Treat Jonathan as Jaya | Jaya **dropped**. Wed 2:05 is Jonathan |
| Email interviewers | Tyler owns process |

---

## How to practice

Teach the day’s **new** material, then mock in that person’s voice.

**Fri:** open [`2026-08-27_onsite-chung-cheng.md`](2026-08-27_onsite-chung-cheng.md) at **Friday Block A**. Do A1→Close in order. Speak every mock. Not RoPE.

---

## After live days

Wed night: `2026-09-02_onsite-day1-debrief.md`. Fri: `2026-09-04_onsite-day2-debrief.md`.

## Hand-off

```
@GenAI/interviews/apple-health-aiml/2026-08-27_onsite-prep.md
@GenAI/interviews/apple-health-aiml/2026-08-27_onsite-chung-cheng.md
Start Friday Block A in 2026-08-27_onsite-chung-cheng.md: A1 memory through A7, interleaved mocks, then 35-min Close. Do not re-teach RoPE. IC verbs. Do not name AXLearn.
```
