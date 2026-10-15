"""12. Batched pairwise similarity — SOLUTION.

Dot is one matmul against Y transposed on the last two axes.
Cosine is that dot after each row has length 1.
Euclidean expands to [B, N, 1, D] and [B, 1, M, D], then the norm on D.
""",

import torch


def pairwise_dot(x, y):
    return x @ y.transpose(-2, -1)


def pairwise_cosine(x, y, eps=1e-8):
    x_n = x / x.norm(dim=-1, keepdim=True).clamp_min(eps)
    y_n = y / y.norm(dim=-1, keepdim=True).clamp_min(eps)
    return pairwise_dot(x_n, y_n)


def pairwise_euclidean(x, y):
    diff = x.unsqueeze(2) - y.unsqueeze(1)
    return torch.linalg.vector_norm(diff, dim=-1)


if __name__ == "__main__":
    x = torch.tensor([[[1.0, 0.0], [0.0, 1.0]]])
    y = torch.tensor([[[1.0, 0.0], [1.0, 1.0]]])
    dot = pairwise_dot(x, y)
    assert dot.shape == (1, 2, 2)
    assert torch.allclose(dot[0, 0], torch.tensor([1.0, 1.0]))
    cos = pairwise_cosine(x, y)
    assert torch.allclose(cos[0, 0, 0], torch.tensor(1.0))
    dist = pairwise_euclidean(x, y)
    assert torch.allclose(dist[0, 0, 0], torch.tensor(0.0))
    assert torch.allclose(dist[0, 0, 1], torch.tensor(1.0))
    print("12_pairwise_solution: ok")
