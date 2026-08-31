# Apple Health — high-ROI coding practice

Six primitives for **multimodal architecture & time-series encoding**, plus one classical GBDT baseline. Not LeetCode. Not the tech-screen shape worksheets in [`../code/`](../code/).

CoderPad on invites is a template (same as HM / Feng). Treat these as a **pad contingency** and as spoken-to-code for slot (2). Do not replace Yujie / Chung-Cheng / Vincent mocks with this set.

## How to practice

Open the **problem** file only. Do not peek at `*_solution.py` until you have a running attempt.

For each problem:

1. State assumptions, I/O, and edge cases **before** coding.
2. Give a simple solution, then improve complexity if needed.
3. Run the file (`python3 01_align_nearest.py`).
4. State time / memory.
5. Connect the code to the modeling decision (one sentence).

Two habits:

- Do not start coding immediately.
- The implementation is easy. The interview is the representation choice.

## Order (~3 h)

| # | Problem | Min | Files |
|---|---------|-----|-------|
| 1 | Multirate timestamp alignment | 30 | [`01_align_nearest.py`](01_align_nearest.py) · [`01_align_nearest_solution.py`](01_align_nearest_solution.py) |
| 2 | Patchify a multivariate series | 20 | [`02_patchify.py`](02_patchify.py) · [`02_patchify_solution.py`](02_patchify_solution.py) |
| 3 | Masked cross-attention | 35 | [`03_cross_attention.py`](03_cross_attention.py) · [`03_cross_attention_solution.py`](03_cross_attention_solution.py) |
| 4 | Trie for event / token sequences | 25 | [`04_trie.py`](04_trie.py) · [`04_trie_solution.py`](04_trie_solution.py) |
| 5 | Sliding mean + variance | 25 | [`05_sliding_stats.py`](05_sliding_stats.py) · [`05_sliding_stats_solution.py`](05_sliding_stats_solution.py) |
| 6 | XGBoost on engineered temporal features | 30–40 | [`06_xgboost_features.py`](06_xgboost_features.py) · [`06_xgboost_features_solution.py`](06_xgboost_features_solution.py) |

Problems 1, 2 (plain), 4, 5: stdlib. 2 (torch) / 3: PyTorch. 6: NumPy; XGBoost optional for the fit smoke test.

## Modeling one-liners (say these after the code)

| Problem | The actual question |
|---------|---------------------|
| Alignment | Nearest timestamps is the coding problem. Whether **hard temporal alignment** is appropriate at all is the modeling issue. Prefer native-rate encode → compress → time-aware fusion. |
| Patchify | Patch size sets **temporal resolution and token budget**, not just a slice length. |
| Cross-attention | Fusion cost is \(O(T_q T_k D)\), not \((T_q+T_k)^2\). Mask is a **validity** mask, not a causal mask. |
| Trie | Prefix structure on event sequences is an empirical next-event model, not a learned dynamics model. |
| Sliding stats | Online moments are the primitive behind many wearable features; watch **numerical cancellation**. |
| XGBoost | Require the deep model to **beat this baseline** on the same split. Feature design is the scientific choice. |
