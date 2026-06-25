# STAR story bank

One file per story: `{lp-slug}_{short-title}.md` (e.g. `ownership_shipped-eval-gating.md`).

**Template:** [Day One Careers (DOC)](https://dayone.careers) — **Title | Outline | Ecosystem | Issue | Objectives | Actions | Results | Learnings and Improvements**. Use this for every draft and rewrite.

**Target role:** Senior Applied Scientist — interview at **L6**; stories should also signal **L7** leverage where true (reusable frameworks, cross-project influence). See length bar below.

## Priority Leadership Principles (PS1)

| LP | Story file | Metric / hook | Ready? |
|----|------------|---------------|--------|
| Customer Obsession | | | ☐ |
| Ownership | [`ownership_killed-tr-synthetic.md`](ownership_killed-tr-synthetic.md) | TR 26.9→21.9 (−5pp gate); killed mix | ☐ |
| Dive Deep | [`dive-deep_tsrbench-reasoning-audit.md`](dive-deep_tsrbench-reasoning-audit.md) | 3 regimes; ~+5 pp 0.8B preliminary | ☐ |
| Deliver Results | [`deliver-results_dual-tower-curriculum.md`](deliver-results_dual-tower-curriculum.md) | 0.618→0.905 TSExam; 0.402→0.452 TSRBench | ☐ |
| Invent and Simplify | [`invent-simplify_imagentime.md`](invent-simplify_imagentime.md) | +58% / +132%; EDM ~35 NFE | ☐ |
| Earn Trust | | | ☐ |
| Have Backbone; Disagree and Commit | | | ☐ |
| Learn and Be Curious | [`learn-be-curious_diffusion-mastery.md`](learn-be-curious_diffusion-mastery.md) | Learned diffusion from SDE up → 7 papers (ICML/ICLR/NeurIPS); ImagenTime/Few infra | ☐ |

## Intro / motivation (not STAR LPs)

| Script | File | Target |
|--------|------|--------|
| Why Amazon | [`why-amazon.md`](why-amazon.md) | ~1:30 · speakable prose + JD verbatim |

| Tell me about yourself | [`tell-me-about-yourself.md`](tell-me-about-yourself.md) | ~2–3 min · career arc |

Current project depth → [`elevator-pitch.md`](../elevator-pitch.md) (~90s).

---

## DOC story template

Copy into a new file when drafting. **Write DOC sections as short narrative paragraphs**, not compressed bullets — bullets are for Results only.

Map to spoken flow: **Ecosystem + Issue** ≈ Situation · **Objectives** ≈ Task · **Actions** ≈ Action · **Results** ≈ Result · **Learnings** ≈ Lesson.

```markdown
# [LP]: [Short title]

**Leadership Principle:** [exact LP name]
**Project:** [anchor or supporting project]
**Status:** Draft | Ready
**Target length:** **L6** ~700–850 words (DOC body) · **~8 min** spoken (descriptive primary) · L7 beats where scope is real

---

## Title

[Short headline — the move in one phrase]

## Outline

[One sentence: what *I* did + outcome. Memorable plain-English principle if possible.]

## Ecosystem

[3–5 sentences: where, your role and personal ownership, who cared (users/stakeholders), fit in larger agenda.
 Name: first/senior author, what you owned vs collaborators. IC hands-on, not PI charter.]

## Issue

[3–5 sentences: concrete "before" baseline, operational pain, why safe path was capped.
 One plain-English complexity sentence for non-specialists.]

## Objectives

[Numbered, testable — use same units as Results where possible:
 e.g. beat baselines on short/long benchmarks, reduce model calls ~1000→~35, fewer custom modules.]

## Actions

[Narrative paragraphs, 3–4 beats. Each beat: what *I* did, risk, how I de-risked or friction I hit.
 No self-labels like "core Invent move". Explain jargon once in plain English.]

## Results

[Map each result to an objective. Metrics first. Causal: which action drove which outcome.
 Practical user/researcher impact. Publication as footnote.]

## Learnings and Improvements

[Lesson in plain English + how you apply it now. Optional FinTech bridge.]

---

## Interview notes

### Personal ownership (say early if probed)

[One sentence: what you owned vs collaborators]

### IC proof (artifacts I personally built/decided)

-

### Spoken script (~8 min)

[Narrative paragraphs — read aloud; target ~950–1050 words, ~110–130 wpm; descriptive, scene-setting OK]

### Short version (~90 sec)

[Backup if interviewer asks for the short version]

### Likely follow-ups

-

### Weak spots / facts to verify

-

### FinTech bridge (one clause)

-
```

---

## DOC quality bar (L6 primary — L7 where earned)

Use this after writing; mirrors DOC AI review. **Do not add filler** — expand only where real detail improves interview quality.

### Length (Omri target: L6 interview, L7 promotion signal)

| Level | DOC body | Spoken | When |
|-------|----------|--------|------|
| L5 | 600–700 w | 5–6 min | Floor only — too thin for L6 loop |
| **L6 (primary target)** | **700–850 w** | **~8 min** (descriptive) | **Default for every PS1 story** |
| **L7 (selective beats)** | **850–1000 w** | **8–9 min** | Cross-team / field-level leverage — do not fabricate |

At **L6**, interviewers expect: developed context, alternatives considered, risk managed, influence on technical direction, broader impact. At **L7**, add **long-term leverage** — reusable frameworks, enabling other teams, strategic bets that paid off across projects (e.g. ImagenTime → VLM arc, open eval protocol).

### Required elements (L6+)

| Element | Where | What good looks like |
|---------|-------|----------------------|
| **Role & ownership** | Ecosystem | Project lead / senior author; what *I* owned vs collaborators — artifacts named |
| **Stakeholders / users** | Ecosystem | Who depended on the outcome; why it mattered beyond a paper |
| **Alternatives considered** | Issue or Actions | Paths you rejected and why (text tokens, single-stream, bespoke TS stack, incremental VAE) |
| **Concrete "before"** | Issue | Baseline metrics, operational pain, cost of wrong path |
| **Testable objectives** | Objectives | Same units as Results |
| **Friction / failure** | Actions | ≥2 setbacks or rejected options with evidence |
| **De-risk / risk management** | Actions | Staged validation, POC before pivot, eval gates |
| **Influence** | Actions | How you aligned collaborators / changed team direction with data |
| **Operational simplify** | Actions + Results | What became simpler to build, maintain, or extend |
| **Causal results** | Results | Which action drove which metric |
| **Broader impact** | Results + Learnings | Field, open stack, methodology others reuse — L7 signal |
| **Plain English** | Throughout | Jargon explained once |
| **No LP self-labels** | Actions | Demonstrate, don't name the LP |
| **False-promote stakes** | Issue or Actions | GPU cycle wasted, misleading progress update |
| **Beyond formal scope** | Ecosystem | What you volunteered to own vs assignment |
| **Delegation chain** | Actions | I did X; collaborator did Y; I owned Z |
| **Process adoption** | Results | Template/protocol others now use — one concrete fact |

### Spoken delivery

- DOC body = **source of truth**; **primary spoken script ~8 min** — descriptive narrative, not bullet compression.
- **Do not read results tables aloud** — summarize 3–5 numbers that drive the decision.
- Setup facts can breathe once in spoken form; avoid repeating the same gate/plateau line three times across sections.
- Keep a **90 sec backup** for time pressure only.

### DOC AI review checklist (apply after draft; Omri’s last manual pass)

From Ownership story review — promote into all future drafts:

| Fix | Do |
|-----|-----|
| **LP self-labels** | Never “this is what ownership looks like” — show operational facts |
| **Ecosystem** | Role + who relied on you + team size/roles in plain English |
| **Beyond scope** | One line: formal assignment vs what you voluntarily owned |
| **Stakes** | What false promote would cost (GPU cycle, misleading lab update) |
| **Friction** | Pressure to ship (aggregate up, resources spent) — one sentence |
| **Delegation** | “I trained X; collaborator ran Y; I remained accountable for Z” |
| **Goals vs guardrails** | Separate success objectives from pre-declared gates |
| **Results table** | Full table in body for prep; spoken = one-sentence summary |
| **Process impact** | One adoption fact (“template now default”) not vague “we changed culture” |
| **Jargon budget** | Name only metrics needed for the decision; skip model/benchmark laundry lists |
| **Lesson** | One direct process line; FinTech bridge only if asked |
| **Spoken length** | **~8 min descriptive** primary script (~950–1050 words) |

---

## IC vs managerial (L6+ — still applies)

| Avoid | Do instead |
|-------|------------|
| "I led a research program" | "I owned the hypothesis, eval gates, and architecture forks" |
| Grant/roadmap/hiring as hero | Technical decisions + measurable delivery |
| "We improved SOTA" | "I chose dual-stream over text tokens because pilot showed…" |

**L7 without sounding managerial:** frame influence as *technical persuasion with data* — POC ablations, eval protocol the team adopted, open stack others build on — not org chart authority.

---

## IC rules (quick reference)

| Rule | Where |
|------|-------|
| Say **"I"**, not "we" | Outline, Actions, Results |
| **Metrics** required | Results (+ Issue baseline) |
| **Tradeoff or failure** | ≥1 Action beat |
| **Artifacts** named | IC proof + Actions |
| **~8 min** spoken | Primary script — descriptive narrative |

## Refinement loop

1. Draft in DOC template (narrative paragraphs).
2. Run **DOC quality bar** checklist above (or DOC AI review).
3. Read **spoken script** aloud; trim jargon, fix awkward transitions.
4. Mark **Ready?** in table when it holds under pressure.
5. After `/debrief` or mock: edit story file; promote repeated fixes to [`AGENTS.md`](../../AGENTS.md).
