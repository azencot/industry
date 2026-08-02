# Contribution plan — Omri → SCOT (Monday with Boris)

**Purpose of the call:** Explore whether there is a path for you at SCOT. Convince Boris you can **contribute** — bridge their existing sim→foundation forecasting line into **modern generative modeling** (diffusion / flow matching + efficient sampling). **Not** a promised role; there may be no opening (or none for you) right now.

**How Boris hears you:** He values **math and modeling**. Lead with generative forecasting / synthetics that can strengthen the FM bet they already made. Show KGO / workshop / Mengfei alignment. Propose a concrete charter as *evidence of fit* — framed as “if there were a path,” not “when I’m on the team.” Say “I.” Avoid PI / lab-roadmap voice ([`talks/README.md`](talks/README.md)).

**Main bet (do not lose this):** SCOT already has FM-from-synthetic ([ZSF](https://arxiv.org/abs/2601.00970)) with relatively **basic** sim. You bring the next jump — diffusion/FM generative synthetics and/or efficient generative forecasting — not “invent foundation models.”

**Side thread (do not center the plan on this):** On KGO, Boris was interested in **epistemic** uncertainty; you offered; never got there. Aleatoric (AUG) already has results. Mention briefly as an optional follow-on, not the 90-day headline.

**Koopman policy:** Do **not** lead with Koopman. Describe KGO as efficient generative / flow-matching forecasting. If he brings up SKOLR / Koopman, acknowledge lightly and steer back to efficient generative forecasting at scale.

**Related:** [`mengfei-notes.md`](mengfei-notes.md) · [`collaboration.md`](collaboration.md) · [ZSF by Simulation Alone](https://arxiv.org/abs/2601.00970)

---

## The argument in one breath

You’re deep on diffusion and flow matching — math and implementation — especially **efficient sampling**. SCOT already has a foundation-forecasting bet on **synthetic pretrain** ([ZSF](https://arxiv.org/abs/2601.00970)) — and that synthetic is still relatively **basic** (SARIMA-style sim). Monday: show how you’d **bridge that existing FM effort into modern generative modeling** if a path existed — and ask honestly whether opportunities / timing / intros make sense. KGO is proof you already collaborate. Epistemic is a side door, not the headline.

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

**0–90:**

- **Default = Wedge A** — Bridge synthetic + ZSF into modern generative modeling: replace/augment basic SARIMA-style sim with diffusion/FM generative synthetics; measure lift vs basic-sim baseline on zero-shot / fine-tune / train-time metrics. Kill if fancy synthetics don’t transfer.
- **Backup B** — Efficient generative forecasting (KGO-lineage) on a SCOT slice; quality + serve cost.
- **Backup C** — Conditional / constrained sampling (group-talk gap). IC crib below. Composes with A (controllable synthetics).
- **Side if he pulls:** Epistemic (aleatoric already in KGO).

### Wedge C — conditioning IC crib (speakable ~45s)

In diffusion / flow matching, the usual recipe is: **embed the time series, concat the condition, then AdaGN** — adaptive scale and translate — to fuse the two signals. That works well for **general / vector-like conditions** (covariates, calendars, promo flags). It works **much worse when the condition is itself a lookback sequence** (a history of values) — concat+AdaGN doesn’t handle sequential conditioning as cleanly. That’s the bakeoff I’ve been running with a PhD student: when concat+AdaGN is enough, and when you need something else for lookback-as-condition. For SCOT, covariates → start with concat+AdaGN; history-conditioned generation → don’t assume the default trick.

**90–180:** Default path = generative synthetic pipeline feeding FM pretrain (from A). Fold in conditioning (C) if controllable synthetics matter. B only if serve-path generative forecast becomes the priority.

---

## Part 4 — Full spoken pitch (read aloud, ~8–12 min)

Rehearse once. Center **efficient generative forecasting**. Epistemic = one short paragraph max.

---

### Open (~45–60s)

Thanks for making time — I’ve really valued the collaboration over the last few months.

Quick status, then I want to shift to whether there’s a path for me to contribute inside SCOT more deeply — not only as an external coauthor. I know openings aren’t always there; I’m mainly here to show fit and get your honest read.

On the NeurIPS paper — the efficient generative forecasting work we’ve been doing — rebuttal is in. One reviewer already said concerns are addressed; waiting on the second; next is a short AC meta-review note. On my side I owned the technical parts around **flow matching and the structured dynamical mechanics** that make single-step generation work — not just running experiments. Happy to sync on the AC summary whenever you want.

The workshop was accepted — Foundation Models for Temporal Systems — which is great news for all of us as co-organizers. I’m looking forward to it. One thing I’d love is that we attract a really strong set of papers — work that connects forecasting research to systems people actually care about shipping. Happy to sync on that whenever useful; we don’t have to dig into ops today.

What I mainly want to talk about today is contribution fit: bridging your foundation-from-synthetic work into modern generative modeling — diffusion and flow matching with **efficient sampling** — and a concrete picture of what I’d own **if** there were a path. Then I want your honest sense of opportunities and timing.

---

### Why me — generative modeling + efficient sampling (~2–3 min)

The core of what I bring is generative modeling for sequential data — especially diffusion and flow matching — from both the mathematical side and the implementation side. The industry punchline is **efficient sampling**: generative flexibility without paying iterative inference that dies at catalog scale.

On the math side I care about the actual generative process: the SDE view for diffusion, the transport view for flow matching, when one-step approximations are justified, and when you’re kidding yourself about quality. I’m not interested in treating these models as black-box samplers you only tune from a config file.

On the implementation side I’ve built and shipped training and sampling stacks for these models. Iterative sampling is scientifically nice and operationally brutal. So I’ve pushed hard on regimes where you keep a generative model but collapse the sampling cost — including one-step style approaches when the latency budget demands it.

That’s exactly how I think about our joint paper. The interesting part for SCOT isn’t a fancy architecture name. It’s probabilistic forecasting with a generative transport that can run in a **single step** instead of an iterative sampler — and on ProbTS that bought strong accuracy on most settings and on the order of **twenty-five times** faster inference versus iterative generative baselines. At Amazon scale, that cost story is the point.

Around that I’ve built a real body of work — on the order of ten papers across VAEs, diffusion, and flow matching. ImagenTime and ImagenFew are about learning trajectory distributions for time series, including few-shot and data-scarce settings. I’ve worked on irregular sampling, synthetic and scarce-data regimes, and distillation for faster sampling. Over the past few months I’ve also gone deep with a PhD student on **conditional generation**. The standard construction is concat the embedded series with the condition, then AdaGN to scale and translate — that works well for covariates and similar signals, and it breaks down more when the condition is a **lookback sequence**. Knowing that split matters if you want controllable synthetics on top of a foundation-from-sim stack. The through-line is: learn a distribution over trajectories so you can forecast, simulate, and synthesize — controllably, and in a way that can survive production cost.

So when I say I’m a generative modeling person, I mean theory plus code plus a track record — aimed at making generative forecasting **practical at scale**, not only accurate on a benchmark.

---

### Why this is already your bet (~1.5–2 min)

I’m not inventing a theme and bringing it to SCOT cold.

A few months ago, Mayank and you contacted me about a joint project on generative modeling and forecasting. That’s how this paper happened. So there’s already a working relationship and a shared artifact — not a blind application. The natural next step is to take that efficient-generative idea and pressure-test it under SCOT constraints: real slices, real latency, real kill criteria.

In parallel, your group published Zero-shot Forecasting by Simulation Alone — foundation-style forecasters trained from synthetic simulation, with an eye on leakage, privacy, cost, and whether the student can beat the teacher process. That’s a real SCOT bet, and I don’t want to pretend it doesn’t exist. What I notice is that the synthetic side is still relatively **basic** — powerful as a simulator class, but not modern generative modeling. That’s exactly where I think I can help: **bridge your foundation-model-from-synthetic line into diffusion and flow matching with efficient sampling** — richer synthetic distributions for pretrain, and/or generative forecasting that stays cheap enough to serve. Mengfei’s point about foundation models mainly to **cut training times** fits the same story: better generative synthetics and efficient gen models are how you make that bet stronger, not how you restart it from zero.

When I sat with Mengfei in February, he reinforced interest in synthetic data for forecasting — cost, latency, cold-start, rare regimes — and foundation models for training-time. Generative work isn’t trying to delete quantile forecasting or throw away ZSF. It’s the next layer on a stack you already started.

There’s also a concrete gap I remember from the group talk: the room was unsure how to do **conditional sampling / constraints** well in this stack. I’ve been building that recently — and the practical takeaway is that concat-plus-AdaGN is a solid default for covariate-like conditions, but not when the condition is a lookback history. Happy to bring that in as a follow-on to better synthetics; it’s not my day-one charter unless you say it should be.

[Side, ~20–30s — optional] One open thread from KGO I’ll flag but not center: we already have aleatoric results via the adaptive uncertainty gate. You were interested in **epistemic** uncertainty; I said we could go there; we didn’t in the submission cycle. Happy to pick that up later if you still care — but the main thing I want to own is bridging modern generative synthetics into the FM-from-synthetic line.

---

### What I’d own — 90 days (~2–2.5 min)

Here’s a concrete charter I’d propose **if** there were a path to contribute inside SCOT next quarter — one narrow bet with you, not a roadmap. Treat this as “how I’d show up,” not as assuming a seat exists.

You already have foundation forecasting from synthetic data. I don’t want to reinvent that. **My default ask is Wedge A:** bridge that synthetic + ZSF line into modern generative modeling — diffusion and flow matching with efficient sampling — so the data that feeds the foundation model isn’t stuck on basic sim.

Concretely: keep the FM pretrain / zero-shot setup, but replace or augment the basic simulator with generative synthetics — rare regimes, richer trajectories, messier demand shapes that a simple sim undersamples. Success looks like measurable lift versus the basic-sim baseline on metrics you already care about — zero-shot quality, fine-tune efficiency, training-cycle time — with a clear kill criterion if fancy synthetics don’t transfer.

I have two backups if you’d rather point me elsewhere. **B:** efficient generative forecasting — KGO-style single-step sampling — on a SCOT slice, judged on quality and serve cost. **C:** conditional sampling — the gap from the group talk. What we’ve found is concat-plus-AdaGN works well for covariate-like conditions and struggles when the condition is a lookback sequence; that’s a real design choice, not a slogan. C also folds into A if you want controllable generative synthetics.

I’d rather own A deeply unless you redirect me. I can bring the generative modeling; I need your judgment on data access and which demand families make the right first comparison to SarSim0-style baselines.

### Wedge A — experiment one-pager (from Boris mock; memorize)

**Protocol:** Freeze FM backbone, data/training budget, and eval. Change **only** the synthetic pretrain corpus: SarSim0 vs generative synthetics (trained on Amazon historic series with a time-based train/val/test split to avoid leakage). Combo / staged pretrain = experiment 2, not experiment 1.

**Slices:** Cold-start and rare regimes (keep hard periods such as COVID in; reweight if needed — don’t delete the ugly years and then claim rare-regime wins).

**Metrics:** Same as their FM eval — **CRPS** (distribution quality), **NMAE** (normalized point error), quantile loss as applicable. Not precision/recall/F1.

**Train-time alignment:** Also track synthetic **generation cost** (or end-to-end pretrain wall-clock to a CRPS target). Quality without a cost bound fights Mengfei’s FM-for-training-time story. Speed via **efficient / one-step sampling**, not “Koopman” branding.

**Kill:** Generative must **match or beat** SarSim0 on the cold-start/rare-regime slice within run-to-run noise. One short debug pass if not. If still no lift → **kill A**. Ask Boris whether backup is B or C — don’t assume C.

What you’d get from me is hands-on modeling, experiments, and an honest recommendation — not a slide deck of open challenges. By day ninety: agreed charter, reproducible comparison to the existing sim→FM line, written ship-or-kill. Paper rebuttal and workshop stay professional in parallel without becoming the main story.

---

### What I’d own — 180 days (~1.5–2 min)

By one-eighty — **if** that charter were real — I’d want it to have become something structural — not a notebook that dies after the write-up.

If we stay on A — my default — that looks like a generative synthetic pipeline that regularly feeds foundation-model pretrain, with known failure modes and a clear rule for when basic sim is enough. Conditioning (C) can layer on so those synthetics are controllable for covariates versus lookback-style conditions. If you redirect to B, a scoped efficient-generative serving path with “use it here / don’t use it there.” The point is to strengthen the FM-from-synthetic bet you already made, not to run a parallel science island.

I’m not asking to replace the production quantile stack on day one. Quantiles are often right for single-period decisions. Generative methods earn their keep when you need richer synthetics, trajectory structure, or distributions that basic sim can’t give you — **and** when sampling is cheap enough that SCOT can afford them. I’d rather kill an attractive idea early than oversell it into serving.

Publish when the science is real — as a consequence of good SCOT work, not instead of it.

---

### Optional multimodal (~20–30s) — only if energy is high

I’ve also built multimodal systems for time-series reasoning. I wouldn’t own that first at SCOT. If later you need reasoning over forecasts or richer context, I have that muscle.

---

### Close (~45–60s)

Putting it together: I think the modeling fit is there — diffusion and flow matching with efficient sampling. You already started the foundation-from-synthetic bet; I’d want to bridge that into modern generative **synthetics** so the data feeding the FM catches up — that’s the charter I’d propose if a path existed. Backups if you’d redirect: efficient generative forecasting, or conditional sampling where concat-plus-AdaGN isn’t enough for lookback conditions. The collaboration already works.

I’m not assuming there’s an opening. What I’m asking for is your honest read — is there a path worth exploring, an intro that makes sense, or is timing off for now? Either way I’m all-in on finishing the NeurIPS paper and the workshop well, and I want this collaboration to stay strong.

If you *do* see a fit and timing allows, an intro to a **Forecasting Science manager** would help. You can say I’m a hands-on generative modeling scientist — diffusion and flow matching — we’ve already collaborated on efficient generative forecasting in KGO, and I’d want to strengthen the sim→foundation line with modern generative synthetics.

What’s your honest read on opportunities and timing?

---

## Prior Amazon loop (Special Projects) — process note

**Do not volunteer** in the pitch. Don’t open with “I already did a loop” or “I don’t need another loop.”

**What happened:** You completed an Amazon loop for **Special Projects**; feedback was you came across **too managerial** for what they needed. Negative IC signal if you lead with it — not a transferable “pass.”

**Real upside (narrow):** process familiarity; recent loop *may* speed a new req if recruiter/HM decides; ask Boris for **referral / intro / process**, not “waive the loop.”

**If conversation is warm and he opens process — optional ~20s:**

> If there’s any path onto Forecasting / Labs worth exploring, I’d love your read — referral, who to talk to, timing, and whether a recent Amazon loop helps speed things. I’m focused on an IC science seat. Totally fine if the answer is “not now.”

**Only if he asks whether you’ve looped:**

> Yes — Special Projects. Feedback was I came across too managerial for what they needed. Fair — years in academia trained a certain presentation style. Since then I’ve been deliberate about IC ownership. Concrete: on KGO I owned the flow matching and efficient-sampling mechanics; separately I’ve owned dual-tower design/implementation and synthetic data pipelines in my multimodal TS work. Happy to go through whatever process SCOT needs; I’m not assuming a skip.

**Anti-pattern:** “I already passed, so I don’t need a loop.” Completing ≠ transferable pass across orgs, especially with managerial feedback.  
**Anti-pattern:** “The loop judged me incorrectly.” Sounds defensive — don’t argue the verdict; show IC evidence.

---

## Timing cheat sheet

| Block | ~Min | Focus |
|-------|------|--------|
| Open | 1 | status + shift to exploratory fit |
| Why me | 2–3 | diffusion/FM + **efficient sampling** + KGO speed story |
| Already your bet | 1.5–2 | ZSF exists but basic sim; Mengfei train-time; bridge to modern gen |
| 90 days | 2–2.5 | **Default A** as hypothetical charter — gen synthetics→ZSF; B/C backups |
| 180 days | 1.5–2 | scoped serving / train-time structural outcome *if* a path existed |
| Optional multimodal | 0.5 | only if pulled |
| Close | 1 | honest read on opportunities / timing; intro only if warm |
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
- Arguing the Special Projects verdict (“judged incorrectly”) — fair + IC evidence only
- Forecasting pitch metrics as precision/recall/F1 — use CRPS / NMAE / quantile loss
- Soft kill (“PoC has no kill”) — match/beat SarSim0 within noise or kill A
- Sounding like a seat is already promised (“when I’m on the team,” “my ninety-day plan at SCOT”) — charter is hypothetical evidence of fit; openings may not exist

### If the March talk comes up

> That talk was still too roadmap-heavy — I’ve gotten sharper on the IC side with you and Mayank. What I want to own next is bridging your sim→foundation line into modern generative modeling with efficient sampling — under real SCOT constraints, with explicit kill criteria.

### If he pushes Koopman / SKOLR

> I’ve used those ideas in research, including pieces of our joint paper, but I don’t think Koopman branding is what SCOT should bet the stack on. The industry path I care about is diffusion and flow matching with sampling cheap enough to run at Amazon scale.

### If he pulls hard on epistemic

> Happy to prioritize that — we left it open on KGO after aleatoric. I’d still anchor it to efficient generative forecasting: epistemic as the trust/gating layer when we take these models to cold-start and shift, not as a standalone research island.

---

## TODO before Monday

- [x] Lock KGO IC slice: flow matching + structured dynamical mechanics
- [x] Read Part 4 aloud; skim ZSF abstract
- [x] Default 90-day ask = **Wedge A** (bridge synthetic + ZSF → modern generative synthetics)
- [x] Conditioning IC crib: concat + AdaGN works for covariates; weaker when condition = lookback sequence
- [x] Boris mock grill — experiment one-pager + loop IC bullets + Forecasting Science intro ask ([`notes/2026-08-01_boris-mock-drill.md`](notes/2026-08-01_boris-mock-drill.md))
- [ ] Optional: one more “Why not scale SarSim0?” interrupt using the one-pager — then stop
- [ ] Do **not** prep a Koopman deep-dive
- [ ] Mon 3 Aug: real call → `notes/2026-08-03_boris-call.md`
