# Contribution plan — Omri → SCOT (Monday with Boris)

**Purpose:** Convince Boris you are the right IC to deepen into SCOT — math/modeling credibility on generative forecasting, proof the collab already works, and a concrete 90/180-day arc under SCOT constraints.

**How Boris hears you:** He values **math and modeling**. Lead with **diffusion, flow matching, and generative forecasting** (theory + implementation). Show KGO / workshop / Mengfei alignment. Propose what you would *own*. Say “I.” Avoid PI / lab-roadmap voice ([`talks/README.md`](talks/README.md)).

**Koopman policy (important):** Do **not** lead with Koopman. You do not believe it is a serious industry path. Describe KGO as **efficient generative / flow-matching forecasting** with adaptive uncertainty — not as a Koopman story. If Boris brings up SKOLR / Koopman himself, acknowledge lightly and steer back to generative modeling, cost, calibration, and synthetic data. Do not volunteer a Koopman tutorial.

**Related:** [`mengfei-notes.md`](mengfei-notes.md) · [`collaboration.md`](collaboration.md) · [ZSF by Simulation Alone](https://arxiv.org/abs/2601.00970)

---

## The argument in one breath

You’re deep on generative models — diffusion, flow matching, VAEs — from the math through the implementation. Mayank and Boris already pulled you into generative forecasting (KGO). Their group is pushing synthetic / sim pretraining ([ZSF](https://arxiv.org/abs/2601.00970)); Mengfei confirmed synthetic data for forecasting **and** foundation models (mainly to **cut training times**). Monday: **I’m already the person for this bet — here’s a 90- and 180-day plan on SCOT’s real problems**, starting with the **epistemic uncertainty** thread we never closed on KGO.

---

## Part 1 — Why me (notes; full words are in Part 4)

### 1. Diffusion and flow matching — math and implementation

Theory and code: SDE / transport view, not only library calls; training and sampling stacks; **one-step** regimes when iterative cost kills you. KGO: flow-matching based transport you can actually run — FM role limited on purpose; ≥25× vs iterative generative on ProbTS ([`collaboration.md`](collaboration.md)).

### 2. Generative modeling body of work (~10 papers)

VAE / diffusion / flow matching family — ImagenTime / ImagenFew, one-step distillation, irregular and data-scarce regimes, KGO. Through-line: distributions over trajectories for forecast, simulate, synthesize under messy/scarce data.

### 3. They already chose this collaboration

Mayank + Boris contacted you → KGO. [ZSF by Simulation Alone](https://arxiv.org/abs/2601.00970). Mengfei: synthetic for forecasting as infrastructure + **foundation models mainly to cut training times** ([`mengfei-notes.md`](mengfei-notes.md)). Convert external collab → owned SCOT work.

### 4. What you want

Generative modeling for forecasting under SCOT constraints: cost/latency, cold-start, rare regimes, **calibrated predictive uncertainty**, synthetic that transfers.

### Koopman — only if he brings it up (~20s)

> I’ve used structured dynamical ideas in research settings, including on KGO, but I don’t think Koopman-as-brand is the industry path. What I care about for SCOT is generative models that are fast enough to serve, calibrated enough to decide on, and honest about synthetic data. Happy to stay in that frame.

---

## Open thread — epistemic uncertainty (use this)

**Correction / facts:** KGO already has **aleatoric** results (AUG — adaptive per-variable / per-horizon aleatoric uncertainty). What Boris was interested in, and what you offered but **never got to**, is **epistemic** uncertainty. That’s the unfinished Monday / 90-day hook.

| Term | Meaning | In KGO today |
|------|---------|--------------|
| **Aleatoric** | Inherent data noise / demand volatility given observations | **Have results** — AUG |
| **Epistemic** | Uncertainty about the model / parameters — shrinks with more data, better models, or better coverage | **Boris’s interest; not done** |

**Why SCOT cares about epistemic:** Cold-start, new categories, distribution shift, synthetic→real transfer — you need to know when the *model* is guessing, not only how noisy demand is. Epistemic high → don’t trust the spread the same way; collect data, fall back, or gate the decision. Mixing epistemic into aleatoric spreads can make you look “calibrated” while still being confidently wrong on OOD SKUs.

**Spoken bridge (in Part 4 below):** we closed a cut of aleatoric; reopen epistemic as the SCOT charter.

---

## Multimodal / reasoning (optional, secondary)

Do **not** lead. 30s only if he asks “what else”:

> I’ve also built multimodal systems for time-series reasoning. I wouldn’t own that first at SCOT. If you later need reasoning over forecasts or richer context, I have that muscle.

---

## 90 / 180-day arc (summary)

**0–90 (pick one with him):**

1. **Epistemic uncertainty (default)** — finish what Boris wanted on KGO: model uncertainty that is useful under SCOT slices (cold-start, shift, synthetic transfer); kill if it doesn’t change decision/gating behavior  
2. **Synthetic → real transfer** — cold-start / rare regimes; kill if synthetics don’t transfer  
3. **Efficient generative under SCOT constraints** — latency + slice eval; honest ship/kill  

**90–180:** Turn finding into infrastructure (epistemic gating / uncertainty layer, synthetic stress-test, or scoped generative serving) + next-quarter proposal.

---

## Part 4 — Full spoken pitch (read aloud, ~8–12 min)

Rehearse once. Target conversational pace. Cut anything that sounds like “backbone of future systems.” Bracketed bits are optional if short on time.

---

### Open (~45–60s)

Thanks for making time — I’ve really valued the collaboration over the last few months.

Quick status, then I want to shift to how I could contribute inside SCOT, not only as an external coauthor.

On the NeurIPS paper — the efficient generative forecasting work we’ve been doing — it’s still under review. The early reviews came back positive, which is encouraging. On my side I owned the technical parts around **flow matching and the structured dynamical mechanics** that make single-step generation work — not just running experiments. Happy to dig into rebuttal or experiments whenever you want.

The workshop was accepted — Foundation Models for Temporal Systems — which is great news for all of us as co-organizers. I’m looking forward to it. One thing I’d love is that we attract a really strong set of papers — work that connects forecasting research to systems people actually care about shipping. Happy to sync on that whenever useful; we don’t have to dig into ops today.

What I mainly want to talk about today is fit: why I think I’m a strong match for the generative-forecasting bets you’re already making, and a concrete ninety- and one-eighty-day picture of what I’d own if I were inside the team.

---

### Why me — generative modeling (~2–3 min)

The core of what I bring is generative modeling for sequential data — especially diffusion and flow matching — from both the mathematical side and the implementation side.

On the math side I care about the actual generative process: the SDE view for diffusion, the transport view for flow matching, when one-step approximations are justified, and when you’re kidding yourself about calibration. I’m not interested in treating these models as black-box samplers you only tune from a config file.

On the implementation side I’ve built and shipped training and sampling stacks for these models. A theme I keep coming back to is cost: iterative sampling is scientifically nice and operationally brutal. So I’ve worked hard on regimes where you get generative flexibility without paying a thousand denoising steps at inference — including one-step style approaches when the latency budget demands it.

That’s also how I think about our joint paper. The interesting part for industry isn’t a fancy name for the architecture. It’s that we’re doing probabilistic forecasting with a generative transport that can run in a single step instead of an iterative sampler — and on ProbTS that bought large accuracy wins on most settings and on the order of twenty-five times faster inference versus iterative generative baselines. At SCOT scale, that kind of cost story matters as much as the leaderboard.

Around that I’ve built a real body of work — on the order of ten papers across VAEs, diffusion, and flow matching. ImagenTime and ImagenFew are about learning trajectory distributions for time series, including few-shot and data-scarce settings. I’ve worked irregular sampling, synthetic and scarce-data regimes, and distillation for faster sampling. The through-line is the same: if you learn a distribution over trajectories, you can forecast, you can simulate, and you can synthesize — and you can do it in regimes where history is short or messy, which is most of retail demand if we’re honest.

So when I say I’m a generative modeling person, I mean theory plus code plus a track record of finishing papers in that family — not a single opportunistic project.

---

### Why this is already your bet (~1.5–2 min)

I’m not inventing a theme and bringing it to SCOT cold.

A few months ago, Mayank and you contacted me about a joint project on generative modeling and forecasting. That’s how this paper happened. So there’s already a working relationship and a shared artifact — not a blind application.

In parallel, your group published Zero-shot Forecasting by Simulation Alone — training strong forecasters from synthetic simulation alone, with a serious eye on leakage, privacy, cost, and whether the student can beat the teacher process. That matches how I think about generative models at scale: not only as a replacement predictor, but as infrastructure for pretraining and for covering regimes you don’t see enough of in real data.

When I sat with Mengfei in February, he reinforced the same direction from the Forecasting Science side. He was interested in synthetic data for forecasting — especially for cost, latency, cold-start, and rare regimes — on top of coherence and decision-alignment work that SCOT already does well. He also said SCOT is particularly interested in **foundation models**, and the driver he emphasized was practical: **cut training times** — pretrain once, adapt faster, spend less cycle time standing up models for new slices. The way I heard it, generative and foundation work isn’t trying to delete quantile forecasting. It’s trying to make the system cheaper to train and serve, more robust, and better in the ugly slices.

There’s one more thread that feels especially SCOT-native. On KGO we already have results on **aleatoric** uncertainty — the adaptive uncertainty gate that adjusts spread across variables and horizons. What you were interested in, and what I said we could push into but we never got to in the submission cycle, is **epistemic** uncertainty — when the model itself is unsure, not just when demand is inherently noisy. I keep thinking that’s a real SCOT problem: cold-start, new slices, distribution shift, synthetic-to-real transfer. If you can’t tell model doubt from data noise, you make the wrong call on when to trust the forecast versus when to gate it or collect more signal.

---

### What I’d own — 90 days (~2–2.5 min)

So here’s what I’d want if I were contributing inside SCOT next quarter — one narrow charter with you, not a roadmap.

My default ask is to pick up the **epistemic uncertainty** thread properly, under SCOT constraints. Aleatoric we already touched in KGO. Epistemic is the open one: can we estimate when the model is out of its depth — cold-start SKUs, shift, regimes we mostly saw in synthetic pretraining — and turn that into something a decision system can use, not just another plot. Clear metrics on the slices that hurt, and a kill criterion if the epistemic signal doesn’t change gating or trust behavior versus pretending all uncertainty is aleatoric. I won’t get lost in vocabulary for its own sake; what matters is whether planners can tell “demand is noisy” from “we shouldn’t trust this model here.”

If you’d rather point me at synthetic-to-real transfer instead, I’m equally happy to own that: which synthetic or sim-pretrained regimes actually help real demand families, and which ones look good offline and fail on the catalog. Same discipline — ship, iterate, or kill, written down.

What I would need from you in the first couple of weeks is judgment on data access and which slice is worth the cost. What you’d get from me is hands-on modeling, experiments, and an honest recommendation — not a slide deck of open challenges.

By day ninety I want a short agreed charter, reproducible results, and a written ship-or-kill note. In parallel I’d keep the paper rebuttal and workshop logistics from becoming a distraction — those stay finished and professional either way.

---

### What I’d own — 180 days (~1.5–2 min)

By one-eighty I’d want that charter to have become something structural — not a notebook that dies after the write-up.

If we went down the epistemic path, that might look like a model-uncertainty / gating layer people actually use next to a buying or inventory decision — especially on cold-start and shift — with known failure modes. If we went down synthetic transfer, that might look like a stress-test or pretraining data recipe that forecasting changes have to survive before rollout. If the interesting result is that efficient generative forecasting only wins on certain SKU families under a latency budget, then the artifact is a scoped serving design with clear “use it here / don’t use it there” rules.

I’m not asking to replace the production quantile stack on day one. Quantiles are often the right object for single-period decisions. Where generative methods earn their keep is when you need trajectory structure, synthetic coverage, or uncertainty behavior that marginal quantiles don’t give you — and only when the cost is acceptable. I’d rather kill an attractive idea early than oversell it into serving.

And I’d still want a paper or workshop story when the science is real — but publish as a consequence of good SCOT work, not instead of it.

---

### Optional multimodal (~20–30s) — only if energy is high

One thing I’ll park unless you pull on it: I’ve also been building multimodal systems for time-series reasoning — not just predicting a number, but answering questions over series. I don’t think that’s the first problem I’d own at SCOT. If later you need models that reason over forecasts or richer context, I already have that muscle. Happy to leave it on the shelf for now.

---

### Close (~45–60s)

Putting it together: I think the modeling fit is there — generative forecasting with serious attention to math, implementation, and cost. The collaboration already works. SCOT’s own directions on synthetic pretraining and production uncertainty make this feel like the right place to go deeper. What I’m asking for is a path to own that work inside the team — starting with a ninety-day charter, ideally the **epistemic** uncertainty thread we left open on KGO after we already had aleatoric results, or synthetic transfer if that’s hotter — and a clear one-eighty picture of turning it into something the stack can use.

If you see a fit, I’d really appreciate an intro or a concrete next step — a hiring manager, a Labs lead, whatever the right door is. If timing isn’t right, I’m still all-in on finishing the NeurIPS paper and the workshop well. Either way I want this collaboration to stay strong.

What would you point me at first if I were on the team next quarter?

---

## Prior Amazon loop (Special Projects) — process note

**Do not volunteer** in the pitch. Don’t open with “I already did a loop” or “I don’t need another loop.”

**What happened:** You completed an Amazon loop for **Special Projects**; feedback was you came across **too managerial** for what they needed. That is a negative IC signal if you lead with it — not a transferable “pass.”

**Real upside (narrower than skip-the-loop):**
- You’ve seen Amazon’s process once → less mystery
- A recent loop *can* sometimes **speed** a new req (reuse notes, shorter path) if recruiter/HM decides that — Boris/referral can help navigate
- Useful ask is **referral / intro / process**, not “waive the loop”

**If fit conversation is going well — light process close (optional ~20s):**

> If there’s a path onto Forecasting / Labs, I’d love your read on process — referral, who to talk to, and whether a recent Amazon loop helps speed things. I’m focused on an IC science seat.

**Only if he asks whether you’ve looped before:**

> Yes — Special Projects. Feedback was I came across too managerial for what they needed. Fair. Since then I’ve been deliberate about IC ownership — including the generative forecasting work with you. Happy to go through whatever process SCOT needs; I’m not assuming a skip.

**Anti-pattern:** “I already passed, so I don’t need a loop.” Completing ≠ transferable pass across orgs, especially with managerial feedback.

---

## Timing cheat sheet

| Block | ~Min | Words (rough) |
|-------|------|----------------|
| Open | 1 | status + shift to fit |
| Why me | 2–3 | diffusion/FM + ~10 papers + KGO cost story |
| Already your bet | 1.5–2 | Mayank/Boris contact, ZSF, Mengfei, **epistemic** thread |
| 90 days | 2–2.5 | epistemic charter + kill criteria |
| 180 days | 1.5–2 | infrastructure outcomes |
| Optional multimodal | 0.5 | only if pulled |
| Close | 1 | ask + next step |
| **Total** | **~8–12** | skip multimodal first if long |

---

## Anti-patterns

- Leading with **Koopman** (or volunteering SKOLR) — only if he brings it up; then redirect to generative / cost / calibration
- PI voice, grants, mentoring, lab size
- March-talk roadmap / open-challenges laundry list
- Leading with multimodal / VLM
- Claiming generative should replace quantile systems wholesale
- Vague “happy to help with whatever”
- Apologizing for the talk unprompted
- Volunteering the Special Projects loop / “I don’t need another loop” (see process note above)

### If the March talk comes up

> That talk was still too roadmap-heavy — I’ve gotten sharper on the IC side with you and Mayank on the generative forecasting paper. What I want to own next is a narrow charter under SCOT constraints — ideally the epistemic uncertainty thread we left open — with explicit kill criteria.

### If he pushes Koopman / SKOLR

> I’ve used those ideas in research, including pieces of our joint paper, but I don’t think Koopman branding is what SCOT should bet the stack on. The industry-relevant parts for me are fast generative forecasting, calibrated uncertainty, and synthetic data that transfers. That’s where I’d spend the ninety days.

---

## TODO before Monday

- [x] Lock **your IC slice** for KGO: flow matching + Koopman / structured dynamical mechanics ([`collaboration.md`](collaboration.md); Open section uses industry-safer wording)
- [ ] Read Part 4 aloud once; cut to ≤12 min (drop multimodal first)
- [ ] Default 90-day ask = **epistemic uncertainty**; fall back to synthetic-transfer if he downplays it
- [ ] Do **not** prep a Koopman deep-dive — only the redirect above
- [ ] Skim [ZSF abstract](https://arxiv.org/abs/2601.00970) for a clean nod — don’t present his paper back to him
- [x] Remember: KGO **aleatoric** (AUG) already has results; unfinished thread = **epistemic**
