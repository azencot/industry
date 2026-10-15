"""02. Pad variable-length sequences — SOLUTION.

Right pad is pad_sequence. Left pad rolls each row by (Tmax - Ti) so the
zeros move to the front. A Python loop over the batch is fine here; the
feature axis stays a tensor.
""",

import torch
from torch.nn.utils.rnn import pad_sequence


def pad_sequences(seqs, pad_value=0.0, left=False):
    padded = pad_sequence(seqs, batch_first=True, padding_value=pad_value)
    if not left:
        return padded
    lengths = [x.shape[0] for x in seqs]
    tmax = padded.shape[1]
    out = padded.clone()
    for i, length in enumerate(lengths):
        shift = tmax - length
        if shift:
            out[i] = torch.roll(padded[i], shifts=shift, dims=0)
    return out


if __name__ == "__main__":
    a = torch.tensor([[1.0], [2.0]])
    b = torch.tensor([[3.0]])
    right = pad_sequences([a, b], pad_value=-1.0)
    assert torch.equal(right, torch.tensor([[[1.0], [2.0]], [[3.0], [-1.0]]]))
    left = pad_sequences([a, b], pad_value=-1.0, left=True)
    assert torch.equal(left, torch.tensor([[[1.0], [2.0]], [[-1.0], [3.0]]]))
    assert pad_sequences([a]).shape == (1, 2, 1)
    eq = pad_sequences([a, a])
    assert eq.shape == (2, 2, 1) and torch.equal(eq[0], a)
    print("02_pad_sequences_solution: ok")
