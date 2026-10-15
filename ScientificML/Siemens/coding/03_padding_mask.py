"""03. Padding mask — PROBLEM.

Do not open 03_padding_mask_solution.py until this file runs.

lengths: long tensor [B], each entry is the valid length Ti.

lengths_to_mask -> bool [B, T].
    valid_true=True:  True means a real token (default in this folder).
    valid_true=False: True means padding. Be able to flip.

attention_key_mask(mask) takes [B, T] and returns a mask broadcastable to
multi-head scores [B, H, Tq, Tk], i.e. shape [B, 1, 1, T].

Build the [B, T] mask with torch.arange and broadcasting. No row loop.
""",
import torch

def lengths_to_mask(lengths, tmax=None, valid_true=True):
    if tmax is None:
        tmax = int(lengths.max())

    grid = torch.arange(tmax)[None, :]  # [1, tmax]
    row_lengths = lengths[:, None]      # [B, 1]
    mask = grid < row_lengths

    if valid_true == False:
        mask = ~mask

    return mask


def attention_key_mask(mask):
    return mask[:, None, None, :]
