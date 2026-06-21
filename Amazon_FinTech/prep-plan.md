# Amazon FinTech PS1 — prep plan

Condensed from initial planning session. Adjust dates against [`INDEX.md`](../INDEX.md) interview date.

---

## Day 1 — Story + resume architecture

- [x] Elevator pitch (~90s) → [`elevator-pitch.md`](elevator-pitch.md) (read aloud; log time in practice table)
- [x] 3 anchor projects (STAR-ready): production ML/LLM, eval/monitoring, cross-functional ambiguity → [`anchor-cheat-sheet.md`](anchor-cheat-sheet.md) (all three angles on VLM project)
- [x] Map each to JD: trust/precision, corrections loop, tiered inference, eval gating
- [x] One-page cheat sheet: project → metric → your role → lesson → [`anchor-cheat-sheet.md`](anchor-cheat-sheet.md)

## Day 2 — ML/LLM depth (FinTech lens)

- [ ] RAG vs fine-tuning vs continual pre-training — when, cost, drift
- [ ] NER/IE on messy finance docs; low-label strategies
- [ ] Eval that gates releases; human-in-the-loop corrections
- [ ] Practice aloud (3 min each): end-to-end LLM system; safe deploy; scarce labels; payment doc extraction
- [x] Read Karan's continual pre-training blog (methodology; results skim TBD) → [`debrief/2026-06-21_continual-pretraining-blog.md`](debrief/2026-06-21_continual-pretraining-blog.md); full paper [arxiv:2311.08545](https://arxiv.org/abs/2311.08545) optional before PS1
- [x] ECG-QALM abstract only (full paper skipped — PS1 bridge is Anchor C: TSExam op coverage audit, not NER synthetic generation) → [Amazon Science](https://www.amazon.science/publications/ecg-qalm-entity-controlled-synthetic-text-generation-using-contextual-q-a-for-ner)

## Day 3 — Leadership Principles

- [ ] 8 STAR stories: Customer Obsession, Ownership, Dive Deep, Deliver Results, Invent and Simplify, Earn Trust, Have Backbone, Learn and Be Curious
- [ ] Rules: "I" not "we"; metrics; tradeoffs; lesson learned
- [ ] Save drafts → [`stories/`](stories/)

## Day 4 — Live coding sprint #1

- [ ] 2 timed mediums (25 min each), narrated
- [ ] Patterns: hash, sliding window, BFS, heap, intervals, trie, binary search
- [ ] Log results in root [`INDEX.md`](../INDEX.md) timed table

## Day 5 — System design lite + FinTech scenarios

- [ ] Template: problem → data → model → train → eval → deploy → monitor → human loop
- [ ] Scenarios: contract intelligence agent; cash application; investigation copilot; eval CI gates

## Day 6 — Mock + coding sprint #2

- [ ] 2 more timed mediums
- [ ] 60-min full mock: pitch → ML project → 2 LP → 1 code → questions
- [ ] `/debrief` → [`.cursor/skills/debrief/`](../.cursor/skills/debrief/) (+ [`mocks/`](mocks/) if full mock)

## Day 7 — Weak areas + polish

- [ ] Re-do failed/slow problems
- [ ] Re-read 3 anchor projects + anticipate follow-ups
- [ ] Prepare 2 questions for Karan
- [ ] Skim [Amazon Leadership Principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles)

## Interview day (30 Jun)

- [ ] Zoom at 21:00 sharp; Live Code link ready
- [ ] Headset; quiet room; phone on backup
- [ ] `/debrief` same night while fresh

---

## Daily default (if short on time)

1. One `/timed-code` problem
2. One `/mock-lp` or `/ml-deep-dive`
3. Update index or mock log (5 min)
