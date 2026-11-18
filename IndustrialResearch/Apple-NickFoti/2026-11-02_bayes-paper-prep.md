# 2026-11-02 — Bayes paper prep

Introductory understanding. Not mastered. Do not mark this paper completed.

| | |
|---|---|
| **Paper** | *LLMs are not (consistently) Bayesian: Quantifying internal (in)consistencies of LLMs’ probabilistic beliefs* (2026) |
| **Link** | [arXiv:2605.06915](https://arxiv.org/abs/2605.06915) · [PDF](https://arxiv.org/pdf/2605.06915) |
| **Authors** | Chacha Chen, Matthew Jörke, Adam Goliński, Masha Fedzechkina, Guillermo Sapiro, Sinead Williamson, Nicholas Foti. Correspondence: Nicholas Foti. |
| **Status** | Ready for a high-level conversation. Not ready for a technical deep dive. |

Plan: [`2026-11-02_nick-foti-prep-plan.md`](2026-11-02_nick-foti-prep-plan.md).

## What is in hand

About 15 minutes of explanation plus his own reading. He can state the question, why it matters, the basic method, and the broad finding. He cannot yet derive the gap, walk the experimental setup, or interpret the results in depth.

**Question.** Does an LLM update probabilistic beliefs consistently with Bayes’ rule?

Two properties, not the same thing:

- **Bayesian consistency.** Given the model’s own prior and likelihoods, does the reported update match Bayes’ rule?
- **Predictive accuracy.** Is the prediction correct?

A consistent update of a bad likelihood can predict badly. An accurate prediction need not be a Bayesian update. Forcing the Bayesian calculation need not help, if the useful map is implicit and the explicit likelihood is worse. That is the link to the team’s interest in a representation the model does not express.

**Method, as he has it.** Elicit a prior over hypotheses, likelihoods for the evidence, and a post-data distribution. Build the Bayesian reference from those elicited prior and likelihoods. Compare the reported post-data distribution to that reference. The true data-generating distribution is not required.

Numerical check he now has. Model says \(P_M(H_1)=0.6\), \(P_M(H_2)=0.4\), \(P_M(E\mid H_1)=0.8\), \(P_M(E\mid H_2)=0.2\). Bayes gives

\[
P(H_1\mid E)=\frac{0.8\cdot 0.6}{0.8\cdot 0.6+0.2\cdot 0.4}=\frac{0.48}{0.56}\approx 0.857.
\]

A report of 0.65 is inconsistent with that reference. This does not say the model’s prior was true.

**Two settings.**

- **Belief propagation.** Prior and likelihoods are in context. The model updates as evidence arrives. Closer to Bayesian.
- **Batch.** Evidence arrives together. The model states probabilities over hypotheses directly. Often less Bayesian, and often more accurate.

**Finding he will say.** Batch can beat explicit Bayesian propagation on the task while agreeing less with Bayes. The interpretation on the table: a useful discriminative map, and a less reliable explicit likelihood. That interpretation is not an established internal mechanism.

## Information processing gap

His current statement: \(\Delta(q)=D_{\mathrm{KL}}(q\mid p)\), with \(q\) the elicited post-data distribution and \(p\) the Bayes posterior from the elicited prior and likelihoods. Larger means more disagreement. He has not derived it.

The paper’s definition, for the next derivation, not yet worked:

\[
\mathrm{I}_{\mathrm{in}}\triangleq\mathrm{I}[\pi]+\mathrm{I}[\ell],\quad
\mathrm{I}_{\mathrm{out}}\triangleq\mathrm{I}[q]+\mathrm{I}[Z_{\pi,\ell}],\quad
\Delta(q)\triangleq\mathrm{I}_{\mathrm{out}}-\mathrm{I}_{\mathrm{in}}=D_{\mathrm{KL}}(q\parallel p)\ge 0.
\]

\(q\) is the elicited post-data distribution. \(p\) is Bayes applied to the elicited prior \(\pi\) and likelihood \(\ell\). The gap is zero only when \(q=p\). The paper ties \(\Delta(q)\) to the ELBO. He has not done that derivation.

Decomposition he still needs, from Sec. 2.1: \(\Delta(q)=D_{\mathrm{KL}}(q\parallel\pi)-\mathrm{I}_{\mathrm{LER}}\). Right-direction but short of the Bayes move is under-updating. Right-direction and past it is over-updating. Wrong-direction means the new evidence has lower expected log-likelihood under \(q\) than under the prior.

## Q&A

**Q1. Inaccurate prior versus inconsistent updating.** Why separate them, and how would you test it? Score **7/10**.

He separated the initial belief from the processing of new evidence, and he reached for synthetic data with a known distribution. He did not yet see that the reference posterior is built from the model’s own elicitations. The numerical example above is the correction.

**Q2. Not answered.** How do you tell these apart?

- A. The internal update itself is inconsistent with Bayes.
- B. The internal update is consistent, and the verbalized probabilities are not.

The session moved to the explanatory guide before this question. Still open.

## Distinctions to keep

- Consistency is not accuracy. A correct Bayes update of a misspecified prior or likelihood can still predict badly.
- Expressed beliefs are not internal representations. Inconsistency among elicited numbers does not show that the internal computation is non-Bayesian.
- A probe is not causal use. Decoding a quantity from activations does not show the model uses it. An intervention is the stronger test.
- A better prediction is not a better probabilistic model. An implicit map can beat Bayes on the elicited likelihoods and still be incoherent.

## Connection, not a completed experiment

Controlled task with known probabilistic structure. Probe intermediate representations for the probabilistic quantities. Compare the probe with the verbalized probabilities and the final prediction. Where they disagree, intervene to test whether the decoded information affects the prediction. Then ask whether a training objective tightens that agreement. Proposed only.

## Still to learn

1. **Math.** Derive \(\Delta(q)\). Its relation to KL and the ELBO. Formal under-updating, over-updating, and wrong-direction updating.
2. **Method.** How priors and likelihoods are elicited. How sequential evidence is handled. BP versus batch, including confounds. Metrics and controls.
3. **Results.** Which figure shows what. What holds across models and datasets. What is a result and what is an explanation.
4. **Critique.** Limits of elicited probabilities. Confounds in BP versus batch. Using a stronger model as a likelihood reference. An experiment that separates the explanations.
5. **Discussion.** 60–90 seconds. The surprising finding. One limitation. One follow-up. The link to representation learning and scientific foundation models.

## Readiness

| Piece | State |
|-------|--------|
| Question and motivation | Basic |
| Consistency versus accuracy | Basic |
| Reference posterior | Simple numerical example only |
| Information processing gap | Concept only. Derivation not done. |
| Experimental method | Partial |
| Detailed results | Limited |
| Critical analysis | Not practiced enough |
| With Nick | High-level yes. Deep dive no. |

## Next session

Do not open with another summary. One question at a time.

1. Reconstruct the Bayesian reference and \(\Delta(q)\).
2. One concrete example from the paper, start to finish.
3. The central figures.
4. One limitation and a follow-up experiment.
5. A short mock discussion.

Q2 above is still unanswered. It belongs in the critique, after the derivation.
