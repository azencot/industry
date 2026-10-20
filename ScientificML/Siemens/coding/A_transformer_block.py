"""A. Pre-norm transformer block — PROBLEM.

No solution file. Do not look up nn.MultiheadAttention or
F.scaled_dot_product_attention. Implement the attention yourself.

    x: [B, T, D]
    return [B, T, D]

    x = x + MultiHeadAttention(LayerNorm(x))
    x = x + MLP(LayerNorm(x))

Multi-head self-attention:
    nn.Linear for Q, K, V
    reshape / transpose to heads
    scores = Q K^T / sqrt(Dh), softmax, times V
    output projection
MLP:
    Linear(D, 4D), GELU, Linear(4D, D)
Optional causal mask: query i cannot attend to key j > i.
D must be divisible by n_heads. Say what you do if it is not.

Write these tests before you trust it:
- output shape equals input shape
- batch size 1
- more than one head
- gradients reach Q, K, V, both MLP linears, and both LayerNorms
- with a causal mask, a future token does not change an earlier output

Time box: 45 minutes. Follow-ups are asked after it runs, not before.
"""

import torch
import torch.nn as nn
import math


class TransformerBlock(nn.Module):
    def __init__(self, d, n_heads, causal=False):
        super().__init__()
        
        assert d % n_heads == 0

        self.d = d
        self.n_heads = n_heads
        self.dh = d // n_heads

        self.ln1 = nn.LayerNorm(d)
        self.wQ = nn.Linear(d, d)
        self.wK = nn.Linear(d, d)
        self.wV = nn.Linear(d, d)
        self.wO = nn.Linear(d, d)

        self.causal = causal
        
        self.ln2 = nn.LayerNorm(d)
        self.gelu = nn.GELU()

        self.wEL = nn.Linear(d, 4*d)
        self.wCL = nn.Linear(4*d, d)

        self.device = next(self.parameters()).device

    def MultiHeadAttention(self, x):
        # x in [B, T, D]
        B, T, D = x.shape

        # extract Q, K, V
        Q = self.wQ(x)                                              # [B, T, D] -> [B, T, D]
        K = self.wK(x)
        V = self.wV(x)

        # reshape d -> dh, transpose
        Q = Q.reshape([B, T, -1, self.dh]).transpose(2,1).contiguous()  # [B, T, D] -> [B, T, H, Dh]
        K = K.reshape([B, T, -1, self.dh]).transpose(2,1).contiguous()
        V = V.reshape([B, T, -1, self.dh]).transpose(2,1).contiguous()

        # scores = Q @ K.T / sqrt(Dh)
        scores = Q @ K.transpose(-2, -1) / math.sqrt(self.dh)       # [B, H, T, Dh] @ [B, H, Dh, T] -> [B, H, T, T]

        # apply mask if needed
        if self.causal:
            Mc = torch.triu(torch.ones([T, T], dtype=bool).to(self.device), diagonal=1)
            Mc = Mc[None, None, :, :]                               # [T, T] -> [1, 1, T, T]
            scores = scores.masked_fill(Mc, float("-inf"))           # [B, H, T, T]

        # softmax
        A = torch.softmax(scores, dim=-1)                           # [B, H, T, T] -> [B, H, T, T]

        # A @ V
        Y = A @ V                                                   # [B, H, T, T] @ [B, H, T, Dh] -> [B, H, T, Dh]

        return self.wO(Y.transpose(2,1).reshape(B, T, D).contiguous())
    
    def MLP(self, x):
        # x in [B, T, D]

        x = self.wEL(x)
        x = self.gelu(x)
        x = self.wCL(x)

        return x

    def forward(self, x):
        # x in [B, T, D]

        # x + MHA(LN(x))                                    # [B, T, D] -> [B, T, D]
        x = x + self.MultiHeadAttention(self.ln1(x))        # ln: [B, T, D] -> [B, T, D]; MLH: [B, T, D] -> [B, T, D]

        # x + MLP(LN(x))            TODO: can use same ln?
        x = x + self.MLP(self.ln2(x))

        return x
