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

def lengths_to_mask(lengths, tmax=None, valid_true=True):
    raise NotImplementedError


def attention_key_mask(mask):
    raise NotImplementedError
