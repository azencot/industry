# Mock — 2026-06-26 — ml-deep-dive (JD technical mini-mock)

## Setup

- Duration: ~25 min
- Focus: general JD-aligned technical topics (not own project)
- ML topics covered: agent architecture + eval gating; A/B testing + null hypothesis; (agent failure debugging — started, unanswered)

## What went well

- Q1 agents (~80%): clean planning/execution/evaluation split; deterministic vs open-ended tools; tiered data + precision-threshold audit routing
- Q2 A/B re-answer (~85% from ~60%): correctly demoted precision to guardrail, business metric primary, case-level randomization, no peeking, safety kill rule

## What broke

- [ ] Technical gap: A/B testing fundamentals weak on first pass (precision as primary; over-weighted in-test drift)
- [ ] Verbal: "test on train set" (should be held-out/replay/shadow); "personal taste" (should be business/policy/risk tier)
- [ ] Coverage: Q3 (agent auto-approved money-moving error) not answered — carry forward

## Corrections to promote

| Observation | Update where |
|-------------|--------------|
| A/B: primary = business outcome, precision = guardrail | this mock + debrief (content) |
| Drift less of an issue within concurrent randomized A/B | debrief |
| Predefine MDE/sample size/stopping rule; no peeking; stratify segments | debrief |

## Next session (one thing)

- Resume at Q3 (agent failure debugging), then LLM system choices + parallelism/scaling.
