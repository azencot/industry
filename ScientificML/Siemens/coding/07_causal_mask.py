"""07. Causal mask — PROBLEM.

Do not open 07_causal_mask_solution.py until this file runs.

causal_mask(T) -> bool [T, T]. True means query i may attend to key j.
Position i cannot attend to j > i. Use triu or a broadcasted comparison.

combine_causal_and_padding(padding_mask):
    padding_mask [B, T] bool, True = valid key.
    return bool [B, 1, T, T], broadcastable to logits [B, H, T, T].
    A position is allowed only if it is causal AND the key is not padding.
""",

def causal_mask(t, device=None):
    raise NotImplementedError


def combine_causal_and_padding(padding_mask):
    raise NotImplementedError
