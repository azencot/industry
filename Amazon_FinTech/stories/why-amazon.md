# Why Amazon — FinTelligence PS1

**Use:** “Why Amazon?” / “Why this role?” — intro block, not a STAR LP.  
**Target:** ~1:30 spoken · connected sentences (read aloud) · **JD phrases verbatim** where they fit.  
**Pair with:** [`elevator-pitch.md`](../elevator-pitch.md) (who + what you built).

---

## Main script (say this)

Amazon is one of the few places where you can work on genuinely ambiguous applied science and still have a line to production — engineering, product constraints, real customers — not only a paper and a leaderboard.

In academia my thread has been messy sequential and multimodal data. The representation is often unclear, and a method only holds if the eval is honest. That runs from ImagenTime through the VLM stack on TSRBench. I built the training pipeline and the eval harness myself — tiered runs, per-task score tables, parse failures tracked separately from accuracy. When a synthetic data mix improved the reasoning average but temporal relations dropped five points, I did not promote it. I had set the floor before training; the gate fired. That is the kind of decision the role is about.

FinTelligence is similar in spirit to what I've been doing — you often start without a fixed product, you make principled decisions under uncertainty, and you need a solution that is simple, scalable, and durable, not just a prototype. I'm used to owning the technical arc: frame the problem, build the training and eval stack, deliver a validated result, and stay accountable for what did not work.

For this team, **finance operations at scale** — payments, contracts, cash application, investigation — is a strong fit. That data is sequential, noisy, and multi-source; it is the regime where I've been most effective. The posting leads with **trust without manual review**; in finance, precision is compliance. I'm strict about evaluation — stress tests, shift checks, failure-mode reporting, **eval frameworks that gate model changes** — not only a leaderboard number. The direction is **LLM and multi-agent systems** with multimodal models, which aligns with my recent work: representing sequential signals and aligning them with text in a grounded way, plus **learning from user corrections** and **tiered inference** — routing, SLMs, cost versus frontier quality. My default is to reduce complexity: find the right representation, design the minimal architecture that captures it, and make it robust enough to scale.

So for me it is the combination: a mission and domain where the modeling challenges matter, a culture with a high bar on eval and delivery, and an environment where I can drive clarity from ambiguity and ship something that holds beyond a research prototype.

---

## Beat map

| Block | ~sec | Content |
|-------|------|---------|
| Why Amazon | 20 | Ambiguous science → production path |
| Your work | 35 | Sequential/multimodal arc → stack you built → TR kill (one example) |
| Why role | 40 | Ambiguity → durable systems; finance ops fit; eval + multimodal LLM; close |

---

## JD phrases (use as written)

From [`INDEX.md`](../INDEX.md) — weave into sentences; do not compress into a slogan list:

- LLM + multi-agent systems for **finance operations** at scale (payments, contracts, cash application, investigation)
- **Trust without manual review** — precision = compliance
- **Learning from user corrections**; eval frameworks that **gate** model changes
- **Tiered inference**: routing, SLMs, cost vs frontier quality

---

## Short version (~45 sec)

Amazon — ambiguous applied science with a path to production. I work on sequential and multimodal modeling with strict eval; I killed a mix when a reasoning slice regressed despite a better average. FinTelligence is finance operations at scale — payments, contracts, cash application — with trust without manual review and eval that gates model changes. Same regime I've worked in; I want it to hold at production scale.

---

## Don't say

- “I'm excited about…” / “I'm drawn to…”
- “That's the discipline I want in production” / “not in a vacuum” / “peer scientists”
- JD as a bullet recitation with no example in the middle
- PI beats: mentoring, building the team, research program

---

## Likely follow-ups

| Question | Point to |
|----------|----------|
| “Won't you miss the lab?” | [`elevator-pitch.md`](../elevator-pitch.md) — gated releases, corrections loop |
| “Example of gating?” | Ownership — TR 26.9→21.9, pre-declared floors |
| “Tiered inference?” | 0.8B pilots → 8B; TSExam near parity — experience profile |

---

## Practice log

| Date | Time (target ~1:30) | Felt natural? | Notes |
|------|---------------------|---------------|-------|
| | | ☐ | v4 — team-fit paragraph from Omri draft (FinTech) |
