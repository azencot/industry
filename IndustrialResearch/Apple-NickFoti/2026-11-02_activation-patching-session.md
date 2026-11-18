# 2026-11-02 — activation patching and causal tracing

Session log for the Nick Foti conversation. Interviewer context: Nick Foti, Apple AIML — Data and ML Innovation. Topic this session: activation patching and causal tracing.

Plan of record: [`2026-11-02_nick-foti-prep-plan.md`](2026-11-02_nick-foti-prep-plan.md). Resume here, not on the multimodal presentation.

## Concepts reviewed

### Activation patching

Intervention-based interpretability. The question is which internal computations causally influence a behavior.

Standard procedure:

1. Construct clean and corrupted inputs.
2. Run the model and record intermediate activations.
3. Replace selected activations in the corrupted run with the corresponding activations from the clean run.
4. Measure the effect on the output, typically logits or a logit difference.
5. Repeat across layers, token positions, or components such as attention heads.

A successful patch shows that the intervention causally influences behavior. It does not show that the patched component implements a particular reasoning mechanism.

### Causal tracing

In the ROME line, the method corrupts input representations and restores selected internal activations. Restorations that recover the original prediction mark components that causally influence that behavior.

Causal tracing is a systematic form of activation patching, not a separate methodology.

### Probing, patching, attention, tracing

| Method | What it establishes |
|--------|---------------------|
| Linear probing | The target is decodable from the representation. |
| Activation patching | Intervening on the representation changes behavior. |
| Attention visualization | A description of attention patterns. Not causal importance. |
| Causal tracing | Systematic interventions on where information is localized and how it flows. |

Information being represented does not imply that the model uses it to generate the prediction.

Three claims, in increasing order of evidence required:

1. The model encodes the information.
2. The model uses the information.
3. A component implements a particular computation or scientific relationship.

## Recall exercise

A linear probe on layer 12 activations predicts the country of a historical figure at 95% accuracy.

**A. Can we conclude that the model uses this information?**

No. The information might be propagated and modified by later layers.

**B. How could activation patching help?**

Intervene on layer 12 activations and measure the change in output logits. Look at later layers to see how the information propagates.

**C. Why might patching produce no effect?**

1. Redundant pathways let the model bypass the corrupted representation.
2. Later layers reconstruct the relevant representation from information stored elsewhere.

**Feedback.** The presence/use distinction is right, and so is the intuition about distributed, redundant computation. Corrections: a successful probe establishes decodability, not causal involvement. Patching needs designed clean and corrupted inputs, not an arbitrary perturbation. A negligible patch effect does not establish that the representation is irrelevant. Conceptual understanding is in place. Experimental specificity is the gap.

## Mock — scientific reasoning vs shortcuts

**Question.** A pretrained transformer does well on a scientific reasoning benchmark. The suspicion is that it uses superficial correlations. How do you investigate that with internal representations and causal interventions?

**Answer given.**

1. Generate activation traces for two input-output pairs.
2. Choose pairs with similar statistical correlations and different scientific requirements.
3. Patch corrupted activations with clean activations.
4. Measure logit changes.
5. Repeat across tokens, layers, and activations to build an intervention map.
6. If patching shifts logits toward the scientifically correct answer, conclude that the model performs scientific reasoning.

**Score: 6.5/10.** Controlled pairs, the patching procedure, and systematic layer/token interventions are right. The conclusion is not. A successful patch shows that the intervention causally influences the output. The patched activation may encode a shortcut, the correct answer, or something else unrelated to the scientific relationship.

**Design to use instead.** Hypothesis, then controlled data, behavioral evaluation, representation analysis, causal intervention, qualified conclusion.

1. Define the scientific capability under test.
2. Name the plausible shortcut features.
3. Build examples that vary the scientific relationship and the shortcuts independently.
4. Evaluate behavior when the shortcuts are unreliable.
5. Probe internal representations for the scientific variables.
6. Patch those representations to test whether they influence the prediction.
7. Include negative controls and matched examples.
8. State only what the result establishes.

Controls:

- **Shortcut.** Superficial correlations predict the wrong answer.
- **Matched.** Irrelevant surface features change. The scientific relationship stays fixed.
- **Intervention.** Patch activations from an unrelated example, to test whether the effect is specific.

## Unanswered follow-up — resume here

The session stopped before this question:

> Suppose activation patching identifies an attention head whose intervention consistently changes an incorrect prediction to the scientifically correct one. How would you determine whether the head actually encodes the scientific relationship rather than merely carrying information about the correct answer?

Directions already named, not yet answered:

- Interventions that manipulate the scientific variable and the answer identity separately.
- Generalization across scientific scenarios.
- Controls that keep the answer fixed and change the underlying relationship.
- Whether the component encodes an intermediate variable or only output-related information.

This is the first question when mechanistic-interpretability prep resumes, unless another interview topic takes priority.

## What this session finished

- Introduction to activation patching.
- Introduction to causal tracing, at the level of its relation to patching.
- Probing versus causal intervention.
- One recall exercise.
- One mock research-design question.

## Still open

- The follow-up above.
- Causal tracing in more detail, including the ROME corruption-and-restore setup.
- A practical activation-patching implementation.
- Further research-design exercises.
- These methods on multimodal time-series foundation models.
- Bayesian modules from the plan: 1A was explained in a separate pass and is still waiting on the forecast-interval check. 1B, 1C, and the Bayes assessment are not started. Verify *LLMs Are Not (Consistently) Bayesian* before citing results.

## Rules for the next session

State a falsifiable hypothesis first. Separate behavioral evidence from mechanistic evidence. Name the controls. Say what each outcome would establish and what it would not. Do not treat causal influence on the prediction as evidence of scientific reasoning.
