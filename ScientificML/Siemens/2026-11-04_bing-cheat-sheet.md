# Bing Xiang — hour 1

**4:00–5:00 AM Thailand** (1:00–2:00 PM Pacific). Breadth or depth. He leads the applied-science team. The other of those two hours is Ramesh. Do not say who assigned the hours, and do not say Danielle’s name.

## 45–60 seconds

I’m an Associate Professor of Computer Science at Ben-Gurion University, on leave and moving into industry research. I work on sequential and generative learning: time series, diffusion, and Koopman representations. Lately I have been building multimodal models that combine those representations with vision-language models. I start from a concrete modeling limit, state a hypothesis, and design the experiment that can kill it. I implement and evaluate that experiment myself. Siemens is interesting because generalization, physical structure, and reliability are the constraints, not optional extras.

## ImagenTime, 30 seconds

We asked whether a time series could be an image, so the vision diffusion stack could be reused. Delay embeddings and a time-frequency transform survived a cheap test. Line plots were too sparse. Gramian angular fields were dense and did not scale. The sampler that cut the cost was EDM, separate from the image step. The paper is ImagenTime, NeurIPS 2024. The claim is that the representation can make the sequential problem tractable. It is not that every series should be an image.

If he asks for a number, one of these: about 58% on short-series discriminative score, or about 133% on long-series classification, against prior diffusion models. Sequences from 24 steps to over 17,000.

If he stays: what each transform keeps, why invertibility matters, the backbone and the sampler as separate ablations, when it fails, why not a 1D diffusion model, and the cost.

## Crisp answers

1. **Diffusion versus autoregressive.** A joint model, flexible conditioning, fidelity against diversity, and a sampling cost. No claim that diffusion wins in general.
2. **Representation versus capacity.** Same backbone, same parameter budget, same training budget, same eval. Swap only the representation. Include a synthetic factor and the inverse map.
3. **Koopman.** An observable \(z=\phi(x)\) with \(z_{t+1}\approx Az_t\), or a controlled extension. Linear latent steps help a long forecast and a controller. They depend on the observables and the regime. One-step accuracy is not a good MPC. A spectral radius below 1 can still have a transient.
4. **Reject a hypothesis.** Gates before the run. A simple baseline. Stop when the targeted metric fails under those gates. Kill the lever, not the objective.
5. **Limited compute.** A small pilot, then a scale check, then a gate. Parameter-efficient tuning. Shared GPUs with a written stop.
6. **Shifts.** Covariate: \(P(X)\) changes, \(P(Y\mid X)\) stays. Label: \(P(Y)\) changes, \(P(X\mid Y)\) stays. Concept: \(P(Y\mid X)\) changes. Prevalence alone is not concept drift.
7. **AdamW.** The L2 term inside Adam enters both moments. AdamW shrinks the weights after the moments. SGD has no moments, so the two forms match.
8. **A scientific generator.** Downstream use, fidelity, a physical residual, rare events, robustness, cost, uncertainty. Not one score.

## Ask two, then stop

- Where is the bottleneck: transferable representations, physical structure, or scale?
- What makes a research idea a platform rather than a one-domain model?
- What does a principal own in the first six months?
- Where does the scientist stop and the engineer start, from the proof of concept through deployment?

## Close

Based on this conversation, which scientific problem would you want this role to own?

## If a story comes up

**A, ImagenTime.** Who disagreed, three kill tests, one number, EDM as the sampler. First person. Invite them into the design of the test. Do not say you will insist they staff it.

**C, the synthetic mix.** Reasoning about 29.5 to 31.2. Temporal relations 26.9 to 21.9. The gates were set first. You stopped the mix. You did not stop the project. “We agreed” is not the decision.
