# STAR story bank

One file per story: `{lp-slug}_{short-title}.md` (e.g. `ownership_shipped-eval-gating.md`).

**Template:** [DayOne Careers (DCC)](https://dayone.careers) — **Title | Outline | Ecosystem | Issue | Objectives | Actions | Results | Learnings and Improvements**. Use this for every draft and rewrite.

**Target role:** Senior Applied Scientist (FinTelligence) ≈ **L5–L6** — see length and quality bar below.

## Priority Leadership Principles (PS1)

| LP | Story file | Metric / hook | Ready? |
|----|------------|---------------|--------|
| Customer Obsession | | | ☐ |
| Ownership | | | ☐ |
| Dive Deep | | | ☐ |
| Deliver Results | | | ☐ |
| Invent and Simplify | [`invent-simplify_imagentime.md`](invent-simplify_imagentime.md) | +58% / +132%; EDM ~35 NFE | ☐ |
| Earn Trust | | | ☐ |
| Have Backbone; Disagree and Commit | | | ☐ |
| Learn and Be Curious | | | ☐ |

---

## DCC story template

Copy into a new file when drafting. **Write DCC sections as short narrative paragraphs**, not compressed bullets — bullets are for Results only.

Map to spoken flow: **Ecosystem + Issue** ≈ Situation · **Objectives** ≈ Task · **Actions** ≈ Action · **Results** ≈ Result · **Learnings** ≈ Lesson.

```markdown
# [LP]: [Short title]

**Leadership Principle:** [exact LP name]
**Project:** [anchor or supporting project]
**Status:** Draft | Ready
**Target length:** ~650–750 words (DCC body) · ~5–6 min spoken

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

### Spoken script (~5–6 min)

[Narrative paragraphs — read aloud; target 650–750 words, ~110–130 wpm]

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

## DCC quality bar (L5–L6 — apply on every draft)

Use this after writing; mirrors DCC AI review. **Do not add filler** — expand only where real detail improves interview quality.

### Length

| Level | DCC body | Spoken |
|-------|----------|--------|
| L4 | ~450 w · ~4 min | OK shorter |
| **L5 (target floor)** | **600–700 w** | **5–6 min** |
| **L6 (stretch)** | **750–850 w** | **6–7 min** |

Senior Applied Scientist stories should hit **L5 minimum**; add L6 depth when scope warrants it.

### Required elements

| Element | Where | What good looks like |
|---------|-------|----------------------|
| **Role & ownership** | Ecosystem | First/senior author; what *I* owned (hypothesis, ablations, pipeline, eval) vs collaborators |
| **Stakeholders / users** | Ecosystem | Who cared — practitioners, downstream scientists, exam users, finance ops |
| **Concrete "before"** | Issue | Baseline limits: length, speed (~1000 model calls), maintenance burden |
| **Testable objectives** | Objectives | Same units as Results (%, model calls, modules removed) |
| **Friction / failure** | Actions | ≥1 failed path (bad encoding, sampler hurt quality until tuned) |
| **De-risk loop** | Actions | How you validated representation didn't destroy structure |
| **Operational simplify** | Actions + Results | What became simpler — modules removed, config vs rewrite, reuse vision stack |
| **Causal results** | Results | Representation → length/quality; sampler → speed |
| **Practical impact** | Results | Who could use it more easily, what it enabled |
| **Plain English** | Throughout | Explain DDPM, EDM, NFE once: "model calls per sample" |
| **No LP self-labels** | Actions | Show behavior; don't say "core Invent move" |
| **Collaborator honesty** | Ecosystem | Transparent team role without diluting "I" |

### IC vs managerial (still applies at L5–L6)

| Avoid | Do instead |
|-------|------------|
| "I led a research program" | "I owned the hypothesis and ablation plan" |
| Publication strategy, grants, hiring | Technical forks you personally drove |
| "We improved SOTA" | "I chose delay embedding over GAF because…" |

### Spoken delivery

- DCC body = **source of truth**; spoken script = **narrative read-aloud** of the same beats.
- Prefer connected sentences over bullet dumps when speaking.
- Keep a **90 sec backup** at the bottom — not the primary target for this role.

---

## IC rules (quick reference)

| Rule | Where |
|------|-------|
| Say **"I"**, not "we" | Outline, Actions, Results |
| **Metrics** required | Results (+ Issue baseline) |
| **Tradeoff or failure** | ≥1 Action beat |
| **Artifacts** named | IC proof + Actions |
| **~5–6 min** spoken | Primary script for Senior Applied Scientist |

## Refinement loop

1. Draft in DCC template (narrative paragraphs).
2. Run **DCC quality bar** checklist above (or DCC AI review).
3. Read **spoken script** aloud; trim jargon, fix awkward transitions.
4. Mark **Ready?** in table when it holds under pressure.
5. After `/debrief` or mock: edit story file; promote repeated fixes to [`AGENTS.md`](../../AGENTS.md).
