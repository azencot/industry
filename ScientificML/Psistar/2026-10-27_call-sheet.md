# Psistar — Technical Discussion

October 27, 2026 | 45 minutes

Participants: Yochai Pagi (CEO), Matan Pagi (CTO)

Role discussed: Part-time Principal Researcher (40–60%), remote from Seattle.

## Meeting objectives

1. Understand Psistar’s current predictive modeling approach and its limitations.
2. Identify where my research background could make the greatest contribution.
3. Align on responsibilities, collaboration, and expectations for the first six months.

---

## 1. Current research and technical challenges

Start by understanding what they are working on now.

- What is the main research problem you’re currently trying to solve?
- Is zero-shot prediction across plants the immediate objective, or a longer-term goal?
- What approaches have you already tried, and where have they fallen short?

### Current predictive model

Bilinear MamKO suggests the following architecture:

\[
\text{History} \rightarrow \text{Mamba} \rightarrow \text{Adaptive Koopman operators} \rightarrow \text{Bilinear dynamics} \rightarrow \text{MPC}.
\]

The model adapts its dynamics based on historical context. MPC optimizes controls using sequential convex programming.

Important distinction: Adaptation within one plant does not establish zero-shot generalization across plants.

Questions to clarify:

- Are you currently training one predictive model per plant?
- How do you represent plants with different sensors, controls, and configurations?
- What information does the model receive when deployed to a new plant?
- What have you observed when transferring models between plants?
- How does the vision model interact with the predictive model?
- What does the upcoming irregular time-series work address?

Technical details worth understanding:

- How are future Koopman operators generated during MPC?
- What are the main prediction and control failure modes?
- What limits the current approach: accuracy, generalization, data, or computational cost?

### Zero-shot generalization

The central distinction:

**Universal predictive model.** One shared model directly predicts dynamics across plants.

**Universal identification mechanism.** One shared model infers plant-specific dynamics from observations and context.

Both can avoid gradient-based retraining, but they imply different architectures and evaluation strategies.

Clarify what zero-shot means in their setting and how much target-plant data is available.

---

## 2. Potential research contributions

My strongest overlap is in transferable representations and predictive modeling of dynamical systems, rather than MPC optimization itself.

Three possible directions:

### A. Context-based system identification

Separate persistent plant characteristics from changing operating conditions:

\[
c_i = E_{\mathrm{plant}}(\mathcal{H}_i), \qquad r_t = E_{\mathrm{state}}(\mathcal{H}_{t-L:t}),
\]

\[
(A_t, B_t) = G_\theta(c_i, r_t).
\]

The shared model identifies plant-specific dynamics from context without parameter updates.

Relevant expertise: Structured Koopman models, disentanglement, sequential learning.

### B. Probabilistic dynamics identification

Infer a distribution over plausible plant dynamics:

\[
p_\theta(A_i, B_i \mid \mathcal{H}_i).
\]

Useful when observations do not uniquely determine the system.

Relevant expertise: Generative modeling, probabilistic forecasting, uncertainty quantification.

### C. Multimodal plant representations

Combine telemetry with equipment descriptions, sensor metadata, and plant topology.

Potentially relevant if engineering documentation can provide structural information that improves transfer.

Relevant expertise: Multimodal representation learning, vision-language models, time series.

### Possible first experiment

If sufficient data from multiple plants are available:

- Train a shared baseline across plants.
- Evaluate on a held-out plant without parameter updates.
- Compare with a plant-specific model.
- Measure multistep prediction accuracy as a function of available context.
- Eventually evaluate control-conditioned prediction and MPC performance.

Do not commit to an architecture before understanding their existing experiments and available data.

---

## 3. Collaboration and expectations

### Research responsibilities

- What research problem would you most want me to own?
- Who would I collaborate with regularly?
- How much freedom would I have to shape the research direction?
- What would constitute a successful first six months?

### Resources and publication

- What data, simulation environments, and compute would be available?
- Can the research lead to publications?
- Can I continue collaborating with my academic students and colleagues?
- Are there restrictions on publishing results obtained using company data?

### Working arrangement

- Confirm expectations for 40–60% involvement.
- Confirm remote work from Seattle.
- Clarify meeting cadence and hands-on research expectations.
- Understand the next steps and timeline.

---

## What I want to establish by the end

**Technical:** What is the most important unsolved research problem, and what has already been attempted?

**Scientific:** Is there a meaningful research direction where my expertise can accelerate progress?

**Practical:** Would I have the resources, collaborators, independence, and time to make that contribution?

**Next step:** Agree on a concrete follow-up, potentially a small technical investigation using their existing model or data.
