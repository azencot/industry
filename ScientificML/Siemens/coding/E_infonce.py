"""E. InfoNCE — PROBLEM.

No solution file. Wednesday, after variate attention.

    z1: [B, D]
    z2: [B, D]
    z1[i] matches z2[i]
    return a scalar loss

1. L2-normalize each embedding.
2. Pairwise similarity [B, B]. Entry (i, j) compares z1[i] with z2[j].
3. Divide by a temperature. Those scaled similarities are the logits.
4. Positive for row i is column i.
   Row i is "which z2 vector matches z1[i]?" The B columns are the B
   candidate classes. The correct class for row i is j = i, the diagonal.
   The label vector is therefore length B, and label[i] = i
   (0 for row 0, 1 for row 1, and so on). Off-diagonal entries are the
   negatives for that row.
5. Cross-entropy.
   One cross-entropy over the B columns of each row, then the mean over
   the B rows. The logits argument is the [B, B] scaled-similarity
   matrix. The target argument is the label vector from step 4, integer
   class indices, not a one-hot matrix and not probabilities.
   Cross-entropy applies the softmax itself. Do not softmax the matrix
   before passing it in.

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
