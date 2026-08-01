# Contribution plan — Omri → SCOT (Monday with Boris)

**Purpose:** Convince Boris you are the right IC to deepen into SCOT — math/modeling credibility on generative forecasting, proof the collab already works, and a concrete 90/180-day arc under SCOT constraints.

**How Boris hears you:** He values **math and modeling**. Lead with **diffusion, flow matching, and generative forecasting** (theory + implementation). Show KGO / workshop / Mengfei alignment. Propose what you would *own*. Say “I.” Avoid PI / lab-roadmap voice ([`talks/README.md`](talks/README.md)).

**Koopman policy (important):** Do **not** lead with Koopman. You do not believe it is a serious industry path. Describe KGO as **efficient generative / flow-matching forecasting** with adaptive uncertainty — not as a Koopman story. If Boris brings up SKOLR / Koopman himself, acknowledge lightly and steer back to generative modeling, cost, calibration, and synthetic data. Do not volunteer a Koopman tutorial.

**Related:** [`mengfei-notes.md`](mengfei-notes.md) · [`collaboration.md`](collaboration.md) · [ZSF by Simulation Alone](https://arxiv.org/abs/2601.00970)

---

## The argument in one breath

You’re deep on generative models — diffusion, flow matching, VAEs — from the math through the implementation. Mayank and Boris already pulled you into generative forecasting (KGO). Their group is pushing synthetic / sim pretraining ([ZSF](https://arxiv.org/abs/2601.00970)); Mengfei confirmed synthetic data for forecasting is a SCOT interest. Monday: **I’m already the person for this bet — here’s a 90- and 180-day plan on SCOT’s real problems**, starting with the aleatoric uncertainty thread we never closed.

---

## Part 1 — Why me (notes; full words are in Part 4)

### 1. Diffusion and flow matching — math and implementation

Theory and code: SDE / transport view, not only library calls; training and sampling stacks; **one-step** regimes when iterative cost kills you. KGO: flow-matching based transport you can actually run — FM role limited on purpose; ≥25× vs iterative generative on ProbTS ([`collaboration.md`](collaboration.md)).

### 2. Generative modeling body of work (~10 papers)

VAE / diffusion / flow matching family — ImagenTime / ImagenFew, one-step distillation, irregular and data-scarce regimes, KGO. Through-line: distributions over trajectories for forecast, simulate, synthesize under messy/scarce data.

### 3. They already chose this collaboration

Mayank + Boris contacted you → KGO. [ZSF by Simulation Alone](https://arxiv.org/abs/2601.00970). Mengfei: synthetic for forecasting as infrastructure ([`mengfei-notes.md`](mengfei-notes.md)). Convert external collab → owned SCOT work.

### 4. What you want

Generative modeling for forecasting under SCOT constraints: cost/latency, cold-start, rare regimes, **calibrated predictive uncertainty**, synthetic that transfers.

### Koopman — only if he brings it up (~20s)

> I’ve used structured dynamical ideas in research settings, including on KGO, but I don’t think Koopman-as-brand is the industry path. What I care about for SCOT is generative models that are fast enough to serve, calibrated enough to decide on, and honest about synthetic data. Happy to stay in that frame.

---

## Open thread — aleatoric uncertainty

Boris raised **aleatoric uncertainty** on KGO; you offered to go further; **never closed**. Strong Monday / 90-day hook.

| Term | Meaning |
|------|---------|
| **Aleatoric** | Inherent data noise / demand volatility given observations — not “model uncertainty” |
| **Epistemic** | Uncertainty about the model — shrinks with data / better models |

AUG in KGO = first cut (per-variable / per-horizon adaptive aleatoric). Next layer: richer adaptation, calibration diagnostics, optional aleatoric vs epistemic split for decisions.

---

## Multimodal / reasoning (optional, secondary)

Do **not** lead. 30s only if he asks “what else”:

> I’ve also built multimodal systems for time-series reasoning. I wouldn’t own that first at SCOT. If you later need reasoning over forecasts or richer context, I have that muscle.

---

## 90 / 180-day arc (summary)

**0–90 (pick one with him):**

1. **Aleatoric / calibration (default)** — finish the KGO thread; decision-relevant calibration; kill if only CRPS cosmetics  
2. **Synthetic → real transfer** — cold-start / rare regimes; kill if synthetics don’t transfer  
3. **Efficient generative under SCOT constraints** — latency + slice eval; honest ship/kill  

**90–180:** Turn finding into infrastructure (calibration layer, synthetic stress-test, or scoped generative serving) + next-quarter proposal.

---

## Part 4 — Full spoken pitch (read aloud, ~8–12 min)

Rehearse once. Target conversational pace. Cut anything that sounds like “backbone of future systems.” Bracketed bits are optional if short on time.

---

### Open (~45–60s)

Thanks for making time — I’ve really valued the collaboration over the last few months.

Quick status, then I want to shift to how I could contribute inside SCOT, not only as an external coauthor.

On the NeurIPS paper — the efficient generative forecasting work we’ve been doing — it’s still under review. The early reviews came back positive, which is encouraging. On my side I owned **[TODO: your IC slice]**. Happy to dig into rebuttal or experiments whenever you want.

The workshop was accepted — Foundation Models for Temporal Systems. Next step for me is locking website and CFP ownership with the co-organizers and making sure the program stays useful for people who actually ship forecasting systems, including SCOT. Tell me what would make that most valuable from your side — we can park ops for a minute if you’d rather go straight to the science conversation.

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

When I sat with Mengfei in February, he reinforced the same direction from the Forecasting Science side: interest in synthetic data for forecasting — especially for cost, latency, cold-start, and rare regimes — on top of coherence and decision-alignment work that SCOT already does well. The way I heard it, generative isn’t trying to delete quantile forecasting. It’s trying to make the system cheaper, more robust, and better in the ugly slices.

There’s one more thread that feels especially SCOT-native. On our paper, you raised aleatoric uncertainty — how predictive uncertainty should behave across variables and horizons, and how much of the spread is real demand noise rather than model confusion. I said we could go further. We put in a first mechanism — the adaptive uncertainty gate — but we never really closed the deeper cut in the submission cycle. I keep thinking that unfinished thread is exactly the kind of problem inventory systems care about: if your uncertainty is wrong, your safety stock is wrong, even when the mean looks fine.

---

### What I’d own — 90 days (~2–2.5 min)

So here’s what I’d want if I were contributing inside SCOT next quarter — one narrow charter with you, not a roadmap.

My default ask is to finish the aleatoric uncertainty thread properly, under SCOT constraints. That means: take generative or probabilistic forecasters and make predictive uncertainty something you can trust for decisions. Clear calibration diagnostics on the slices that hurt — cold-start, intermittent SKUs, peak-ish weeks — and a kill criterion if we’re only moving CRPS around without changing decision quality. If you also care about separating aleatoric from epistemic uncertainty — what’s inherent noise versus what shrinks with more data or a better model — we can put that in scope explicitly. I won’t pretend vocabulary wars matter; what matters is whether a buyer or a planner can trust the spread.

If you’d rather point me at synthetic-to-real transfer instead, I’m equally happy to own that: which synthetic or sim-pretrained regimes actually help real demand families, and which ones look good offline and fail on the catalog. Same discipline — ship, iterate, or kill, written down.

What I would need from you in the first couple of weeks is judgment on data access and which slice is worth the cost. What you’d get from me is hands-on modeling, experiments, and an honest recommendation — not a slide deck of open challenges.

By day ninety I want a short agreed charter, reproducible results, and a written ship-or-kill note. In parallel I’d keep the paper rebuttal and workshop logistics from becoming a distraction — those stay finished and professional either way.

---

### What I’d own — 180 days (~1.5–2 min)

By one-eighty I’d want that charter to have become something structural — not a notebook that dies after the write-up.

If we went down the uncertainty path, that might look like a calibration layer people actually use next to a buying or inventory decision — with known failure modes. If we went down synthetic transfer, that might look like a stress-test or pretraining data recipe that forecasting changes have to survive before rollout. If the interesting result is that efficient generative forecasting only wins on certain SKU families under a latency budget, then the artifact is a scoped serving design with clear “use it here / don’t use it there” rules.

I’m not asking to replace the production quantile stack on day one. Quantiles are often the right object for single-period decisions. Where generative methods earn their keep is when you need trajectory structure, synthetic coverage, or uncertainty behavior that marginal quantiles don’t give you — and only when the cost is acceptable. I’d rather kill an attractive idea early than oversell it into serving.

And I’d still want a paper or workshop story when the science is real — but publish as a consequence of good SCOT work, not instead of it.

---

### Optional multimodal (~20–30s) — only if energy is high

One thing I’ll park unless you pull on it: I’ve also been building multimodal systems for time-series reasoning — not just predicting a number, but answering questions over series. I don’t think that’s the first problem I’d own at SCOT. If later you need models that reason over forecasts or richer context, I already have that muscle. Happy to leave it on the shelf for now.

---

### Close (~45–60s)

Putting it together: I think the modeling fit is there — generative forecasting with serious attention to math, implementation, and cost. The collaboration already works. SCOT’s own directions on synthetic pretraining and production uncertainty make this feel like the right place to go deeper. What I’m asking for is a path to own that work inside the team — starting with a ninety-day charter, ideally the aleatoric thread we never closed, or synthetic transfer if that’s hotter — and a clear one-eighty picture of turning it into something the stack can use.

If you see a fit, I’d really appreciate an intro or a concrete next step — a hiring manager, a Labs lead, whatever the right door is. If timing isn’t right, I’m still all-in on finishing the NeurIPS paper and the workshop well. Either way I want this collaboration to stay strong.

What would you point me at first if I were on the team next quarter?

---

## Timing cheat sheet

| Block | ~Min | Words (rough) |
|-------|------|----------------|
| Open | 1 | status + shift to fit |
| Why me | 2–3 | diffusion/FM + ~10 papers + KGO cost story |
| Already your bet | 1.5–2 | Mayank/Boris contact, ZSF, Mengfei, aleatoric thread |
| 90 days | 2–2.5 | charter + kill criteria |
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

### If the March talk comes up

> That talk was still too roadmap-heavy — I’ve gotten sharper on the IC side with you and Mayank on the generative forecasting paper. What I want to own next is a narrow charter under SCOT constraints — ideally the uncertainty thread we left open — with explicit kill criteria.

### If he pushes Koopman / SKOLR

> I’ve used those ideas in research, including pieces of our joint paper, but I don’t think Koopman branding is what SCOT should bet the stack on. The industry-relevant parts for me are fast generative forecasting, calibrated uncertainty, and synthetic data that transfers. That’s where I’d spend the ninety days.

---

## TODO before Monday

- [ ] Lock **your IC slice** one-liner for KGO; paste into the Open section TODO
- [ ] Read Part 4 aloud once; cut to ≤12 min (drop multimodal first)
- [ ] Default 90-day ask = **aleatoric/calibration**; fall back to synthetic-transfer if he downplays uncertainty
- [ ] Do **not** prep a Koopman deep-dive — only the redirect above
- [ ] Skim [ZSF abstract](https://arxiv.org/abs/2601.00970) for a clean nod — don’t present his paper back to him
