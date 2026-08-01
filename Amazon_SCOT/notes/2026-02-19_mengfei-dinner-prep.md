# Raw: Mengfei prep + dinner (19 Feb 2026)

Unedited paste from Omri (2026-08-01). Structured version: [`../mengfei-notes.md`](../mengfei-notes.md).

---

SCOT

Team:

	Mengfei Cao: https://scholar.google.com/citations?user=uWNc_7sAAAAJ&hl=en 
	Dmitry Efimov: https://scholar.google.com/citations?user=ABTWMYwAAAAJ&hl=en
	Boris Oreshkin: https://scholar.google.com/citations?user=48MBCeIAAAAJ&hl=en
	Michael Mahoney: https://scholar.google.com/citations?user=QXyvv94AAAAJ&hl=en
	Abhishek Gupta: https://www.linkedin.com/in/abhishek-arun-gupta/


Dinner with Mengfei (Feb. 19th, 17:00-19:00); Meet at Amazon Grace SEA104 lobby



0–20 min — Calibration & Context

Goal: Establish peer-level tone and understand his mandate.


PHF via DPM: Hierarchical forecasting benefits when the bottom-level dependence structure is modeled correctly — especially when hierarchy encodes real signal; 

CLOVER: If you model the joint distribution of the bottom-level series and then aggregate them, coherence comes “for free” by construction; Training with CRPS directly (via reparameterization ??) significantly outperforms training via log-likelihood.

	CLOVER assumes additive aggregation, which makes sense for hierarchical demand. I’m curious whether the more challenging structure in practice comes from 			nonlinear cross-series interactions rather than the hierarchy itself

	At first glance the Poisson mixture paper looks similar to CLOVER in modeling bottom-level joint distributions, but the emphasis feels different — CLOVER is about 		objective alignment via CRPS, while the Poisson mixture work is more about expressive covariance modeling for counts.

ZSF by Simulation alone: pre-training on synthetic data reduces inferences costs, decreases latency, avoids leakage and copyright issues; closes the gap between forecasting models trained on real vs. synthetic data

I: I’ve been collaborating with Mayank and Boris recently on generative forecasting

I: Mayank mentioned that generative time-series modeling and synthetic data for forecasting are becoming priorities. I’d love to understand how you see that fitting into SCOT.



20-45 min - Where generative modeling could help at SCOT scale

Goal: I understand the production friction — and generative modeling may address some of it

Q: Where does forecasting systematically fail in production?
	follow-up: Is it tail events? Cold start SKUs (little to no historical demand data)? Lifecycle transitions? Hierarchical reconciliation side effects? Latency / cost trade-offs?

Q: Are the hardest SKUs statistically hard (demand process difficult to predict) or operationally constrained?
	follow-up: sparsity/intermittency; feature limitations; supply-side censoring (you observe sales, not true demand); serving constraints (model too heavy)

Q: Given that retail demand is typically long-tailed — with many low-volume SKUs — does inference cost end up being dominated by the tail? Or is compute mostly concentrated on head items?


From your recent paper, what stood out to me is using generative modeling less as a replacement for forecasting and more as infrastructure — generating synthetic demand data to reduce inference cost, improve latency, and mitigate leakage. That feels like a very scalable direction. Especially at Amazon scale, inference cost across millions of SKUs can dominate theoretical optimality gains.

I’ve been thinking about generative time-series models in a similar dual role: not just estimating distributions, but serving as data engines — for pretraining, for augmenting rare regimes, or for supporting cold-start SKUs. I’m curious whether you see synthetic data primarily as: a cost reduction tool, a robustness tool, or eventually as something that reshapes the forecasting architecture itself.


I1:  Synthetic Data as Infrastructure: Generative models can: Pretrain global forecasters; Reduce inference cost; Improve latency; Avoid leakage; Support cold-start SKUs

I2: Rare Regime Amplification: Likelihood training often underweights rare but costly regimes. Synthetic generation could let us rebalance exposure.



lead with: Quantile forecasting is economically elegant for single-period decisions. Where I sometimes wonder about generative models is whether they help in edge regimes — for example, when rare tail behavior drives disproportionate cost.

or lead with: When evaluating policies internally, do you simulate demand paths — or primarily rely on quantile-based decision rules?
	follow-up: Are you constrained by quantile outputs? Do you simulate downstream policies? Is joint dependence limiting you? Are you thinking generatively already?

	if quantiles are sufficient: That makes sense under single-period assumptions. I’m curious whether multi-period interactions ever create gaps.

Many production forecasting systems output marginal quantiles — for example P50 or P90 for each SKU at each future week. That means for each time step independently, we estimate a point on the CDF — say the 90th percentile — which tells us 90% of demand realizations are expected to fall below that level. In classical single-period newsvendor settings, that’s actually sufficient. The optimal order quantity is just a particular quantile of the demand distribution determined by the cost ratio. So if decisions are made independently per period, marginal quantiles are economically aligned and very efficient.

Where the distinction appears is when decisions become intertemporal or coupled. Quantiles are marginal in time — they don’t encode how demand co-moves across weeks. If I have P90 for week 1 and P90 for week 2, that doesn’t tell me how likely it is that both weeks are simultaneously high. The joint dependence structure is missing.

A generative trajectory model, in contrast, produces full sampled paths — entire demand trajectories over the horizon. Each sample is a coherent realization across time, and potentially across SKUs. That means we can simulate inventory evolution under realistic demand scenarios, rather than optimizing each period in isolation.

So I think of it this way: Quantile forecasting is decision-optimal for single-period asymmetric costs. Generative trajectory modeling becomes useful when costs depend on paths — inventory carryover, lead times, capacity constraints, multi-echelon coupling.

It’s not that one replaces the other — it’s about whether the downstream decision problem requires joint structure or only marginals.

I3: Joint Structure: In settings where lead times (time between replenishment and receiving inventory)  or coupling matter, joint trajectory samples could allow richer simulation.






45–75 min — Generative modeling as scalable forecasting infrastructure

Goal: establish my credentials as generative modeling expert and thinker

(KoVAE +) ImagenTime + ImagenFew: vision diffusion-based models for unified generation of irregularly-sampled, sparse and out-of-distribution time series data
Freq-Synth: Fourier-based synthetic data for zero-shot time series forecasting

In my work on generative time-series modeling, I’ve focused on learning joint distributions over temporal processes rather than just point or quantile summaries. The motivation wasn’t only predictive accuracy — it was controllability, simulation, and structural robustness. A generative model can serve two roles: As a probabilistic forecaster; And as a synthetic data engine. The second role becomes especially powerful at scale — where inference cost, data sparsity, and rare regimes become bottlenecks. The first role is under-explored

1. Generative Coherent Hierarchical Forecasting: I’ve been thinking about whether synthetic generative modeling could go beyond cost reduction and serve as a pretraining mechanism for coherent hierarchical forecasting. For example, one could generate large amounts of structurally coherent hierarchical demand data — bottom-level series that aggregate consistently — and pretrain a model to internalize that structure. Then, when fine-tuned on real data, the model already ‘knows’ hierarchical relationships implicitly, rather than learning them purely from limited real data or relying on reconciliation post hoc. I’m curious whether you see synthetic generation as something that could eventually support foundation-style hierarchical models.
	follow-up: collab. with Mayank and Boris explores Koopman-based modeling

2. Cold-Start SKU Pretraining: Generative pretraining across millions of SKUs could produce structural priors that help cold-start forecasting without per-SKU heavy inference.
	follow-up: How much of forecasting complexity is cold-start driven?

3. Synthetic Data for Rare Regimes: Rare demand spikes are underrepresented in training. A generative model could amplify rare regimes to improve robustness without waiting years for natural data.
	follow-up: Do you explicitly stress-test models under synthetic shock scenarios?



I1: Generative Pretraining for Forecast Foundation Models: Pretrain on: Real + synthetic hierarchical data; Massive cross-SKU corpus; Fine-tune on: Specific categories; Specific regions
I1:  Foundation Forecasting Model for Retail: Large-scale pretraining across hierarchical demand data, augmented with synthetic regimes, producing a foundation forecasting model adaptable to new SKUs with minimal fine-tuning.
	Q: Is SCOT thinking about foundation-style forecasting models?
	position as: Foundation forecasting models with synthetic augmentation

I2: Hierarchically Coherent Synthetic Data: Instead of generating independent SKU data, we generate bottom-level demand jointly and aggregate upward — coherence by construction
I2: Generative Hierarchical Modeling by Construction: Instead of reconciling forecasts post hoc, we build generative models that produce bottom-level demand jointly, so aggregation is coherent automatically.
	Q: Do you think reconciliation will remain necessary long-term, or could structure be embedded directly in generative models?
	Q: Do you see synthetic data generation happening independently per series, or structurally across hierarchy?

I3: Synthetic Data for Evaluation: Could synthetic generative models be used not only for training, but for stress-testing forecasting policies before deployment?
I3:  Synthetic Stress-Testing as Policy Validation Layer: What if synthetic generative models become the sandbox for evaluating new inventory policies before deployment?
	Q: How do you currently stress-test forecasting changes before rollout?


Bring up potential risks yourself: Synthetic data distribution mismatch; Amplifying model bias; Calibration drift; Governance and interpretability; Overfitting to synthetic regimes
	lead with: One thing I’ve been thinking about with synthetic augmentation is the risk of amplifying distribution drift — especially if the generator starts reinforcing its own biases. I’m curious how you think about guarding against that in production.


It feels like generative modeling at SCOT could evolve from being a cost-reduction mechanism into a structural backbone for scalable forecasting — especially for cold-start and rare-event robustness as well as for coherent hierarchical forecasts



75–105 min — What would make SCOT fundamentally better in 3 years?

Goal: Clarify their long-term direction

Q: If we fast-forward 2–3 years, what do you think changes most in SCOT’s forecasting stack?
	follow-up: Do you see generative models staying as synthetic-data engines, or becoming primary forecasters?
	follow-up: What technical bottleneck is currently structural rather than incremental?
	follow-up: What decision constraint limits forecasting impact today?
	follow-up: What is the hardest unsolved forecasting problem at SCOT right now?


Q: How do you balance exploratory research vs production constraints in SCOT?
Q: What kind of research tends to survive deployment?
Q: Are there ideas that look great on paper but break at Amazon scale?


Q: What kind of problems require cross-team coordination?
Q: Is forecasting the main bottleneck, or is it data infrastructure, evaluation, or policy integration?
Q: If you could double investment in one capability — what would it be?

It feels like SCOT has solved coherence and decision alignment at scale. The next frontier might not just be better models, but systems that are robust to distribution shifts, scalable across millions of SKUs, and structurally adaptable.



105–120 min — Closing Phase

Synthesis: This was really helpful. What I’m taking away is that generative modeling at SCOT is less about replacing forecasting and more about building scalable infrastructure — especially for cost reduction, latency, cold-start robustness, and synthetic augmentation. It feels like coherence and decision alignment are already strong pillars, and the next layer may be scalable generative infrastructure that improves robustness at Amazon scale.

Closing questions: 
	Q: Where do you see the biggest technical gaps in the team right now?
	Q: If someone joined and was successful in 18 months, what would they have built?
	Q: What kind of problems would you want them to own?
	Q: Do you see generative modeling becoming a core capability inside SCOT?

Q: Is there a direction we discussed today that feels particularly aligned — or misaligned — with where SCOT is going?

Closing: What excites me most is working at the intersection of generative modeling and decision systems — especially at scale. SCOT feels like one of the few places where forecasting, optimization, and infrastructure genuinely intersect. I’d be very excited to contribute in that space.



Mengfei might ask:
	You don’t have production experience? That’s true — most of my work has been research-driven. But I’ve thought deeply about scalability, system constraints, and 		deployment implications. I’d be excited to learn the production side quickly

	What level are you targeting? I’m primarily focused on scope and impact. I’m confident I can contribute at a senior level, but I’m open to aligning based on team needs 	and where you see the best fit.


New concepts:
	SKU = Stock Keeping Unit (product x variant x packaging x location)




March 19: follow up with Mengfei


I was actually curious to hear your thoughts after the talk; both on the work itself and whether you see directions where it could connect with what your team is building

Next research steps: one thing I’m increasingly thinking about is how to scale generative forecasting in a way that actually works in production settings

Use: generative modeling complements and extends foundation models for forecasting; especially when thinking about efficiency and scalability

I believe generative forecasting opens up benefits such as controllability, synthetic data generation, and few shot adaptation; which might be useful depending on the use case

How do you currently think about the tradeoff between model expressivity and inference cost in your forecasting systems?

s: Generative models are too expensive and don’t scale well

I think that’s a very valid concern—and honestly one of the main challenges. A lot of what I’m thinking about now is exactly how to make these models competitive in terms of latency and cost.
