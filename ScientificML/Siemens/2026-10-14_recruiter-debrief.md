# Debrief — 2026-10-14 — Siemens recruiter (Danielle Chandler)

**Type:** Recruiter screen, Microsoft Teams  
**Recruiter:** Danielle Chandler  
**Prior:** [`2026-10-14_recruiter-prep.md`](2026-10-14_recruiter-prep.md)  
**Next:** Send availability for the technical screen. Target **Mon 2026-10-19** and **Tue 2026-10-20**.

Cleared the soft gate. The hiring manager wants a technical screen. She talked about the **org**, not the specific seat. Hiring manager still unnamed. Org details were not written down.

---

## Loop (Chandler — this is the process)

| Stage | Format | Focus |
|-------|--------|--------|
| 0. Recruiter | **Done 2026-10-14** | Org overview. Not a deep pass on the role. |
| **1. Phone / technical screen** | Virtual, **live coding** | Chandler: **STAR** + PyTorch. Robinson (2026-10-15): **PyTorch/Python coding** + **ML breadth**. Examples she named: **DataLoader**, **simple padding**, **attention matrix**. Code must **run on simple unit tests**. LeetCode helps the live-coding muscle; the questions are ML. |
| **2. Virtual on-site** | **3 × 1 hour**, all virtual | **Behavioral** · **technical** · **functional** |

“Functional” is her word. She did not define it. Do not invent a case study.

Robinson’s earlier note (ML breadth, depth, system design; scientific ML; AI4simulation; time series on the team) is still the **later-loop theme**. For this phone screen, her 2026-10-15 note is the spec. Chandler’s table is the schedule. Do not quote either note back.

---

## Availability to send

Send it now. Do not wait until you have practiced. The practice days are the gap between the email and the screen.

Offer **Monday 19 and Tuesday 20 October** only. State **Pacific Time**, and keep the hours you can actually take from UTC+7.

| Pacific | Your clock (UTC+7) |
|---------|---------------------|
| Mon/Tue **8:00–10:00 AM PT** | Same evening, **10:00 PM–midnight** |
| Mon/Tue **4:00–6:00 PM PT** | **Next morning, 6:00–8:00 AM** |

Skip midday PT. That is the middle of your night.

Draft:

> Hi Danielle,
>
> Thank you for the overview today. I would be glad to do the technical screen.
>
> These windows are Pacific Time:
>
> - Monday, October 19, 8:00–10:00 AM or 4:00–6:00 PM
> - Tuesday, October 20, 8:00–10:00 AM or 4:00–6:00 PM
>
> Happy to adjust within those two days if the interviewer needs a different hour.
>
> Best,  
> Omri

---

## Update 2026-10-15 — Robinson on the phone screen

Private. Do not quote.

> Phone screen is typically divided into PyTorch/Python coding and ML Breadth. It can cover questions on the DataLoader, simple padding, attention matrix. It is live coding and typically you need to run the code on some simple unit tests so practicing some LeetCode can help but the questions are more ML focused.

Chandler still said STAR is in this screen. Prepare both. Robinson is describing the technical half.

## Practice before that screen

Phone screen is **Mon 2026-10-19** or **Tue 2026-10-20**. Files and the full drill list: [`coding/README.md`](coding/README.md). Open the problem file only. Do not open `*_solution.py` until your file runs.

About **80–85%** of the coding time is these PyTorch problems. **15–20%** is easy Python (lists, dicts, two pointers, a sliding window) so the live-coding muscle stays warm. No DP, graphs, or obscure APIs.

On every problem: state shapes, state assumptions, code without a Python loop when a tensor op will do, write 2–4 asserts, run them, fix the failure out loud.

| Day | Date | Do |
|-----|------|----|
| 1 | **Thu 15** | **01–04 done.** Still file 13 (`Dataset`). Then speak three stories from the [bank](2026-10-15_behavioral-story-bank.md): **A ImagenTime, B dual-tower, C TR kill.** |
| 2 | **Fri 16** | Scaled dot-product attention, padding mask, causal mask, multi-head shapes. Files 05–08. One timed attention from scratch. |
| 3 | **Sat 17** | `nn.Module`, train loop, eval loop, pairwise similarity, masked cross-entropy. Files 09–12, 15. One or two easy Python problems. |
| 4 | **Sun 18** | Two 40–45 min mocks. Mock 1: variable-length batch + mask. Mock 2: attention. No solution file open. |
| Screen morning | **Mon or Tue** | From memory only: collate, padding mask, attention, one training loop. Then 20–30 min ML breadth. No new topic. |

STAR still belongs on this screen (Chandler). The bank is [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md). Six stories, not the old four-topic list. Speak **A, B, C** on Thu 15. **D, E, F** on a later day. IC verbs. Do not lead with the lab. Do not invent a product ship.

Before you walk in, you can write these without docs or autocomplete: custom `Dataset`, `collate_fn`, pad, padding mask, masked mean, masked loss, scaled dot-product attention, causal mask, padding+causal, multi-head reshape, a small `nn.Module`, train loop, eval loop, batched pairwise similarity, sliding-window time-series `Dataset`.
