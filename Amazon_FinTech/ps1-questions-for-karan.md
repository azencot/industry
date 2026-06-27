# PS1 questions for Karan Aggarwal

**Use on:** Tue 30 Jun 2026 PS1 (last ~5 min)  
**Interviewer:** Karan Aggarwal — Senior Applied Scientist, FinTelligence  
**Rule:** Ask **2 questions**. Have 2 backups ready if he already covered one.

Full context: [`INDEX.md`](INDEX.md#interviewer--karan-aggarwal) · JD: [`job-description.md`](job-description.md)

---

## PS1 night — ask these two

### 1. Eval gating before ship

> When you promote a model change on a FinTelligence document workflow, what does your actual gate look like offline — gold slices by doc type, shadow or replay mode, and which metrics are blocking versus advisory? I'm especially curious what you treat as a hard fail on precision-critical fields versus something you'd monitor but not block on.

**Why it's strong:** Maps to JD (“eval frameworks that gate every model change”) and your Anchor B tiered eval. Invites concrete production detail, not philosophy.

**If he answers briefly:** “What slice regression has actually blocked a ship for you?”

---

### 2. User corrections → durable signal

> How do user corrections flow back into the system today — regression tests and failure taxonomy first, or do some corrections go straight into training? What's been the hardest class of error to close with corrections alone?

**Why it's strong:** Core JD responsibility. Shows you care about the closed loop, not just model quality at one snapshot.

**If he answers briefly:** “Do corrections ever become training signal automatically, or is there a human review step on the taxonomy first?”

---

## Backups (pick if #1 or #2 already covered)

### 3. Chronos vs multimodal routing

> For time-series work on the team, how do you decide between a Chronos-class forecaster and a multimodal reasoning path in production — is it task-type routing, confidence thresholds, or cost-quality tiers?

**Why:** Shows you read team stack (Chronos/Bolt) and won't over-claim your VLM project fits every TS task.

**Bridge if natural:** “In my project I routed reasoning to a VLM and would keep forecasting on a dedicated model — I'm curious how you draw that line at scale.”

---

### 4. Hardest failure mode offline eval misses

> What's a failure mode on financial documents that offline eval struggled to catch until you had production signal — extraction that looks right but reconciliation or policy reasoning is wrong, or something else?

**Why:** Opens his hardest-problem story; connects to your mock gap on reconciliation-layer debugging.

---

## Full bank (by theme)

### Production eval and monitoring

**A. Post-ship kill criteria**

> After partial automation is live, what post-ship signal has actually triggered a rollback or kill switch — slice precision drop, schema validity, unsupported-action rate — and how quickly could you detect it?

**B. Parse/schema vs semantic accuracy**

> On structured extraction tasks, how do you separate schema or format failures from semantic wrong answers in monitoring — and do you gate promotion on both?

*Ties to your parse-miss work on TSRBench (NR/TSF).*

---

### Agents and high-stakes actions

**C. Planning vs execution**

> When agents can act on financial data, how do you separate planning from execution in the architecture, and where do you hard-block versus route to human review?

**D. Money-moving failure you mentioned in prep**

> If an agent auto-approved a bad cash-application match, what would you inspect first in your stack — extraction logs, reconciliation step, or policy layer — and what would you ship first: containment or root-cause fix?

*Use only if conversation already went there; otherwise sounds rehearsed.*

---

### Model strategy (his research + team stack)

**E. Continual pre-training vs task FT**

> In your continual pre-training work on financial domains, when did domain adaptation move the needle versus when you still needed task-specific fine-tuning — and how did you gate against general-capability regression?

*References his [FinPythia paper](https://arxiv.org/abs/2311.08545); don't lead with “I read your paper” — let him connect it.*

**F. Low-label document types**

> For document types with thin labels, what has worked better in practice — controlled synthetic generation with audit gates, or retrieval-heavy pipelines with human corrections as the main signal?

---

### Role and team (use only if time and tone fit)

**G. What “good” looks like in the first year**

> For a senior applied scientist on FinTelligence, what does strong impact look like in the first 6–12 months — a shipped model change, an eval framework, or owning a slice end to end?

*Softer; use if technical questions feel exhausted.*

---

## Do not ask

| Avoid | Why |
|-------|-----|
| “What's the culture like?” | Generic; wastes scarce time |
| “How do I get promoted?” | Wrong round |
| “Can you tell me about the team?” | Too broad for Karan's technical style |
| “I read your paper — can you explain it?” | Puts him in lecturer mode; ask a *specific* comparison question instead (E) |
| Anything answerable from the JD posting | Shows you didn't read it |
| More than 2 questions | PS1 format is ~5 min |

---

## Delivery notes

- **Order:** Technical depth first (eval or corrections), second question can be routing or failure-mode if the first sparked discussion.
- **Length:** One question = 2–3 sentences max spoken. Stop. Let him talk.
- **Listen for hooks:** If he mentions shadow mode, slice gates, or corrections taxonomy — ask one short follow-up, not a third new question.
- **Don't debate:** If his answer differs from your prep (e.g. CPT vs RAG), note it; don't argue in PS1.

---

## Quick reference card (glance during PS1)

```
1. Eval gates — blocking vs advisory metrics? Hard fail on precision fields?
2. Corrections — regression tests/taxonomy first, or straight to training? Hardest error class?

Backup: Chronos vs multimodal routing in production?
Backup: Failure mode offline eval missed until production?
```
