# Breadth review — calibration, rank, and a cap

One page. From the 29 Oct breadth mock. The formulas are the review, not the answers he gave. Mock: [`mocks.md`](mocks.md). Do not retest this page until it has been read.

## The example

10,000 machines, one score a day, about 1% fail, about 100 failures, at most 200 inspections. A miss costs $20,000. An inspection costs $500. Assume the inspection prevents the failure.

If the $500 is paid only when the machine would not have failed: inspect when \(500(1-p) < 20000 p\), so \(p > 500/20500 \approx 2.44\%\). If every inspection costs $500: \(p > 500/20000 = 2.5\%\). Both lines need a probability, known costs, and an inspection that actually prevents the loss.

Benefit of inspecting machine \(i\): \(B_i = 20500 p_i - 500\). Same costs on every machine, so sorting by \(B\) is sorting by \(p\). Inspect down that list. Stop at 200, or at the first machine with \(B \le 0\), whichever comes first. Fewer than 200 is allowed. If the miss cost or the inspection cost differs by machine, sort by \(B\), not by \(p\).

Score the policy with precision at 200, recall at 200, inspections used, misses, and net dollars. Not AUROC alone.

## Ranking and calibration

Ranking: higher score means higher risk. Calibration: a predicted 20% fails about 20% of the time.

- **Platt.** A sigmoid on the score. Few positives: start here.
- **Isotonic regression.** A nondecreasing map. More flexible. Can overfit a small calibration set, and ties can move AUROC slightly.
- **Temperature.** One scalar on the logits.
- **Histogram binning.** Empirical frequency inside score bins. Coarse.

A strictly increasing map keeps the order, so it does not by itself raise AUROC or precision at K. It does change a threshold written as a probability. Fit the map on held-out data from the factory you will deploy to.

## Precision at K

Precision at K is positives inside the top K, divided by K. Recall at K is those positives divided by all positives. Compute both on each day’s ranking. A global top-200 is not that.

Precision falls as prevalence falls, even when the true-positive rate and the false-positive rate stay fixed:

\[
\mathrm{Precision} = \frac{\mathrm{TPR}\,\pi}{\mathrm{TPR}\,\pi + \mathrm{FPR}\,(1-\pi)}.
\]

True-positive rate 0.8, false-positive rate 0.05: precision is 64% at 10% prevalence and about 13.9% at 1%. A stable AUROC does not say the top 200 are still worth inspecting.

## Still open, and not this page’s drill

The 28 Oct arithmetic is still unanswered in the mock log: 1,000 machines, 40 failures, 8 in the top 10, 12 in the top 20. Do not look up the four rates before computing them.
