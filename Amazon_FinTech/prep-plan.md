# Amazon FinTech PS1 — prep plan

Condensed from initial planning session. Adjust dates against [`INDEX.md`](INDEX.md) interview date (**PS1: Tue 30 Jun 2026**).

**Story bank:** [`stories/README.md`](stories/README.md) · **Writing rules:** [`INDEX.md`](INDEX.md#writing-rules-scripts--stories)

---

## Day 1 — Story + resume architecture

- [x] Elevator pitch (~90s) → [`elevator-pitch.md`](elevator-pitch.md) (read aloud; log time in practice table)
- [x] 3 anchor projects (STAR-ready): production ML/LLM, eval/monitoring, cross-functional ambiguity → [`anchor-cheat-sheet.md`](anchor-cheat-sheet.md) (all three angles on VLM project)
- [x] Map each to JD: trust/precision, corrections loop, tiered inference, eval gating
- [x] One-page cheat sheet: project → metric → your role → lesson → [`anchor-cheat-sheet.md`](anchor-cheat-sheet.md)

## Day 2 — ML/LLM depth (FinTech lens)

- [x] RAG vs fine-tuning vs continual pre-training — when, cost, drift → [`.cursor/skills/debrief/2026-06-21_day2-ml-depth.md`](../.cursor/skills/debrief/2026-06-21_day2-ml-depth.md)
- [x] NER/IE on messy finance docs; low-label strategies → same debrief (Topic 3)
- [x] Eval that gates releases; human-in-the-loop corrections → same debrief (Topic 2)
- [ ] Practice aloud (3 min each): end-to-end LLM system; safe deploy; scarce labels; payment doc extraction → `/ml-deep-dive` retakes; mock log [2026-06-21](mocks/2026-06-21_ml-deep-dive.md)
- [x] Read Karan's continual pre-training blog (methodology; results skim TBD) → [`debrief/2026-06-21_continual-pretraining-blog.md`](debrief/2026-06-21_continual-pretraining-blog.md); full paper [arxiv:2311.08545](https://arxiv.org/abs/2311.08545) optional before PS1
- [x] ECG-QALM abstract only (full paper skipped — PS1 bridge is Anchor C: TSExam op coverage audit, not NER synthetic generation) → [Amazon Science](https://www.amazon.science/publications/ecg-qalm-entity-controlled-synthetic-text-generation-using-contextual-q-a-for-ner)

## Day 3 — Leadership Principles + intro scripts

### Intro stack (read aloud in order once)

| Order | Script | File | Target |
|-------|--------|------|--------|
| 1 | Tell me about yourself | [`stories/tell-me-about-yourself.md`](stories/tell-me-about-yourself.md) | ~2–3 min |
| 2 | Current project (if he pulls) | [`elevator-pitch.md`](elevator-pitch.md) | ~90s |
| 3 | Why Amazon / why FinTelligence | [`stories/why-amazon.md`](stories/why-amazon.md) | ~1:30–2 min; **trim overlap** with TMAY if asked right after |

- [x] DOC template + L6 quality bar → [`stories/README.md`](stories/README.md) (~700–850 w body · **~8 min** descriptive spoken)
- [x] Intro scripts drafted (TMAY + Why Amazon)
- [ ] **4/8 LP stories drafted** — read aloud; none marked Ready

| LP | File | Status |
|----|------|--------|
| Invent and Simplify | [`invent-simplify_imagentime.md`](stories/invent-simplify_imagentime.md) | Draft v3 |
| Deliver Results | [`deliver-results_dual-tower-curriculum.md`](stories/deliver-results_dual-tower-curriculum.md) | Draft v4 |
| Ownership | [`ownership_killed-tr-synthetic.md`](stories/ownership_killed-tr-synthetic.md) | Draft v2 |
| Dive Deep | [`dive-deep_tsrbench-reasoning-audit.md`](stories/dive-deep_tsrbench-reasoning-audit.md) | Draft v1 |
| Customer Obsession | — | **Next** (Anchor C / user-needs frame) |
| Learn and Be Curious | — | optional alt on Anchor C |
| Have Backbone | — | optional; same TR event as Ownership |
| Earn Trust | — | skip standalone unless needed |

- [ ] Practice intro stack + 2 LP stories (`/mock-lp`)
- [ ] Verify weak spots: Ownership lab template; Dive Deep ~+5 pp numbers; Deliver Results leaderboard rank

## Day 4 — Live coding sprint #1

- [ ] 2 timed mediums (25 min each), narrated
- [ ] Patterns: hash, sliding window, BFS, heap, intervals, trie, binary search
- [ ] Log results in root [`INDEX.md`](../INDEX.md) timed table

## Day 5 — System design lite + FinTech scenarios

- [ ] Template: problem → data → model → train → eval → deploy → monitor → human loop
- [ ] Scenarios: contract intelligence agent; cash application; investigation copilot; eval CI gates

## Day 6 — Mock + coding sprint #2

- [ ] 2 more timed mediums
- [ ] 60-min full mock: TMAY → ML project → 2 LP → 1 code → questions
- [ ] `/debrief` → [`.cursor/skills/debrief/`](../.cursor/skills/debrief/) (+ [`mocks/`](mocks/) if full mock)

## Day 7 — Weak areas + polish

- [ ] Re-do failed/slow problems
- [ ] Re-read anchors + intro stack; anticipate Karan follow-ups
- [ ] Prepare 2 questions for Karan ([`INDEX.md`](INDEX.md))
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
