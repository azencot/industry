"""12. Batched pairwise similarity — PROBLEM.

Do not open 12_pairwise_solution.py until this file runs.

X [B, N, D]
Y [B, M, D]

Return [B, N, M] with no Python loop over N or M.

pairwise_dot: dot product.
pairwise_cosine: normalize each vector on D, then dot. Guard norm 0.
pairwise_euclidean: L2 distance between every pair.
""",

def pairwise_dot(x, y):
    raise NotImplementedError


def pairwise_cosine(x, y, eps=1e-8):
    raise NotImplementedError


def pairwise_euclidean(x, y):
    raise NotImplementedError
