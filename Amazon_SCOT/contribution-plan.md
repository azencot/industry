# Contribution plan — Omri → SCOT (Monday with Boris)

**Purpose:** Convince Boris you are the right IC to deepen into SCOT — **bridge** their existing sim→foundation forecasting line into **modern generative modeling** (diffusion / flow matching + efficient sampling).

**How Boris hears you:** He values **math and modeling**. Lead with generative forecasting / synthetics that can actually strengthen the FM bet they already made. Show KGO / workshop / Mengfei alignment. Propose what you would *own*. Say “I.” Avoid PI / lab-roadmap voice ([`talks/README.md`](talks/README.md)).

**Main bet (do not lose this):** SCOT already has FM-from-synthetic ([ZSF](https://arxiv.org/abs/2601.00970)) with relatively **basic** sim. You bring the next jump — diffusion/FM generative synthetics and/or efficient generative forecasting — not “invent foundation models.”

**Side thread (do not center the plan on this):** On KGO, Boris was interested in **epistemic** uncertainty; you offered; never got there. Aleatoric (AUG) already has results. Mention briefly as an optional follow-on, not the 90-day headline.

**Koopman policy:** Do **not** lead with Koopman. Describe KGO as efficient generative / flow-matching forecasting. If he brings up SKOLR / Koopman, acknowledge lightly and steer back to efficient generative forecasting at scale.

**Related:** [`mengfei-notes.md`](mengfei-notes.md) · [`collaboration.md`](collaboration.md) · [ZSF by Simulation Alone](https://arxiv.org/abs/2601.00970)

---

## The argument in one breath

You’re deep on diffusion and flow matching — math and implementation — especially **efficient sampling**. SCOT already has a foundation-forecasting bet on **synthetic pretrain** ([ZSF](https://arxiv.org/abs/2601.00970)) — and that synthetic is still relatively **basic** (SARIMA-style sim). Monday: **I want to bridge that existing FM effort into modern generative modeling** — richer diffusion/FM synthetics and/or efficient generative forecasting — under SCOT constraints. KGO is proof we already collaborate on the efficient-gen side. Epistemic is a side door, not the headline.

---

## Part 1 — Why me (notes; full words in Part 4)

### 1. Diffusion and flow matching — math + efficient sampling

Theory and code: SDE / transport view; training and sampling stacks; **one-step / few-step** regimes when iterative cost kills you. KGO proves the industry-relevant punchline: generative probabilistic forecasting without iterative sampling tax (≥25× vs iterative generative on ProbTS).

### 2. Generative body of work (~10 papers)

VAE / diffusion / FM — ImagenTime / ImagenFew, one-step distillation, irregular / data-scarce, KGO. Through-line: trajectory distributions for forecast, simulate, synthesize.

### 3. They already chose this collaboration

Mayank + Boris → KGO. [ZSF](https://arxiv.org/abs/2601.00970). Mengfei: synthetic infrastructure + **foundation models mainly to cut training times**.

### 4. What you want (main)

Bridge their **existing** FM-from-synthetic stack into modern generative modeling — richer diffusion/FM synthetics and/or efficient generative forecasting — under SCOT constraints. Not “invent FMs.”

### Side — epistemic (optional mention)

Aleatoric already in KGO (AUG). Boris wanted **epistemic**; unfinished. Useful for cold-start / shift gating later — **not** the center of the pitch.

### Koopman — only if he brings it up (~20s)

> I’ve used structured dynamical ideas in research, including on KGO, but I don’t think Koopman-as-brand is the industry path. What I care about for SCOT is generative models with efficient sampling that can run at Amazon scale. Happy to stay in that frame.

---

## Multimodal / reasoning (optional, secondary)

Do **not** lead. 30s only if he asks “what else.”

---

## 90 / 180-day arc (summary)

**Main theme:** Bridge SCOT’s **existing** synthetic→foundation forecasting line into **modern generative modeling** (diffusion / flow matching + efficient sampling).

**Context you must respect:** They already showed zero-shot FM forecasting from simulation alone ([ZSF / SarSim0](https://arxiv.org/abs/2601.00970)). You’re not proposing “discover foundation models.” You’re proposing the next capability jump: **basic sim → modern generative synthetics / efficient generative forecasters**, including **conditional / constrained sampling** (a gap they voiced after your group talk).

**0–90 (pick one primary wedge with Boris):**

1. **Bridge ZSF-style FM into modern generative modeling**
   - **Wedge A — Better synthetic for their FM:** replace or augment basic SARIMA-style sim with diffusion/FM generative synthetics; measure lift vs basic-sim baseline.
   - **Wedge B — Efficient generative forecaster beside/on top of FM:** single-step / cheap-sampling generative forecasting (KGO-lineage) on a SCOT slice; quality + serve cost.
   - **Wedge C — Conditional / constrained sampling (strong if they still care):** during the group talk they were unsure how to add **constraints / conditioning** into generative or FM-style work. You’ve spent the last few months with a PhD student on this — AdaGN-style conditioning, concat-to-input, and more recent techniques. Own a scoped bakeoff: which conditioning mechanism works for SCOT-relevant constraints (covariates, calendars, promo flags, capacity-ish bounds, etc.) under an efficient-sampling regime. Kill if conditioning doesn’t beat naive concat on a pre-agreed constraint set.
2. **Side if he pulls:** Epistemic uncertainty (aleatoric already in KGO).

**90–180:** Make the winning wedge structural — generative synthetic pipeline; scoped efficient-gen serving; and/or a **reusable conditioning module** the FM/gen stack can call when constraints matter.

---

## Part 4 — Full spoken pitch (read aloud, ~8–12 min)

Rehearse once. Center **efficient generative forecasting**. Epistemic = one short paragraph max.

---

### Open (~45–60s)

Thanks for making time — I’ve really valued the collaboration over the last few months.

Quick status, then I want to shift to how I could contribute inside SCOT, not only as an external coauthor.

On the NeurIPS paper — the efficient generative forecasting work we’ve been doing — it’s still under review. The early reviews came back positive, which is encouraging. On my side I owned the technical parts around **flow matching and the structured dynamical mechanics** that make single-step generation work — not just running experiments. Happy to dig into rebuttal or experiments whenever you want.

The workshop was accepted — Foundation Models for Temporal Systems — which is great news for all of us as co-organizers. I’m looking forward to it. One thing I’d love is that we attract a really strong set of papers — work that connects forecasting research to systems people actually care about shipping. Happy to sync on that whenever useful; we don’t have to dig into ops today.

What I mainly want to talk about today is fit: bridging your foundation-from-synthetic work into modern generative modeling — diffusion and flow matching with **efficient sampling** — and a concrete ninety- and one-eighty-day picture of what I’d own if I were inside the team.

---

### Why me — generative modeling + efficient sampling (~2–3 min)

The core of what I bring is generative modeling for sequential data — especially diffusion and flow matching — from both the mathematical side and the implementation side. The industry punchline is **efficient sampling**: generative flexibility without paying iterative inference that dies at catalog scale.

On the math side I care about the actual generative process: the SDE view for diffusion, the transport view for flow matching, when one-step approximations are justified, and when you’re kidding yourself about quality. I’m not interested in treating these models as black-box samplers you only tune from a config file.

On the implementation side I’ve built and shipped training and sampling stacks for these models. Iterative sampling is scientifically nice and operationally brutal. So I’ve pushed hard on regimes where you keep a generative model but collapse the sampling cost — including one-step style approaches when the latency budget demands it.

That’s exactly how I think about our joint paper. The interesting part for SCOT isn’t a fancy architecture name. It’s probabilistic forecasting with a generative transport that can run in a **single step** instead of an iterative sampler — and on ProbTS that bought strong accuracy on most settings and on the order of **twenty-five times** faster inference versus iterative generative baselines. At Amazon scale, that cost story is the point.

Around that I’ve built a real body of work — on the order of ten papers across VAEs, diffusion, and flow matching. ImagenTime and ImagenFew are about learning trajectory distributions for time series, including few-shot and data-scarce settings. I’ve worked on irregular sampling, synthetic and scarce-data regimes, and distillation for faster sampling. Over the past few months I’ve also gone deep with a PhD student on **conditional / constrained generation** — how you actually inject constraints into diffusion and related models: AdaGN-style conditioning, concat-to-input, and more recent techniques, with honest bakeoffs rather than one default trick. The through-line is: learn a distribution over trajectories so you can forecast, simulate, and synthesize — controllably, and in a way that can survive production cost.

So when I say I’m a generative modeling person, I mean theory plus code plus a track record — aimed at making generative forecasting **practical at scale**, not only accurate on a benchmark.

---

### Why this is already your bet (~1.5–2 min)

I’m not inventing a theme and bringing it to SCOT cold.

A few months ago, Mayank and you contacted me about a joint project on generative modeling and forecasting. That’s how this paper happened. So there’s already a working relationship and a shared artifact — not a blind application. The natural next step is to take that efficient-generative idea and pressure-test it under SCOT constraints: real slices, real latency, real kill criteria.

In parallel, your group published Zero-shot Forecasting by Simulation Alone — foundation-style forecasters trained from synthetic simulation, with an eye on leakage, privacy, cost, and whether the student can beat the teacher process. That’s a real SCOT bet, and I don’t want to pretend it doesn’t exist. What I notice is that the synthetic side is still relatively **basic** — powerful as a simulator class, but not modern generative modeling. That’s exactly where I think I can help: **bridge your foundation-model-from-synthetic line into diffusion and flow matching with efficient sampling** — richer synthetic distributions for pretrain, and/or generative forecasting that stays cheap enough to serve. Mengfei’s point about foundation models mainly to **cut training times** fits the same story: better generative synthetics and efficient gen models are how you make that bet stronger, not how you restart it from zero.

When I sat with Mengfei in February, he reinforced interest in synthetic data for forecasting — cost, latency, cold-start, rare regimes — and foundation models for training-time. Generative work isn’t trying to delete quantile forecasting or throw away ZSF. It’s the next layer on a stack you already started.

There’s also a concrete gap I remember from the group talk: the room was unsure how to do **conditional sampling / constraints** well in this stack. That’s a real systems need — calendars, promos, covariates, soft operational constraints — and it’s something I’ve been actively building recently, not a slide-deck idea.

[Side, ~20–30s — optional] One open thread from KGO I’ll flag but not center: we already have aleatoric results via the adaptive uncertainty gate. You were interested in **epistemic** uncertainty; I said we could go there; we didn’t in the submission cycle. Happy to pick that up later if you still care — but the main thing I want to own is bridging modern generative modeling into the FM-from-synthetic line, including conditioning when that’s the bottleneck.

---

### What I’d own — 90 days (~2–2.5 min)

So here’s what I’d want if I were contributing inside SCOT next quarter — one narrow charter with you, not a roadmap.

You already have foundation forecasting from synthetic data. I don’t want to reinvent that. I want to **bridge it into modern generative modeling** — diffusion and flow matching with efficient sampling.

Concretely, I’d pick one wedge with you in week one:

**Wedge A:** upgrade the synthetic side. Keep the FM pretrain / zero-shot setup, but replace or augment the basic simulator with generative synthetics — so rare regimes, richer trajectories, and messier demand shapes aren’t undersampled the way they are in a simple sim. Success looks like measurable lift versus the basic-sim baseline on the metrics you already care about — zero-shot quality, fine-tune efficiency, training-cycle time — with a kill criterion if fancy synthetics don’t transfer.

**Wedge B:** bring efficient generative forecasting — the KGO-style single-step / cheap-sampling idea — onto a SCOT-relevant slice beside or on top of the FM path. Success looks like quality plus a serve-cost envelope that could plausibly live at Amazon scale, again versus a clear baseline, with a kill if it only wins offline.

**Wedge C:** solve **conditional / constrained sampling** for the generative or FM-style stack. After the group talk it was clear this was an open question for the team. I’ve been working this with a PhD student — AdaGN-style, concat-to-input, and newer conditioning methods — comparing what actually holds constraints without wrecking sample quality or latency. Success looks like a small bakeoff on SCOT-relevant constraint types, with a recommended default and a kill if nothing beats naive concat by enough to matter.

I’d rather own one wedge deeply than all three shallowly. A and C also compose well — better synthetics that are *conditionally* controllable. I can bring the generative modeling; I need your judgment on which wedge is the hotter SCOT need right now.

What you’d get from me is hands-on modeling, experiments, and an honest recommendation — not a slide deck of open challenges. By day ninety: agreed charter, reproducible comparison to the existing sim→FM line, written ship-or-kill. Paper rebuttal and workshop stay professional in parallel without becoming the main story.

---

### What I’d own — 180 days (~1.5–2 min)

By one-eighty I’d want that charter to have become something structural — not a notebook that dies after the write-up.

If we took wedge A, that might look like a generative synthetic pipeline that regularly feeds foundation-model pretrain — with known failure modes and a clear rule for when basic sim is enough. If we took wedge B, a scoped path where efficient generative forecasting is allowed for the SKU families or decisions where trajectory modeling is worth the cost — “use it here / don’t use it there.” If we took wedge C — or A+C — a **conditioning / constraints module** the stack can reuse when you need controlled synthetics or constrained forecasts, with a documented recipe (when AdaGN-style wins, when concat is enough, when you need something newer). Either way, the point is to strengthen the FM-from-synthetic bet you already made, not to run a parallel science island.

I’m not asking to replace the production quantile stack on day one. Quantiles are often right for single-period decisions. Generative methods earn their keep when you need richer synthetics, trajectory structure, or distributions that basic sim can’t give you — **and** when sampling is cheap enough that SCOT can afford them. I’d rather kill an attractive idea early than oversell it into serving.

Publish when the science is real — as a consequence of good SCOT work, not instead of it.

---

### Optional multimodal (~20–30s) — only if energy is high

I’ve also built multimodal systems for time-series reasoning. I wouldn’t own that first at SCOT. If later you need reasoning over forecasts or richer context, I have that muscle.

---

### Close (~45–60s)

Putting it together: I think the modeling fit is there — diffusion and flow matching with efficient sampling. You already started the foundation-from-synthetic bet; I want to bridge that into modern generative modeling so the synthetics and the forecasters catch up to what generative methods can actually do at scale. The collaboration already works. What I’m asking for is a path to own that bridge inside the team — a ninety-day charter on one clear wedge, a one-eighty picture of turning it into something the stack can use, and a clear next step if you see a fit.

If you see a fit, I’d really appreciate an intro or a concrete next step — a hiring manager, a Labs lead, whatever the right door is. If timing isn’t right, I’m still all-in on finishing the NeurIPS paper and the workshop well. Either way I want this collaboration to stay strong.

What would you point me at first if I were on the team next quarter?

---

## Prior Amazon loop (Special Projects) — process note

**Do not volunteer** in the pitch. Don’t open with “I already did a loop” or “I don’t need another loop.”

**What happened:** You completed an Amazon loop for **Special Projects**; feedback was you came across **too managerial** for what they needed. Negative IC signal if you lead with it — not a transferable “pass.”

**Real upside (narrow):** process familiarity; recent loop *may* speed a new req if recruiter/HM decides; ask Boris for **referral / intro / process**, not “waive the loop.”

**If fit is warm — optional ~20s:**

> If there’s a path onto Forecasting / Labs, I’d love your read on process — referral, who to talk to, and whether a recent Amazon loop helps speed things. I’m focused on an IC science seat.

**Only if he asks whether you’ve looped:**

> Yes — Special Projects. Feedback was I came across too managerial for what they needed. Fair. Since then I’ve been deliberate about IC ownership — including the generative forecasting work with you. Happy to go through whatever process SCOT needs; I’m not assuming a skip.

---

## Timing cheat sheet

| Block | ~Min | Focus |
|-------|------|--------|
| Open | 1 | status + shift to fit |
| Why me | 2–3 | diffusion/FM + **efficient sampling** + KGO speed story |
| Already your bet | 1.5–2 | ZSF exists but basic sim; Mengfei train-time; bridge to modern gen |
| 90 days | 2–2.5 | wedge A / B / C (conditioning) — pick one |
| 180 days | 1.5–2 | scoped serving / train-time structural outcome |
| Optional multimodal | 0.5 | only if pulled |
| Close | 1 | ask + next step |
| **Total** | **~8–12** | |

---

## Anti-patterns

- Centering the pitch on **epistemic uncertainty** (side thread only)
- Leading with **Koopman** / volunteering SKOLR
- PI voice, grants, mentoring, lab size
- March-talk roadmap / open-challenges laundry list
- Leading with multimodal / VLM
- Claiming generative should replace quantile systems wholesale
- Vague “happy to help with whatever”
- Volunteering Special Projects loop / “I don’t need another loop”

### If the March talk comes up

> That talk was still too roadmap-heavy — I’ve gotten sharper on the IC side with you and Mayank. What I want to own next is bridging your sim→foundation line into modern generative modeling with efficient sampling — under real SCOT constraints, with explicit kill criteria.

### If he pushes Koopman / SKOLR

> I’ve used those ideas in research, including pieces of our joint paper, but I don’t think Koopman branding is what SCOT should bet the stack on. The industry path I care about is diffusion and flow matching with sampling cheap enough to run at Amazon scale.

### If he pulls hard on epistemic

> Happy to prioritize that — we left it open on KGO after aleatoric. I’d still anchor it to efficient generative forecasting: epistemic as the trust/gating layer when we take these models to cold-start and shift, not as a standalone research island.

---

## TODO before Monday

- [x] Lock KGO IC slice: flow matching + structured dynamical mechanics
- [ ] Read Part 4 aloud once; cut to ≤12 min
- [ ] Default 90-day ask = **bridge ZSF → modern gen** (A synthetics / B efficient forecast / **C conditional sampling**); epistemic only if he pulls
- [ ] If leading with C: 2–3 sentence IC summary of AdaGN vs concat vs newer methods + one SCOT constraint example
- [ ] Do **not** prep a Koopman deep-dive
- [ ] Skim [ZSF abstract](https://arxiv.org/abs/2601.00970) for a clean nod
