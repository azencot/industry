# Breadth rapid-fire — 30 Oct 2026

**Kind:** Five questions, feedback after each one. Not a full mock. The three breadth mocks stay at 6.5. Do not average 8.1 into that number. Mocks stay in [`mocks.md`](mocks.md).
**Scores:** 7.5, 8.5, 8.5, 8.5, 7.5. Average 8.1.
**Against the morning recall:** AdamW 4 to 8.5. Layer norm 3 to 8.5. Those two do not need another dedicated pass. The next breadth question should not name the topic.

The corrections are the review. They are not what he said. The behavioral review of stories A and C was deferred for this session.

---

## 1. Overfitting — 7.5

Train loss 0.8 to 0.15 over 30 epochs. Validation 0.9 to 0.45 in 10 epochs, then up to 0.65. Same distribution.

He called it overfitting. To check, he would fine-tune the trained model on the validation set. If that failed, he would call it imbalance. Then early stopping, weight decay, dropout, fewer weights, and resampling. He would grow the model only after balancing, and only if the regime was then underfit.

The name and the three regularizers are the improvement on the morning mock, where a larger model came first. Do not fine-tune on the validation set. That spends it. Read the curves, check eval mode and the preprocessing, and cut errors by horizon and by regime. The prompt already said the two sets match, so resampling is not the next hypothesis. Order: the checkpoint near epoch 10, then weight decay or dropout, then a smaller model if the gap remains. More capacity only if the curves say underfit.

## 2. Adam versus AdamW — 8.5

He said an L2 term inside Adam puts the decay into the first and second moments. AdamW estimates those moments from the loss and shrinks the weights after. SGD uses only the gradient, so the two forms match. Adam rescales the penalty. He tied the practical gain to warmup: AdamW keeps the decay out of the moments while they settle.

The split of the updates is right. The practical gain is a shrink that Adam does not rescale, so the learning rate and the decay can be tuned apart. The decay is still multiplied by the learning rate, including during warmup. It is not “left out of warmup.”

No further dedicated pass unless it slips.

## 3. Batch norm versus layer norm — 8.5

\(X\in\mathbb{R}^{B\times T\times D}\). He said layer norm over \(D\), and BatchNorm1d over \(B\) and possibly \(T\). A transformer has variable length, variable batch, and an inference pass that is not the training pass. Layer norm does not use running statistics, and it is per token, so length and batch can change. At batch size 1, he said, layer norm is unchanged and batch norm has variance zero, so the mean depends on epsilon and the step is unstable.

The axes and the reason for layer norm are right. Variance is not automatically zero at batch size 1. If \(T=100\), that feature still has 100 positions. The statistic is just noisier, and the positions are correlated. The broken case is \(B=T=1\): training-mode BatchNorm1d cannot form a variance, and PyTorch errors. Keep that one limit. Do not drill the rest again.

## 4. Imbalance — 8.5

Prevalence 0.5%, accuracy 99.2%, AUROC 0.96, precision 12%, recall 80%.

He said precision means many false alarms, and he would not call the model good without calibration and the two costs. AUROC is whether a random positive ranks above a random negative, and it misleads when positives are rare. He asked for AUPRC, precision at K, recall at K, calibration, and the costs.

That is the deployment list. He did not check that the four rates cannot be one confusion matrix. Prevalence 0.005 and recall 0.8 put true positives at 0.4% of the rows. Precision 0.12 then puts false positives near 2.93% of the rows. False negatives are 0.1%. Accuracy is about 97.0%, not 99.2%. Read the matrix before interpreting it. Also the inspection cap, lead time, and the cut by machine and regime.

## 5. Leakage — 7.5

Five years, hourly, 200 machines. A random 80/10/10 split of overlapping windows.

He said leakage in time, across machines, and across factories, so the score flatters generalization. He would split time, then hold out machines, then hold out factories. Unseen machines, he said, were already in that plan.

The three axes are right. Say the leak: a window on steps 1–100 and a window on steps 2–101 share 99 points, so a random cut trains on the test. Do not always stack all three splits. Match the deployment. Future times on known machines: a chronological cut, and a gap so the target does not cross it. Unseen machines: no row from those machines in train or in model selection. Unseen factories: a factory holdout, which is a harder claim. Future times on unseen machines: both the group holdout and the time cut.

## Next

Not another named quiz on AdamW or layer norm. One failure, with the cause unnamed. Rank the hypotheses, name the cheap test, then the change, then how to know it worked. Design stays on the token, the loss, and latency versus throughput. Standard EM is still five minutes, and it is not the Closing the Loop theorem. Stories A and C were not reviewed.
