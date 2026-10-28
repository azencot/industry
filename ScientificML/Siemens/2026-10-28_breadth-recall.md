# Breadth recall — 28 Oct 2026

**Kind:** Concept refresh and recall. Not a mock. Mocks stay in [`mocks.md`](mocks.md).
**Scope:** Class imbalance, calibration, threshold selection, prevalence shift, event-level evaluation.
**Status:** Recall pass done. The breadth mock is still separate.

Guided practice, not a principal-level score. Second set of four concepts was the stronger half.

---

## 1. AUROC vs AUPRC

TPR = recall = TP / (TP + FN). FPR = FP / (FP + TN). Precision = TP / (TP + FP). AUROC is ranking across thresholds. AUPRC is the precision-recall tradeoff. Precision moves with prevalence. One ROC point does not determine AUROC.

**Question.** 10,000 observations, 1% positive, TPR 90%, FPR 5%. TP, FP, and precision.

He had 100 positives and 9,900 negatives, and TP = 90. He used FP = 45. The FPR is on the negatives: FP = 0.05 × 9,900 = 495. Precision = 90 / (90 + 495) ≈ 15.4%.

High recall and a small FPR still leave poor precision when positives are rare.

## 2. Class weighting

Raising the positive weight makes a false negative more expensive. Recall at a fixed threshold usually rises. False positives can rise and precision can fall. Weighting changes training. The threshold changes the decision. Weighting can also wreck calibration.

**Question.** Positive weight from 1 to 100.

He had it: false negatives cost more, the model cuts them, recall rises, false positives can rise. Precision does not have to fall. That depends on how TP and FP move relative to each other.

## 3. Calibration vs discrimination

Calibrated means the stated probability matches the observed frequency. A high AUROC can sit on badly calibrated probabilities.

**Question.** 100 machines each scored 70%. Twenty fail. Calibrated? Does a bad calibration imply a bad AUROC?

He had it: the score overstates the rate (20%, not 70%), and AUROC is ranking, so a calibration miss does not by itself kill AUROC. If those 100 scores are identical, AUROC inside that subset is 0.5. AUROC on the full set can still be high.

## 4. How to measure it

A reliability diagram bins scores and plots mean predicted probability against the observed frequency. Brier score is the mean squared error, \((1/N)\sum_i (p_i - y_i)^2\). It is overall probabilistic quality, not calibration alone. ECE is the bin-size-weighted mean absolute gap, \(\sum_b (n_b/N)\,|\mathrm{freq}_b - \mathrm{conf}_b|\). Binning can hide a miss in a rare high-risk bin.

**Question.** Name three.

He described the reliability diagram and forgot the name. He had the Brier score and what it computes. He did not have ECE. He then got the distinction: Brier is per sample, the diagram is per bin.

Priority: reliability diagram, Brier, ECE, and what each one is.

## 5. Post-hoc calibration

Platt scaling is a sigmoid on the scores. Few parameters, so it is the start when positives are scarce. Isotonic regression is a flexible nondecreasing map and overfits when failures are few.

**Question.** 100,000 rows, 50 failures. Platt or isotonic?

He chose Platt. Right.

A strictly increasing map keeps the ranking, so AUROC stays. Isotonic regression can tie scores and move AUROC a little. He first reached for class weights and an FP/FN search. Those are the wrong knobs.

- Class weight changes the training objective.
- The threshold changes the decision.
- Platt or isotonic changes the probability.

## 6. Cost threshold

Alert when the expected cost of alerting exceeds the expected cost of staying quiet: \((1-p) C_{FP}\) versus \(p\, C_{FN}\), so \(p > C_{FP}/(C_{FP}+C_{FN})\), if the probability is calibrated and there is no alert cap.

**Question.** A false alarm costs $100. A miss costs $9,900. The model says 3%. Alert?

Threshold = 100 / 10,000 = 1%. 3% is above it, so alert. He had the arithmetic. The formula assumes known costs, a calibrated \(p\), and no capacity cap.

## 7. Prevalence shift

If TPR and FPR stay fixed and prevalence falls, precision falls. Under pure label shift, \(P(x\mid y)\) stays and \(P(y)\) changes. The probabilities may need a new calibration.

**Question.** Train at 10% positive, deploy at 1%, TPR and FPR unchanged. Precision?

He had it: true positives drop about tenfold, the negative mass grows, precision drops.

\[\mathrm{Precision} = \frac{\mathrm{TPR}\cdot\pi}{\mathrm{TPR}\cdot\pi + \mathrm{FPR}\cdot(1-\pi)}\]

## 8. Event-level evaluation

A pointwise metric counts repeated alerts on one failure as many successes. Event recall is distinct failures found. Also lead time, false alerts per machine per day, and deduped events.

**Question.** 20 failures. The model hits 15 of them with 150 alerts, plus 50 unrelated false alerts. Event recall, and why “200 alerts” misleads.

Event recall = 15/20 = 75%. He had that. The 150 alerts are 15 failures said many times. The 50 are not detections. Those 50 may be fewer than 50 false events after deduping. Event precision needs a definition of an event. He did not need one to answer, and it is not determined by the counts alone.

---

## Discrimination vs calibration

| Model | AUROC | ECE |
|-------|-------|-----|
| A | 0.95 | 0.20 |
| B | 0.85 | 0.02 |

He picked B for ranking machines into preventive maintenance, because the probabilities were calibrated. For a fixed inspection budget, A is the better ranker. For insurance prices, B is the better probability. AUROC is not precision at the top of the list. ECE is not the whole probability score. Brier, log loss, and calibration inside a subgroup still matter. The metric follows the decision: rank, probability, or an action under a constraint.

---

## What to redo

1. Weight, threshold, and post-hoc calibration are three different edits.
2. AUROC, precision at K, and calibration answer different decisions.
3. Names: reliability diagram, Brier, ECE.
4. One arithmetic slip: FPR times the negative count, not a small invented FP.

Conceptual understanding and the cost and prevalence answers were strong. Terminology and the ranking-versus-probability choice need another pass. Do not treat this page as a mock score.

## Still open, before the breadth mock

**A.** XGBoost trained with positive weight 100. AUROC is high. Failure probabilities are systematically too high. What do you do before an expected-cost threshold?

**B.** The crew can inspect 10 machines a day. Do you pick the model by AUROC, ECE, precision at 10, or Brier?

**C.** Every machine gets the same score, equal to the base rate. Can that be calibrated? Can discrimination be poor?

**D.** Prevalence 0.5%, TPR 90%, FPR 1%. Precision?
