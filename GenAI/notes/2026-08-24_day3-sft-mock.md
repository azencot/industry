# Debrief — 2026-08-24 — Day 3 SFT + debug + mock (Q1–Q11)

## Session

- Type: exploration / tech-screen study (Apple Health AIML, Feng Zhu Tue 8/25)
- Duration: ~2 h (SFT teach + quiz, broken-attn worksheet, mock Q1–Q11). **Q12 not spoken.**
- Prior: [`2026-08-23_day2-multimodal-recap.md`](2026-08-23_day2-multimodal-recap.md)
- Worksheet: [`../interviews/apple-health-aiml/code/day3_broken_attention.py`](../interviews/apple-health-aiml/code/day3_broken_attention.py)

## Conclusions

**Day 3 — SFT + Q1–Q11 mostly locked. Q12 is the leftover speak.**

### SFT

SFT is teacher-forced next-token CE on a **fixed** string. There is **no train decode**, no temperature in the inner loop. Generate is eval, synthetic-data collection, or RL.

| Object | Lock |
|--------|------|
| Template | Train tokens = serve tokens. Dump one train row vs one inference prompt. ChatML in, ChatML out. |
| Completion-only | User/system (and vision) = `-100`. `answer_from` = **last prompt index** so `logits[last prompt] → first answer` stays in CE. Else the question owns the loss. |
| Short answer | Mask the prompt **harder**. Do not unmask “for signal.” |
| Pretrain vs SFT | All-tokens vs assistant-only. Select pretrain on **held-out NLL** (still ≠ task). Select SFT on a **held-out task** vs frozen Instruct, same decode. Report test once. |
| Stage A | Caption **next-token**, LM frozen. Not CLIP. Do not say bare “alignment.” |
| Stage B | Completion-only QA, LoRA. Kill + gates belong **here** (TR 26.9 → 21.9; 8B 0.62 → ~0.90). |

**“Loss fine, decode garbage” — different bugs, walk this order:**

1. **Template** — Alpaca vs ChatML, thinking on/off. Prefix ≠ train string. Greedy still junk.
2. **Labels** — prompt in CE, `answer_from` off by one, truncated answers.
3. **Decode settings** — same template; demo is `do_sample` / extra system prompt / wrong stop. **Not labels.**
4. **Tokenizer / pad** — `pad_token = eos` trains “predict EOS” on unmasked pads; new special id without resized \(E\).
5. **Then** LR / bf16.

### Broken attention (`attn_*`)

One defect each. Do **not** hunt missing \(W_O\) (none of the stubs have it).

| Fn | Bug | Symptom |
|----|-----|---------|
| `attn_a` | no \(1/\sqrt{d_k}\) | Dots \(\sim d_k\); softmax saturates; grads die. Not “overflow.” |
| `attn_b` | no causal \(M\) | Bidirectional. **Not an LM.** CE can still fall. |
| `attn_c` | not multi-head (merge to width \(C\)) | One subspace. \(1/\sqrt{C}\) is correct **for that** one head. |
| `attn_d` | `+ pad_mask` → `+1` on pad **scores** | Pad keys preferred, not masked. |
| NaN | whole row \(-\infty\), then softmax | `softmax([-inf,…])` is NaN. Then unscaled dots / fp16. **Not** new-token ids (those crash or are a decode bug). |

### Mock Q1–Q11 (what to say)

| Q | Status | Tuesday sentence |
|---|--------|------------------|
| 1 | spine; two kills | RMS**Norm** (not RMSprop); `lm_head` not classification head; close with shift CE → AdamW |
| 2 | formula locked | Scale exists so softmax does **not** saturate. \(d_k=C/H\). \(y_i=\sum_j A_{ij}v_j\) |
| 3 | RoPE miss | Rotate **Q/K**; score \(q_i^\top R_{j-i}k_j\); relative; **not** “rotation invariant”; not in \(M\) |
| 4 | almost | Insert **FlashAttention** before checkpointing. FSDP = params, grads, Adam \(m,v\). Not activations |
| 5 | labels locked | Caption next-token A, completion B. Promote on **task**. Include the kill |
| 6 | drawing locked | Projector = **spaces**. Concat length \(T_{\mathrm{mod}}+T\); scatter stays \(T\). RoPE on fused index |
| 7 | locked | Do not pick concat to stop a shortcut. Xattn gate \(\gamma\sim 0\) |
| 8 | CLIP locked | L2 then \(s_{ij}/\tau\). Retrieval ≠ generation. Adding images = projector + insert + SFT, **not CLIP** |
| 9 | 1 locked | Why: shortcut, or no grad (`detach` / \(\gamma\sim 0\)). Seq too long ≠ no-grad. Fix (if asked): task/eval |
| 10 | encodings locked | Don’t name OpenTSLM. Charts on PPG are a **kill**. Long seq is **fusion**, not “use patches” |
| 11 | first check locked | All-\(-\infty\) row → fp16/unscaled → vision NaN → then LR. Not tokenizer |
| 12 | **not spoken** | [`2026-08-23_day2-multimodal-recap.md`](2026-08-23_day2-multimodal-recap.md) §9 |

## Corrections (keep)

- There is **no train decode**. SFT is teacher force on the tokenized train rows.
- Template ≠ decode settings ≠ `pad = eos`.
- RMSNorm ≠ RMSprop. RoPE ≠ rotation-invariant embeddings.
- \(1/\sqrt{d_k}\) is saturation / dead grads, not “softmax overflow.”
- Bare “alignment” sounds like CLIP. Stage A is caption next-token.
- Q9 mechanism 2 is a **cut graph**, not length.
- Q10/Q12: do not reprint matplotlib on PPG. Do not name OpenTSLM / RelCon / Feng’s mood paper.
- Q11 NaN is not the “loss fine, decode garbage” walk.

## Decisions / artifacts updated

- [x] this file; `GenAI/INDEX.md`; `GenAI/interviews/INDEX.md`; `GenAI/notes/README.md`
- [x] `day3_broken_attention.py`; code README
- [x] leftover Day 2 recap already on disk, now indexed
- [ ] Q12 spoken
- [ ] `day1_attention.py` FromMemory — still open (skip; screen is spoken)
- [ ] AGENTS.md — no change

## Open questions

- Q12 20s landing, out loud, once. Then stop until Tue AM.

## Next session

> Speak **Q12** from [`2026-08-23_day2-multimodal-recap.md`](2026-08-23_day2-multimodal-recap.md) §9 (window-align, mix subsets, no charts on PPG, concat vs bottleneck). Do not reopen Q1–Q11 unless a sentence slips. Then **Tue AM retrieval only**: Q1 spine, Q6 concat, Q10 encodings, Q12 missingness. Join Webex after 1:25 PM PDT. Do not open RelCon or Bosch.
