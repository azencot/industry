# Siemens phone screen — PyTorch coding

Live coding for **Fri 23 Oct 2026, 22:00–23:00 Thailand**, with Huzefa Rangwala. The coding half is still one PyTorch function plus a unit test. Robinson’s examples: `DataLoader`, simple padding, attention matrix. The full hour (resume half, what to raise, the three mornings) is [`../2026-10-17_huzefa-screen.md`](../2026-10-17_huzefa-screen.md).

Stories stay in the [bank](../2026-10-15_behavioral-story-bank.md). This folder is the coding half.

Prep is **~70–75% coding**. Attention is already practiced. The live schedule is [`../2026-10-20_coding-plan.md`](../2026-10-20_coding-plan.md). A–N have no solution file. L runs as written; the bugs are not marked.

## How to practice

Open the **problem** file only. Do not open `*_solution.py` until your file runs.

1. Restate the problem.
2. State input and output shapes before writing code.
3. Name assumptions (mask convention, padding side, what an empty mask should do).
4. Implement. Prefer tensor ops over Python loops.
5. Write 2–4 asserts: shape, a tiny numeric case, batch size 1, equal lengths, one edge.
6. Run the file. Fix the failure out loud.
7. Say complexity if it matters (attention is about `Tq * Tk * D`).

## Schedule

Sun 18 and Mon 19 are off. Three mornings start Tuesday. Detail and the spoken half: [`../2026-10-17_huzefa-screen.md`](../2026-10-17_huzefa-screen.md).

| Day | Date | Files |
|-----|------|-------|
| — | Thu 15–Fri 16 | **01–04 and 13 done.** **05–08 drafted** in the problem files; core asserts passed 2026-10-17. Tuesday does not reread them. |
| — | **Sat 17** | [`tue_attention.py`](tue_attention.py) and broadcast A, B, D. Attention is no longer the main track. |
| 1 | **Tue 20** | [`A_transformer_block.py`](A_transformer_block.py) and [`B_train_eval.py`](B_train_eval.py) drafted. [`E_infonce.py`](E_infonce.py) drafted the same day. C drafted later; do not repeat it. |
| 2 | **Wed 21** | **17**, [`G_layernorm.py`](G_layernorm.py), [`14_sliding_window.py`](14_sliding_window.py), [`H_kmeans.py`](H_kmeans.py), [`F_minigpt.py`](F_minigpt.py), and [`I_mean_pool.py`](I_mean_pool.py) drafted. 17b not started. |
| 3 | **Thu 22** | [`J_gaussian_nll.py`](J_gaussian_nll.py), [`K_forecast_covariates.py`](K_forecast_covariates.py), [`M_gru_classifier.py`](M_gru_classifier.py), then [`L_wont_learn.py`](L_wont_learn.py), then unseen mock 1. Mock 2 if time remains. **N** only after both mocks. |
| Daytime | **Fri 23** | Mock 2, if Thursday did not reach it. Not in the hour before the call. |
| Pre-call | **Fri 23, last 20 min** | Block structure, train step, one mask shape, three story anchors. No new exercise. |

## Order

| # | Problem | Files | Status |
|---|---------|-------|--------|
| 1 | `collate_fn` for variable-length sequences | [`01_collate.py`](01_collate.py) · [`01_collate_solution.py`](01_collate_solution.py) | **Done 2026-10-15.** Runs on the sample. Lengths still need one pass over `.shape[0]`. `pad_sequence` does the same copy loop in C++. Mask is `arange(Tmax)[None, :] < lengths[:, None]`. |
| 2 | Right and left padding | [`02_pad_sequences.py`](02_pad_sequences.py) · [`02_pad_sequences_solution.py`](02_pad_sequences_solution.py) | **Done 2026-10-15.** Right pad is `[:Ti]`, left pad is `[-Ti:]`. Equal lengths need no extra branch. |
| 3 | Padding mask, and the attention broadcast shape | [`03_padding_mask.py`](03_padding_mask.py) · [`03_padding_mask_solution.py`](03_padding_mask_solution.py) | **Done 2026-10-15.** `valid_true=False` flips the mask. Key mask is `[B, 1, 1, T]`. |
| 4 | Masked sum, mean, MSE | [`04_masked_reductions.py`](04_masked_reductions.py) · [`04_masked_reductions_solution.py`](04_masked_reductions_solution.py) | **Done 2026-10-15.** Sum and mean reduce over T. MSE averages every valid element. `clamp_min(1)` covers an all-pad row. |
| 5 | Scaled dot-product attention | [`05_attention.py`](05_attention.py) · [`05_attention_solution.py`](05_attention_solution.py) | **Drafted.** Core assert passed 2026-10-17. Not the main track. |
| 6 | Attention with key padding and a causal mask | [`06_masked_attention.py`](06_masked_attention.py) · [`06_masked_attention_solution.py`](06_masked_attention_solution.py) | **Drafted.** Padding, causal, both, and the all-pad row passed 2026-10-17. |
| 7 | Causal mask, combined with padding | [`07_causal_mask.py`](07_causal_mask.py) · [`07_causal_mask_solution.py`](07_causal_mask_solution.py) | **Drafted.** `tril` mask and the `[B, 1, T, T]` combine passed 2026-10-17. |
| 8 | Multi-head split, attend, merge | [`08_multihead.py`](08_multihead.py) · [`08_multihead_solution.py`](08_multihead_solution.py) | **Drafted.** Shape and the identical-token case passed 2026-10-17. |
| 9 | MLP and a residual block | [`09_mlp.py`](09_mlp.py) · [`09_mlp_solution.py`](09_mlp_solution.py) | |
| 10 | One training epoch | [`10_train_loop.py`](10_train_loop.py) · [`10_train_loop_solution.py`](10_train_loop_solution.py) | |
| 11 | Eval loop | [`11_eval_loop.py`](11_eval_loop.py) · [`11_eval_loop_solution.py`](11_eval_loop_solution.py) | |
| 12 | Batched dot, cosine, Euclidean | [`12_pairwise.py`](12_pairwise.py) · [`12_pairwise_solution.py`](12_pairwise_solution.py) | |
| 13 | `Dataset` of tensor pairs | [`13_dataset.py`](13_dataset.py) · [`13_dataset_solution.py`](13_dataset_solution.py) | **Done 2026-10-15.** One index per `__getitem__`. `DataLoader` stacks equal shapes. |
| 14 | Sliding-window time series | [`14_sliding_window.py`](14_sliding_window.py) · [`14_sliding_window_solution.py`](14_sliding_window_solution.py) | **Drafted Wed 21.** Length is `max(T - L - H + 1, 0)`. |
| 15 | Cross-entropy that ignores padding | [`15_masked_ce.py`](15_masked_ce.py) · [`15_masked_ce_solution.py`](15_masked_ce_solution.py) | Covered in composed form by 18. |
| 16 | Pad, self-attend, masked mean pool | [`16_varlen_pool.py`](16_varlen_pool.py) · [`16_varlen_pool_solution.py`](16_varlen_pool_solution.py) | Off the main track as of 2026-10-20. |
| 17 | Attention across series, not time | [`17_group_attention.py`](17_group_attention.py) · [`17_group_attention_solution.py`](17_group_attention_solution.py) | **Drafted Wed 21.** `[B, G, T, D]`, attend on `G`. Key mask is `[B*T, 1, G]`. |
| 17b | Cross-group attention | [`17b_cross_group.py`](17b_cross_group.py) · [`17b_cross_group_solution.py`](17b_cross_group_solution.py) | Set aside Wed 21. Same rearrange as 17. |
| 17c | Multi-head cross-group | [`17c_group_multihead.py`](17c_group_multihead.py) · [`17c_group_multihead_solution.py`](17c_group_multihead_solution.py) | Optional after 17b, only inside the 30 min cap. |
| 18 | Masked cross-entropy and one train step | [`18_masked_train_step_broken.py`](18_masked_train_step_broken.py) · [`18_masked_train_step.py`](18_masked_train_step.py) · [`18_masked_train_step_solution.py`](18_masked_train_step_solution.py) | Superseded by **C** for Tue 20. |
| 19 | Per-series attend over time, then pool | [`19_thu_mock.py`](19_thu_mock.py) · [`19_thu_mock_solution.py`](19_thu_mock_solution.py) | Not the Thursday mock anymore. Leave it closed. |
| — | Tuesday attention, heads in the shape | [`tue_attention.py`](tue_attention.py) · [`tue_attention_solution.py`](tue_attention_solution.py) | **Drafted Sat 17.** Passes. Do not repeat as its own drill. |
| — | Broadcast / mask micro-drills | [`tue_broadcast.py`](tue_broadcast.py) · [`tue_broadcast_solution.py`](tue_broadcast_solution.py) | **Sat 17: A, B, D pass.** C (`mask_group_keys`) still open. |
| — | Shape micro-drills | [`tue_shapes.py`](tue_shapes.py) · [`tue_shapes_solution.py`](tue_shapes_solution.py) | Dropped from the main track on 2026-10-20. |
| A | Pre-norm transformer block | [`A_transformer_block.py`](A_transformer_block.py) | **Drafted Tue 20.** No solution file. |
| B | Train step and eval | [`B_train_eval.py`](B_train_eval.py) | **Drafted Tue 20.** No solution file. |
| C | Masked CE, two ways, start broken | [`C_masked_ce_broken.py`](C_masked_ce_broken.py) | **Drafted.** Both reductions. Not a Thu 22 problem. No solution file. The unreduced comment still says `[B*T, C]`; `reduction="none"` returns `[B*T]`. |
| E | InfoNCE | [`E_infonce.py`](E_infonce.py) | **Drafted Tue 20.** No solution file. Diagonal of the softmax. |
| G | LayerNorm by hand | [`G_layernorm.py`](G_layernorm.py) | **Drafted Wed 21.** No solution file. Matches `nn.LayerNorm`. Mean and variance are `[..., 1]`. |
| H | K-means | [`H_kmeans.py`](H_kmeans.py) | **Drafted Wed 21.** No solution file. Centroids are `x[:k].clone()`. Assignments are recomputed from the returned centroids. |
| I | Mean-pool classifier | [`I_mean_pool.py`](I_mean_pool.py) | **Drafted Wed 21.** Embed, mean over T, linear to C. No solution file. |
| F | Mini causal LM | [`F_minigpt.py`](F_minigpt.py) | **Drafted Wed 21.** Embedding, causal block from A, next-token loss. No solution file. |
| J | Gaussian NLL | [`J_gaussian_nll.py`](J_gaussian_nll.py) | **Thu 22.** Problem only. Diagonal Gaussian, log-variance, pad mask. No solution file. |
| K | Forecast with covariates | [`K_forecast_covariates.py`](K_forecast_covariates.py) | **Thu 22.** Problem only. You choose the module. No future target. No solution file. |
| L | A model that does not learn | [`L_wont_learn.py`](L_wont_learn.py) | **Thu 22.** Runnable. Fit should fall under 1 after the fix. Bugs are not marked. No solution file. |
| M | Variable-length GRU classifier | [`M_gru_classifier.py`](M_gru_classifier.py) | **Thu 22.** Problem only. Last valid state. No solution file. |
| N | Supervised contrastive | [`N_supervised_contrastive.py`](N_supervised_contrastive.py) | **Optional, after both mocks.** Problem only. No solution file. |
| O | Bagging (screen redo) | [`O_bagging.py`](O_bagging.py) | **23 Oct screen.** Platform swapped SGD for this. Problem only. `n` indices via `randint(0, n - 1)`, list rows by index, majority vote, tie → smaller label. |

Mask convention in every file: **True = valid token**, False = pad. Say it before you code. If they flip it, flip the `~`.

## Shapes to know cold

```
sequences          Ti x D
padded batch       B x Tmax x D
padding mask       B x Tmax

Q                  B x Tq x D
K                  B x Tk x D
V                  B x Tk x Dv
Q K^T              B x Tq x Tk
attention out      B x Tq x Dv

multi-head Q/K/V   B x H x T x Dh
logits             B x H x T x T
merged             B x T x D
```

Key padding mask `[B, Tk]` becomes `[B, 1, Tk]` for single-head scores `[B, Tq, Tk]`, or `[B, 1, 1, Tk]` for multi-head scores `[B, H, T, T]`.

## Say these if they ask

- `Dataset` returns one item. `DataLoader` batches items and calls `collate_fn`.
- Pad so the batch is one tensor. Mask so the pad does not enter the softmax or the loss.
- Scale `Q K^T` by `sqrt(d)` so the softmax does not saturate.
- Mask **before** softmax. Filling invalid logits with 0 still lets them take probability mass. Use `-inf`.
- A causal mask blocks `j > i`. A padding mask blocks pad keys. They combine with AND on the allowed positions.
- If you skip the pad mask, pad positions change the weights and the output.
- `model.train()` / `model.eval()` flips dropout and batch-norm. `eval()` does not turn off gradients. `torch.no_grad()` does.
- `zero_grad` before the forward, or gradients add across steps.
- `CrossEntropyLoss` wants raw logits, not probabilities.
- Attention time is about `O(Tq * Tk * D)`. The score matrix is `O(Tq * Tk)` memory.

## Cold checklist

- [ ] custom `Dataset`
- [ ] `collate_fn`
- [ ] pad to the longest sequence
- [ ] padding mask from lengths
- [ ] masked mean
- [ ] masked loss
- [ ] scaled dot-product attention
- [ ] causal mask
- [ ] padding plus causal
- [ ] multi-head reshape
- [ ] small `nn.Module`
- [ ] training loop
- [ ] eval loop
- [ ] batched pairwise similarity
- [ ] sliding-window time-series `Dataset`
- [ ] variable-length attention pool (16), under 15 min or stop repeating it
- [ ] attention across the series axis (17)
- [ ] cross-group attention (17b) and multi-head (17c)
- [ ] masked train step, starting from the broken file (18)
- [ ] Gaussian NLL (J)
- [ ] Forecast with past and future covariates (K)
- [ ] GRU on a right-padded batch (M)
- [ ] Debug [`L_wont_learn.py`](L_wont_learn.py), then re-run until held-out MSE is under 1
- [ ] Unseen mock 1, then mock 2
- [ ] Supervised contrastive (N), only after both mocks
- [ ] 19 stays closed. It is not a mock.
