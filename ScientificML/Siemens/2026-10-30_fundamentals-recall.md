# Fundamentals recall — 30 Oct 2026

**Kind:** Active recall with feedback after each answer. Not a mock. Mocks stay in [`mocks.md`](mocks.md).
**Scope:** Early stopping, AdamW, dropout, normalization, learning-rate schedules, dataset sampling.
**Status:** Stopped at his request before question 7. Six answers. Scores 8, 4, 7, 3, 7, 8. Average 37/60, about 6.2. The breadth-mock average stays 6.5.

The corrections below are the review. They are not what he said.

---

## 1. Early stopping — 8

Training loss still falls. Validation loss rises after epoch 20. Why is early stopping regularization, how does it differ from L2, and are they equivalent?

He said early stopping picks the validation minimum and, under some assumptions, relates to weight decay because it caps capacity. Weight decay pulls weights toward zero and shrinks the function class. Near an optimum, to second order, the two can be equivalent.

The checkpoint is right. It does not shrink the architecture. It stops the optimizer before later solutions. L2 adds \(\frac{\lambda}{2}\|\theta\|^2\) to the loss. Early stopping adds no penalty.

In linear least squares both act as spectral filters, and the filters differ. Gradient flow from zero gives \(1-e^{-\lambda t}\). Ridge gives \(\lambda/(\lambda+\alpha)\). Similar effect on small eigenvalues. Not the same map, and not a general identity.

## 2. Adam versus AdamW — 4

He said Adam applies weight decay uniformly and AdamW scales it by the weight’s magnitude. He did not know why an L2 term is not weight decay under Adam. A large decay, he said, raises both training and validation loss because the model is simpler.

SGD with an L2 term is multiplicative decay: \(\theta \leftarrow (1-\eta\lambda)\theta - \eta\nabla L\). Adam folds \(\lambda\theta\) into the gradient, then rescales that mix by the moments, so the penalty is no longer a fixed shrink. AdamW keeps the shrink outside the adaptive step: \(\theta \leftarrow (1-\eta\lambda)\theta - \eta\,\hat m/(\sqrt{\hat v}+\epsilon)\).

More decay usually raises the training loss. Validation can fall, then rise. Both losses high means underfitting, not a success.

**Say again before the interview.**

## 3. Dropout — 7

At \(p=0.2\), he said an activation is kept with probability \(1-p\) or zeroed with probability \(p\). At inference it is passed unchanged, because the model learned the connections and should not be rescaled. Dropout is an ensemble in one net. If \(p\) is too high, he said expressivity falls and the model overfits.

The zeroing is right. Inverted dropout multiplies the survivors by \(1/(1-p)\). At \(p=0.2\) that factor is 1.25, so the expected activation stays \(h\). Inference then needs no extra scale. Too much dropout underfits: both losses stay high and learning slows. It does not overfit.

## 4. Batch norm versus layer norm — 3

Input \(X\in\mathbb{R}^{B\times T\times D}\). He said batch norm reduces over \(B\), and layer norm over all dimensions. He did not know why a transformer uses layer norm.

Batch norm, in the usual sequence layout, averages a feature over the batch and the time axis: \(\mu_d = \frac{1}{BT}\sum_{b,t} X_{b,t,d}\). The exact axes depend on the implementation. It depends on the other examples, and inference usually uses running statistics.

Layer norm averages the features of one token: \(\mu_{b,t} = \frac{1}{D}\sum_d X_{b,t,d}\). Same rule in training and in generation. No batch, so a short or padded sequence does not change the statistic. That is why a transformer uses it. RMSNorm is the same family.

Batch norm: one feature across examples. Layer norm: the features inside one token.

**Say again before the interview.**

## 5. Learning-rate schedule — 7

Linear warmup for 5% of steps, then cosine decay. He said early attention maps are bad, so the maximum rate diverges, and warmup ramps the rate. Cosine, he said, alternates fast and slow learning to leave local minima. Too high a rate gives NaNs.

Warmup is right, and it is not special to attention. The moments are also immature. Cosine decay falls smoothly from the peak toward a floor. It does not cycle. Warm restarts are the schedule that raises the rate again. A rate that is too high can diverge. That part landed.

## 6. Dataset sampling — 8

Sets of \(10^6\), \(10^5\), and \(10^4\) windows. He said sampling windows uniformly leaves the sets unequal. Sampling sets uniformly repeats the small set and does not help training. He would sample sets equally and cap the epochs so he knows how often the small set was seen.

The two failures are right. Repeating the small set can memorize it. The missing knob is \(P(i)\propto N_i^\alpha\). \(\alpha=1\) is proportional to size. \(\alpha=0\) is one set, one share. Between them, square-root sampling is about 71%, 22%, and 7% on these three sizes, against 90%, 9%, and 0.9% if every window is equal. Tune \(\alpha\) on per-dataset validation.

## 7. Not taken

Three experiments only. Training loss falls, validation rises, the small sets are worst, and a larger model makes validation worse. He stopped. No score. Do not write the three experiments for him. A later recall can ask this once AdamW and layer norm are fluent.
