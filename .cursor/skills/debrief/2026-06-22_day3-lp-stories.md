# Debrief — 2026-06-22 — Day 3 LP stories (DOC + L6)

## Session

- Type: exploration + story drafting (Day 3 Leadership Principles)
- Duration: ~multi-turn session (continued from Day 3 planning)
- Prior context: Day 1 anchors, Day 2 ML depth; DOC ImagenTime draft committed 2026-06-22 (`6ebcdb6`)

## Conclusions

- **Story format locked:** DOC sections (Title · Outline · Ecosystem · Issue · Objectives · Actions · Results · Learnings) + Interview notes with **~6–7 min spoken** primary script and 90s backup. See [`Amazon_FinTech/stories/README.md`](../../Amazon_FinTech/stories/README.md).
- **Seniority target:** Interview at **L6**; stories need alternatives considered, influence, risk management, broader impact — not compressed L5 (~5 min) summaries. L7 beats = reusable methodology / cross-project arc (ImagenTime → VLM), not org-chart management.
- **IC rule unchanged:** "I" + named artifacts; project lead OK when paired with patches, collator, eval harness — not PI charter.
- **Deliver Results baseline (final):** Only **stock Qwen3-VL-8B** (TSExam **0.618**, TSRBench **0.402**) vs our **3ep** stack (**0.905**, **0.452**). **Do not use internal config names** (`capnumicl`, `allcap-a5b3`) in LP stories — interviewers won't know them.
- **Invent & Simplify:** ImagenTime v3 L6 — senior author, DE/STFT, reject GAF/line graphs, EDM ~35 vs ~1000 model calls, +58%/+133%.
- **Deliver Results:** Anchor A — dual tower, two-stage curriculum, tiered eval; headline lift **+28.7 pp TSExam**, **+5.0 pp TSRBench** from stock Qwen3-VL-8B.
- **Story bank:** 2/8 priority LPs drafted (Invent & Simplify, Deliver Results). Neither marked Ready — need DOC AI review + read-aloud.

## Decisions / artifacts updated

- [x] `Amazon_FinTech/stories/README.md` — DOC template, L6 quality bar
- [x] `Amazon_FinTech/stories/invent-simplify_imagentime.md` — v3 L6
- [x] `Amazon_FinTech/stories/deliver-results_dual-tower-curriculum.md` — v4, Qwen3-VL-8B baseline only
- [x] `Amazon_FinTech/anchor-cheat-sheet.md` — Anchor A metrics + supporting LP table
- [x] `AGENTS.md`, `prep-plan.md`, `mock-lp/SKILL.md` — L6 length + DOC
- [ ] `elevator-pitch.md` — still says ~46% TSRBench; align to **0.452** + Qwen3-VL-8B arc (optional polish)
- [ ] `omri_azencot_experience.md` — quick numbers table still has older TSExam 0.890/0.901 in places

## Open questions

- [ ] TSRBench leaderboard rank vs "~45.2% near proprietary" before PS1 (30 Jun)
- [ ] Collaborator split wording for "project lead" if probed
- [ ] Which LP to draft first from Anchor B TR kill: **Ownership** vs **Have Backbone** (same event, different emphasis)

## Next story recommendation — failed TR mixes (Anchor B)

**Raw material captured:** metrics and per-task table folded into [`ownership_killed-tr-synthetic.md`](../../Amazon_FinTech/stories/ownership_killed-tr-synthetic.md)

| LP | Why this event |
|----|----------------|
| **Ownership** (draft first) | Plateau ~46% TSRBench vs proprietary 46–55%; reasoning gap. You owned tiered TR plan, synthetic TSExam templates, **hard-failure gates (−3 pp overall, −5 pp per task)**, trained 0.8B, student ran 8B — **killed** path when TR flat and other tasks regressed. |
| **Have Backbone** (same event, alt emphasis) | Disagreed with “add more synthetic TR data” after gates fired; committed to stop and study. |
| **Earn Trust** (third use) | Transparent negative result; didn’t promote a mix that hurt slices. |
- **Dive Deep:** Anchor C audit drafted — [`dive-deep_tsrbench-reasoning-audit.md`](../../Amazon_FinTech/stories/dive-deep_tsrbench-reasoning-audit.md). Ownership handoff only; 3 regimes; ~+5 pp 0.8B preliminary.

**Do not reuse** Deliver Results tiered-eval paragraphs verbatim — Ownership foregrounds **gates + kill decision**.

## Next session (one prompt for session B)

> Read `@Files .cursor/skills/debrief/2026-06-22_day3-lp-stories.md` and `@Files Amazon_FinTech/anchor-cheat-sheet.md` (Anchor B). Draft **Ownership** story DOC L6: killed TR bucket mixes — tiered eval, slice regression, IC artifacts. Baseline: stock metrics only where relevant; no internal config names in spoken script.
