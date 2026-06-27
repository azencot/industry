# PS1 questions for Karan Aggarwal

**Use on:** Tue 30 Jun 2026 PS1 (last ~5 min)  
**Interviewer:** Karan Aggarwal — Senior Applied Scientist, FinTelligence  
**Rule:** Ask **2 questions**. Have 1–2 backups if he already covered one.

Full context: [`INDEX.md`](INDEX.md#interviewer--karan-aggarwal) · JD: [`job-description.md`](job-description.md)

---

## Tone for PS1 (read this first)

PS1 questions should sound like **genuine curiosity about the role**, not like you're interviewing him or auditing the team's stack.

| Sounds natural | Sounds awkward in PS1 |
|----------------|----------------------|
| "Where is trust hardest to earn in practice?" | "What does your actual offline gate look like?" |
| "What separates strong impact here?" | "Which metrics are blocking versus advisory?" |
| "How do corrections usually feed back?" | "Do corrections go straight into training?" |

Keep each question to **1–2 sentences**. Stop. Let him talk. One short follow-up is fine if he opens a door — not a third prepared question.

---

## PS1 night — ask these two

### 1. Where trust is hardest (JD-aligned)

> The JD talks about finance teams trusting the system enough to rely on it without manual review. In your experience on FinTelligence, where is that trust hardest to earn — getting extraction right, reconciling across documents, or knowing when the system should abstain?

**Why it works:** Technical enough for Karan; opens eval, precision, abstention, and product judgment without asking him to describe internal runbooks.

**If he answers briefly:** "Is that different for cash application versus contract or invoice workflows?"

---

### 2. What strong impact looks like

> From your perspective, what separates a strong senior applied scientist on this team from someone who is only strong at modeling — is it mostly eval discipline, product judgment around financial risk, or owning a slice end to end?

**Why it works:** Lets him define success on his own terms. You learn role expectations without sounding like you're grading the org.

**If he answers briefly:** "What does that look like in the first year — a shipped change, an eval framework, or something else?"

---

## Backups (pick if #1 or #2 already covered)

### 3. Corrections loop (softer)

> The role mentions systems that learn from user corrections. In practice, how do those corrections usually change the product — do they mostly improve eval coverage, tighten rules and guardrails, or eventually become training signal?

**Bridge if natural:** "I've found that turning recurring corrections into regression tests before retraining is often the safer path — curious how that plays out on your team."

---

### 4. Hardest problem class

> What's the class of problem on financial documents that still feels genuinely hard — messy real-world formats, low-label regimes, or getting agents to act safely at scale?

**Why it works:** Opens his view of the frontier without asking for a post-mortem on a specific incident.

---

### 5. Time-series at FinTelligence (only if TS came up in your project discussion)

> I saw the team works with Chronos for forecasting. For problems that need reasoning or explanation rather than a forecast, how do you usually think about routing or combining different model types?

**Use only if** your VLM / time-series thread already landed — otherwise it can feel like name-dropping homework.

---

## Deeper follow-ups (only if conversation naturally goes there)

*Don't lead with these in PS1. Use if he mentions eval gates, shadow mode, corrections, or agents and invites you to dig in.*

| Theme | Follow-up (one sentence) |
|-------|--------------------------|
| Eval before ship | "Do slice regressions on high-risk fields usually block promotion, or is it more about monitoring first?" |
| Post-ship | "What kind of production signal has actually triggered a rollback for you?" |
| Schema vs semantics | "Do you treat format failures separately from wrong extractions when you're measuring quality?" |
| Agents / money-moving | "When an agent can take action on financial data, where do you draw the line between recommendation and automation?" |
| Continual pre-training | "When has domain adaptation helped versus when you still needed task-specific fine-tuning?" |

---

## Do not ask

| Avoid | Why |
|-------|-----|
| "What's the culture like?" | Generic; wastes scarce time |
| "How do I get promoted?" | Wrong round |
| "Can you tell me about the team?" | Too broad |
| "I read your paper — can you explain it?" | Puts him in lecturer mode |
| Detailed implementation audits ("what's your gate ladder?", "blocking vs advisory metrics?") | Sounds like you're interviewing him |
| Anything fully answerable from the JD posting alone | Shows you didn't read it |
| More than 2 questions + one follow-up | PS1 format is ~5 min |

---

## Delivery notes

- **Order:** Start with trust (#1) or role fit (#2) — both work after a technical screen.
- **Listen:** If he mentions eval, corrections, or routing, you can use one row from the deeper follow-ups table — not a new scripted question.
- **Don't debate:** If his answer differs from your prep, note it; don't argue in PS1.
- **Rehearse once aloud** Mon 29 — goal is conversational, not memorized.

---

## Quick reference card (glance during PS1)

```
1. Where is trust hardest — extraction, reconciliation, or abstention?
2. What separates strong senior AS impact here — eval, risk judgment, or owning a slice?

Backup: How do user corrections usually change the product?
Backup: What problem class still feels genuinely hard?

Follow-up only if he opens the door — don't lead with audit-style detail.
```
