# 2026-11-02 — Nick Foti prep plan

Talk prep for later today. Interactive tutorial. Multimodal project presentation is deferred until Omri asks for it.

| | |
|---|---|
| **Person** | Nick Foti, Principal Research Scientist, Seattle. Hiring manager. |
| **Role** | AIML — Sr Machine Learning Research Scientist, Data and ML Innovation. Seattle, WA. Req **200668189-3337**. |
| **Team brief** | Fundamental research on how foundation models work and how to expand them in scientific domains. |
| **Status** | Plan logged 2026-11-02. Bayes 1A explained, check unanswered. Activation patching and causal tracing introduced the same day; session log and the resume question are in [`2026-11-02_activation-patching-session.md`](2026-11-02_activation-patching-session.md). |

Strategy lock still holds: [`2026-10-22_strategy.md`](2026-10-22_strategy.md). Do not open with Health, Sapiro, or Ozan. The paper to know before Part C is *LLMs Are Not (Consistently) Bayesian* (Apple ML Research, August 2026). Verify findings from the paper. Do not invent them.

## Gaps to close today

Omri’s background is generative modeling, diffusion, Koopman operators, dynamical systems, sequential representation learning, and multimodal foundation models. He is an Associate Professor of CS at Ben-Gurion University.

He does not have working familiarity with:

1. Bayesian statistical methods for scientific inference.
2. Activation patching.
3. Causal tracing and mechanistic interpretability.

Do not pretend he has hands-on experience with methods he has not used.

## What the req asks for

- Design robust experiments on the internals of foundation models.
- Implement experimental pipelines.
- Analyze and interpret results.
- Bayesian statistical methods for scientific inference.
- Experiments on foundation-model behavior.
- Activation patching and causal tracing.
- A coherent research story from an ambiguous question.

Nick’s public line: Bayesian statistical modeling, probabilistic inference, dynamical systems, and recent work on foundation models and probabilistic reasoning in LLMs.

## How to teach

- Assume probability, linear algebra, optimization, neural nets, diffusion, and modern ML research.
- Do not assume specialized Bayesian or interpretability vocabulary.
- Skip introductions to mathematics he already knows.
- Derive the important equations. Connect them to scientific inference and foundation models.
- One topic, then one question. Wait. Critique the answer. Then continue.
- Track weaknesses and revisit them.
- Separate established methods from open research.
- No generic behavioral questions.
- No multimodal project prep until he asks.

## Modules

### 1 — Bayesian statistical methods (35 min)

**Part A — Foundations.** Prior, likelihood, posterior, evidence. MAP vs MLE. Posterior predictive. Credible vs confidence intervals. Aleatoric vs epistemic uncertainty. Misspecification and posterior predictive checks. Each item: definition, formula, why it matters for scientific inference, one sequential or scientific example.

**Part B — Computation.** Why MCMC and HMC exist, assumptions, limits. No HMC implementation. Variational inference and the ELBO. Amortized inference. Approximate Bayesian inference in deep learning. Pay attention to variational inference, VAEs, and diffusion, because that is his background.

**Part C — Bayesian reasoning in LLMs.** What it would mean for an LLM to be Bayesian. How to test consistent belief updates. Calibration vs coherent Bayesian updates. Why a useful model need not be Bayesian. Experiment design. Connect to Foti’s probabilistic-reasoning work only after the paper is checked.

**Assessment.** 3–4 questions, one at a time. At least one derivation and one experimental design. Critique missing points.

### 2 — Activation patching (25 min)

Question: which internal computations causally contribute to a behavior?

Correlation vs intervention. Clean and corrupted inputs. Caching activations. Patching them across runs. Effect on a target output. Layers, heads, positions. Positive and negative results. Standard workflow on a small factual or temporal Transformer example.

Caveats: off-distribution interventions, choice of corruption, confounding and interactions, what one head cannot mean, why a successful patch is not a unique localized mechanism.

**Assessment.** He designs a patching experiment. Judge whether it supports a causal claim.

### 3 — Causal tracing and related methods (20 min)

Causal tracing in mechanistic interpretability. Relation to activation patching. The ROME line. Causal tracing vs statistical causal discovery. Comparison: activation patching, probing, attention maps, model editing — what each can and cannot establish. Comparison table.

Then a scientific foundation-model case: a multimodal model sees a time series and answers questions about order, trend, and periodicity. How to tell internal temporal order from a superficial visual shortcut. Synthetic controls, counterfactuals, probes, interventions, behavior, negative controls.

**Assessment.** He designs an experiment that separates temporal reasoning from shortcut learning. Challenge the assumptions.

### 4 — Integration (10 min)

Three questions Nick might ask, with no answer given first:

1. How would you test whether an LLM performs Bayesian belief updating?
2. How would you tell whether a foundation model internally represents a scientific concept?
3. How would you design a research program on the limitations of foundation models on scientific data?

Score each answer on correctness, experimental rigor, clarity, missing controls, novelty, and whether it sounds like an independent senior research scientist. Offer a stronger answer when the reply is weak.

## Session log

| Module | State |
|--------|--------|
| 1A Foundations | Explained 2026-11-02. Forecast-interval check not answered. |
| 1B Computation | Not started |
| 1C LLMs and Bayes | Not started. Verify the August 2026 paper before citing results. |
| 1 assessment | Not started |
| 2 Activation patching | Introduced 2026-11-02. Recall exercise done. Mock scored 6.5/10: a successful patch was treated as evidence of scientific reasoning. Log: [`2026-11-02_activation-patching-session.md`](2026-11-02_activation-patching-session.md). |
| 3 Causal tracing | Introduced as systematic patching, including the probe/patch/attention distinction. ROME corruption-and-restore detail not yet covered. |
| 4 Interview simulation | One research-design mock done inside the patching session. The three planned questions are not started. |
| Resume question | Does a head that flips an incorrect prediction to the scientific answer encode the relationship, or only the answer? Unanswered. Start here for mech-interp. |
| Multimodal presentation | Explicitly deferred |
