# Mengfei Cao — prep + dinner notes

**When:** Thu 19 Feb 2026, 17:00–19:00 (dinner)  
**Where:** Meet at Amazon Grace SEA104 lobby  
**Who:** Mengfei Cao — Sr Applied Scientist / Science Manager, Forecasting Science, Amazon SCOT  
**Follow-up:** 19 Mar 2026 (post-talk ping)  
**Use for:** Monday Boris pitch — [`contribution-plan.md`](contribution-plan.md), [`questions-for-boris.md`](questions-for-boris.md)

**SKU** = Stock Keeping Unit (product × variant × packaging × location)

---

## Structured capture

### What I heard as team / org needs

- Generative / synthetic data as **infrastructure** (pretrain, cost/latency, leakage/copyright, cold-start) — not only as a replacement forecaster
- Mayank flagged generative TS + synthetic data for forecasting as rising priorities; Omri already collabing with Mayank + Boris on generative forecasting
- Zero-shot / sim-only pretraining (ZSF by Simulation Alone): cut inference cost & latency; avoid leakage; close real-vs-synthetic gap
- Coherence + decision alignment already strong (CLOVER / hierarchical lines); next layer = scale, robustness to shift, cold-start, rare regimes
- Production friction questions that mattered: where forecasts fail (tails, cold-start, lifecycle, reconciliation side effects, latency/cost); hard SKUs statistically vs operationally (sparsity, censoring, serving constraints); whether inference cost is dominated by long tail vs head

### Problems / research directions they care about

| Direction | Notes |
|-----------|--------|
| **CLOVER** | Joint bottom-level → aggregate ⇒ coherence by construction; CRPS via reparameterization beats log-likelihood; assumes **additive** aggregation |
| **PHF / DPM** | Hierarchical forecasting gains when bottom-level dependence is modeled; hierarchy can encode real signal |
| **Poisson mixture** | Similar “bottom-level joint” vibe to CLOVER, but emphasis = expressive covariance for counts vs CLOVER’s objective alignment (CRPS) |
| **ZSF by Simulation Alone** | Synthetic pretrain → cheaper/faster inference, less leakage; close real vs synthetic gap |
| **Foundation-style retail forecasting** | Cross-SKU / hierarchical pretrain + synthetic regimes → adapt to new SKUs with light fine-tune |
| **Quantiles vs trajectories** | Marginal quantiles enough for single-period newsvendor; generative paths matter when costs are intertemporal / coupled (lead times, carryover, multi-echelon) |

### What resonated about my background

- ImagenTime + ImagenFew (+ KoVAE): vision diffusion for irregular / sparse / OOD series — joint temporal distributions, controllability, simulation
- Freq-Synth: Fourier synthetic data for zero-shot forecasting
- Framing: generative model as **probabilistic forecaster** *and* **synthetic data engine**; second role especially powerful at Amazon scale
- Concrete pitches Mengfei-side prep used:
  1. Generative coherent hierarchical pretraining (structure by construction, not only post-hoc reconciliation)
  2. Cold-start SKU pretraining / structural priors
  3. Rare-regime amplification + synthetic stress-testing for policy validation
- Collab with Mayank + Boris (Koopman-based / generative forecasting) as proof of fit

### Risks I raised (good IC signal)

- Synthetic distribution mismatch; amplifying model bias; calibration drift; governance / interpretability; overfitting to synthetic regimes
- Lead line: guard against generator reinforcing its own biases in production

### Production-experience pushback (ready answers)

| Probe | Answer |
|-------|--------|
| No production experience? | True — research-driven so far. I’ve thought hard about scale, constraints, deployment implications; excited to learn production side fast |
| What level? | Focused on scope and impact; confident at senior; open to align to team need / best fit |

### Follow-up (19 Mar)

- Ask thoughts after the talk; where it connects to what the team is building
- Frame: scale generative forecasting for production; generative **complements** foundation models (efficiency/scalability); controllability, synthetic data, few-shot adaptation
- Tradeoff question: expressivity vs inference cost
- If “generative too expensive”: agree — main challenge is making them competitive on latency/cost

### Quotes / phrases worth reusing with Boris

> Generative modeling at SCOT is less about replacing forecasting and more about building scalable infrastructure — cost, latency, cold-start, synthetic augmentation.

> Quantile forecasting is decision-optimal for single-period asymmetric costs. Generative trajectory modeling becomes useful when costs depend on paths.

> Coherence and decision alignment are already strong pillars; the next layer may be scalable generative infrastructure for robustness at Amazon scale.

### Bridge sentence for Monday

> When I spoke with Mengfei in February, the theme that stuck was generative modeling as **forecasting infrastructure** — synthetic pretrain for cost and latency, cold-start and rare regimes — on top of coherence work like CLOVER that’s already strong. I’ve been collaborating with you and Mayank on generative forecasting; I’d like your read on where that maps to Labs priorities this half, and where I’d contribute first inside the team.

---

## Dinner agenda (as prepared)

| Block | Min | Goal |
|-------|-----|------|
| Calibration & context | 0–20 | Peer tone; mandate; CLOVER / PHF / ZSF hooks |
| Where generative helps at SCOT scale | 20–45 | Production friction; synthetic as infrastructure vs robustness vs architecture |
| Generative as scalable infrastructure | 45–75 | Credentials (ImagenTime/Few, Freq-Synth); hierarchical / cold-start / rare-regime / stress-test theses + risks |
| SCOT in 3 years | 75–105 | Long-term stack; research vs production; what survives deployment |
| Close | 105–120 | Synthesis; gaps; 18-month success; alignment check |

### Key talking points (compressed)

**CLOVER curiosity:** Additive aggregation fits hierarchical demand — is the harder structure in practice **nonlinear cross-series interaction** rather than hierarchy itself?

**Synthetic dual role:** Pretrain global forecasters; reduce inference cost; improve latency; avoid leakage; support cold-start; rebalance rare costly regimes that likelihood underweights.

**Quantiles vs paths:** P50/P90 per SKU-week = marginal; joint path samples needed when inventory evolves under lead times / coupling.

**Three contribution hooks:** (I1) foundation forecasting with real+synthetic hierarchical pretrain; (I2) hierarchically coherent synthetic data by construction; (I3) synthetic stress-test as policy validation sandbox.

**3-year close:** What changes most — generative as data engine vs primary forecaster? Structural bottleneck? If double investment in one capability, which?

---

## Raw archive

Full prep paste (including unused Q banks) kept for searchability:

<details>
<summary>Raw notes (click to expand in editors that support details)</summary>

Team Scholar/LinkedIn: Mengfei Cao, Dmitry Efimov, Boris Oreshkin, Michael Mahoney, Abhishek Gupta.

Dinner Feb 19 17:00–19:00; Amazon Grace SEA104 lobby.

PHF via DPM; CLOVER (CRPS reparam, additive aggregation); ZSF by Simulation Alone; collab Mayank+Boris generative forecasting; Mayank: generative TS + synthetic for forecasting becoming priorities.

Production fail modes: tails, cold-start, lifecycle, hierarchical reconciliation, latency/cost. Hard SKUs: statistical vs operational (sparsity, censoring, serving). Long-tail inference cost vs head.

Synthetic as infrastructure / rare-regime amplification / joint trajectories for multi-period decisions.

Creds: KoVAE + ImagenTime + ImagenFew; Freq-Synth. Theses: generative coherent hierarchical forecasting; cold-start pretraining; rare regimes; synthetic eval/stress-test. Risks: mismatch, bias amp, calibration drift, governance, overfitting synthetic.

Close: biggest gaps; 18-month success build; problems to own; is generative core capability; aligned vs misaligned direction.

Pushbacks: no production experience; what level.

Mar 19 follow-up email themes: talk reaction; production-scale generative forecasting; complements foundation models; expressivity vs inference cost.

</details>
