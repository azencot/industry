# Contribution plan — Omri → SCOT (Monday with Boris)

**Purpose:** Convince Boris you are the right IC to deepen into SCOT — bring **diffusion / flow matching with efficient sampling** to forecasting at Amazon / SCOT scale.

**How Boris hears you:** He values **math and modeling**. Lead with generative forecasting that can actually *serve* (fast sampling, cost, scale). Show KGO / workshop / Mengfei alignment. Propose what you would *own*. Say “I.” Avoid PI / lab-roadmap voice ([`talks/README.md`](talks/README.md)).

**Main bet (do not lose this):** Efficient generative forecasting — diffusion and flow matching, with sampling cheap enough for catalog-scale forecasting — plus related wins (synthetic / foundation pretrain that cuts training time, honest transfer).

**Side thread (do not center the plan on this):** On KGO, Boris was interested in **epistemic** uncertainty; you offered; never got there. Aleatoric (AUG) already has results. Mention briefly as an optional follow-on, not the 90-day headline.

**Koopman policy:** Do **not** lead with Koopman. Describe KGO as efficient generative / flow-matching forecasting. If he brings up SKOLR / Koopman, acknowledge lightly and steer back to efficient generative forecasting at scale.

**Related:** [`mengfei-notes.md`](mengfei-notes.md) · [`collaboration.md`](collaboration.md) · [ZSF by Simulation Alone](https://arxiv.org/abs/2601.00970)

---

## The argument in one breath

You’re deep on diffusion and flow matching — math and implementation — especially **efficient sampling**. Mayank and Boris already pulled you into generative forecasting (KGO: single-step generative transport, big inference speedups). SCOT cares about foundation / synthetic paths that cut training time and serve at catalog scale (Mengfei, ZSF). Monday: **I want to own bringing efficient diffusion/FM-style generative forecasting into SCOT’s real constraints** — with a clear 90/180-day arc. Epistemic uncertainty is a side door we left open on KGO, not the main pitch.

---

## Part 1 — Why me (notes; full words in Part 4)

### 1. Diffusion and flow matching — math + efficient sampling

Theory and code: SDE / transport view; training and sampling stacks; **one-step / few-step** regimes when iterative cost kills you. KGO proves the industry-relevant punchline: generative probabilistic forecasting without iterative sampling tax (≥25× vs iterative generative on ProbTS).

### 2. Generative body of work (~10 papers)

VAE / diffusion / FM — ImagenTime / ImagenFew, one-step distillation, irregular / data-scarce, KGO. Through-line: trajectory distributions for forecast, simulate, synthesize.

### 3. They already chose this collaboration

Mayank + Boris → KGO. [ZSF](https://arxiv.org/abs/2601.00970). Mengfei: synthetic infrastructure + **foundation models mainly to cut training times**.

### 4. What you want (main)

Own **efficient generative forecasting at SCOT scale** — diffusion/FM (or FM-class transports) that survive latency, cost, and catalog reality; connect to foundation/synthetic pretrain where it cuts train time and improves ugly slices.

### Side — epistemic (optional mention)

Aleatoric already in KGO (AUG). Boris wanted **epistemic**; unfinished. Useful for cold-start / shift gating later — **not** the center of the pitch.

### Koopman — only if he brings it up (~20s)

> I’ve used structured dynamical ideas in research, including on KGO, but I don’t think Koopman-as-brand is the industry path. What I care about for SCOT is generative models with efficient sampling that can run at Amazon scale. Happy to stay in that frame.

---

## Multimodal / reasoning (optional, secondary)

Do **not** lead. 30s only if he asks “what else.”

---

## 90 / 180-day arc (summary)

**Main theme:** Efficient diffusion / flow-matching generative forecasting at SCOT scale.

**0–90 (default):**

1. **Efficient generative forecasting under SCOT constraints (default)** — Take FM/diffusion-class probabilistic forecasting (KGO-lineage or sibling) onto a real SCOT slice: latency/cost envelope, honest ship/kill on accuracy + serve cost. Kill if it only wins offline.
2. **Synthetic / foundation pretrain for train-time** — Align with Mengfei: does generative/synthetic pretrain actually cut training cycle time or cold-start cost on SCOT-like families?
3. **Side option if he pulls:** Epistemic uncertainty on top of existing aleatoric — only if he still cares.

**90–180:** Structural outcome — scoped serving path for efficient generative forecasts; or synthetic/foundation recipe that shortens train/adapt cycles; optional epistemic gating if the main line needs trust under shift.

---

## Part 4 — Full spoken pitch (read aloud, ~8–12 min)

Rehearse once. Center **efficient generative forecasting**. Epistemic = one short paragraph max.

---

### Open (~45–60s)

Thanks for making time — I’ve really valued the collaboration over the last few months.

Quick status, then I want to shift to how I could contribute inside SCOT, not only as an external coauthor.

On the NeurIPS paper — the efficient generative forecasting work we’ve been doing — it’s still under review. The early reviews came back positive, which is encouraging. On my side I owned the technical parts around **flow matching and the structured dynamical mechanics** that make single-step generation work — not just running experiments. Happy to dig into rebuttal or experiments whenever you want.

The workshop was accepted — Foundation Models for Temporal Systems — which is great news for all of us as co-organizers. I’m looking forward to it. One thing I’d love is that we attract a really strong set of papers — work that connects forecasting research to systems people actually care about shipping. Happy to sync on that whenever useful; we don’t have to dig into ops today.

What I mainly want to talk about today is fit: bringing diffusion and flow matching with **efficient sampling** into forecasting at SCOT scale — and a concrete ninety- and one-eighty-day picture of what I’d own if I were inside the team.

---

### Why me — generative modeling + efficient sampling (~2–3 min)

The core of what I bring is generative modeling for sequential data — especially diffusion and flow matching — from both the mathematical side and the implementation side. The industry punchline is **efficient sampling**: generative flexibility without paying iterative inference that dies at catalog scale.

On the math side I care about the actual generative process: the SDE view for diffusion, the transport view for flow matching, when one-step approximations are justified, and when you’re kidding yourself about quality. I’m not interested in treating these models as black-box samplers you only tune from a config file.

On the implementation side I’ve built and shipped training and sampling stacks for these models. Iterative sampling is scientifically nice and operationally brutal. So I’ve pushed hard on regimes where you keep a generative model but collapse the sampling cost — including one-step style approaches when the latency budget demands it.

That’s exactly how I think about our joint paper. The interesting part for SCOT isn’t a fancy architecture name. It’s probabilistic forecasting with a generative transport that can run in a **single step** instead of an iterative sampler — and on ProbTS that bought strong accuracy on most settings and on the order of **twenty-five times** faster inference versus iterative generative baselines. At Amazon scale, that cost story is the point.

Around that I’ve built a real body of work — on the order of ten papers across VAEs, diffusion, and flow matching. ImagenTime and ImagenFew are about learning trajectory distributions for time series, including few-shot and data-scarce settings. I’ve worked irregular sampling, synthetic and scarce-data regimes, and distillation for faster sampling. The through-line is: learn a distribution over trajectories so you can forecast, simulate, and synthesize — and do it in a way that can survive production cost.

So when I say I’m a generative modeling person, I mean theory plus code plus a track record — aimed at making generative forecasting **practical at scale**, not only accurate on a benchmark.

---

### Why this is already your bet (~1.5–2 min)

I’m not inventing a theme and bringing it to SCOT cold.

A few months ago, Mayank and you contacted me about a joint project on generative modeling and forecasting. That’s how this paper happened. So there’s already a working relationship and a shared artifact — not a blind application. The natural next step is to take that efficient-generative idea and pressure-test it under SCOT constraints: real slices, real latency, real kill criteria.

In parallel, your group published Zero-shot Forecasting by Simulation Alone — training strong forecasters from synthetic simulation, with an eye on leakage, privacy, cost, and whether the student can beat the teacher process. That fits how I think about generative models at scale: not only as a drop-in predictor, but as part of the stack that makes foundation-style forecasting cheaper to train and more robust in regimes you undersample.

When I sat with Mengfei in February, he reinforced the same direction. Interest in synthetic data for forecasting — cost, latency, cold-start, rare regimes — and he said SCOT is particularly interested in **foundation models**, mainly to **cut training times**: pretrain once, adapt faster, less cycle time standing up models for new slices. Generative and foundation work isn’t trying to delete quantile forecasting. It’s trying to make the system cheaper to train and serve, and better in the ugly slices.

[Side, ~20–30s — optional] One open thread from KGO I’ll flag but not center: we already have aleatoric results via the adaptive uncertainty gate. You were interested in **epistemic** uncertainty; I said we could go there; we didn’t in the submission cycle. Happy to pick that up later if you still care — cold-start and shift are where model doubt matters — but the main thing I want to own is efficient generative forecasting at scale.

---

### What I’d own — 90 days (~2–2.5 min)

So here’s what I’d want if I were contributing inside SCOT next quarter — one narrow charter with you, not a roadmap.

**Default:** take efficient generative forecasting — diffusion / flow-matching class models with cheap sampling — and put it on a SCOT-relevant slice under a real cost and latency envelope. Agree up front what “good” means: forecast quality on the slices that hurt, plus inference cost that could plausibly serve. Clear kill criterion if it only wins offline or only on clean benchmarks. I can bring the generative modeling; I need your judgment on which family of SKUs or which serving constraint is the right first battlefield.

**Aligned alternate** if you’d rather start from Mengfei’s training-time angle: synthetic or foundation-style pretrain that actually shortens train/adapt cycles for SCOT-like demand — again with ship/kill written down, not a research tour.

What you’d get from me is hands-on modeling, experiments, and an honest recommendation — not a slide deck of open challenges. By day ninety: agreed charter, reproducible results, written ship-or-kill. Paper rebuttal and workshop stay professional in parallel without becoming the main story.

---

### What I’d own — 180 days (~1.5–2 min)

By one-eighty I’d want that charter to have become something structural — not a notebook that dies after the write-up.

Most likely: a scoped path where efficient generative forecasting is allowed to live in the stack for the SKU families or decision settings where trajectory / distribution modeling is worth the cost — with clear “use it here / don’t use it there” rules. Or a synthetic / foundation pretrain recipe that measurably cuts training or adaptation time and survives transfer checks. If along the way epistemic uncertainty becomes the missing trust piece for cold-start gating, we can add it — as a layer on the main line, not as a substitute for it.

I’m not asking to replace the production quantile stack on day one. Quantiles are often right for single-period decisions. Generative methods earn their keep when you need trajectory structure, synthetic coverage, or richer distributions — **and** when sampling is cheap enough that SCOT can afford them. I’d rather kill an attractive idea early than oversell it into serving.

Publish when the science is real — as a consequence of good SCOT work, not instead of it.

---

### Optional multimodal (~20–30s) — only if energy is high

I’ve also built multimodal systems for time-series reasoning. I wouldn’t own that first at SCOT. If later you need reasoning over forecasts or richer context, I have that muscle.

---

### Close (~45–60s)

Putting it together: I think the modeling fit is there — diffusion and flow matching with efficient sampling, aimed at generative forecasting that can survive Amazon scale. The collaboration already works. SCOT’s own directions on synthetic pretraining and foundation models for training-time fit the same story. What I’m asking for is a path to own that work inside the team — a ninety-day charter on efficient generative forecasting under real constraints, a one-eighty picture of turning it into something the stack can use, and a clear next step if you see a fit.

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
| Already your bet | 1.5–2 | Mayank/Boris, ZSF, Mengfei train-time; epistemic **optional side** |
| 90 days | 2–2.5 | efficient generative @ SCOT scale charter |
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

> That talk was still too roadmap-heavy — I’ve gotten sharper on the IC side with you and Mayank on efficient generative forecasting. What I want to own next is bringing that to SCOT scale under real cost and latency constraints, with explicit kill criteria.

### If he pushes Koopman / SKOLR

> I’ve used those ideas in research, including pieces of our joint paper, but I don’t think Koopman branding is what SCOT should bet the stack on. The industry path I care about is diffusion and flow matching with sampling cheap enough to run at Amazon scale.

### If he pulls hard on epistemic

> Happy to prioritize that — we left it open on KGO after aleatoric. I’d still anchor it to efficient generative forecasting: epistemic as the trust/gating layer when we take these models to cold-start and shift, not as a standalone research island.

---

## TODO before Monday

- [x] Lock KGO IC slice: flow matching + structured dynamical mechanics
- [ ] Read Part 4 aloud once; cut to ≤12 min
- [ ] Default 90-day ask = **efficient generative forecasting @ SCOT scale**; epistemic only if he pulls
- [ ] Do **not** prep a Koopman deep-dive
- [ ] Skim [ZSF abstract](https://arxiv.org/abs/2601.00970) for a clean nod
