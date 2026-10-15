"""08. Multi-head shapes — PROBLEM.

Do not open 08_multihead_solution.py until this file runs.

split_heads: [B, T, D] -> [B, H, T, Dh] with Dh = D / H. D must divide H.
merge_heads: reverse that.

multihead_attention(q, k, v, n_heads):
    q, k, v are [B, T, D] (same T and D here).
    Split, scaled dot-product per head (scale by sqrt(Dh)), merge.
    return [B, T, D]

Say the shape after transpose(-2, -1) on keys: [B, H, Dh, T].
Q @ K^T is [B, H, T, T]. Attention @ V is [B, H, T, Dh].

view/reshape after permute needs contiguous memory.
""",

def split_heads(x, n_heads):
    raise NotImplementedError


def merge_heads(x):
    raise NotImplementedError


def multihead_attention(q, k, v, n_heads):
    raise NotImplementedError
