"""F. Mini causal LM — PROBLEM.

No solution file.

    token_ids: [B, T] long, each entry an id in 0 .. V-1
    return logits [B, T, V]
    V is vocab. T must be <= max_len.

The forward is four stages, in this order. Shapes after each stage
are [B, T, D] until the head.

1. Token embedding. One vector of size D per id.
2. Position embedding. Positions are 0, 1, ..., T-1 for every row.
   Look those up in a table of max_len vectors of size D, and add
   them to the token vectors. Add, do not concatenate.
   The position index has to be on the same device as token_ids.
3. One pre-norm block, the TransformerBlock from exercise A, with
   the causal flag on. Position i may use tokens at positions <= i.
   It may not use a later token. Do not write a second attention
   implementation in this file.
4. A final LayerNorm over D, then a linear map from D to V.
   Those are the logits. Do not softmax them here.

next_token_loss(logits, token_ids) is a scalar.

The token at position t is predicted from positions 0 .. t-1, so the
pair is (logits at t, token id at t+1). Drop the last logit position,
because it has no following token. Drop the first target position,
because nothing was asked to predict it. After that drop:
    logits used:  [B, T-1, V]
    targets used: [B, T-1] long
Cross-entropy wants a class axis of size V and integer class ids.
Flatten the batch and time of those two tensors yourself.
Pass the raw logits. The loss applies the softmax.
If T < 2 there is no pair. Return a zero scalar on the same device
as the logits.

Do not implement generation, a KV cache, or a weight load.

Tests to write before you trust it:
- logits are [B, T, V], including batch size 1
- T = max_len runs; a longer sequence is rejected by you, not by a crash inside the embedding
- changing a token at position j does not change logits at position i < j
- gradients reach the token embedding, the position embedding, and the output linear
- the loss on a batch where the next token is easy is lower than the loss on a shuffled target
- the loss does not change if you edit only the logit at the final position

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
