# ScientificML — scientific machine learning roles

Prep for **principal / senior applied scientist** roles where the center of gravity is **scientific ML for physical systems** (surrogates, operator learning, simulation, industrial time series) — not a forecasting-AS loop and not a GenAI / LLM loop.

**Not** forecasting demand systems ([`Forecasting/`](../Forecasting/)). **Not** multimodal LLM / TSFM research-scientist loops ([`GenAI/`](../GenAI/)). **Not** FinTelligence ([`Amazon_FinTech/`](../Amazon_FinTech/)).

---

## Goal

Company-loop prep: take an ambiguous industrial or physical problem through hypothesis, method, experiment, eval, and a model that can run in production. Speak as a hands-on IC.

---

## Key files

| File | What |
|------|------|
| [`Siemens/`](Siemens/) | Siemens Principal Applied Scientist — Data & AI, Washington hybrid |
| [`Psistar/`](Psistar/) | Psistar founders — follow-up Tue 27 Oct 2026, 00:15 Thailand. [One-to-many](Psistar/2026-10-27_one-to-many.md) · [call card](Psistar/2026-10-27_contribution-and-call.md) |

Shared profile: [`.cursor/skills/debrief/omri_azencot_experience.md`](../.cursor/skills/debrief/omri_azencot_experience.md).

---

## Companies

| Company | Contact | Next | Prep |
|---------|---------|------|------|
| **Siemens — Principal Applied Scientist** | **Danielle Chandler** (recruiter) · referral **Danielle Robinson** · screen **Huzefa Rangwala** | **Booked Tue 3 Nov, 1:00–4:00 PM PT** (Wed 4 Nov, 4:00–7:00 AM Thailand). Xiang, Govindan, Nallapati. Coding not confirmed. | [`Siemens/`](Siemens/) — [loop prep](Siemens/2026-10-25_virtual-loop-prep.md) · [screen](Siemens/2026-10-23_huzefa-debrief.md) |
| **Psistar — founders** | **Yochai Pagi** (CEO) · **Matan Pagi** (CTO). Raz Marshanski was a candidate; Omri recommended him on the 20 Oct call. | **Tue 27 Oct 2026, 00:15 Thailand** (Mon 26 Oct, 20:15 Israel). 45-min technical deep dive. Role frame: Principal Researcher, 40%–60%. | [`Psistar/`](Psistar/) — [briefing](Psistar/2026-10-27_technical-deep-dive.md) · [control log](Psistar/2026-10-26_koopman-control-prep.md) · [20 Oct](Psistar/2026-10-20_founders-call.md) |

After each call: drop `YYYY-MM-DD_*.md` in that company’s folder and add a row to the session log below.

---

## Session log

| Date | Session | Notes |
|------|---------|-------|
| 2026-10-14 | Siemens recruiter thread + prep | Chandler outreach via Robinson referral. Teams, not cell. Prep: [`Siemens/2026-10-14_recruiter-prep.md`](Siemens/2026-10-14_recruiter-prep.md). Insider: SciML; later rounds ML breadth / depth / system design; AI4simulation is the match; time series projects exist. |
| 2026-10-14 | Siemens recruiter screen (Chandler) | Org, not the seat. Advancing. Screen = STAR + PyTorch; then 3 × 1h virtual (behavioral, technical, functional). Offer **Mon 19 / Tue 20**. [`Siemens/2026-10-14_recruiter-debrief.md`](Siemens/2026-10-14_recruiter-debrief.md). |
| 2026-10-15 | Robinson on the phone screen | Live PyTorch/Python + ML breadth. DataLoader, padding, attention. Must run unit tests. Drills: [`Siemens/coding/`](Siemens/coding/). Stories: [`Siemens/2026-10-15_behavioral-story-bank.md`](Siemens/2026-10-15_behavioral-story-bank.md). |
| 2026-10-16 | Story A mock | ~15 min, ImagenTime. GAF off-diagonal called zero. Log: [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-17 | Psistar founders prep | Call **Tue 20 Oct, 00:00 Thailand** with **Yochai Pagi** and **Matan Pagi**. Intro via Raz Marshanski. Prep: [`Psistar/2026-10-20_founders-call-prep.md`](Psistar/2026-10-20_founders-call-prep.md). |
| 2026-10-17 | Huzefa screen booked | Fri 23 Oct, 22:00–23:00 Thailand. Half resume methodology, half PyTorch. Three mornings Tue 20–Thu 22. [`Siemens/2026-10-17_huzefa-screen.md`](Siemens/2026-10-17_huzefa-screen.md). |
| 2026-10-17 | Prep revised | Coding-heavy (~65–70%). 17 extended to cross-group and multi-head. 18 starts broken. Thursday mock is a different composition (19). |
| 2026-10-17 | Coding, evening | Attention with heads, plus broadcast A/B/D. Misses: tensor truthiness, `tril` polarity, mask lined up with features. Group-key mask and shape drills not started. |
| 2026-10-20 | Coding plan revised | Attention is done enough. Tue–Thu shifts to a transformer block, train/eval, masked CE, variate attention, InfoNCE, and two unseen mocks. [`Siemens/2026-10-20_coding-plan.md`](Siemens/2026-10-20_coding-plan.md). |
| 2026-10-21 | Story C mock | TR kill. 26.9→21.9 and the pre-commit landed. Reasoning average said as 28. The telling left the kill for the audit, and the 0.8B deltas were not said. [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-21 | Coding | Group attention, LayerNorm, a sliding-window dataset, and K-means. 17b and another attention change were set aside. Misses: key-mask broadcast, LayerNorm device, a negative window count, and a centroid view of `x`. [`Siemens/coding/`](Siemens/coding/). |
| 2026-10-21 | Story B mock | Dual tower. Matched controls landed. TSExam was first a win, then corrected to flat. Follow-ups chased scores; the next mock stays on the decision. [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-21 | Story A mock, full transcript | ImagenTime with Huzefa simulated. Three kill tests and the combined-system limit landed. Opening still has no number and still says "my students." Four-week plan stayed generic. [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-22 | Coding plan for Thu–Fri | Unseen mocks first if the day slips. New drills are Gaussian NLL, a covariate forecast, a GRU classifier, and a script that does not learn. [`Siemens/2026-10-20_coding-plan.md`](Siemens/2026-10-20_coding-plan.md). |
| 2026-10-22 | Story E mock | Bosch. He took the sensor constraint and refused a product claim. The method told was an EM loop; the bank's change is interpolation plus an observation mask. No number. [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-23 | Huzefa technical screen | He will recommend proceeding. Multimodal project, then overfit/underfit/regularization, then bagging (platform swapped off SGD). Vote not finished; he said that was fine. Team = PM, two scientists, engineers; projects cross domains. [`Siemens/2026-10-23_huzefa-debrief.md`](Siemens/2026-10-23_huzefa-debrief.md). |
| 2026-10-25 | Virtual loop confirmed | Chandler: 3 × 45–60 min, depth / breadth / system design, 2–3 leadership items each. Omri offered 29–30 Oct and 3–5 Nov, 8–11 AM Seattle, and asked about coding. [`Siemens/2026-10-25_virtual-loop-prep.md`](Siemens/2026-10-25_virtual-loop-prep.md). |
| 2026-10-25 | Psistar follow-up prep | One-to-many as two problems (Rosetta ingest, PsiFM lift). Koopman paper is the frozen-backbone cut on one simulator. World models and JEPA used as the loss and the planning picture. [`Psistar/2026-10-27_one-to-many.md`](Psistar/2026-10-27_one-to-many.md) · [`Psistar/2026-10-27_contribution-and-call.md`](Psistar/2026-10-27_contribution-and-call.md). Call assumed **Tue 27 Oct, 00:15 Thailand**. |
| 2026-10-25 | Psistar 20 Oct call logged | From Omri’s meeting summary. One-to-many, TSFM plus vision twin, predictive operations, research-lab hiring. Matan to formalize a zero-shot irregular resampler and a second paper. [`Psistar/2026-10-20_founders-call.md`](Psistar/2026-10-20_founders-call.md). |
| 2026-10-25 | Psistar role frame | Omri proposed part-time Principal Research Scientist, 2–3 days/week, remote Seattle. They agreed Principal Researcher at 40%–60%, technical leadership and hands-on. Seattle not restated. |
| 2026-10-25 | Psistar deep-dive briefing | 45-min technical meeting. Own transferable Koopman (shared lift, local \(G\), held-out regime). Resampler and flowsheet mask attach. Probabilistic control waits. [`Psistar/2026-10-27_technical-deep-dive.md`](Psistar/2026-10-27_technical-deep-dive.md). |
| 2026-10-26 | Psistar control reading | Skimmed Korda & Mezić. Read MamKO and bilinear MamKO. Watched Brunton’s MPC lecture, plus two industrial-autonomy videos (XMPro, IT/OT Insider). SCP lecture and the two robustness papers not done. [`Psistar/2026-10-26_koopman-control-prep.md`](Psistar/2026-10-26_koopman-control-prep.md). |
| 2026-10-26 | Where the control is chosen | The net emits a horizon of Koopman matrices from observed history before the QP (MamKO eq. 9g, Section 4). MPC chooses \(u\). Bilinear SCP re-linearizes that step in the candidate \(u\); it does not re-encode imagined futures in the paper’s account. [`Psistar/2026-10-26_where-control-is-optimized.md`](Psistar/2026-10-26_where-control-is-optimized.md). |
| 2026-10-26 | Psistar call sheet | Live page for the 45 minutes: problem, current solution, where Omri fits and with whom, expectations. [`Psistar/2026-10-27_call-sheet.md`](Psistar/2026-10-27_call-sheet.md). |
| 2026-10-26 | Siemens system-design mock | 500 machines, five sensors, anomaly alerts. Clarification 9. Deployment 4. Overall 6.5. Supervised plan on 20 failures, then a masked autoencoder. Eval used synthetic prevalence and F1. No shadow or rollout. [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-26 | Siemens ML depth mock | VAE, diffusion, flow matching. 8/10. Objectives and train-on-synthetic test-on-real landed. Marginal trajectories called straight. Optimal velocity called a moving average. [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-28 | Siemens loop booked | Omri confirmed Tue 3 Nov, 1:00–4:00 PM PT: Bing Xiang, Vivek Govindan, Ramesh Nallapati. Thailand is Wed 4 Nov, 4:00–7:00 AM. Coding still unstated. [`Siemens/2026-10-25_virtual-loop-prep.md`](Siemens/2026-10-25_virtual-loop-prep.md). |
| 2026-10-28 | Siemens loop prep plan | Revised the same day. Depth, breadth, and system design every day through 2 Nov. One-domain days are retired. Stories stay the bank. [`Siemens/2026-10-28_loop-prep-plan.md`](Siemens/2026-10-28_loop-prep-plan.md). |
| 2026-10-28 | Siemens breadth recall | Not a mock. Cost threshold and prevalence shift landed. Misses: FP = 0.05 × 9,900, the name ECE, and using calibration to pick a ranker. [`Siemens/2026-10-28_breadth-recall.md`](Siemens/2026-10-28_breadth-recall.md). |
| 2026-10-28 | Siemens ML breadth mock | Stopped at question 3. Cost threshold 0.99% landed. A cap of 20 inspections was not turned into a top-K rank. Precision@K was new. Provisional 6.5. [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-28 | Siemens ML depth mock, Koopman | 7.5. Lift and the encoder–linear–decoder baseline landed. Unit-circle eigenvalues left unqualified. A low-data win was read as proof the system is Koopman. Synthetic-data question not answered. Separate from the 26 Oct flow-matching depth mock. [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-28 | Siemens behavioral mock | ImagenTime disagreement, 8.0. Kill tests and EDM landed. Still “my students.” No number. “Insist” on the proof of concept. Last question, the unpopular stop, not answered. [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-29 | Siemens plan, Robinson’s hours | Vivek is system design. Bing and Ramesh split breadth and depth. Depth is any CV paper. Design priority is PDE generation and scale. Six CV titles mapped. The PDF is not in the repo. [`Siemens/2026-10-28_loop-prep-plan.md`](Siemens/2026-10-28_loop-prep-plan.md). |
| 2026-10-29 | Siemens system-design mock, PDE data | 7.0. The 100,000-trajectory shortfall and the turbulence diagnosis landed. Later counts ignored the remaining node-hours. Storage and the PDE residual were not said. Repair question not scored. [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-29 | Siemens ML depth mock, Closing the Loop | 7.0. Motivation and four missingness regimes landed. The monotone quantity was not stated. Classical EM in the debrief is not the paper’s theorem. [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-29 | Siemens ML breadth mock, new factory | 6.5, stopped. Shift and the time split landed. Calibration unnamed. The 2.44% line is review, not his answer. [`Siemens/mocks.md`](Siemens/mocks.md). Sheet: [`Siemens/2026-10-29_breadth-review.md`](Siemens/2026-10-29_breadth-review.md). |
| 2026-10-29 | Siemens behavioral mock, TR kill | 8.0. Gates and 26.9 to 21.9 landed. Reasoning again said as 28 to 29.2. The bank stays 29.5 to 31.2. Consensus stood in for the decision. [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-30 | Siemens ML breadth mock, overfitting | 6.5. Overfit named. The step-6,000 checkpoint, weight decay, and dropout were not. A larger model and a learned map came first. [`Siemens/mocks.md`](Siemens/mocks.md). |
| 2026-10-30 | Siemens fundamentals recall | Not a mock. 6.2 on six answers. AdamW 4. Layer norm 3. Question 7 not taken. [`Siemens/2026-10-30_fundamentals-recall.md`](Siemens/2026-10-30_fundamentals-recall.md). |
| 2026-10-30 | Siemens system-design mock, time series | 7.0. CFD opening aborted and unscored. Three holdouts landed. The token and the factory count did not. [`Siemens/mocks.md`](Siemens/mocks.md). |

---

## Boundaries

| Track | Use for |
|-------|---------|
| **This folder (`ScientificML/`)** | Scientific ML / physical-AI / industrial applied-science interviews |
| [`GenAI/`](../GenAI/) | LLM, multimodal, TSFM research-scientist loops |
| [`IndustrialResearch/`](../IndustrialResearch/) | Industry research-lab intros (Apple Koltun org). Not this folder |
| [`Forecasting/`](../Forecasting/) | Forecasting AS roles (LightGBM, Chronos, demand) |
| [`Amazon_FinTech/`](../Amazon_FinTech/) | FinTelligence formal loop |
| [`Amazon_SCOT/`](../Amazon_SCOT/) | SCOT relationship / contribution |
