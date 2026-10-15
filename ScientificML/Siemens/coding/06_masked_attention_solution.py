"""06. Masked attention — SOLUTION.

Key mask [B, Tk] lines up with scores [B, Tq, Tk] as [B, 1, Tk].
Causal: tril, so key j is allowed when j <= query i.
masked_fill uses -inf. softmax of an all -inf row is NaN; nan_to_num
makes that row contribute nothing, which is the right empty-key behavior.
""",

import math
import torch


def masked_attention(q, k, v, key_padding_mask=None, causal=False):
    d = q.shape[-1]
    scores = q @ k.transpose(-2, -1) / math.sqrt(d)
    if key_padding_mask is not None:
        scores = scores.masked_fill(~key_padding_mask[:, None, :], float("-inf"))
    if causal:
        tq, tk = scores.shape[-2:]
        allowed = torch.arange(tk, device=scores.device) <= torch.arange(tq, device=scores.device).unsqueeze(1)
        scores = scores.masked_fill(~allowed, float("-inf"))
    weights = torch.softmax(scores, dim=-1)
    weights = torch.nan_to_num(weights, nan=0.0)
    return weights @ v


if __name__ == "__main__":
    q = torch.zeros(1, 2, 1)
    k = torch.zeros(1, 2, 1)
    v = torch.tensor([[[1.0], [100.0]]])
    mask = torch.tensor([[True, False]])
    out = masked_attention(q, k, v, key_padding_mask=mask)
    assert torch.allclose(out, torch.tensor([[[1.0], [1.0]]]))
    causal = masked_attention(q, k, v, causal=True)
    # query 0 sees only key 0 -> 1. query 1 sees both keys, equal -> 50.5
    assert torch.allclose(causal[0, 0], torch.tensor([1.0]))
    assert torch.allclose(causal[0, 1], torch.tensor([50.5]))
    both = masked_attention(q, k, v, key_padding_mask=mask, causal=True)
    assert torch.allclose(both, torch.tensor([[[1.0], [1.0]]]))
    dead = torch.tensor([[False, False]])
    assert torch.allclose(masked_attention(q, k, v, key_padding_mask=dead), torch.zeros(1, 2, 1))
    print("06_masked_attention_solution: ok")
