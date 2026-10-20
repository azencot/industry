"""F. Mini causal LM — OPTIONAL.

No solution file. Open this only after A–E are clean and a mock is not
about to be skipped.

    token_ids: [B, T] long
    return logits [B, T, V]

token embedding + position embedding + one TransformerBlock (exercise A)
+ final LayerNorm + linear head to V.

Next-token loss uses logits[:, :-1] and targets[:, 1:].
Causal mask inside the block.

Do not implement generation, a KV cache, or a pretrained weight load.

Time box: 40 minutes, then stop.
"""

import torch.nn as nn


class MiniGPT(nn.Module):
    def __init__(self, vocab, d, n_heads, max_len):
        super().__init__()
        raise NotImplementedError

    def forward(self, token_ids):
        raise NotImplementedError


def next_token_loss(logits, token_ids):
    raise NotImplementedError
