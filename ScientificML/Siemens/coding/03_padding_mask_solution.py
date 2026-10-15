"""03. Padding mask — SOLUTION.

t < length is the valid position. unsqueeze so [T] compares to [B, 1].
For scores [B, H, Tq, Tk], a key mask [B, Tk] needs two extra axes: [B, 1, 1, Tk].
""",

import torch


def lengths_to_mask(lengths, tmax=None, valid_true=True):
    if tmax is None:
        tmax = int(lengths.max())
    t = torch.arange(tmax, device=lengths.device)
    valid = t.unsqueeze(0) < lengths.unsqueeze(1)
    return valid if valid_true else ~valid


def attention_key_mask(mask):
    return mask[:, None, None, :]


if __name__ == "__main__":
    lengths = torch.tensor([2, 1, 3])
    mask = lengths_to_mask(lengths)
    assert mask.shape == (3, 3)
    assert torch.equal(mask[0], torch.tensor([True, True, False]))
    assert torch.equal(mask[1], torch.tensor([True, False, False]))
    assert lengths_to_mask(lengths, valid_true=False)[0, 2]
    assert lengths_to_mask(torch.tensor([4]), tmax=4).shape == (1, 4)
    key = attention_key_mask(mask)
    assert key.shape == (3, 1, 1, 3)
    scores = torch.zeros(3, 2, 5, 3)
    assert (scores + key).shape == scores.shape
    print("03_padding_mask_solution: ok")
