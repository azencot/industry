# Mock — 2026-06-28 — ml-deep-dive (LLM / agentic trends)

## Setup

- Duration: ~40 min (Sat 27 evening + Sun 28 morning)
- Focus: low-level engineering decisions — MCP, ReAct, attention kernels, FSDP/DDP, LoRA/RAG/synthetic, serving stack, agent observability
- ML topics: agent protocols, orchestration, inference optimization, distributed training, eval/observability

## What went well

- Layer separation instinct strong (protocol vs orchestration vs kernel vs architecture)
- Serving optimization ranking correct: behavior-preserving first (vLLM, cache), routing next, quantization last behind evals
- Tool-vs-agent diagnostic framing for production failures
- MCP + ReAct answers finance-aware (auth, audit, human approval for writes)

## What broke

- [ ] Technical gap: LoRA described as alleviating forgetting (should be: frozen base, small reversible adapters)
- [ ] Technical gap: FSDP described as "parallelizing at every level" (should be: sharded data parallel — shards params/grads/optimizer; DDP = replicated)
- [ ] Framing: quantization risk as abstract "numerical thinking" (should be: calibration, extraction, tool-call JSON, numeric fidelity)
- [ ] Observability: missing structured tracing, per-failure-mode evals (partial/stale/permission-scoped), abstention metric
- [ ] Unanswered: FlashAttention vs linear attention vs summarization (reference only)

## Corrections to promote

| Observation | Update where |
|-------------|--------------|
| MCP = interoperability; ReAct = observability; evals/auth/approval = safety | debrief keeper phrases |
| FSDP vs DDP in PyTorch (`fsdp` vs `DDP`) | debrief |
| Quantization eval-gate framing for finance | debrief |
| Abstention on degraded tool data = first-class metric | debrief |

## Next session (one thing)

- Sun 28: 2× timed-code + JD technical refresh; optional 90s retake on long-context optimization drill.
