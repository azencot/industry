# Siemens phone screen — PyTorch coding

Live coding for the **Mon 2026-10-19 / Tue 2026-10-20** screen. Robinson: PyTorch/Python plus ML breadth. Examples she named: `DataLoader`, simple padding, attention matrix. The code has to **run on simple unit tests**.

Chandler also put **STAR** on this screen. Stories stay in the [debrief](../2026-10-14_recruiter-debrief.md). This folder is the coding half.

Not LeetCode. Not ML theory. The job is to implement tensor ops fast, say the shapes, and make a test pass.

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

| Day | Date | Files |
|-----|------|-------|
| 1 | Thu 15 | **01–03 done.** Still 04, 13. |
| 2 | Fri 16 | 05–08. End with attention from scratch, timed. |
| 3 | Sat 17 | 09–12, 15. Then one easy Python problem, not from this folder. |
| 4 | Sun 18 | Two 40–45 min mocks. No solution file. Mock 1 = 01+03. Mock 2 = 05+06. |
| Screen morning | Mon or Tue | From memory: collate, padding mask, attention, one train loop. Stop there. |

## Order

| # | Problem | Files | Status |
|---|---------|-------|--------|
| 1 | `collate_fn` for variable-length sequences | [`01_collate.py`](01_collate.py) · [`01_collate_solution.py`](01_collate_solution.py) | **Done 2026-10-15.** Runs on the sample. Lengths still need one pass over `.shape[0]`. `pad_sequence` does the same copy loop in C++. Mask is `arange(Tmax)[None, :] < lengths[:, None]`. |
| 2 | Right and left padding | [`02_pad_sequences.py`](02_pad_sequences.py) · [`02_pad_sequences_solution.py`](02_pad_sequences_solution.py) | **Done 2026-10-15.** Right pad is `[:Ti]`, left pad is `[-Ti:]`. Equal lengths need no extra branch. |
| 3 | Padding mask, and the attention broadcast shape | [`03_padding_mask.py`](03_padding_mask.py) · [`03_padding_mask_solution.py`](03_padding_mask_solution.py) | **Done 2026-10-15.** `valid_true=False` flips the mask. Key mask is `[B, 1, 1, T]`. |
| 4 | Masked sum, mean, MSE | [`04_masked_reductions.py`](04_masked_reductions.py) · [`04_masked_reductions_solution.py`](04_masked_reductions_solution.py) | |
| 5 | Scaled dot-product attention | [`05_attention.py`](05_attention.py) · [`05_attention_solution.py`](05_attention_solution.py) | |
| 6 | Attention with key padding and a causal mask | [`06_masked_attention.py`](06_masked_attention.py) · [`06_masked_attention_solution.py`](06_masked_attention_solution.py) | |
| 7 | Causal mask, combined with padding | [`07_causal_mask.py`](07_causal_mask.py) · [`07_causal_mask_solution.py`](07_causal_mask_solution.py) | |
| 8 | Multi-head split, attend, merge | [`08_multihead.py`](08_multihead.py) · [`08_multihead_solution.py`](08_multihead_solution.py) | |
| 9 | MLP and a residual block | [`09_mlp.py`](09_mlp.py) · [`09_mlp_solution.py`](09_mlp_solution.py) | |
| 10 | One training epoch | [`10_train_loop.py`](10_train_loop.py) · [`10_train_loop_solution.py`](10_train_loop_solution.py) | |
| 11 | Eval loop | [`11_eval_loop.py`](11_eval_loop.py) · [`11_eval_loop_solution.py`](11_eval_loop_solution.py) | |
| 12 | Batched dot, cosine, Euclidean | [`12_pairwise.py`](12_pairwise.py) · [`12_pairwise_solution.py`](12_pairwise_solution.py) | |
| 13 | `Dataset` of tensor pairs | [`13_dataset.py`](13_dataset.py) · [`13_dataset_solution.py`](13_dataset_solution.py) | |
| 14 | Sliding-window time series | [`14_sliding_window.py`](14_sliding_window.py) · [`14_sliding_window_solution.py`](14_sliding_window_solution.py) | |
| 15 | Cross-entropy that ignores padding | [`15_masked_ce.py`](15_masked_ce.py) · [`15_masked_ce_solution.py`](15_masked_ce_solution.py) | |

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
