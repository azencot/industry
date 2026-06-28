# Debrief — 2026-06-28 — LLM / agentic trends (low-level decisions)

## Session

- **Type:** ml-deep-dive / exploration (teach → answer → tighten)
- **Duration:** ~40 min (started Sat 27 evening, continued Sun 28 morning)
- **Prior context:** Sat 27 agentic-workflows lesson stopped high-level track; user wanted low-level engineering decisions on recent tools (MCP, ReAct, FlashAttention, linear attention, FSDP, vLLM, routing, quantization, observability)
- **Format:** 6 decision drills with reference answers; no full timed retake

## Conclusions

Strong improvement over Sat 27 generic agent track. Answers consistently landed on the right **layer** (protocol vs orchestration vs kernel vs architecture vs pipeline). Main gaps were terminology precision and FinTech framing — not missing the concepts.

### Drills covered (~score trajectory)

| # | Topic | User | After tighten |
|---|-------|------|---------------|
| 1 | MCP + ReAct for payment-dispute agent | ~75% | ~90% |
| 2 | FlashAttention vs linear attention vs summarization | unanswered (prompted) | reference locked |
| 3 | LoRA/QLoRA vs FSDP vs RAG vs synthetic | ~70% | ~85% |
| 4 | Serving stack (vLLM, cache, routing, quant, spec decode) | ~80% | ~90% |
| 5 | FSDP vs DDP (PyTorch) | clarified in follow-up | ~90% |
| 6 | Agent observability when tools return bad data | ~75% | ~85% |

### What went well

- **MCP:** correctly framed as external-tool integration protocol; production needs auth, tenant isolation, audit, approvals — not just "version freeze."
- **ReAct:** right instinct — debuggable Thought/Action/Observation loop, but not fully autonomous; per-step verification for risky writes.
- **Serving ranking:** vLLM → caching → routing → quantization is the right risk order (behavior-preserving first, quality-risk last).
- **Observability:** correct first move — isolate tool failure vs agent failure; gold-label offline set + production replay for diagnosis.
- **FSDP vs DDP:** absorbed correction — FSDP is still data parallel on batches, but shards params/grads/optimizer instead of replicating full model per GPU.

### Corrections landed

| Weak phrasing | Stronger phrasing |
|---------------|-------------------|
| LoRA "alleviates forgetting" | LoRA reduces blast radius: frozen base, small reversible adapters, eval-gated rollout |
| FSDP "parallelizes at every level" | FSDP = sharded data parallel (`torch.distributed.fsdp`); DDP = replicated data parallel (`torch.nn.parallel.DistributedDataParallel`) |
| Quantization risky because finance needs "large representation bits" | Gate on calibration, rare-token behavior, extraction accuracy, tool-call JSON validity, numeric fidelity |
| "Version freeze" for MCP tools | Versioned tool contracts + regression tests on recorded trajectories |
| Observability = tool vs agent only | Add structured tracing + per-failure-mode evals (partial / stale / permission-scoped) + abstention as first-class metric |

### Keeper phrases (memorize for PS1)

- **Agents:** "MCP gives interoperability; ReAct gives observability; evals, auth, and approval gates give production safety."
- **Long context:** "FlashAttention is a low-risk systems optimization; linear attention is a higher-risk model choice; summarization is a lossy data-pipeline choice."
- **Adaptation:** "RAG teaches facts at inference time; LoRA teaches behavior; FSDP makes large training physically possible; synthetic data fills coverage gaps but must be audited."
- **Serving:** "Optimize serving first, route by risk second, compress the model only behind eval gates."
- **Observability:** "Trace everything; test the tool contract and the agent trajectory separately; correct abstention on bad data is a first-class metric."

### Quick reference — which layer?

| Tool / technique | Layer | Risk to quality | When first |
|----------------|-------|-----------------|------------|
| MCP | Integration protocol | Low (if wrapped with auth/audit) | Standardizing tool access |
| ReAct | Orchestration pattern | Medium (unbounded loops) | Default tool-using agent; add bounds + verification |
| FlashAttention | Kernel / IO optimization | Low (exact attention) | Attention is the GPU bottleneck |
| Linear attention | Model architecture | High | Only if exact attention is infeasible and evals pass |
| FSDP | Training sharding | Low (infra) | 70B+ won't fit per-GPU |
| LoRA / QLoRA | Parameter-efficient FT | Medium | Behavior change without full FT cost |
| RAG | Retrieval at inference | Low–medium | Changing facts, citations, auditability |
| vLLM / PagedAttention | Serving / KV cache | Low | Production throughput + memory |
| Routing | Tiered inference | Medium | Cost/latency after serving opts work |
| Quantization | Precision reduction | Medium–high | After eval gates on extraction + tool calls |
| Speculative decoding | Decode acceleration | Low if correct | Latency when draft acceptance is high |

### Unanswered / carry to JD refresh (Sun 28)

- FlashAttention vs linear attention vs summarization — user got reference answer only; no spoken retake.
- Guardrails for autonomous write actions — drill was offered but session pivoted to debrief.

## Decisions / artifacts updated

- [x] [`prep-plan.md`](../prep-plan.md) — Sun 28 agentic-trends block marked done
- [x] [`INDEX.md`](../INDEX.md) — debrief + mock rows
- [ ] No story/profile change

## Next session (one prompt for session B)

> Read `@Files Amazon_FinTech/debrief/2026-06-28_llm-agentic-trends-drill.md`. Sun 28 remaining: 2× `/timed-code` mediums + JD technical refresh from `job-description.md` (LLM choices, parallelism, eval gates, corrections loop, calibration/abstention, retrieval quality). Optional 90s retake: FlashAttention vs linear attention vs summarization.
