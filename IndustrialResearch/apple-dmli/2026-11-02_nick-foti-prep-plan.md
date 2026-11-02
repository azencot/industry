# 2026-11-02 — Nick Foti prep plan

Updated the same day after Masha Fedzechkina’s LinkedIn post. Live questions: [`2026-11-02_questions-for-nick.md`](2026-11-02_questions-for-nick.md). Patching session: [`2026-11-02_activation-patching-session.md`](2026-11-02_activation-patching-session.md).

| | |
|---|---|
| **Person** | Nick Foti, Principal Research Scientist, Seattle. Hiring manager. |
| **Role** | AIML — Sr Machine Learning Research Scientist, Data and ML Innovation. Seattle, WA. Req **200668189-3337**. |
| **Next** | Interactive pass on *LLMs are not (consistently) Bayesian*. Then the multimodal project presentation. |
| **Do not claim** | Established expertise in mechanistic interpretability or Bayesian inference. Transferable research skill and real interest only. |

Strategy lock still holds: [`2026-10-22_strategy.md`](2026-10-22_strategy.md). Do not open with Health, Sapiro, or Ozan.

## 1. Masha Fedzechkina’s LinkedIn post

Omri’s reading of a public post. Not re-checked against LinkedIn here. The post advertises an Apple PhD research internship on understanding foundation models and improving their reliability. It is not necessarily Nick’s req. The themes overlap the JD and the August 2026 paper. Masha Fedzechkina is a coauthor on that paper.

Her question, as he recorded it: “What does it take to build models that know what they know and say what they know?”

Three directions:

1. **Internal representations.** What information do foundation models encode internally?
2. **Representation–output alignment.** Why do models fail to express information they appear to possess?
3. **Early training and representation formation.** Can better inductive biases and training procedures prevent these discrepancies?

Methods named in the post: representation probing, training models from scratch, controlled synthetic experiments, and behavior across conditions and scales.

## 2. How to read the seat

The team looks interested in how foundation models acquire, organize, and express knowledge. That can include how training procedures shape internal representations and downstream reliability, not only analysis of a frozen pretrained model.

Priorities, in order:

1. **Representation learning and reliability.** What is encoded. What downstream components can read. What actually influences the prediction. Why a representation and the expressed output can disagree.
2. **Controlled experiments.** A falsifiable hypothesis. Synthetic data that isolates one mechanism. Counterfactuals and distribution shift. Correlation, decodability, and causal influence kept apart.
3. **Training dynamics and inductive biases.** How architecture and objective shape the representation. Whether structured representations improve reliability. Whether an early training intervention prevents a later failure.
4. **Bayesian reasoning.** Posterior inference and uncertainty. Probabilistic consistency. Belief updating. Calibration versus a coherent probabilistic update.
5. **Mechanistic interpretability.** Activation patching, causal tracing, probing, and the limits of an intervention.

## 3. Alignment

**Structured representation learning — strong conceptual fit.** Koopman VAEs, sequential disentanglement, structured latent dynamical models. The work is about how architecture and objective shape representations of sequential observations. That is the link to early representation formation and later reliability.

**Multimodal foundation models — strong practical fit.** Time-series representations for vision-language models, dual-view representations, multimodal alignment, Qwen adaptation, LoRA, controlled evaluation. Two views of the same series are a way to ask which scientific properties are encoded, which survive alignment, and which are expressed in language.

Proposed extension, not a completed experiment:

1. Probe visual representations for temporal properties.
2. Compare those probes with the language-model answers.
3. Find representation–output discrepancies.
4. Intervene to see where the information is lost or ignored.
5. Test whether another training objective improves the alignment.

**Generative modeling — supporting fit.** Diffusion, scientific time-series generation, data-scarce learning. A generator with known factors can supply the synthetic experiments in which those factors are manipulated separately.

## 4. Positioning

The through-line is how models learn representations of complex data, and how architecture and objective change those representations. The recent work asks the same question for multimodal models that connect continuous scientific data to a pretrained vision-language model.

The interest to state: what the model represents, how that information influences the prediction, and how training can improve reliability. Benchmark score is not the point.

Do not claim a record in mechanistic interpretability or Bayesian inference.

## 5. Questions

Current wording is in [`2026-11-02_questions-for-nick.md`](2026-11-02_questions-for-nick.md). Q3 now asks whether the gap in Masha’s post, and early training as a cause of that gap, is one of the team’s directions. Q5 combines independence and what success looks like after a year.

## 6. Next session — the paper

*LLMs are not (consistently) Bayesian: Quantifying internal (in)consistencies of LLMs’ probabilistic beliefs.* Chacha Chen, Matthew Jörke, Adam Goliński, Masha Fedzechkina, Guillermo Sapiro, Sinead Williamson, Nicholas Foti. Correspondence: Nicholas Foti. [arXiv:2605.06915](https://arxiv.org/abs/2605.06915). [Apple ML Research](https://machinelearning.apple.com/research/llms-not-consistently-bayesian).

Interactive, one question at a time, critique the answer. Stay on the paper’s method and conclusions. Do not recite a summary that has not been worked through in that pass.

Cover, in the Q&A:

1. Central hypothesis.
2. Definition of Bayesian consistency.
3. Experimental methodology.
4. Main findings.
5. Expressed probabilities versus internal beliefs.
6. Limitations and alternative explanations.
7. Implications.

## 7. Status

Done, as of this update:

- Basic Bayesian inference tutorial and recall.
- Activation patching and causal tracing, at introduction level. Session: [`2026-11-02_activation-patching-session.md`](2026-11-02_activation-patching-session.md).
- Mechanistic-interpretability recall.
- Scientific-reasoning versus shortcut mock. Score on file: 6.5/10. A successful patch was treated as evidence of scientific reasoning.
- Five interview questions, revised after the post.
- Positioning revised around representation, expression, and training.

Still open:

- The paper Q&A above. This is the next session.
- Multimodal project presentation, after that paper.
- Patching follow-up, if mech-interp comes back: a head that flips a wrong answer to the scientific one may encode the relationship, or only the answer. Unanswered in the session log.
- ROME corruption-and-restore in detail. No hands-on patching implementation yet.

Teaching constraints that still apply: one question at a time, derive what matters, do not pretend he has run these methods, separate established technique from open research, no generic behavioral questions.
