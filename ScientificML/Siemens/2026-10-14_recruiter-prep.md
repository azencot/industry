# Prep — Siemens recruiter screen (Principal Applied Scientist)

**When:** **Thu 2026-10-15** · Microsoft **Teams** (not a cell call). High-level. Confirm the invite time before you join.  
**Role:** [Principal Applied Scientist](https://jobs.siemens.com/en_US/externaljobs/JobDetail/523023?source=Indeed) (Job ID 523023 · Washington · hybrid)  
**Recruiter:** **Danielle Chandler** ([danielle.chandler.ext@siemens.com](mailto:danielle.chandler.ext@siemens.com))  
**Referral:** **Danielle Robinson** — she sent the resume. Different person. Do not recite her loop notes.  
**Format:** Brief recruiter call — your experience, an overview of the opportunity, your questions.

**Your goal:** clear the soft gate. Leave her able to say: *hands-on IC who puts dynamical systems theory, mostly operator methods, into practical ML; same bet as Simcenter; PhD; Seattle; wants this seat.* Time series is a pocket if she asks, not the opener.

Thread: [`2026-10-14_recruiter-correspondence.md`](2026-10-14_recruiter-correspondence.md). Hub: [`README.md`](README.md).

---

## 0. Tonight (45–60 min) — read, then say the intro

Do not prep ML breadth, depth, or system design. Read §0a, then say §3 out loud twice.

1. Read **RomAI, PhysicsAI, and the executable-twin post** (§0a). Skim the digital-twin page if time is left.
2. **Say the 90s intro out loud twice.** Dynamical systems and simulation. Not forecasting. Not the VLM. Not the lab.
3. Lock logistics (§5) and the three questions (§6).
4. Open the Teams link once. You are abroad with no cell — that link is the call.
5. Skim anti-patterns (§7) once.

---

## 0a. Reading list

ChatGPT’s priority order is right in spirit. Two corrections: there is no single research page that lists those five bullets cleanly, and **RomAI** is a closer match to Koopman than PhysicsAI is. PhysicsAI is geometric deep learning on meshes. Do not tell the recruiter your Koopman work *is* PhysicsAI.

| Priority | Read | Time | What to take |
|----------|------|------|----------------|
| 1 | [Simcenter RomAI](https://www.siemens.com/en-us/products/simcenter/engineering-data-science-ai/romai/) | 10 min | AI reduced-order models **plus dynamic system theory**. Fast surrogates of CFD / FEA / system simulation, including from small datasets, exported into a digital twin. This is the product sentence that rhymes with Koopman. |
| 2 | [Simcenter PhysicsAI](https://www.siemens.com/en-us/products/simcenter/engineering-data-science-ai/physicsai/) | 10 min | Geometric deep learning: shape and mesh → physics fields. Siemens’ claim is **up to 1000×** faster than the solver. Attribute the number. You have not done mesh/CAD geometric DL. |
| 3 | [Executable digital twin, 1 Sep 2026](https://blogs.sw.siemens.com/simcenter/siemens-executable-digital-twin-for-industrial-intelligence/) | 10 min | High-fidelity simulation is too slow to sit next to the asset. A purely data-driven model can violate physics. Their answer is a reduced model plus AI plus live measurements. |
| 4 | [Digital twin overview](https://www.siemens.com/en-us/company/digital-twin/) | 5 min | Physics simulation, sensor loop, executable twin near the asset. Enough strategy. Stop. |
| Skip unless curious | [Feb 2026 digital-enterprise post](https://blog.siemens.com/2026/02/ai-and-the-digital-twin-combine-to-supercharge-the-digital-enterprise/) | — | Exists. The reduced-order point is clearer on RomAI and the Sep 2026 post. |
| Hub, don’t read end to end | [Engineering data science and AI](https://www.siemens.com/en-us/products/simcenter/engineering-data-science-ai/) | 2 min | One map: PhysicsAI, RomAI, reduced-order modeling, executable twins. |

### How your work maps

**Identity:** you put dynamical systems theory and practice — mostly the operator literature — into machine learning someone can train and evaluate.

**Where that matches Simcenter:** the portfolio’s bet is the same shape. Physical structure goes into a learned model so you do not rerun the expensive solver. PhysicsAI is the shape-and-mesh version of that bet. RomAI is the dynamics version (“AI with dynamic system theory”). You match the bet, and you match the dynamics product more than the mesh product.

| Your research | Say | Do not say |
|---------------|-----|------------|
| Operator / dynamical systems → ML | Same move as Simcenter: structure from the physical system, then a model that runs. Yours is how a process evolves. | “My work is PhysicsAI” or “I do geometric deep learning on CAD.” |
| Koopman, if she asks what the operator part is | A representation where a nonlinear process evolves in a simpler way, so the reduced model is fast enough to run. | A theory lecture. |
| Generative models | When real trajectories are short, a generator is a simulator, and it gives you a **distribution**, not one guess. | “My diffusion papers are their uncertainty-quantification product.” |
| Time series | Forecasting and representation for sensor-like series, with an eval gate. Second pillar. | Opening the call as a forecasting researcher. |

One sentence if she asks what Koopman is: “It learns coordinates where nonlinear dynamics are approximately linear, which is a principled way to build a fast reduced model.” Then stop. Do not teach the theory.

---

## 1. What this call is

| Is | Isn’t |
|----|--------|
| Soft screen: who you are, why Siemens, location and timing | ML breadth, depth, or system design |
| Her mapping you to **level + pod fit** | A quiz on physics-informed nets |
| Chance to sound like a **hands-on principal IC** | Lab-PI / grant / mentoring pitch |
| Mutual interest + what the loop is next | Offer negotiation |

She already has the resume from Danielle Robinson and wrote that she was impressed. Give her a clean story she can forward, plus logistics.

---

## 2. JD → you (fit map)

Headline for yourself: they want a principal who **owns scientific ML on physical systems** and takes it to production. Robinson: **AI4simulation** is the match they care about. **Time series** is real work on the team, second.

### They want (from the [JD](https://jobs.siemens.com/en_US/externaljobs/JobDetail/523023?source=Indeed))

| JD signal | Your evidence | How to say it |
|-----------|---------------|---------------|
| **Scientific ML / AI4simulation** | Koopman / operator view of dynamics (ICML 2020, ICLR 2024); one-step diffusion as operator learning (NeurIPS 2025); ImagenTime as a generator you can roll forward when trajectories are scarce (NeurIPS 2024) | “I learn models of dynamical systems you can simulate forward — operator-style models, and generative models when you do not have enough real trajectories.” |
| **Time series** | Forecasting and generative TS; irregular series; eval that matches the decision | “Time series is the other half of the same program. I keep a baseline and I only keep a model when the metric matches the decision.” |
| **Ambiguous problem → hypothesis → experiment → production** | Config-first sweeps, ablations, killed data mixes, tiered eval | “I write the question down, run the comparison, and stop when the evidence does not hold.” |
| **Eval pipelines you own** | Tiered gates, slice metrics, negative results | “I do not promote on training loss.” |
| **Partnership with engineering** | PyTorch, multi-GPU training, eval harness; engineers own serving | “I own the science and the experiment. I expect to pair with engineers on data readiness, training infra, and inference.” |
| **Python + modern ML** | Primary stack | Easy checkbox. |
| **8+ years, models that mattered, paper → reliable system** | PhD Technion; UCLA; BGU; 40+ NeurIPS / ICML / ICLR; end-to-end training stacks | One sentence. Do not list papers unless asked. |
| **Industrial / physical domains** (preferred) | Bosch Center for AI collaboration (synthetic series, modality translation) — adjacent, not a Siemens product | “I have collaborated with industrial research. I have not owned a factory or grid model. That domain is why I want the role.” |
| **Mentor / raise the rigor bar** (preferred) | Technical direction on experiments | Technical standard, not headcount. |

### Gaps — don’t hide; don’t over-explain

| Gap | Pocket |
|-----|--------|
| Not a PINN / CFD / differentiable-simulation / EDA specialist | “The deep match is operator learning and simulation from data. Physics-informed nets, geometry, and chip design are adjacent — I would not pretend that is my publication record.” |
| Research systems, not a shipped industrial controller | “What I have run in production is the training and eval system. Putting the model on an industrial pipeline, with drift and safety, is the job I want.” |
| PI title reads managerial | Designed, implemented, trained, ablated, killed. |
| Traveling, no cell | Already explained. Teams is the plan. Do not re-negotiate the link. |

**One sentence for yourself:** I put dynamical systems theory, mostly operator methods, into practical ML. That is Simcenter’s bet. PhysicsAI does it for shape; I have done it for dynamics.

---

## 3. Spoken scripts

### Intro (~2 min)

Do not open with “I’m an associate professor.” Prior loops heard the title as managerial. Start on the work. If she asks what you do now: associate professor, looking for a hands-on principal IC role, based in Seattle.

> The common thread in my research has been learning representations and models of complex dynamical systems. A substantial part of my earlier work was on Koopman operators and learning representations in which nonlinear dynamics become easier to model. More recently, I’ve worked extensively on generative and probabilistic modeling of dynamics, particularly for time series, including irregularly sampled systems. Over the last year I’ve also worked on multimodal models, specifically how to make a foundation model use temporal and dynamical information rather than only text and images. That’s one reason I find this Siemens role interesting. Scientific machine learning and AI for simulation bring these areas together. Siemens already has PhysicsAI and RomAI for learning physical systems, and the executable-twin work connects simulation with agents. The question that interests me is how those agents reason about physical dynamics, generalize across systems and operating conditions, and know when a learned model is reliable enough for a decision — with the physical model checking the decision. That is the natural next step for me: dynamical systems, generative modeling, and the recent multimodal work.

If she jumps in early, stop after PhysicsAI and RomAI. The last two sentences repeat the question.

### Three beats for Danielle

Do not recite these on top of the intro. Pull one when she asks.

**Science** — if she wants the short version of the work:

> I’ve spent much of my career modeling complex dynamical systems, from Koopman representations to generative and probabilistic models.

**Seniority** — if she asks about level, scope, or leadership. Say it, then the second sentence. “Leading researchers” alone reads as a people-manager pitch, and this seat is a hands-on principal.

> As a professor I’ve been responsible not only for developing methods, but for identifying research directions, leading researchers and collaborations, and taking ambiguous problems from an initial idea through successful research outcomes. The role I want is still hands-on: I lead the science and the collaborations, not a people-manager seat.

**Motivation** — if she asks why Siemens, or why leave academia:

> What attracts me to Siemens is the opportunity to take this kind of scientific ML beyond papers and have it become part of real simulation and engineering systems.

### Why Siemens / why this role (20–30s)

> PhysicsAI and the rest of that Simcenter line take a physical system and learn a model so engineers do not rerun the expensive solver. I do the same kind of thing with operator methods: the structure I put in is how the process evolves. I want that work where the model has to land in a product, inside a company that owns the physical systems. I’m in Washington, so the hybrid setup matches where I live.




### Recent work (45–60s, only if she asks)

> A line I keep coming back to is simulation from learned dynamics. Earlier that was Koopman and operator models of sequential processes. More recently I treated generation itself as the simulator: when you do not have enough real series, a generative model has to produce trajectories you would actually trust, including very long ones. In parallel I have been strict about evaluation — baselines first, ablations, and killing a mix when a slice gets worse. That is the working style I would bring: hypothesis, experiment, and a decision the team can act on.

### Time series in one breath (only if she asks)

> Time series shows up as forecasting, as generative models for short and long series, and as irregular sampling. I start from a baseline and I change the representation only when the baseline loses on the decision metric.

### Multimodal reasoning (only if she asks about language, agents, or recent work beyond dynamics)

The VLM is the layer **above** the twin. Simcenter already simulates a state and checks a what-if against physics. Their executable-twin writeup adds agents that are supposed to name a cause and prescribe an action. Your project is practice at that interface for series: more than one view of the same process, a question in, an answer out, and an eval that rejects a fluent wrong answer.

> I have also trained multimodal models that answer questions about a series — classify, give a number, explain a temporal relation — and I only keep a change when the answer is right, not when the loss drops. In a Simcenter setting I would put that above the twin, not inside it. The reasoner can propose a decision. The physics model accepts or rejects it. A language model that invents the physics is the failure mode their own writeup warns about.

**Research question, for a scientist later — not for Danielle.** Do not teach the LLM physics. Teach it to query a world model. PhysicsAI and RomAI already predict; the executable-twin writeup already claims what-if and a prescribed action. The open problems are grounding (the proposal has to obey the physics), generalization to a new objective without a new training run, and uncertainty (use the cheap surrogate, or pay for the solver, or abstain). You have not built the thermal-management loop. Do not describe it as a system you have. Do not ask Danielle whether the team connects foundation models to PhysicsAI or RomAI. Save that for the hiring manager.

---

## 4. Likely recruiter questions

| Question | Answer direction |
|----------|------------------|
| Walk me through your background | Chronology light → land on **learned dynamical systems / simulation**. Time series only if she stays on it |
| What are you looking for? | Full-time principal IC; scientific ML that ships; Washington hybrid |
| Why leave academia / why now? | Want models of physical systems that have to run; available full-time (BGU through October; align start with the team) |
| Why this role? | §3. Physical systems, not a generic LLM seat |
| Do you have industrial / Siemens experience? | Bosch research collaboration, not a product owner. Eager to learn the plant, grid, or product constraints |
| Papers vs production? | Papers are the research arc. I also own training, ablation, and eval gates |
| People management? | Looking for **IC** impact. I will raise the experimental standard. I am not seeking a people-manager seat |
| Competing processes? | Optional and short: a few applied-science conversations in flight. This one is high priority because it is scientific ML and Washington |
| Comp? | Prefer level and scope first. Happy to discuss the full package later |
| Remote / which site? | JD is Washington hybrid. You are in Seattle. Ask which site the pod uses. Do not open with full remote |
| Work authorization? | US permanent resident. No sponsorship |

---

## 5. Logistics pocket

> I’m a US permanent resident. I’m based in Seattle. I’m traveling right now, which is why we’re on Teams. I’m looking for a full-time IC role. I’m at BGU through October on an academic timeline, and I can align a full-time start with the team. No visa sponsorship needed.

Washington hybrid is a fit. Do not demand remote. Do not invent a Siemens office city — ask.

**Public pay** (only if she brings it): base **$167,178–$226,236** plus **15%** target incentive. If pressed: “I’d expect a competitive package for the level you assess. Happy to sync once we know scope and total comp.”

---

## 6. Questions to ask

Ask these three. They match the JD: science and a product.

1. Is the team mainly scientific ML for simulation and digital twins, or does it also own broader industrial AI such as forecasting?
2. How is the principal role structured — an individual contributor who owns a scientific area, or technical leadership across several projects?
3. How does the team balance longer-term research with capabilities that land in Siemens products?

If she turns question 2 back on you: you want the **IC** version. You will own the science and the experimental standard. You are not looking for a people-manager seat.

If there is time:

4. Which Washington site is the hybrid anchor, and what does the loop look like after this call?

Avoid: solver or PINN trivia, compensation first, and anything that sounds like you were briefed on their rubric.

---

## 7. Anti-patterns

| Avoid | Do |
|-------|-----|
| “I run a lab / I supervise students…” | “I designed the model and owned the experiments and the eval…” |
| Opening with “I’m an associate professor” | Start on the work. Title only if she asks your current role, then hands-on principal IC |
| Opening as a time-series forecasting researcher | Koopman and learned simulation first. Forecasting is the pocket in §3 |
| Opening on the vision-language stack or Apple Health | Dynamical systems and reduced-order simulation |
| “My work is PhysicsAI” or quoting 1000× as your result | PhysicsAI is their geometric-DL product. RomAI / reduced-order dynamics is the bridge. The 1000× figure is Siemens’ claim |
| Equating diffusion with their uncertainty product | A generator gives a distribution of trajectories. Their UQ is a separate engineering stack |
| Claiming PINNs, CFD, mesh geometric DL, EDA, or a shipped plant model | Name the gap in one sentence, then the bridge |
| Quoting Danielle Robinson’s interview menu | Ask what the process is |
| Renegotiating Teams vs Zoom | You already flagged cell. Join the Teams link |
| Negotiating base on call one | Learn the pod and the next step |

---

## 8. If she asks about fit gaps

> The strongest overlap is scientific machine learning for dynamical systems — operator-style models and generative simulation — plus time series and strict evaluation. I have not spent my career inside a PINN or semiconductor-design group. The learning curve I expect is Siemens’ physical system and the production bar around it. That is why I want the role.

---

## 9. Close

> I’m very interested in this role. I’d like to meet the hiring manager or a scientist on the pod next. Happy to send anything else that helps.

After the call: write `YYYY-MM-DD_recruiter-debrief.md` (her questions, level signal, site, HM name, next step) and update [`README.md`](README.md) plus the session log in [`../INDEX.md`](../INDEX.md).
