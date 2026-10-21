# Siemens coding plan — 20–23 Oct 2026

Supersedes the attention-and-mask schedule in [`2026-10-17_huzefa-screen.md`](2026-10-17_huzefa-screen.md). Resume questions in that file still stand. This file is the coding schedule.

**Screen:** Fri 23 Oct, 22:00–23:00 Thailand. About 25–30 min resume / ML breadth, then 25–30 min live PyTorch with unit tests. DataLoader, padding, and an attention matrix are examples, not the whole menu.

**Split:** about **70–75% coding**, **25–30%** resume. Across the coding time: **35%** modules, **25%** training / losses / debugging, **25%** attention and tensor ops, **15%** another ML algorithm.

No solution files for A–F. Do not look up an implementation before the attempt.

## Already done — not the focus

Dataset, `collate_fn`, padding, padding masks, masked reductions, scaled dot-product attention, causal attention, multi-head shapes. Sat 17: [`coding/tue_attention.py`](coding/tue_attention.py) and broadcast A, B, D.

The weakness is syntax under a clock: APIs, transpose / permute / reshape, broadcasting, mask polarity, cross-entropy layout, the training step, debugging.

APIs to stay inside: `nn.Module`, `nn.Linear`, `nn.LayerNorm`, `nn.Embedding`, `F.softmax`, `F.cross_entropy`, `matmul`, transpose / permute / reshape, masking, an optimizer, autograd. A problem should fit in 20–30 minutes, except the transformer block (40–45).

## Exercises

| | Priority | Time | File | When |
|--|----------|------|------|------|
| **A** Pre-norm transformer block. No `nn.MultiheadAttention`, no `F.scaled_dot_product_attention`. | Very high | 40–45 min | [`coding/A_transformer_block.py`](coding/A_transformer_block.py) | **Drafted Tue 20.** |
| **B** Train step and eval loop | Very high | 25–30 min | [`coding/B_train_eval.py`](coding/B_train_eval.py) | **Drafted Tue 20.** |
| **C** Masked CE, two ways. Start from the broken file. | High | 20–25 min | [`coding/C_masked_ce_broken.py`](coding/C_masked_ce_broken.py) | **Drafted Thu 22.** Both reductions. |
| **D** Attend across variates, not time. Then cross-group. Multi-head only if time remains, cap 30 min. | High | 25–30 min | [`coding/17_group_attention.py`](coding/17_group_attention.py), then [`coding/17b_cross_group.py`](coding/17b_cross_group.py). Do not open the solution files. | **17 drafted Wed 21.** 17b not started. |
| **E** InfoNCE. K-means only if E is done and mocks are not at risk. | Medium-high | 25–30 min | [`coding/E_infonce.py`](coding/E_infonce.py) | **Drafted Tue 20.** |
| **14** Sliding-window time series. Not on the original menu. | Extra | — | [`coding/14_sliding_window.py`](coding/14_sliding_window.py) | **Drafted Wed 21.** |
| **F** Mini causal LM | Optional | 30–40 min | [`coding/F_minigpt.py`](coding/F_minigpt.py) | **Drafted Wed 21.** |
| **G** LayerNorm by hand | Extra | 25 min | [`coding/G_layernorm.py`](coding/G_layernorm.py) | **Drafted Wed 21.** |
| **H** K-means | Extra | 25 min | [`coding/H_kmeans.py`](coding/H_kmeans.py) | **Drafted Wed 21.** |
| **I** Mean-pool classifier | Extra | 20 min | [`coding/I_mean_pool.py`](coding/I_mean_pool.py) | **Drafted Wed 21,** after F. |

A–E, 14, and F–I are drafted. 17b and 17c are not. Still open: the two unseen coding mocks.

## Days

### Tuesday 20 — modules (~2.5–3 h)

| | |
|--|--|
| 45 min | **A.** Transformer block. **Drafted.** |
| 30 min | **B.** Train and eval. **Drafted.** |
| 25 min | **C.** Broken masked CE, then the second approach. Slipped to **Thu 22.** |
| 20 min | Debugging sprint. One broken snippet at a time, from the session. Name the bug before editing. |
| 30 min | Resume. Stories A and B, the questions in the [screen note](2026-10-17_huzefa-screen.md). |

Not today: another standalone attention drill, problem 16, broadcast C, shape drills, exercise D.

### Wednesday 21 — broader coding (~2.5–3 h)

| | |
|--|--|
| 30 min | **D.** Variate attention. **Drafted.** Cross-group (17b) not started. |
| — | **E.** InfoNCE. **Drafted Tue 20.** |
| 25 min | **G.** LayerNorm by hand. **Drafted.** [`coding/G_layernorm.py`](coding/G_layernorm.py). |
| 25 min | **H.** K-means. **Drafted.** [`coding/H_kmeans.py`](coding/H_kmeans.py). The transformer-block change is set aside. |
| — | **14.** Sliding-window dataset. **Drafted.** [`coding/14_sliding_window.py`](coding/14_sliding_window.py). |
| 30–40 min | **F.** Mini causal LM. **Drafted.** [`coding/F_minigpt.py`](coding/F_minigpt.py). |
| 20 min | **I.** Mean-pool classifier. **Drafted** after F. [`coding/I_mean_pool.py`](coding/I_mean_pool.py). |
| 30–40 min | Resume / breadth. Questions already listed in the screen note. |

### Thursday 22 — mocks (~2.5–3 h)

| | |
|--|--|
| — | **C** is already drafted. Do not repeat it as the day’s new problem. |
| 50 min | Mock 1. 20 min resume. 30 min an unseen coding problem. Not an exact repeat. Run tests. Log in [`mocks.md`](mocks.md). |
| 30 min | Repair only the weakest miss: syntax, shape, mask, API, or time. |
| 30 min | Mock 2, coding only, a different category from mock 1. |
| 20–30 min | Review mistakes from the week. No new topic. |

### Friday 23 — 20 minutes, around 20:30

| | |
|--|--|
| 5 min | Transformer block structure, from memory. |
| 5 min | Train step and cross-entropy. |
| 5 min | One attention shape and one mask broadcast. |
| 5 min | Resume anchors: ImagenTime kill test, dual-tower controls, TR slice gate. |

## After each exercise

Score 1–5: problem understanding, shapes, PyTorch fluency, correctness, debugging, communication. Note time, hints, failed tests, and the main error.

| Time | What happens |
|------|----------------|
| Under 15 min | One harder follow-up. Do not repeat the problem. |
| 15–25 min | Target. One follow-up. |
| 25–35 min | Review the miss. One shorter related drill. |
| Over 35 min | Stop. Name the gap (concept, syntax, shape, debugging, or time). Explain only the missing piece. A simpler related problem, then the original later. |

## How a drill is run

Problem statement only. You state shapes. You code. You write 2–3 tests. Run them. On a failure, you diagnose before a hint. Then one follow-up. No second attention drill when the category was already attention.
