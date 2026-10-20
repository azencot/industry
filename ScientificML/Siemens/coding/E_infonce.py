"""E. InfoNCE — PROBLEM.

No solution file. Wednesday, after variate attention.

    z1: [B, D]
    z2: [B, D]
    z1[i] matches z2[i]
    return a scalar loss

1. L2-normalize each embedding.
2. Pairwise similarity [B, B].
3. Divide by a temperature.
4. Positive for row i is column i.
5. Cross-entropy.

Optional: add the loss with z1 and z2 swapped, and average the two.

Tests:
- similarity is [B, B]
- a batch of matched orthogonal-ish pairs scores lower than the same
  batch with z2 rolled by one
- gradients reach z1 and z2
- a lower temperature makes the correct-class probability more peaked
  on a fixed similarity matrix (check the softmax, not a story)

Time box: 30 minutes. Do not also implement K-means today.
"""

import torch


def infonce(z1, z2, temperature=0.1):
    raise NotImplementedError
