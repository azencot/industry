"""07. Causal mask — SOLUTION.

tril is True on and below the diagonal: j <= i.
padding_mask [B, T] is a constraint on keys, so it occupies the last axis.
causal [T, T] & padding [B, 1, T] -> [B, T, T], then a head axis.
""",

import torch


def causal_mask(t, device=None):
    return torch.tril(torch.ones(t, t, device=device, dtype=torch.bool))


def combine_causal_and_padding(padding_mask):
    t = padding_mask.shape[-1]
    causal = causal_mask(t, device=padding_mask.device)
    allowed = causal.unsqueeze(0) & padding_mask.unsqueeze(1)
    return allowed.unsqueeze(1)


if __name__ == "__main__":
    c = causal_mask(3)
    assert torch.equal(c, torch.tensor([
        [True, False, False],
        [True, True, False],
        [True, True, True],
    ]))
    pad = torch.tensor([[True, True, False]])
    both = combine_causal_and_padding(pad)
    assert both.shape == (1, 1, 3, 3)
    assert not both[0, 0, 2, 2]
    assert both[0, 0, 1, 1]
    assert not both[0, 0, 0, 1]
    print("07_causal_mask_solution: ok")
