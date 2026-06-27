# Debrief — 2026-06-27 — Agentic workflows (teach-and-quiz)

## Session

- **Type:** exploration / learning (teach → question → answer → feedback)
- **Duration:** ~25 min total across two short blocks; stopped intentionally after Q2 because the drill was too high-level for Karan's style
- **Prior context:** Sat 27 Karan mock + eval/monitoring lesson; JD emphasizes multi-agent systems for finance ops
- **Format:** general agentic-workflow concepts, finance-aware framing

## Conclusions

Solid grasp of the core distinction, but this format was **not the highest ROI for Karan**. Imry's guidance was that Karan wants maximum technical detail (model, training, eval, ablations, concrete structure), so future agent practice should avoid broad agent vocabulary and drill lower-level design decisions instead.

One correction landed:

1. **Don't overclaim ReAct for finance.** Said "in finance a ReAct pattern is typically applied" — overstated. Unconstrained ReAct is risky (agent wanders, unpredictable tool calls, hard-to-audit traces). Correct framing: ReAct useful for *investigation*, but constrain with explicit planning, typed tools, per-step verification, and narrow action permissions.

### Concepts covered

- **Agentic workflow vs LLM pipeline:** pipeline = fixed Q→A; agent = plan → tool use → state → verification → (maybe) action.
- **Components:** planner, tools, memory/state, verifier/critic, policy/guardrail layer.
- **Patterns:** router agent, ReAct loop, plan-and-execute (more controllable), multi-agent (hard to debug without per-component evals).
- **Control boundaries:** narrow typed tools, not one `approve_payment()`. Agent orchestrates; deterministic code verifies exact agreement; policy service decides eligibility; humans handle exceptions.
- **Finance risk:** the danger is a wrong *action*, not just a wrong answer → "reason broadly, act narrowly."

### What to change if resuming

Do **not** continue with generic agent taxonomy. Resume only as a concrete low-level architecture drill:

- Define exact tool schemas: inputs, outputs, failure modes, confidence/citations.
- Draw the invoice/remittance/ERP reconciliation flow step by step.
- Specify verifier checks: amount/currency/payee/invoice ID/duplicate/payment status/policy/risk tier.
- Specify logs emitted per step: extracted fields, evidence spans, tool outputs, decision trace, guardrail result, action attempt.
- Specify online eval: false auto-approval rate, human override by slice, unsupported-action rate, schema validity, reconciliation accuracy.
- Debug one failure end to end: wrong OCR vs wrong extraction vs wrong reconciliation vs wrong policy vs wrong executor permission.

### Keeper phrases

- "In production, agents are less autonomous brains and more controlled workflows: planning, tools, verification, escalation."
- "The agent may reason broadly, but action permissions should be narrow."
- "What is the agent allowed to decide, vs what must be deterministic code or a human?"

## Paused at (resume here)

**Do not resume with generic Q2 as written.** If continuing, use this lower-level prompt:

> Design the invoice + remittance + ERP reconciliation workflow as if you were writing the engineering spec. List each tool with typed inputs/outputs, the verifier checks after each tool, the exact action boundary, and the logs you would need to debug a bad auto-approval.

## Decisions / artifacts updated

- [x] [`prep-plan.md`](../prep-plan.md) — Sat 27 learning-session entry
- [x] [`INDEX.md`](../INDEX.md) — debrief index row
- [ ] No story/profile change (general ML knowledge)

## Next session (one prompt for session B)

> Read `@Files Amazon_FinTech/debrief/2026-06-27_agentic-workflows-lesson.md`. If practicing agents again, skip generic concepts and run a low-level engineering-spec drill for invoice/remittance/ERP reconciliation: tool schemas, verifier checks, logs, action boundaries, and one failure-debug trace.
