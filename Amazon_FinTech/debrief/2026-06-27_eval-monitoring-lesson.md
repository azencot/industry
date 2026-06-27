# Debrief — 2026-06-27 — Finance production eval & monitoring (teach-and-quiz)

## Session

- **Type:** exploration / learning (teach → question → answer → feedback loop)
- **Duration:** ~40 min (paused once, resumed)
- **Prior context:** Sat 27 Karan mock JD probe was ~70%; this block targets that gap directly
- **Format:** 6 lessons + 6 comprehension questions on eval-as-release-gate for finance doc intelligence

## Conclusions

Strong grasp by end. Self-driven senior framing on corrections loop (Q5) and abstention analysis (Q6) — minimal correction needed. Two conceptual slips fixed:

1. **Shadow mode is diagnostic, not a thing you "kill."** Kill switches apply to *automation* (model acting → risk). Shadow mode is risk-free, so when a slice looks bad you withhold it from automation but keep it in shadow. (Q4)
2. **A real citation ≠ a supporting citation.** Don't reflex to OCR/fine-tune on a grounding failure; first check whether the cited span entails the extracted value, and whether the model confuses date types (renewal vs effective vs termination). (Q3)

### Other refinements landed

- Don't ship headline F1 gains if a critical finance slice regresses (amount precision 99.2→97.8 on scanned invoices = block broad ship; at most partial w/ routing). (Q1)
- Business metric ≠ guardrail: phrase business metric as "manual review reduction **at fixed quality**" / STP rate, not raw intervention rate. Schema validity is a **hard** guardrail, not monitor-only. (Q2)
- Corrections loop order: taxonomy → slice analysis → regression tests + holdout → component fix (prompt/ICL/validation) → selective FT on reviewed subset. Add correction-quality review (reviewers disagree/err). (Q5)
- Abstention: 70% abstain + 98% auto-approve precision is only good if abstentions concentrate in high-risk slices; check miscalibration on easy cases; compare against STP on eligible population. (Q6)

## 6-line PS1 crib (memorize)

1. Gate by slice, not headline metric.
2. Business metric ≠ guardrail (STP/review-reduction vs precision/schema/false-approval/policy).
3. Schema validity = deterministic; separate format failure from semantic failure.
4. Real citation ≠ supporting citation.
5. Shadow mode is diagnostic; high override = slice signal; withhold automation, don't kill shadow.
6. Corrections → taxonomy → regression tests → component fix → selective FT.

## Decisions / artifacts updated

- [x] [`prep-plan.md`](../prep-plan.md) — Sat 27 learning-session entry
- [x] [`INDEX.md`](../INDEX.md) — debrief index row
- [ ] stories / experience profile — no change (general ML knowledge, not project facts)

## Open questions

- Optional next round: agent money-moving failure debugging (contain → 4-layer taxonomy → regression test) — deferred
- Rehearse Q4 (shadow vs kill) and Q5 (corrections loop) aloud once before PS1 — strongest new material

## Next session (one prompt for session B)

> Read `@Files Amazon_FinTech/debrief/2026-06-27_eval-monitoring-lesson.md` and `@Files Amazon_FinTech/prep-plan.md` (Sun 28 block). Run 2× `/timed-code` + JD refresh; optionally do the agent money-moving failure-debugging teach-and-quiz round.
