# Debrief — 2026-06-27 — Karan full mock

## Session

- **Type:** post-mock (Karan PS1 simulation)
- **Duration:** ~90 min (mock segments + linked-list timed-code with 2 fix iterations)
- **Prior context:** Jun 26 JD mock left Q3 (agent money-moving failure) unanswered; Sat 27 prep-plan target

## Conclusions

### Ready for PS1

- **VLM depth** is grill-ready: dual visual encodings, Stage A (DINO+proj) vs Stage B (DINO+LLM LoRA), tiered eval available if pulled
- **Chronos contrast** is clean: patch-16 Bolt for forecast quantiles vs VLM for reasoning/NL; routing answer rehearsed
- **Ownership LP** (TR synthetic kill) lands with numbers and a principled kill — use “evidence invalidated the hypothesis”
- **Linked-list template** memorized: dummy → advance `right` n → `while right != None` → `left.next = left.next.next`

### Fix before PS1 (3 items)

1. **Finance eval framing:** Lead with gated rollout (gold → messy replay → shadow). Business outcome can be primary (STP, time-to-resolution); **precision is a hard guardrail** for automation eligibility, not always the sole primary metric.
2. **Schema reliability:** Deterministic validation for JSON/required fields/citations — not LLM-as-judge. LLM-judge only for semantic triage on lower-risk rationales.
3. **Agent failure debug script:** (1) contain — disable auto-approve / hold similar actions, (2) localize — extraction → **reconciliation** → policy → guardrail, (3) ship — threshold + human escalation, (4) durable — regression test + labeled slice gates future models.

### Coding lesson

First-pass bugs were classic interview traps: wrong delete target (parent vs victim), missing dummy for head removal, loop condition off-by-one. **Always state invariant aloud:** “When `right` falls off the list, `left` is the node before the one to delete.”

## Decisions / artifacts updated

- [x] [`prep-plan.md`](../prep-plan.md) — Sat 27 mock checkbox
- [x] root [`INDEX.md`](../../INDEX.md) — timed log row for LC 19
- [x] [`ps1-questions-for-karan.md`](../ps1-questions-for-karan.md) — PS1 night question bank
- [x] [`mocks/2026-06-27_full-mock.md`](../mocks/2026-06-27_full-mock.md)
- [ ] Sun 28 JD refresh checkboxes — carry monitoring + corrections retake

## Open questions

- Rehearse 2 PS1 questions aloud once (see ps1-questions doc)
- Deliver Results backup LP — verify leaderboard rank if Karan asks for second story
- Learn & Be Curious — lock distillation numbers if non-VLM LP surfaces

## Next session (one prompt for session B)

> Read `@Files Amazon_FinTech/debrief/2026-06-27_karan-full-mock.md` and `@Files Amazon_FinTech/prep-plan.md` (Sun 28 block). Run 2× `/timed-code` (trie wildcard + one other pattern) and 30 min JD technical refresh: production monitoring, corrections loop, calibration/abstention.
