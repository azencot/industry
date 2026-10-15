"""02. Pad variable-length sequences — PROBLEM.

Do not open 02_pad_sequences_solution.py until this file runs.

seqs: list of [Ti, D] float tensors.
Return [B, Tmax, D].

left=False: content on the left, pad on the right.
left=True: pad on the left, content on the right.
pad_value fills the empty slots.

Tests to write: shape, pad value, batch of 1, equal lengths, one left-pad case.
""",
import torch

def pad_sequences(seqs, pad_value=0.0, left=False):
    if len(seqs) == 0:
        return []

    # find Tmax
    Tmax = -1
    for seq in seqs:
        Tmax = max(Tmax, seq.shape[0])

    padded = torch.ones(len(seqs), Tmax, seqs[0].shape[-1]) * pad_value

    for i, seq in enumerate(seqs):
        if left:
            padded[i][-seq.shape[0]:] = seq 
        else:
            padded[i][:seq.shape[0]] = seq 
            
    return padded
