"""Friday redo 3. Pre-norm transformer block. 25 minutes.

Do not open A_transformer_block.py or F_minigpt.py.
Do not call nn.MultiheadAttention or F.scaled_dot_product_attention.

    x: [B, T, D]
    return [B, T, D]

    x = x + MultiHeadAttention(LayerNorm(x))
    x = x + MLP(LayerNorm(x))

Self-attention: Linear Q, K, V. Split into n_heads. D is divisible by
n_heads; raise if it is not. Scores are scaled by sqrt(head dim).
Causal: query i cannot attend to key j > i. Then the output projection.

MLP: Linear(D, 4D), GELU, Linear(4D, D).

Checks:
- output shape equals input shape, including batch size 1 and n_heads > 1
- gradients reach Q, K, V, both MLP linears, and both LayerNorms
- editing a future token does not change an earlier output
"""

import torch
import torch.nn as nn
import math

class TransformerBlock(nn.Module):
    def __init__(self, d, n_heads):
        super().__init__()
        
        assert d % n_heads == 0

        self.d = d
        self.n_heads = n_heads
        self.dh = d // n_heads

        # MHA
        self.ln1 = nn.LayerNorm(d)
        self.wK = nn.Linear(d, d)
        self.wQ = nn.Linear(d, d)
        self.wV = nn.Linear(d, d)
        self.wO = nn.Linear(d, d)

        # MLP
        self.ln2 = nn.LayerNorm(d)
        self.MLP = nn.Sequential(
            nn.Linear(d, 4*d),
            nn.GELU(),
            nn.Linear(4*d, d)
        )

    def MultiHeadAttention(self, x):
        # x in [B, T, D]
        B, T, D = x.shape

        # extract Q, K, V
        Q = self.wQ(x)
        K = self.wK(x)
        V = self.wV(x)

        # reshape
        Q = Q.reshape([B, T, -1, self.dh]).transpose(2, 1).contiguous()             # [B, T, D] -> [B, T, H, Dh] -> [B, H, T, dh]
        K = K.reshape([B, T, -1, self.dh]).transpose(2, 1).contiguous()
        V = V.reshape([B, T, -1, self.dh]).transpose(2, 1).contiguous()

        # scaled dot product
        QKT = Q @ K.transpose(-2, -1) / math.sqrt(self.dh)                          # [B, H, T, dh] @ [B, H, dh, T] -> [B, H, T, T]
        
        # mask
        mask = torch.triu(torch.ones([T, T], dtype=bool).to(x.device), diagonal=1)  # [T, T] -> [T, T]
        scores = QKT.masked_fill(mask[None, None, :, :], float("-inf"))            # [B, H, T, T] -> [B, H, T, T]

        # softmax
        A = torch.softmax(scores, dim=-1)                                           # [B, H, T, T] -> [B, H, T, T]

        # nan to num
        A = torch.nan_to_num(A, nan=0.0)                                            # [B, H, T, T] -> [B, H, T, T]

        # scale V
        Y = A @ V                                                                   # [B, H, T, T] @ [B, H, T, dh] -> [B, H, T, dh]

        # reshape back
        Y = Y.transpose(2, 1).reshape([B, T, self.d]).contiguous()                  # [B, H, T, dh] -> [B, T, H, dh] -> [B, T, D]

        return self.wO(Y)                                                           # [B, T, D] -> [B, T, D]



    def forward(self, x):
        # x in [B, T, D]
        
        # MHA
        x = x + self.MultiHeadAttention(self.ln1(x))

        # MLP
        x = x + self.MLP(self.ln2(x))

        return x