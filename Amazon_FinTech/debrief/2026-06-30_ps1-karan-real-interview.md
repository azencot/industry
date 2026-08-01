# Debrief — 2026-06-30 — PS1 with Karan (real interview)

## Session

- **Type:** post-interview (PS1 — Karan Aggarwal, FinTelligence)
- **Date:** Tue 30 Jun 2026
- **Format observed:** LP first → synthetic-data / verifier depth → VLM project (long) → ML fundamentals rapid-fire → live coding (trailing-window z-score)
- **Outcome:** Mixed — Karan pivoted LP until a story fit; pacing too slow; fundamentals gaps on TS/stats; coding incomplete under time pressure

## What happened (chronological)

1. **Ownership LP (TR synthetic kill)** — Karan did not accept this as Ownership. His read: setting promotion gates and killing a bad mix was **your job as eval lead**, not going beyond responsibility. He re-asked the LP several times until a different story fit better (user did not recall which LP landed).
2. **Pacing** — Interviewer tried to hasten; user felt they talked too much. The ~8 min Ownership script is far too long for PS1 LP (~2–3 min answer + probes).
3. **Synthetic data correctness** — Karan was interested in how you **guarantee synthetic data is correct** and what **verifiers** you use. Strong prep thread; likely FinTech-relevant (ECG-QALM / audit lineage).
4. **VLM project** — User spent too long; Karan wanted to move on. **Lesson:** 90s hook → one metric → stop; let him pull threads.
5. **ML fundamentals (rapid-fire)** — LoRA, transformer, attention, why RNNs are bad, stationary time series + how to make stationary, RF vs XGBoost, plus others not recalled. User felt weak on TS stationarity and RF vs XGBoost.
6. **Live coding** — Trailing-window z-score normalization (see [`code/2026-06-30_trailing_zscore_normalization.py`](../../code/2026-06-30_trailing_zscore_normalization.py)). User's draft had structural bugs (see below); likely did not finish cleanly.

## Conclusions

### LP mapping (critical fix)

| Story | Good for | Bad for Ownership because… |
|-------|----------|----------------------------|
| TR synthetic kill | **Have Backbone** (kill despite sunk 8B + good average), **Invent and Simplify** (per-task gates), **Dive Deep** (audit) | "I owned eval" = expected job, not extra mile |
| Dual-tower / TSExam lift | **Deliver Results** | — |
| ImagenTime representation bet | **Invent and Simplify**, **Learn and Be Curious** | — |

**Ownership reframe if you reuse TR kill:** Lead with **pressure to promote after GPU spend** and **lab wanted the average win** — you killed anyway. That is the extraordinary part, not "I wrote gates."

**PS1 LP target length:** **90 sec setup + 60 sec actions + 30 sec result** (~2–3 min). Save 8 min script for onsite loops only.

### Pacing rules (Karan confirmed live)

- Answer the question, then **stop**.
- Project depth: **one anchor metric**, wait for follow-up.
- If he says "let's move on" — stop mid-sentence.

### Synthetic data / verifiers (what he wanted)

Speak in layers:

1. **Generator constraints** — schema, valid ranges, invertibility checks (ImagenTime: decode(encode(x)) ≈ x).
2. **Automated verifiers** — unit tests on invariants (segment count, ordering, label consistency with program that generated the item).
3. **Human audit slice** — sample N items per tier before mix enters training.
4. **Downstream gate** — per-task eval floors before promote (same FinTech frame as doc-type regression tests).

### Fundamentals crib (30-sec answers)

See section below in this file — drill aloud 2× before any follow-up round.

### Coding post-mortem

User draft bugs:

| Bug | Fix |
|-----|-----|
| `q` never initialized | `deque()` before use |
| `math.std` does not exist | `statistics.pstdev` or manual `sqrt(var)` |
| First loop batches first `k` points into one window | **Each index `i` gets its own trailing window** `[max(0,i-k+1)..i]` |
| Second loop starts at `k+1` | Start at `k` (or unify in one loop `for i in range(len(ts))`) |
| `std_tss` typo | — |
| Recomputes full window stats from scratch inconsistently | One loop; slice or sliding deque |

**Interview invariant to say aloud:** "At index `i`, window is `ts[max(0, i-k+1) : i+1]`; z-score uses mean/std over that window only; `eps` when std≈0."

## Fundamentals — rehearse these

### LoRA

Low-rank adapters: freeze base weights W; train small matrices A,B so update is ΔW = BA (rank r ≪ dim). Cuts trainable params and memory; same inference path with merged weights or side adapters.

### Transformer

Sequence model built from stacked blocks: self-attention (mix tokens) + FFN (per-token transform) + residuals/LayerNorm. Parallel over sequence length at train time vs RNN serial steps.

### Attention (one sentence)

For each query token, compute softmax(QKᵀ/√d) over keys to weight values — learned soft lookup over the sequence.

### Why RNNs are bad (for long context / modern NLP)

Vanishing/exploding gradients over long dependencies; **serial** computation (can't parallelize length); hard to retain distant context. Transformers: direct pairwise paths + parallel training.

### Stationary time series

Statistical properties (mean, variance, autocovariance) **constant over time**. Needed for many classical models (ARIMA) and stable rolling stats.

**Make stationary:** (1) **differencing** Δx_t = x_t − x_{t−1}; (2) **log** for variance stabilization; (3) **seasonal differencing**; (4) **detrending** (remove linear trend). Test with ADF/KPSS in production; in interview, differencing + log is enough.
### Random forest vs XGBoost

| | Random Forest | XGBoost |
|---|---------------|---------|
| Ensemble | **Bagging** — trees independent, vote/average | **Boosting** — trees sequential, each fits prior residuals |
| Bias/variance | Lowers **variance** | Often lower bias; can overfit if not regularized |
| Training | Parallel trees | Sequential (fast implementations still optimized) |
| Extra | Random feature subsampling | Shrinkage (η), depth limits, L1/L2 on splits |

One-liner: "RF averages decorrelated trees; XGBoost iteratively corrects errors with shallow trees and strong regularization."

## Decisions / artifacts updated

- [x] [`debrief/2026-06-30_ps1-karan-real-interview.md`](2026-06-30_ps1-karan-real-interview.md)
- [x] [`code/2026-06-30_trailing_zscore_normalization.py`](../../code/2026-06-30_trailing_zscore_normalization.py)
- [x] [`INDEX.md`](../INDEX.md) — PS1 outcome row + debrief index
- [x] root [`INDEX.md`](../../INDEX.md) — timed log row (real PS1 coding)
- [ ] [`stories/ownership_killed-tr-synthetic.md`](../stories/ownership_killed-tr-synthetic.md) — re-tag LP; add 2–3 min version
- [ ] [`stories/README.md`](../stories/README.md) — Ownership → Have Backbone mapping note

## Open questions

- Which LP question did Karan settle on? (User to recall — update story bank.)
- Did coding partially pass or fail entirely?
- Any signal on next round / timeline?

## Next session (one prompt for session B)

> Read `@Files Amazon_FinTech/debrief/2026-06-30_ps1-karan-real-interview.md`. (1) Draft a **2–3 min Have Backbone** version of TR kill. (2) Run 15 min spoken drill on stationary TS + RF vs XGBoost + LoRA. (3) Retype trailing z-score from memory in 15 min with narration.
