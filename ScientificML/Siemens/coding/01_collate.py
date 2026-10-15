"""01. Variable-length collate — PROBLEM.

Do not open 01_collate_solution.py until this file runs.

A batch is a list of float tensors, each [Ti, D]. Lengths differ. D matches.

Return:
    padded   [B, Tmax, D]
    lengths  [B] long
    mask     [B, Tmax] bool, True = real token, False = pad

Say before coding: right pad, pad value 0, mask from lengths with arange
(no per-timestep Python loop for the mask).

DataLoader calls this as collate_fn, once per batch, after __getitem__.
"""

import torch

def collate_sequences(batch):
    
    # find Tmax, and create lengths (need a loop)
    lengths = [item.shape[0] for item in batch]
    Tmax = max(lengths)

    # pad zeros (if it is acceptable is a padding value) to the right; (need another loop)
    padded = torch.zeros(len(batch), Tmax, batch[0].shape[-1])
    for i, item in enumerate(batch):
        padded[i][:lengths[i]] = item 
    # can replace with padded = torch.nn.utils.rnn.pad_sequence(batch, batch_first=True)

    # create mask without a loop (not sure how to do this)
    grid = torch.arange(Tmax)[None, :]
    row_lengths = torch.tensor(lengths)[:, None]
    mask = grid < row_lengths       # uses broadcasting bahhh

    return padded, row_lengths.squeeze(), mask

if __name__ == "__main__":
    import torch
    a = torch.tensor([[1.0, 10.0], [2.0, 20.0]])
    b = torch.tensor([[3.0, 30.0]])
    padded, lengths, mask = collate_sequences([a, b])
    print(padded.shape, lengths, mask)
