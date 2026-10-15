"""05. Scaled dot-product attention — SOLUTION.

scores [B, Tq, Tk] = (Q @ K^T) / sqrt(D)
weights = softmax over Tk
out [B, Tq, Dv] = weights @ V

sqrt(D): if each product Q_i·K_j has variance about D, softmax saturates.
""",

import math
import torch


def scaled_dot_product_attention(q, k, v):
    d = q.shape[-1]
    scores = q @ k.transpose(-2, -1) / math.sqrt(d)
    weights = torch.softmax(scores, dim=-1)
    return weights @ v


if __name__ == "__main__":
    torch.manual_seed(0)
    q = torch.randn(2, 3, 4)
    k = torch.randn(2, 5, 4)
    v = torch.randn(2, 5, 7)
    out = scaled_dot_product_attention(q, k, v)
    assert out.shape == (2, 3, 7)
    # Identical keys and a one-hot value: uniform attention -> mean of V rows.
    q = torch.zeros(1, 1, 2)
    k = torch.zeros(1, 2, 2)
    v = torch.tensor([[[0.0], [4.0]]])
    out = scaled_dot_product_attention(q, k, v)
    assert torch.allclose(out, torch.tensor([[[2.0]]]))
    print("05_attention_solution: ok")
