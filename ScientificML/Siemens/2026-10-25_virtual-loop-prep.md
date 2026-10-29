# Siemens virtual loop — prep — 25 Oct 2026

**Role:** Principal Applied Scientist, Physical AI, Siemens. Job ID 523023.  
**Recruiter:** Danielle Chandler. **Referral:** Danielle Robinson. **Screen:** Huzefa Rangwala, 23 Oct.  
**Source:** Chat brief Omri shared on 25 Oct, plus his replies to Danielle inside that brief. The brief’s study plan is a proposal. Danielle’s sentences are the spec.

Screen notes: [`2026-10-23_huzefa-debrief.md`](2026-10-23_huzefa-debrief.md). Stories: [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md). Spoken “why Siemens”: [`2026-10-14_recruiter-prep.md`](2026-10-14_recruiter-prep.md).

---

## Status

**Booked.** Omri confirmed Danielle Chandler’s times on 28 Oct. Live coding is still **not confirmed**. Danielle Robinson, 29 Oct: Vivek is system design. Bing leads the applied-science team. Bing and Ramesh split breadth and depth. She did not say which. Do not quote her on the call. Day plan: [`2026-10-28_loop-prep-plan.md`](2026-10-28_loop-prep-plan.md).

Do not prep another coding round unless she says so. Do not treat the four system-design scenarios below as Siemens questions.

---

## What Danielle said (25 Oct)

- Three interviews. Each **45–60 minutes**. About three hours total.
- Interviewers are stakeholders and potential teammates.
- Each interviewer assesses **2–3 leadership principles or functional competencies**.
- The last **10 minutes** of each interview are for candidate questions.
- She named three technical areas: **ML depth**, **ML breadth**, **ML system design**. She did not say which interviewer owns which, or that these replace the leadership questions.
- STAR. Interviewers follow up in detail.
- Siemens is data-driven: concrete metrics.
- Individual contribution. Distinguish Omri’s decisions from students and collaborators. Avoid “we.”
- Different projects across the interviews.
- Reflection: what worked, what failed, what he learned, what he would do differently.
- Be concise. Clarify an ambiguous question. Do not fill silence.
- A specific “Why Siemens?”
- Thoughtful questions. No generic questions.
- Do not disclose proprietary or confidential information from prior employers or collaborators.

This supersedes the 14 Oct schedule labels “behavioral / technical / functional” as the name of the three hours. Those competencies still sit inside the hours: every interviewer scores leadership or functional items, and the technical menu is depth, breadth, and system design. Robinson’s private theme (scientific ML, AI4simulation, time series) still says what the work is. Do not quote her.

---

## Omri’s response to Danielle

He offered:

| Day | Seattle (her window) | Thailand |
|-----|----------------------|----------|
| Thu 29 Oct, Fri 30 Oct | 8:00–11:00 AM PDT | 22:00–01:00 |
| Tue 3 Nov, Wed 4 Nov, Thu 5 Nov | 8:00–11:00 AM PST | 23:00–02:00 |

US clocks change on Sun 1 Nov, so the November nights start an hour later in Thailand. He said he can flex if another time is easier for the team. He asked whether the loop includes live coding. That answer is still open.

Danielle came back with Tuesday afternoon, not the morning window. Omri confirmed. Pacific is PST that week.

| Order | Pacific, Tue 3 Nov | Thailand, Wed 4 Nov | Interviewer |
|-------|--------------------|---------------------|-------------|
| 1 | 1:00–2:00 PM | 4:00–5:00 AM | Bing Xiang |
| 2 | 2:00–3:00 PM | 5:00–6:00 AM | Vivek Govindan |
| 3 | 3:00–4:00 PM | 6:00–7:00 AM | Ramesh Nallapati |

Three hours back to back. The Thailand block is early morning. He said it will be difficult and that he will do it.

Public pages, not from Danielle, and the scrapers disagree with each other. Use the names. Do not open by reciting a title. Chandler posted in May 2026 that Bing Xiang joined Data & AI. A public profile lists Vivek Govindan as a senior principal ML engineer in Siemens Physical AI, Seattle, on design and simulation. Ramesh Nallapati posted in May 2026 that he joined Siemens as VP of Applied Science for a Physical AI science organization. Amazon Science still lists him at AWS, so treat the title as his own post, not a confirmed org chart.

---

## What the chat recommended, and what changes

The chat’s split was system design 35%, depth 25%, breadth 20%, behavioral 15%, coding 5%, until coding is confirmed. System design is the new gap relative to the Huzefa screen. The 15% for stories is too small. Danielle said every interviewer scores two or three leadership or functional items and is trained to follow a STAR answer. Stories are in all three hours.

Working split until she answers on coding:

| Share | Work |
|-------|------|
| 30% | System design, on Omri’s own systems |
| 25% | Depth on those same systems: hypothesis, alternative, ablation, what is unproven |
| 25% | Stories already in the bank: one metric, the decision he made, the follow-up |
| 15% | Breadth as a tradeoff, not a definition |
| 5% | Nothing new in `coding/`. [`coding/O_bagging.py`](coding/O_bagging.py) only if she confirms coding |

The chat said two behavioral mocks exist (ImagenTime, Bosch). The log has more: story A twice (16 Oct and 21 Oct), B and C on 21 Oct, E on 22 Oct. D and F were left cold for the screen on purpose. Do not add a seventh story. Repair A, B, C, and E.

Known repairs, still open:

- **A.** One number in the opening (short-series discriminative score about **58%**, or the long-series classification figure about **133%**). Say who owned the 1D stack. Drop “my students.” A Gramian angular field is dense. The sparse image is the line plot. The drop from about 1,000 evaluations to about **35** is the EDM sampler.
- **B.** TSExam was flat. Matched controls are the point. Do not chase a list of scores.
- **C.** The kill was pre-committed. Say the slice drop. The reasoning average is not 28.
- **E.** The change in the bank is interpolation plus an observation mask. The 22 Oct mock told an EM loop. Lock one procedure before the loop. Research baseline, not a production deployment. No number is still missing; do not invent one.

Story F (diffusion program, mentoring) is the one that slides into a people-manager telling. Use it only if they ask how a capability was built, and lead with the technical artifact.

---

## System design

Practice prompts, not a leaked panel. Anchor each one in work he has already done. Clarify the decision the model feeds, the slice that would kill the design, and what happens when the surrogate and the measurement or the solver disagree.

| Prompt | Ground it in |
|--------|----------------|
| Industrial sensor forecasting: irregular samples, missing values, horizon, online inference, drift | Bosch. The measurement process changed the model. |
| Generative model for physical series: representation, constraints, fidelity, sampling cost | ImagenTime. Three kill tests before the expensive run. |
| One model, several industrial series tasks: pretraining, heterogeneity, adaptation, cost | Only if they open it. A foundation model is the first try when related series share structure and the target history is short. A model trained on the task wins when sampling is irregular, covariates are specific, or the error has to be calibrated. |
| Sensors plus text, sometimes images: alignment, a missing modality, a fluent wrong answer | Dual tower. A second view helps on some tasks and not others. |

Huzefa already heard a short pass on the multimodal project: architecture, the bet, his role, results. A system-design hour should go to the decision and the failure, not repeat that overview.

For a design answer, in order: the decision the system supports, the data failure mode, the model and the alternative he rejected, the metric that can kill it, train versus serve, and the monitor that sends a case back to a solver or a person.

---

## Depth and breadth

Depth is defense of his own choices, in the nine questions from the brief: hypothesis, why that architecture, alternatives, strongest baseline, what the ablation shows, what is unproven, failure modes, what he would change, how it would run. Mock 1 is logged (26 Oct, VAE / diffusion / flow matching, 8/10): [`mocks.md`](mocks.md). The miss is the marginal field. Conditional paths can be straight. The learned velocity is \(\mathbb{E}[x_1-x_0\mid x_t=x]\), and those trajectories need not be straight. The next mock that session named is breadth.

Breadth stays applied. He already answered overfit, underfit, and regularization with Huzefa. Have the one-minute version ready: high train fit and a weak holdout is overfit; both weak is underfit; weight decay, early stopping, and dropout each shrink a different gap. Other topics worth one tradeoff each: calibration, distribution shift, leakage, and when a point forecast is the wrong output.

---

## Why Siemens

The spoken version is already in the recruiter prep. Use that. Do not replace it with a line about innovation or reputation.

> PhysicsAI and the rest of that Simcenter line take a physical system and learn a model so engineers do not rerun the expensive solver. I do the same kind of thing with operator methods: the structure I put in is how the process evolves. I want that work where the model has to land in a product, inside a company that owns the physical systems. I’m in Washington, so the hybrid setup matches where I live.

If they ask why leave academia, the seniority beat stays hands-on: he leads the science, not a people-manager seat.

---

## Questions

Two per interviewer, then stop. Skip any he has already heard answered.

Huzefa already said a team is a PM, two scientists, and engineers, and that projects cross domains. Do not ask that again.

Still unused from the screen list:

1. What result would make this group drop an approach in the first two quarters?
2. When the learned model and the numerical solver disagree, what is the rule for which one an engineer trusts?

Add one of these only if that interviewer is a teammate or a stakeholder and the first two do not fit: how a research result becomes something an engineer runs, or what has to be true before a model sits next to a simulator. Skip compute, infra, and “what is the culture.”

---

## Until the loop

1. Follow the revised [`2026-10-28_loop-prep-plan.md`](2026-10-28_loop-prep-plan.md). All three domains each day. Stories stay A, B, C, E. Coding stays closed unless she says otherwise.
2. System design. Mock 1 is logged (26 Oct, 500 machines, anomaly alerts, 6.5/10): [`mocks.md`](mocks.md). The miss is the frame. Requirements, a baseline, the operational metric, and a shadow rollout come before a second model. The follow-up that session named is a 15-minute probabilistic forecast for 1,000 sensors. Still ground one pass in Bosch and one in ImagenTime.
3. Speak A, C, and E once each with a metric and the method the bank actually records.
4. Say the Why Siemens paragraph once.
5. Leave `coding/` closed unless she confirms a coding interview.
