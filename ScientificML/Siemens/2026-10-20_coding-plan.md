# Siemens coding plan — 20–23 Oct 2026

Supersedes the attention-and-mask schedule in [`2026-10-17_huzefa-screen.md`](2026-10-17_huzefa-screen.md). Resume questions in that file still stand. This file is the coding schedule.

**Revised 22 Oct.** Thursday and Friday no longer start from another attention or mask drill. The open question is an unseen ML problem in about 25 minutes.

**Screen:** Fri 23 Oct, 22:00–23:00 Thailand. About 25–30 min resume / ML breadth, then 25–30 min live PyTorch with unit tests. DataLoader, padding, and an attention matrix are examples, not the whole menu.

No solution files for A–N. Do not look up an implementation before the attempt. [`coding/L_wont_learn.py`](coding/L_wont_learn.py) is the exception that runs: the bugs are not marked, and there is no solution file.

## Already practiced — do not repeat as standalone drills

Dataset, `collate_fn`, padding, padding masks, masked reductions, scaled dot-product attention, causal attention, multi-head attention, the pre-norm block, train and eval, masked cross-entropy (both reductions), attention across variates, InfoNCE, the sliding-window dataset, the mini causal LM, LayerNorm, K-means, the mean-pool classifier.

Cross-group attention (17b) and multi-head group attention (17c) are unfinished. They are not priorities.

Do not add another Transformer exercise, an algorithm puzzle, or an obscure API.

## Still open, in this order

| | Priority | Time | File |
|--|----------|------|------|
| Unseen mock 1, then mock 2 | Highest | 25–30 min each | Not written ahead. Given at the start of the mock. |
| **J** Gaussian NLL | Very high | 20–25 min | [`coding/J_gaussian_nll.py`](coding/J_gaussian_nll.py) |
| **K** Forecast with covariates | Very high | 25–30 min | [`coding/K_forecast_covariates.py`](coding/K_forecast_covariates.py) |
| **L** A model that does not learn | Very high | 25–30 min | [`coding/L_wont_learn.py`](coding/L_wont_learn.py) |
| **M** Variable-length GRU classifier | Medium | 20–25 min | [`coding/M_gru_classifier.py`](coding/M_gru_classifier.py) |
| **N** Supervised contrastive | Optional | 20–25 min | [`coding/N_supervised_contrastive.py`](coding/N_supervised_contrastive.py) |

If the day slips, cut **N** first, then **M**. Do not skip mock 1 in order to finish an optional exercise.

## Days already done

**Tuesday 20.** A (transformer block), B (train and eval), and E (InfoNCE) drafted. C slipped off that day and was drafted later. Do not repeat C as a new problem.

**Wednesday 21.** 17 (variate attention), G (LayerNorm), 14 (sliding window), H (K-means), F (mini causal LM), and I (mean-pool classifier) drafted. 17b set aside. Story C and story B mocks logged in [`mocks.md`](mocks.md).

## Thursday 22 — primary coding day

| | |
|--|--|
| 20–25 min | **J.** Gaussian NLL. Formula is in the file. You state the reduction, then code. |
| 25–30 min | **K.** Covariate forecast. You propose the architecture before any code. |
| 20–25 min | **M.** GRU classifier. Last valid state, not the state after the padding. |
| | Short break. |
| 25–30 min | **L.** Run the script. It does not learn. Diagnose, then fix, then re-run. |
| 25–30 min | **Mock 1.** Unseen. Not an exact repeat. Log in [`mocks.md`](mocks.md). |
| 15–20 min | Review the misses. No new topic. |
| If time remains | **Mock 2**, a different category from mock 1. |

**N** only after both mocks.

### How a mock is given

The category is not announced ahead of time. At least one of the two mocks is outside attention, masking, and Transformers. The prompt is a signature, the input and output contract, and the imports. You explain the shapes and the computation, then implement, then write 2–3 tests. On a failure, you diagnose before a hint. One follow-up if time remains.

Score 1–5: problem understanding, shapes, PyTorch fluency, correctness, debugging, communication. Record time, hints, failed tests, the main mistake, and whether it was finished without a hint.

Do not use [`coding/19_thu_mock.py`](coding/19_thu_mock.py). Leave it closed.

## Friday 23

Light. If mock 2 did not happen on Thursday, do it earlier in the day, then 15 min on the misses. Do not run a hard mock in the hour before the call.

### Last 20 minutes before 22:00

No new exercise.

| | |
|--|--|
| 5 min | Transformer block structure, from memory. |
| 5 min | Train step and cross-entropy. |
| 5 min | One attention shape and one mask broadcast. |
| 5 min | Resume anchors: ImagenTime kill test, dual-tower controls, TR slice gate. |

Call at 22:00.

## After each exercise

| Time | What happens |
|------|----------------|
| Under 15 min | One harder follow-up. |
| 15–25 min | On pace. One follow-up, then the next category. |
| 25–35 min | Review that miss. One short repair. |
| Over 35 min | Stop. Name the gap. Explain only the missing piece. Move on. |

One follow-up, and it changes the problem that was just solved: missing values, variable length, the reduction, an extra output, stability, or what is known at inference. Not a second problem from the same family.

Before coding, state the operation and the shapes. After it runs, say why it is correct, the cost, and the limitation.

## What this is for

An unfamiliar ML component in about 25 minutes. Shapes said out loud. A small `nn.Module`. A standard loss. A correct training step. Masks and broadcasting. A model that does not learn. A few tests. The assumption and the limitation.

Not a larger set of memorized implementations.
