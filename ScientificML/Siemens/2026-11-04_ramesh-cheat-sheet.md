# Ramesh Nallapati — hour 3

**6:00–7:00 AM Thailand** (3:00–4:00 PM Pacific). Breadth or depth, whichever Bing did not take. Do not say who assigned the hours, and do not say Danielle’s name.

## 45–60 seconds

I’m an Associate Professor of Computer Science at Ben-Gurion University. I work on sequential and generative modeling: time series, diffusion, and Koopman representations. Recently I have been in the multimodal system myself: the data, the LoRA stages, and the eval gates. The question I keep is why a representation works, and where it stops generalizing. I want that standard on scientific ML at a scale I cannot get from one lab.

## Anchor

Chart views carry numerical scale. Delay embeddings carry dynamics that a chart flattens. I want the internal state that makes that difference, not only the end-task score.

The experiment: a synthetic series with one factor, a linear trend. Chart and delay views through the pretrained VLM. Hidden states by layer. Can the probe recover the sign and the size of the trend. Flip the trend as a counterfactual. Repeat for peaks, seasonality, and noise. Hold the rendering fixed. A probe shows the factor is decodable. It does not show the model uses it. Use a patch, an ablation, or the counterfactual for use.

Hands-on: Qwen3-VL-8B, two views, DINO and LM LoRA, gates, parse failures tracked. If a number is required, name the set. On TSRBench, plot-only was 45.2 and plot plus delay was 53.2. Plot plus plot was 44.8 and delay plus delay was 42.6. The prediction slice moved from 38.0 to 61.7. TSExam stayed flat at 89.9 for both. One number, then stop.

## If he goes deep

1. A falsifiable claim, and the other explanation.
2. A rendering shortcut: reversed trend, shuffled axes, matched visual statistics, then an intervention.
3. A probe is decodability. Patching, ablation, or a counterfactual is use.
4. More data, a bigger model, or a higher LoRA rank: same base model, matched budget, seeds, a held-out domain. A higher training loss with better validation accuracy is generalization. It is not a reason to raise the rank.
5. Chart, delay, or raw 1D: match the task. Say what the map drops, what the render costs, and what bias you are refusing to learn.
6. Diffusion training draws a noise level. Sampling integrates a reverse SDE or a probability-flow ODE in order.
7. Five steps: a longer integration interval and a larger local error. A better sampler or distillation can hold quality. EDM is a sampler, not a new claim.
8. Koopman: a finite matrix is an approximation. Long-horizon error, a bad observable, a new regime, and a control the training set never saw. One-step accuracy is not a good MPC.
9. Scarce labels: a simple baseline, seeds, a sensitivity check, a real holdout, and the negative result.
10. InfoNCE is a negative log of a softmax of similarities. A smaller temperature sharpens it. More negatives add hard contrasts, cost, and false negatives. Two series can share a trend and still be a false negative pair.

## Breadth, if it turns that way

- LoRA rank up, training loss down, validation worse: overfit. Checkpoint first, then a lower rank. Do not open with a shift.
- L1 can zero a weight. L2 shrinks it.
- Double the batch, same tokens: half the optimizer steps. A larger learning rate is something to test. It is not automatic. Rewrite warmup and the decay for the new step count.
- Attention is \(O(T^2 d)\) compute and \(O(T^2)\) memory for the scores. A patch trades a short transient for that cost.
- AUROC can hold while the probabilities drift. Recalibrate on recent labeled data, and score the map on a slice you did not fit.

## Shifts, one sentence each

Covariate: \(P(X)\) changes, \(P(Y\mid X)\) stays. Label: \(P(Y)\) changes, \(P(X\mid Y)\) stays. Concept: \(P(Y\mid X)\) changes. A new labeling manual is not label shift. A higher defect rate is not concept drift.

## Ask two, then stop

- Which scientific problems have failed to transfer across machines or regimes?
- When do you want a physical structure, and when a general model?
- What evidence has to exist before the group funds a new direction?
- Where would a shared benchmark change more than another model?

## Close

Which direction has room for a real scientific contribution in the next year?

## Papers

Say what you did. Fadlon and Arbiv lead Closing the Loop. The classical ELBO is not that paper’s theorem. If he picks a paper you did not implement, say the part you can defend and the part you cannot.
