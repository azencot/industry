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

Thu 15 through Sun 18. Three drills. Depth and system design wait for the three-hour loop.

1. **Live coding that runs.** Write it in a file, run a few asserts, fix the failure out loud. A short LeetCode is only for that muscle. The screen questions are ML.
2. **Three implementations, narrating shapes.**
   - **DataLoader:** variable-length sequences, a `collate_fn`, batch tensor out.
   - **Padding:** pad to the longest item in the batch, and a mask that is 0 on pads.
   - **Attention:** `Q K^T / sqrt(d)`, mask, softmax, times `V`. Say what the mask does to a pad token.
3. **STAR, four stories, only if time remains after the code runs.** Ambiguous scientific problem. A method you killed. A result with a number. Work with engineers. IC verbs. Do not lead with the lab.
