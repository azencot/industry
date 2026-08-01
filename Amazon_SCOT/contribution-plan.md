# Contribution plan — Omri → SCOT (Monday with Boris)

**Purpose:** Convince Boris you are the right IC to deepen into SCOT — not with a generic “I’m interested,” but with a clear math/modeling fit plus a 90/180-day arc on generative forecasting under real SCOT constraints.

**How Boris hears you:** He cares about **math and modeling**. Lead with diffusion / flow matching / Koopman depth (theory + code), then show the collab is already real (KGO, workshop), then propose what you would *own* inside SCOT. Say “I.” Avoid PI / lab-roadmap voice ([`talks/README.md`](talks/README.md)).

**Related:** [`mengfei-notes.md`](mengfei-notes.md) · [`collaboration.md`](collaboration.md) · [ZSF by Simulation Alone](https://arxiv.org/abs/2601.00970) · [SKOLR](https://arxiv.org/abs/2506.14113)

---

## The argument in one breath

You’ve spent years on the exact stack SCOT is leaning into: generative models (diffusion, flow matching, VAEs), Koopman structure for dynamics, and synthetic data as forecasting infrastructure. Mayank and Boris already pulled you into that lane — that’s how KGO happened. Mengfei independently confirmed synthetic data for forecasting is a SCOT interest. So Monday is not “hire me someday.” It’s: **here’s why I’m already the person for this bet, and here’s a 90- and 180-day plan to put it on SCOT’s real problems.**

---

## Part 1 — Why me (speakable credentials)

Speak these as connected paragraphs, not a CV bullet dump. Order matters: math credibility first (Boris), then proof you already work with them, then the plan.

### 1. Diffusion and flow matching — math and implementation

I work on diffusion and flow matching from both sides. On the modeling side I care about the SDE / transport view, not just calling a library. On the implementation side I’ve shipped training and sampling stacks, including pushing diffusion toward **one-step** regimes when iterative cost is the blocker. KGO sits in that world: it’s built around **flow matching**, even though FM’s role there is deliberately limited — the point is a structured transport you can actually run, not a thousand denoising steps. That matters at SCOT scale, where inference cost across SKUs can eat theoretical wins.

If he goes deep: be ready to talk KoFM vs classical iterative FM/diffusion, and why closed-form / single-step generation is the production-relevant move ([`collaboration.md`](collaboration.md) — ≥25× vs iterative generative baselines on ProbTS).

### 2. Koopman — theory and practice (his excitement lane)

I’m deep on Koopman in theory and in practice — lifting nonlinear dynamics into a space where evolution is linear / structured, then using that for generation and forecasting. This isn’t a buzzword for me; it’s been a through-line in my work (Koopman VAEs / operator views / one-step diffusion via Koopman). Boris has been publishing in this direction too — e.g. [SKOLR](https://arxiv.org/abs/2506.14113) (structured Koopman ↔ linear RNN) and related IEEE work ([IEEE Xplore](https://ieeexplore.ieee.org/document/11423976)). KGO is the natural joint of **his** Koopman interest and **my** generative / FM stack. On Monday, treat Koopman as shared language, not a tutorial.

### 3. Generative modeling body of work (~10 papers)

Across VAE, diffusion, and flow matching I’ve built a real body of work — on the order of **ten papers** in this family — not a single opportunistic project. ImagenTime / ImagenFew, one-step distillation, irregular and data-scarce regimes, and now KGO with him and Mayank. The through-line is: learn a distribution over trajectories so you can forecast, simulate, and synthesize — and do it in a way that stays controllable when data is messy or scarce.

### 4. They already chose this collaboration — and SCOT already wants the theme

A few months ago **Mayank and Boris contacted me** for a joint project on generative modeling and forecasting. That’s how KGO came into existence — not me cold-pitching a random paper. In parallel, their group (Boris, Mayank, Mengfei, and others) put out [Zero-shot Forecasting by Simulation Alone](https://arxiv.org/abs/2601.00970) (ICLR’26): synthetic / sim pretraining as a serious path for foundation-style forecasting under leakage, privacy, and cost constraints. Separately, when I sat with **Mengfei**, he confirmed SCOT’s interest in **synthetic data for forecasting** — generative as infrastructure (cost, latency, cold-start, rare regimes), not as a cute replacement for every quantile forecaster ([`mengfei-notes.md`](mengfei-notes.md)).

So the strategic picture is already aligned. Monday is about converting an external collab into **owned SCOT work** with real catalog constraints.

### 5. What I want: a clear 90 / 180-day arc inside SCOT

I want to propose working on **generative modeling for forecasting** under SCOT’s real-world constraints — serving cost, cold-start SKUs, rare regimes, eval that matches business damage, synthetic distributions that transfer instead of lying. Concrete arc below. The math/modeling depth is how I earn the seat; the arc is what I do once I’m in it.

---

## Part 2 — Multimodal / reasoning (optional, secondary)

**Recommendation:** Do **not** lead with multimodal or VLM reasoning. Boris’s door is Koopman + generative + synthetic forecasting. Multimodal is a *horizon* card.

**When to mention (30s, only if energy is high or he asks “what else”):**

> Separate from the generative forecasting arc, I’ve also been building multimodal / VLM systems for time-series *reasoning* — not just predicting a number, but explaining and answering over series. I don’t think that’s the first problem I’d own at SCOT. But if the stack eventually needs models that reason over forecasts, demand context, or multimodal signals, I already have that muscle. Happy to park it unless you see an earlier pull.

**Why hold it back:** March group talk already skewed vision/roadmap; FinTech loop feedback was “too managerial.” Multimodal as a second act keeps Monday IC and math-forward. SCOT may go multimodal later — you don’t need to force it now.

---

## Part 3 — The 90 / 180-day arc (what you’d own)

Frame this as **one program** with two horizons, not four disconnected theses. Primary theme: generative modeling for forecasting at SCOT — synthetic + structured dynamics + cost-aware serving.

### Days 0–90 — Prove transfer and earn trust

**Goal:** One sharp problem, one owner (you), one kill/ship recommendation. Prefer something that sits at the intersection of KGO / Koopman–generative skill and ZSF-by-simulation / synthetic infrastructure.

**Candidate problem (pick with Boris in week 1):**

- **Synthetic → real transfer audit:** Which regimes from sim/synthetic pretraining (SarSim0-style or richer generative synthetics) actually help SCOT-like demand families, and which inflate offline metrics? Explicit slices: cold-start, intermittent/tail SKUs, promo / peak-ish shocks.
- **Or:** Take a KGO-style structured generative forecaster and stress it on a SCOT-relevant constraint — latency budget, multivariate/hierarchical slice, or calibration under shift — and report honestly.

**What “done” looks like at day 90:**

- A short charter everyone agrees on (problem, data access reality, success metric)
- Reproducible experiments + a written recommendation: ship / iterate / kill
- Explicit failure modes called out: synthetic mismatch, bias amplification, calibration drift (you already raise these — keep doing that)
- Parallel: KGO rebuttal / follow-ups clean; workshop ops not blocking science

**Spoken version:**

> For the first ninety days I’d want one narrow charter with you — not a roadmap. Most likely: synthetic or sim-pretrained models into real demand slices that matter for SCOT, with cold-start and rare regimes in the eval, and a clear kill criterion if the synthetic distribution isn’t transferring. I can bring the generative and Koopman modeling; I need your judgment on which slice is worth the access cost.

### Days 90–180 — Make it structural

**Goal:** Turn the 90-day finding into something that can live inside the stack — not a one-off notebook.

Examples of 180-day outcomes (choose based on 90-day result):

- A **synthetic data / stress-test layer** used before forecast or policy changes ship (sandbox, not only training data)
- A **structured generative** component (Koopman / FM lineage) that is competitive on a scoped serving envelope — where trajectory samples are worth more than marginal quantiles
- A design for **hierarchically coherent** synthetic or generative pretrain (Mengfei / CLOVER vocabulary) if reconciliation and structure are the pain
- Internal note + optional paper/workshop track that SCOT is happy to stand behind

**Spoken version:**

> By one-eighty I’d want that charter to have become infrastructure or a scoped production-adjacent prototype — synthetic stress tests, or a generative/Koopman forecaster that survives a real latency and slice eval — with a clear next-quarter proposal. Publish when it’s real; don’t publish instead of shipping judgment.

### How this maps to their papers (use lightly, don’t lecture)

| Their work | Your bridge |
|------------|-------------|
| [ZSF by Simulation Alone](https://arxiv.org/abs/2601.00970) | You’ve built generative TS engines; you can attack *transfer quality*, rare regimes, and richer generators beyond SARIMA-style sims — and you know when generative cost is worth it |
| [SKOLR](https://arxiv.org/abs/2506.14113) / Boris Koopman line | Shared language; KGO is already the collab artifact that combines Koopman structure with generative transport |
| Mengfei / CLOVER / coherence | Generative as complement to strong coherence/decision pillars — infrastructure and robustness, not “throw away quantiles” |

---

## Part 4 — Full spoken pitch (~8–12 min)

Rehearse once aloud. Cut anything that sounds like the March talk’s “backbone of future systems.”

1. **Open (30–45s)** — Thanks for the collab; paper under review with positive early signal; workshop accepted. Then: *I want to talk about how I contribute inside SCOT, not only as an external coauthor.*

2. **Math / modeling fit (2–3 min)** — Diffusion + flow matching (theory + impl); Koopman (theory + practice); ~10 generative papers. Nod to his Koopman line and to KGO as the joint object. One concrete number from KGO if natural (speed / ProbTS) — then your IC slice when you’ve locked it.

3. **Why this is already their bet (1–2 min)** — Mayank and Boris contacted you → KGO. ZSF-by-simulation. Mengfei: synthetic for forecasting. You’re not inventing a theme; you’re offering to own it under production constraints.

4. **90 / 180 arc (3–4 min)** — One charter in 90 days; structural outcome by 180. Ask him which problem he’d point you at first.

5. **Optional multimodal (30s)** — Only if it fits; park as later pull.

6. **Close (45–60s)** — Ask for openings / intros / next step. Stay in on NeurIPS either way.

### Closing lines (draft)

> What I’m asking for is a path to own generative forecasting work inside SCOT — with the real constraints, not only the NeurIPS constraints. I think the modeling fit is there, the collab already works, and I can be concrete about ninety and one-eighty days. If you see a fit, I’d love an intro or a clear next step. If timing is off, I’m still all-in on finishing KGO and the workshop well.

---

## Anti-patterns

- PI voice, grants, student mentoring, lab size
- March-talk roadmap / open-challenges laundry list
- Leading with multimodal / VLM / “reasoning over everything”
- Claiming generative should replace quantile systems wholesale
- Vague “happy to help with whatever”
- Apologizing for the talk unprompted (if he brings it up → one sentence, then IC pivot)

### If the March talk comes up

> That talk was still too roadmap-heavy — I’ve gotten sharper on the IC side with you and Mayank on KGO. What I want to own next is a narrow generative-for-forecasting charter under SCOT constraints, with explicit kill criteria.

---

## TODO before Monday

- [ ] Lock **your IC slice** one-liner for KGO in [`collaboration.md`](collaboration.md)
- [ ] Rehearse Parts 1 + 3 aloud once (math fit → 90/180); time it
- [ ] Decide: mention multimodal only if he opens the door
- [ ] Skim [SKOLR abstract](https://arxiv.org/abs/2506.14113) + [ZSF abstract](https://arxiv.org/abs/2601.00970) so nods land cleanly — don’t present his papers back to him
