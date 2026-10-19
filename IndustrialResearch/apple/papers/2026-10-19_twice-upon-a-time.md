# Chat card — Twice Upon a Time

**Paper:** *Twice Upon a Time: Complementary Representations for Time-Series Reasoning.* arXiv:[2610.22327](https://arxiv.org/abs/2610.22327).

**Use this second**, if he asks about representations, multimodal models, or why a second view should exist. Do not open with it. It is a time-series reasoning paper. Profile A is the distillation paper.

**Authors:** Hedi Zisling and Liran Nochumsohn (equal contribution), Ilan Naiman, Mihir Parmar (Google), Omri Azencot. Parmar’s affiliation is not a deployment claim.

Older prep notes quote TSRBench around 45.6 and TSExam 0.926. This preprint is the one to use.

---

## One sentence

Qwen3-VL-8B sees each series twice: a line plot that keeps the measurement frame, and a normalized delay image that throws away positive rescaling and offset. The gain shows up past perception, and a second copy of the same view does not reproduce it.

## The two views

Line plot: raw values, own axis per variate, no amplitude normalization. The native Qwen3-VL vision encoder stays frozen and emits **230 tokens** per series.

Delay map: \(W\) overlapping windows, each resampled to \(H\) samples, stacked as columns, then min–max normalized to \([0,1]\). Any \(ax+b\) with \(a>0\) yields the same image. DINOv3 ViT-L/16, with LoRA only in stage I, emits **64 tokens** per variate. Window length is a fraction of the series length, with floors and caps. The rendered delay image is \(256\times 256\).

Fusion is not a learned gate. The two token spans are concatenated, each wrapped in vision-start and vision-end. DeepStack adds three intermediate feature maps into the first three language-model layers, at each stream’s own token positions. Plot features come from the frozen Qwen tower. Delay features come from DINOv3 blocks 6, 12, and 18.

## Training

Stage I: freeze Qwen’s vision encoder and the language model. Train DINOv3 LoRA (rank 64, \(\alpha=128\)) and the delay projections on captions. Stage I data: 15,995 real CaTS captions, 32,000 synthetic ChatTS-style captions, 7,701 structural captions. Equal sampling.

Stage II: merge the DINOv3 LoRA, freeze the whole visual path, LoRA the language model (rank 32, \(\alpha=64\), dropout 0.05) on question answering. Loss is next-token loss on answer tokens only. Stage II is 182,815 examples, mostly synthetic, with labels taken from the generator rather than from another LLM. A small set of real sports series is in the reasoning mix.

They say no TSRBench or TSExam eval items are in training, and they checked the reasoning corpus for exact series overlap, shared sports games, and exact question–answer matches. The task families and answer formats were aligned with TSRBench. That alignment is a fair attack even though the instances are new.

## Numbers

TSRBench overall, 4,125 questions. Quote the table, not the abstract. The abstract says the plot-only model is at 44.5%. Table 3 says **45.2%**. Yours is **53.2%**.

| Model | TSRBench overall |
|---|---:|
| Qwen3-VL-8B, plots, no your training | 38.9 |
| TimeOmni-1-7B, strongest dedicated TSLM they rank | 36.7 |
| ChatTS-14B | 33.5 |
| TS-Reasoner-7B | 36.4 |
| Plot only, your training | 45.2 |
| Delay only | 40.5 |
| Plot+Plot (same view, both towers) | 44.8 |
| Delay+Delay | 42.6 |
| **Dual view** | **53.2** |
| GPT-5, visual only (reference, not size-matched) | 52.4 |
| GPT-5, text and visual | 55.6 |

Category totals, which matter more than the headline:

| | Perception | Reasoning | Prediction | Decision | Overall |
|---|---:|---:|---:|---:|---:|
| Plot only | 87.4 | 35.8 | 38.0 | 36.4 | 45.2 |
| Dual | 86.4 | 40.1 | 61.7 | 37.6 | 53.2 |

Perception does not improve. Decision is +1.2 points. Reasoning is +4.3. The overall jump is the prediction category.

Inside prediction, say this before he asks. Event prediction goes from **21.7 to 84.2**. Forecasting goes from **46.2 to 50.4**. The category number 61.7 is mostly one task.

**TSExam, 746 questions: plot only 89.9%, dual view 89.9%.** The delay stream does not move this benchmark. The abstract’s “89.9% on TSExam” is true and is not evidence for the second view.

**ChatTS numerical alignment.** Univariate 78.1% plot only to 80.5% dual. Multivariate 86.4% to 86.8%. Real, small. Delay only falls to about 29–31% numerical. The plot carries the numbers. Delay only is also stronger than the plot on some ChatTS reasoning slices (deductive 0.605 versus 0.548; causal 0.857 versus 0.851). The dual model’s ChatTS reasoning average is 0.615 versus 0.613 for plot only. Do not say the second view wins reasoning in general.

## The control that answers “you just added capacity”

Plot+Plot and Delay+Delay keep both encoders, both token budgets, and the same two-stage training. They feed the same picture to both towers. They land at 44.8 and 42.6, next to the single-view models, not at 53.2. The claim that survives is complementarity, not a second stream.

## Invariance

Delay only, on the 2,020-item subset, stays near its clean 44.7% under \(\times 0.1\), \(\times 10\), \(\pm 5\sigma\), and z-scoring. That matches the normalization. The dual model stays sensitive, because the plot stream still sees the axes. On that subset its clean accuracy is 66.5, and it remains higher in absolute accuracy than plot only under noise, smoothing, and horizon changes. Do not say the combined model is invariant. Say it has access to an invariant view and still has the measurement frame.

Appendix C.5: delay embeddings win on TSRBench; STFT has small advantages on ChatTS numerical alignment and average reasoning. The second representation is not uniquely determined.

## Where he will push

1. **Event prediction, 21.7 to 84.2.** That single cell is most of the prediction story. Be ready to say how the label is defined and why it is not a format leak. If you cannot, do not lean on the 53.2.
2. **TSExam is a plot-only result.** 89.9 either way.
3. **Training formats were aligned to TSRBench’s task families.** Instances are held out. The interface was not.
4. **A numerical encoder might be cheaper than 230 vision tokens.** Delay only cannot read numbers. The plot is doing the quantitative work. You have not shown that a small numeric encoder plus the delay image would lose.
5. **The combined model is not robust in the sense of the delay map.** Affine changes still move it.
6. **Most training series are synthetic.** Real data in the mix are CaTS captions and a small sports subset.

## Link to their work, one sentence

*Electric sheep* asks whether a multimodal model forms an implicit state while predicting actions. This paper asks whether two explicit views, with different invariances, change reasoning once a single view is already a strong perceptual encoder. The same-view control is the result to mention. Their visual-token chain of thought is a different intervention: they add imagined frames, you add a second view of the same series.
