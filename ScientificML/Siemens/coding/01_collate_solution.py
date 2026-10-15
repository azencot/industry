"""01. Variable-length collate — SOLUTION.

pad_sequence stacks on dim 0 when batch_first=True and fills the tail with 0.
Mask: position t is valid when t < length. Broadcast [1, T] < [B, 1].
""",

import torch
from torch.nn.utils.rnn import pad_sequence


def collate_sequences(batch):
    lengths = torch.tensor([x.shape[0] for x in batch], dtype=torch.long)
    padded = pad_sequence(batch, batch_first=True, padding_value=0.0)
    tmax = padded.shape[1]
    t = torch.arange(tmax)
    mask = t.unsqueeze(0) < lengths.unsqueeze(1)
    return padded, lengths, mask


if __name__ == "__main__":
    a = torch.tensor([[1.0, 10.0], [2.0, 20.0]])
    b = torch.tensor([[3.0, 30.0]])
    padded, lengths, mask = collate_sequences([a, b])
    assert padded.shape == (2, 2, 2)
    assert torch.equal(lengths, torch.tensor([2, 1]))
    assert torch.equal(mask, torch.tensor([[True, True], [True, False]]))
    assert padded[1, 1].abs().sum() == 0
    one, one_len, one_mask = collate_sequences([a])
    assert one.shape == (1, 2, 2) and one_mask.all()
    same, _, same_mask = collate_sequences([a, a])
    assert same_mask.all()
    print("01_collate_solution: ok")
