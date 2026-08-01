# SCOT talks

## 2026-03 — Generative Forecasting as a Foundation Model

| | |
|---|---|
| **File** | [`2026-03_generative-forecasting-foundation-model.pdf`](2026-03_generative-forecasting-foundation-model.pdf) (34 slides; PDF dated 12 Mar 2026) |
| **Title** | Generative Forecasting as a Foundation Model: From Synthetic Time Series to Few-Shot Adaptation |
| **Audience** | SCOT Forecasting group; **director likely present** |
| **Context** | Early industry/Amazon exposure; Mar 19 Mengfei follow-up was post-talk |
| **Self-read** | Came across **more managerial / vision** than IC — correct for Monday |

### What the deck actually argued (strong content)

1. Forecasting at SKU scale → latency, cost, cold-start, rare regimes, long tail  
2. Bottleneck may be **data coverage**, not architecture  
3. Generative view: learn \(p_\theta(x_{1:T})\) → forecast, trajectory sim, synthetic data  
4. Quantiles (marginal) vs generative paths (joint temporal) — same decision framing as Mengfei prep  
5. Method stack: delay embedding → vision diffusion (**ImagenTime** NeurIPS’24) → few-shot (**ImagenFew** NeurIPS’25) → one-step / Koopman (NeurIPS’25) → spectral bias / Freq work → cite **Oreshkin et al. ICLR’26** synthetic foundation forecasting  
6. Open: scalable FM, controllability, trajectory eval, integrate with decision systems  

### Why it read managerial (fix for Monday)

| Slide pattern | Managerial signal | IC rewrite |
|---------------|-------------------|------------|
| “Toward foundation models…” / field ubiquity | Lab roadmap opener | “I built X; the production constraint I care about is Y” |
| Author lists “Naiman, …, and A.” | Senior-author PI voice | “I owned [method / transform / training / kill decision]” |
| Open challenges + “backbone of future systems” | Visionary close | “In 90 days I would ship [narrow experiment + kill criteria]” |
| Few personal metrics / ablations / failures | Thought-leadership talk | Name one negative result or cost/latency constraint |
| Generative as *the* future backbone | Replace-the-stack energy | Infrastructure complement to quantiles (Mengfei line) |

**Do not** apologize for the talk on Monday unless Boris brings it up. If he does:

> That talk was me still learning how to speak to SCOT — too much roadmap, not enough of what I personally build and measure. Since then the collab with you and Mayank has been much more IC: [one concrete artifact]. What I want to own next is [thesis #1 90-day slice].

### Assets to reuse verbally (IC)

- Delay embedding → small images → leverage vision diffusion (concrete representation bet you made)  
- ImagenFew few-shot / data-scarce angle → cold-start SKUs  
- One-step / efficient sampling → **inference cost / latency** (their pushback)  
- Explicit cite of Boris’s sim-only FM line — already framed as complementary  
- Quantile vs trajectory decision split — keep; it’s applied, not managerial  
- **Group Q that stuck:** how to do **conditional / constrained sampling** — you now have recent IC work (AdaGN / concat / newer methods) → Wedge C in [`../contribution-plan.md`](../contribution-plan.md)

### Assets to leave on the shelf Monday

- “Generative models may be the backbone of future forecasting systems”  
- Long open-challenges laundry list  
- PI-flavored author-list tour of the whole lab portfolio  
- Relitigating the whole talk — extract the **conditioning gap**, don’t re-present the deck
