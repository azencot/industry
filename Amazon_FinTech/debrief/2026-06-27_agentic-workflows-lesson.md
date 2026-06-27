# Debrief — 2026-06-27 — Agentic workflows (teach-and-quiz)

## Session

- **Type:** exploration / learning (teach → question → answer → feedback)
- **Duration:** ~15 min (paused mid-lesson at Q2; may resume same night)
- **Prior context:** Sat 27 Karan mock + eval/monitoring lesson; JD emphasizes multi-agent systems for finance ops
- **Format:** general agentic-workflow concepts, finance-aware framing

## Conclusions

Solid grasp of the core distinction. One correction landed:

1. **Don't overclaim ReAct for finance.** Said "in finance a ReAct pattern is typically applied" — overstated. Unconstrained ReAct is risky (agent wanders, unpredictable tool calls, hard-to-audit traces). Correct framing: ReAct useful for *investigation*, but constrain with explicit planning, typed tools, per-step verification, and narrow action permissions.

### Concepts covered

- **Agentic workflow vs LLM pipeline:** pipeline = fixed Q→A; agent = plan → tool use → state → verification → (maybe) action.
- **Components:** planner, tools, memory/state, verifier/critic, policy/guardrail layer.
- **Patterns:** router agent, ReAct loop, plan-and-execute (more controllable), multi-agent (hard to debug without per-component evals).
- **Control boundaries:** narrow typed tools, not one `approve_payment()`. Agent orchestrates; deterministic code verifies exact agreement; policy service decides eligibility; humans handle exceptions.
- **Finance risk:** the danger is a wrong *action*, not just a wrong answer → "reason broadly, act narrowly."

### Keeper phrases

- "In production, agents are less autonomous brains and more controlled workflows: planning, tools, verification, escalation."
- "The agent may reason broadly, but action permissions should be narrow."
- "What is the agent allowed to decide, vs what must be deterministic code or a human?"

## Paused at (resume here)

**Q2:** For an invoice + remittance + ERP reconciliation agent — name 4–5 typed tools to expose, and which final actions you would NOT let the agent take directly. (Then continue: verification/critic layer, multi-agent debugging, abstention/escalation for agents.)

## Decisions / artifacts updated

- [x] [`prep-plan.md`](../prep-plan.md) — Sat 27 learning-session entry
- [x] [`INDEX.md`](../INDEX.md) — debrief index row
- [ ] No story/profile change (general ML knowledge)

## Next session (one prompt for session B)

> Read `@Files Amazon_FinTech/debrief/2026-06-27_agentic-workflows-lesson.md` and resume the agentic-workflows teach-and-quiz at Q2 (tool design + action boundaries), then verifier/critic, multi-agent debugging, and agent abstention/escalation.
