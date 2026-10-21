"""H. K-means — PROBLEM.

No solution file. No attention, no mask.

    x: [N, D]
    k: number of clusters
    n_iters: how many assign-and-update steps
    return centroids [k, D], assignments [N] long

Initialize each centroid to a row of x: centroid j starts as x[j].
Do not draw them at random. Tests need a fixed start.

One iteration:
1. Assign every point to the nearest centroid.
   Distance is squared Euclidean. No Python loop over the N points.
2. Replace each centroid by the mean of the points assigned to it.
   A cluster with no points keeps its previous centroid.
   Do not divide by zero.

The returned assignments are computed from the returned centroids.
Values are in 0 .. k-1.

Tests:
- shapes [k, D] and [N]
- on two distant blobs, with the first k rows in different blobs,
  every point is assigned to its own blob
- an empty cluster stays finite and equal to the centroid it had
  before the update
- one iteration changes at least one centroid when the init is not
  already the means

Time box: 25 minutes.
"""

import torch

def assign(x, c):
  # assign pts to centroids
  xe, ce = x[:, None, :], c[None, :, :]       # [N, D] -> [N, 1, D]; [k, D] -> [1, k, D]
  dist = torch.sum((xe - ce) ** 2, dim=-1)    # [N, 1, D] [1, k, D] -> [N, k]             # NOTE: no need for sqrt since monotonic
  labels = torch.argmin(dist, dim=-1)         # [N, k] -> [N]

  return labels

def kmeans(x, k, n_iters=5):
    # init k centroids
    c = x[:k].clone() # [k, D]

    for it in range(n_iters):
      labels = assign(x, c)

      # update centroids
      for j in range(k):
        nj = torch.sum(labels == j)
        if nj > 0:
          c[j] = torch.sum(x[labels == j, :], dim=0) / nj

    return c, assign(x, c)

