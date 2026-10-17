"""Tuesday mask / broadcasting micro-drills — SOLUTION."""

import torch


def mask_attn_keys(scores, key_mask):
    return scores.masked_fill(~key_mask[:, None, None, :], float("-inf"))


def masked_mean_time(x, mask):
    m = mask.to(dtype=x.dtype).unsqueeze(-1)
    return (x * m).sum(dim=1) / m.sum(dim=1).clamp_min(1.0)


def mask_group_keys(scores, key_mask):
    return scores.masked_fill(~key_mask[:, None, None, :], float("-inf"))


def mask_causal_and_padding(scores, padding_mask):
    t = scores.shape[-1]
    causal = torch.arange(t, device=scores.device) <= torch.arange(t, device=scores.device).unsqueeze(1)
    allowed = causal[None, None, :, :] & padding_mask[:, None, None, :]
    return scores.masked_fill(~allowed, float("-inf"))


if __name__ == "__main__":
    scores = torch.zeros(2, 3, 4, 5)
    key = torch.tensor([[True, False, True, False, True], [True, True, True, True, False]])
    out = mask_attn_keys(scores, key)
    assert out.shape == scores.shape
    assert torch.isneginf(out[0, 0, 0, 1]) and not torch.isneginf(out[0, 0, 0, 0])

    x = torch.tensor([[[1.0, 1.0], [3.0, 3.0], [100.0, 100.0]]])
    m = torch.tensor([[True, True, False]])
    assert torch.allclose(masked_mean_time(x, m), torch.tensor([[2.0, 2.0]]))

    gs = torch.zeros(2, 3, 4, 5)
    gout = mask_group_keys(gs, key)
    assert torch.isneginf(gout[0, 0, 0, 1]) and gout.shape == gs.shape

    s = torch.zeros(1, 1, 3, 3)
    pad = torch.tensor([[True, False, True]])
    blocked = mask_causal_and_padding(s, pad)
    assert torch.isneginf(blocked[0, 0, 0, 1]) and torch.isneginf(blocked[0, 0, 0, 2])
    assert not torch.isneginf(blocked[0, 0, 2, 0]) and torch.isneginf(blocked[0, 0, 2, 1])
    assert not torch.isneginf(blocked[0, 0, 2, 2])
    print("tue_broadcast_solution: ok")
