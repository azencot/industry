# Debrief — 2026-08-21 — LLM pipeline + attention lock-in

## Session

- Type: exploration / tech-screen study (Apple Health AIML, Feng Zhu Tue 8/25)
- Duration: ~1.5 h (plan recast + pipeline Q&A). Attention implementation **not** started.
- Prior context: HM screen same day; Tyler locked spoken LLM training + multimodality, no pad.

## Conclusions

**Plan:** 3-day bootcamp (pipeline/attn → multimodal fusion → SFT + 12 Q). Study object is equations ↔ architecture ↔ training decision ↔ small code. VLM run is evidence, not the textbook. Screen stays spoken.

**Day 1A pipeline — locked**

| Object | Lock |
|--------|------|
| Tokenizer | Frozen string→id (BPE). Not updated by CE. |
| `E` `[V,C]` | Trainable lookup. Row `i` = token id `i`. LoRA SFT often freezes `E`. |
| Ids | `0 … V-1` (`< V`). `V` = vocab. |
| `C` | Hidden size. `x` is `[B,T,C]`. |
| RoPE | **Not** in `M`. Per-position rotations on **Q and K only**. |
| `M` | Causal mask on scores. |
| SwiGLU | The MLP / FFN. |
| RMSNorm | RMS, no mean-center. Qwen/LLaMA. |
| Training CE | Parallel: `CE(logits[:,:-1], ids[:,1:])`. Loop is **inference**. |
| AdamW | Decoupled **weight** decay. **Not** per-sample loss weights. |

**RoPE (do not cancel):** one shared `R` gives `Q R Rᵀ Kᵀ = QKᵀ`. Correct: \(\tilde q_i=R_i q_i\), \(\tilde k_j=R_j k_j\), score \(q_i^\top R_{j-i} k_j\).

**Why \(Y=AV\):** tokens as **rows**. \(y_i=\sum_j A_{ij} v_j\). Column-vector habit would be \(VA^\top\).

## Corrections (keep)

- AdamW ≠ “weighting per sample.”
- RoPE ≠ term in `M`; ≠ one `R` on both Q and K.
- Next-token training is not an RNN loop.

## Decisions / artifacts updated

- [x] [`../interviews/apple-health-aiml/2026-08-21_tech-screen-prep.md`](../interviews/apple-health-aiml/2026-08-21_tech-screen-prep.md) — 3-day bootcamp
- [x] [`../interviews/apple-health-aiml/code/day1_attention.py`](../interviews/apple-health-aiml/code/day1_attention.py) — trace + `FromMemory` stub
- [ ] experience profile / AGENTS.md — no change

## Open questions

- Continue tonight vs stop: user unsure. If continue → attention forward + shapes, not Day 2.

## Next session (one prompt for session B)

> Read `GenAI/notes/2026-08-21_llm-pipeline-attn-lockin.md` and `GenAI/interviews/apple-health-aiml/code/day1_attention.py`. Pipeline is locked. Implement `CausalSelfAttentionFromMemory`, say every shape including why `Y=AV`. Then Day 1B (AdamW/bf16/packing/7B-doesn’t-fit) only if energy. Do not start multimodal.
