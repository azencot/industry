"""Tuesday blank-file attention — SOLUTION."""

import math
import torch


def scaled_dot_product_attention(q, k, v, key_padding_mask=None, causal=False):
    dh = q.shape[-1]
    scores = q @ k.transpose(-2, -1) / math.sqrt(dh)
    if key_padding_mask is not None:
        scores = scores.masked_fill(~key_padding_mask[:, None, None, :], float("-inf"))
    if causal:
        tq, tk = scores.shape[-2:]
        allowed = torch.arange(tk, device=scores.device) <= torch.arange(tq, device=scores.device).unsqueeze(1)
        scores = scores.masked_fill(~allowed, float("-inf"))
    weights = torch.nan_to_num(torch.softmax(scores, dim=-1), nan=0.0)
    return weights @ v


if __name__ == "__main__":
    q = torch.zeros(1, 2, 2, 1)
    k = torch.zeros(1, 2, 2, 1)
    v = torch.tensor([[[[1.0], [100.0]]]]).expand(1, 2, 2, 1).contiguous()
    mask = torch.tensor([[True, False]])
    out = scaled_dot_product_attention(q, k, v, key_padding_mask=mask)
    assert out.shape == (1, 2, 2, 1)
    assert torch.allclose(out, torch.ones_like(out))
    causal = scaled_dot_product_attention(q, k, v, causal=True)
    assert torch.allclose(causal[0, 0, 0], torch.tensor([1.0]))
    assert torch.allclose(causal[0, 0, 1], torch.tensor([50.5]))
    dead = torch.tensor([[False, False]])
    assert torch.allclose(
        scaled_dot_product_attention(q, k, v, key_padding_mask=dead),
        torch.zeros(1, 2, 2, 1),
    )
    print("tue_attention_solution: ok")
