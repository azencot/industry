# Debrief — 2026-08-22 — LLM training mechanics (Day 1B)

## Session

- Type: exploration / tech-screen study (Apple Health AIML, Feng Zhu Tue 8/25)
- Duration: ~45 min spoken + quiz. nanoGPT / `FromMemory` attn **still not done**.
- Prior: [`2026-08-21_llm-pipeline-attn-lockin.md`](2026-08-21_llm-pipeline-attn-lockin.md)

## Conclusions

**Day 1B — mostly locked.** Object is one parameter update: forward → CE → backward (maybe accum) → clip → AdamW → zero.

| Knob | Lock |
|------|------|
| \(\eta\) | Learning rate / step size. Warmup **is** \(\eta(t)\) ramping from ~0, then cosine. Not a separate “tune weights then start the scheduler.” |
| \(\lambda\) | Weight-decay coefficient. \(w \leftarrow w - \eta\lambda w\) **outside** \(m,v\). Not per-sample loss weight. No decay on bias / RMSNorm. |
| \(m\) | 1st moment: EMA of \(g\). Direction (momentum). |
| \(v\) | 2nd moment: EMA of \(g^2\). Per-parameter scale. Not the SGD “velocity” \(v\). |
| fp16 loss scale | 5-**bit** exponent; tiny grads **underflow to 0**. \(L \times S\), backward, **unscale** in fp32, then Adam. Inf/NaN = \(S\) too big → skip, cut \(S\). bf16: same range as fp32, no scale. |
| Pack | Labels `-100` and/or block attn at the splice. Else doc B is in doc A’s CE. Files ≠ tokens. |
| Clip | After accum, not per micro-batch. |
| tokens/step | \(B_{\mathrm{micro}}\times\mathrm{accum}\times T\times n_{\mathrm{gpu}}\) |

**7B doesn’t fit — try order:** bf16 + LoRA → smaller \(T\) / microbatch + **accum** → FlashAttention → **grad checkpointing** → DDP if it fits → **FSDP/ZeRO last**. FSDP shards **params, grads, Adam \(m,v\)**. Not activations.

**Train ↓ val ↑:** eval bug / mix first; then overfit (epochs, no replay). Too-high LR usually wrecks **train** too. Task flat + NLL ↓ = mixture NLL ≠ task.

## Corrections (keep)

- \(\beta\): \(m \leftarrow \beta_1 m + (1-\beta_1)g\) with \(\beta_1\approx 0.9\), \(\beta_2\approx 0.999\). **Most weight on the past.** Do not write \((1-\beta)m + \beta g\).
- Warmup first pass was “tune coefficients until scheduler kicks in” — wrong.
- fp16 “5 digits” → 5 **bits**. Underflow ≠ overflow.
- Do not lead 7B with ZeRO on activations. Checkpointing before FSDP.
- First 6-Q pass: high LR as first check for train↓ val↑ — wrong order.

## Decisions / artifacts updated

- [x] this file; prep calendar Sat line; `GenAI/INDEX.md`
- [ ] `day1_attention.py` FromMemory — still open
- [ ] AGENTS.md — no change

## Open questions

- Re-say AdamW with \(\beta_1,\beta_2\) and the 7B order once more if they feel mushy. Else Day 2.

## Next session (one prompt for session B)

> Read `GenAI/notes/2026-08-22_llm-training-mechanics-lockin.md`. Day 1A+1B locked except optional attn `FromMemory`. Start **Day 2 multimodal**: concat vs cross-attn vs unified tokens; CLIP \(s_{ij}\); LLaVA projector; then wearables Q12. Do not open RelCon or Bosch.
