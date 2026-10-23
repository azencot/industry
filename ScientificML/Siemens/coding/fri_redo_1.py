"""Friday redo 1. Masked attention. 20 minutes.

Do not open 05_attention.py, 06_masked_attention.py, or their solutions.

    q:    [B, Tq, D]
    k:    [B, Tk, D]
    v:    [B, Tk, Dv]
    mask: [B, Tk]  True = valid key, False = pad
    return [B, Tq, Dv]

Scale the scores by sqrt(D). An invalid key must receive no probability.
A row whose keys are all invalid returns zeros, not NaNs.
No loop over the batch.

Write 2–3 tests before you trust it:
- shape [B, Tq, Dv], including a batch of 1
- editing an invalid key does not change the output
- gradients reach q, k, and v
"""

import torch
import math

def masked_attention(q, k, v, mask):
    
    # scaled dot product
    d = q.shape[-1]
    qkt = q @ k.transpose(-2, -1) / math.sqrt(d)                # [B, Tq, D] @ [B, D, Tk] -> [B, Tq, Tk]

    # mask broadcast
    scores = qkt.masked_fill(~mask[:, None, :], float("-inf"))  # [B, Tk] -> [B, 1, Tk] -> [B, Tq, Tk]

    # softmax
    a = torch.softmax(scores, dim=-1)                       # [B, Tq, Tk] -> [B, Tq, Tk]
    
    # nan to num after softmax
    a = torch.nan_to_num(a, nan=0.0)

    # scale v by a
    return a @ v                                            # [B, Tq, Tk] @ [B, Tk, Dv] -> [B, Tq, Dv] 