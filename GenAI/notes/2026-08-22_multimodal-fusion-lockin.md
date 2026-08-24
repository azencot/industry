# Debrief — 2026-08-22 — multimodal fusion (Day 2, partial)

## Session

- Type: exploration / tech-screen study (Apple Health AIML, Feng Zhu Tue 8/25)
- Duration: ~40 min teach + 5 spoken Q. Stopped before CLIP, toy `MultiModalLM`, wearables Q12.
- Prior: [`2026-08-22_llm-training-mechanics-lockin.md`](2026-08-22_llm-training-mechanics-lockin.md)

## Conclusions

**Day 2 — families + labels + concat-vs-xattn, not the full day.** Two axes: **encoding** (text / images / native TS — HM) vs **fusion** (how it meets the LM — today).

| Object | Lock |
|--------|------|
| Projector | \(z\in\mathbb{R}^{d_v}\mapsto Wz\in\mathbb{R}^{d_{\mathrm{LLM}}}\). Exists because **spaces** differ, not only widths. Equal \(d\) still needs \(W\). Not fusion. Skip → crash or pad-junk. |
| Concat (LLaVA) | Scatter/replace into the LM sequence. Length \(T+T_{\mathrm{mod}}\). Cost \(\mathcal{O}((T+T_{\mathrm{mod}})^2)\). Dual tower = this family **twice**. |
| Xattn (Flamingo) | Text is Q, modality is K/V. Length stays \(T\). Cost \(\mathcal{O}(T\cdot T_{\mathrm{mod}})\). **Resample** to fixed latents = bottleneck. Gated: \(\gamma\sim 0\) → modality unused. |
| Unified | Same Transformer sees patched/quantized signal. You **train** that encoder. Vocab expansion is plumbing, not the fusion site. Native TS encoder + projector + concat into Mistral = **family 1 with an honest encoder**. |
| Causal + labels | Early vision does **not** see later text; later text **does** see vision. Loss on **answer** tokens only. Vision (and usually prompt) = `-100`. |
| Forget `-100` | Distinctive **CE** leak is \(\mathrm{vis}_i\rightarrow\mathrm{vis}_{i+1}\) (or repeated `<image>` id). Causal already stops last-vis from attending forward. After `-100`, **first-text still attends to last-vis**. |
| When xattn | Long \(T_{\mathrm{mod}}\) (video / hours of IMU/PPG) or you want a latent bottleneck. |
| When concat | Small \(T_{\mathrm{mod}}\) (chart ~114 + delay 64), reuse the pretrained LM. **Your stack.** |

**Text shortcut:** neither family prevents it. Change the **task/eval**. Concat makes patches first-class tokens (availability). It is not a stronger constraint.

## Corrections (keep)

- Projector: do not stop at “dims don’t match.” Equal width still needs a learned basis.
- Unified ≠ “fusion at the dictionary.”
- Concat family failure is \(T_{\mathrm{mod}}\) / \(T^2\) (or ignore patches) — **not** the `-100` label bug (that is any insert-token recipe).
- `-100` on vision does **not** stop first-text from attending to last-vis. Last-vis attending forward is causal, not labels.
- Do **not** pick concat “because it stops a text shortcut.”

## Decisions / artifacts updated

- [x] this file; prep calendar Sun line; `GenAI/INDEX.md`; `GenAI/interviews/INDEX.md`
- [x] CLIP + Q12 + Q9 taught (2026-08-23). Readable recap: [`2026-08-23_day2-multimodal-recap.md`](2026-08-23_day2-multimodal-recap.md)
- [x] `day2_multimodal.py` — scatter path shaped; concat impl left blank
- [ ] `day1_attention.py` FromMemory — still open
- [ ] AGENTS.md — no change

## Open questions

- Day 2 recap is the recall object. Monday = Day 3 SFT + 12 Q.

## Next session (Day 3)

> Read `GenAI/notes/2026-08-23_day2-multimodal-recap.md` if fusion is mushy (15 min max). Then **Day 3**: SFT template / `-100` on the question, broken Attention, 12 questions aloud. Do not reopen RelCon or Bosch.
