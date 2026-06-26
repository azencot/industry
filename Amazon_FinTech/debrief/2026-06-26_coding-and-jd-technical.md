# Debrief — 2026-06-26 — Coding sprint #1 + JD technical mini-mock

## Session

- **Type:** mixed — timed-code sprint + JD-technical mini-mock + plan adaptation
- **Duration:** ~half day
- **Prior context:** [`2026-06-25_qwen-peft-technical.md`](2026-06-25_qwen-peft-technical.md); Thu 26 coding sprint in [`prep-plan.md`](../prep-plan.md)

## Conclusions

### Coding (2/2 mediums, both under 25 min — logged in root INDEX)

- `347` Top-K Frequent — heap, ~15 min, pass. Size-k min-heap on `(freq, num)`; one bug (returned `heappop(h)` instead of draining `h`).
- `56` Merge Intervals — intervals, ~19 min, pass. Sort by start + scan; `start > max_end` flush else extend; clean first pass.
- **Trend:** big improvement vs Jun 24–25 (567 ~50 min, 200 ~35 min, both over 25). Now comfortably under time.

### Karan paper skim (FinPythia / continual pre-training)

- Results modest, mostly vs Pythia base (+10% 6.9B, +2% 1B); efficient data selection matches DACP at ~10% corpus; appears to lose to BloombergGPT (appendix unread).
- **Honest framing if probed:** contribution is *efficiency* (matching DACP at ~10% corpus on open base), not beating a finance-native 50B model.
- **Connection point:** same logic as TR-synthetic kill — domain adaptation ships only if task gains hold without general-capability regression.

### Plan adaptation — added JD technical track

User flagged prep was over-indexed on own projects + LPs + (outdated) Karan work + basic coding; wanted general JD-aligned topics. Added to [`prep-plan.md`](../prep-plan.md): agents, LLM system choices, A/B testing + null hypothesis, parallelism/scaling, eval gates — spread across Thu (mock), Fri (mock probe), Sat (refresh), Sun (review crib).

### JD technical mini-mock (interactive Q&A format)

**Q1 — Agent architecture + eval before removing human review (~80%)**
- **Landed:** planning / execution / evaluation split; deterministic tools vs open-ended LLM calls; tiered data (toy gold → messy weak labels); precision thresholds → critical-path audit vs automatic paths.
- **Fixes:** don't say "test on train set" → held-out / replay / shadow; avoid "personal taste" → business rules / policy / risk tier; sharpen autonomy ladder (read-only rec → low-risk action → high-risk after gates); every step emits inputs/evidence/tool calls/confidence/escalation reason for audit.

**Q2 — A/B testing + null hypothesis (~60% → ~85% on re-answer)**
- **Weak spot self-identified.** First pass made precision the primary metric and over-weighted distribution drift.
- **Corrections:** primary metric = business outcome (manual review rate / time-to-resolution); precision/error rate = guardrail not primary. Drift matters less *within* a properly randomized concurrent A/B (both arms see live traffic) — matters more live-vs-offline. Randomize at case/account level (no leakage). Predefine MDE / sample size / duration / stopping rule. No peeking without sequential testing. Stratify by segment (payment type, amount, region). Kill on safety even if primary improves.
- **Re-answer hit:** business primary metric, safety guardrails, case-level randomization, no peeking, kill rule. Still add: pre-launch sizing + segment stratification.

**Q3 — Agent failure (auto-approved cases moved money) — NOT answered**
- Asked but session pivoted to debrief. **Carry to next session.**

## Decisions / artifacts updated

- [x] prep-plan.md — JD technical track (Thu/Fri/Sat/Sun); Thu 26 mini-mock checked
- [x] This debrief + mock log [`mocks/2026-06-26_jd-technical-mock.md`](../mocks/2026-06-26_jd-technical-mock.md)
- [x] INDEX.md debrief + mock rows
- [ ] No AGENTS.md change yet (A/B weakness is content, not behavior)

## Open questions

- A/B: sequential testing mechanics (when does peeking actually inflate FPR; alpha-spending vs fixed-horizon)?
- Q3 agent-failure debugging answer (root-cause → targeted gate, not full human review).

## Next session (one prompt for session B)

> Read `@Files Amazon_FinTech/debrief/2026-06-26_coding-and-jd-technical.md`. Resume the JD technical mini-mock at Q3 (agent auto-approved a money-moving error — debug + fix without collapsing to full human review), then cover LLM system choices and parallelism/scaling.
