"""N. Supervised contrastive loss — PROBLEM. Optional.

No solution file. Only after both unseen mocks. Skip if the day is short.

    embeddings: [N, D]
    labels:     [N] long
    return a scalar

Samples with the same label are positives. Different labels are negatives.

1. L2-normalize each row.
2. Pairwise similarity [N, N]. Entry (i, j) is the dot product of row i
   and row j.
3. Divide by temperature.
4. A row is not a positive for itself, and it is not in its own
   denominator.
5. Positive mask: same label, and not the diagonal.
6. For an anchor that has at least one positive, average the
   log-softmax of its positive columns. Then mean over those anchors.
   The loss applies the softmax. Do not softmax the matrix first.
7. An anchor with no positive is left out of the mean. If every anchor
   has no positive, return a 0-dimensional zero on the embeddings'
   device.

Tests to write before you trust it:
- similarity is [N, N], and the diagonal was excluded
- the positive mask matches the labels
- the loss is finite
- gradients reach the embeddings

Time box: 20–25 minutes. One follow-up after it runs.
"""

import torch


def supervised_contrastive(embeddings, labels, temperature=0.1):
    raise NotImplementedError
