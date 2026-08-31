"""2. Patchify a multivariate time series — SOLUTION.

Plain Python: sliding start += stride while start + P <= T.

PyTorch: unfold on time, then permute [N, C, P] -> [N, P, C].

    N = floor((T - P) / S) + 1
    Time  O(N P C) to materialize (unfold itself is a view)
    Space O(N P C)

Modeling: patch size is the temporal resolution / token-budget knob.

Small P: keeps fine structure; many tokens; attention is quadratic in N.
Large P: compresses; may erase high-frequency events (HR spikes, steps).

If stride doubles with patch size, N halves — Transformer self-attn cost
drops ~4x in the token axis, at the price of temporal resolution.

Follow-ups:
1. Pad last patch with zeros (or repeat last sample) up to P.
2. Boolean mask [N, P] False on padded steps; also drop incomplete
   patches if you refuse to invent time.
3. Different rates: patch per modality at native rate, then fuse
   (problem 1 + 3). Do not first resample onto one grid.
4. P doubles, S fixed: N ≈ (T-2P)/S + 1, slightly fewer tokens, each
   covering more time. Cost ~ N^2 still. If you also scale S with P,
   N halves and attention cost falls ~4x.
5. Strided conv learns the patch projection; hard slice + linear is a
   frozen boxcar. Conv can be a better tokenizer when phase of the
   window matters.
"""

from __future__ import annotations


def patchify(x, patch_size, stride):
    if patch_size <= 0 or stride <= 0:
        raise ValueError("patch_size and stride must be positive")
    patches = []
    start = 0
    while start + patch_size <= len(x):
        patches.append(x[start:start + patch_size])
        start += stride
    return patches


def patchify_torch(x, patch_size, stride):
    # x: [T, C] -> unfold time -> [N, C, P] -> [N, P, C]
    patches = x.unfold(dimension=0, size=patch_size, step=stride)
    return patches.permute(0, 2, 1)


if __name__ == "__main__":
    x = [
        [1, 10],
        [2, 20],
        [3, 30],
        [4, 40],
        [5, 50],
    ]
    got = patchify(x, 3, 2)
    expected = [
        [[1, 10], [2, 20], [3, 30]],
        [[3, 30], [4, 40], [5, 50]],
    ]
    assert got == expected, got
    assert patchify(x, 6, 1) == []
    assert patchify(x, 5, 1) == [x]
    print("02_patchify_solution (python): PASS")

    try:
        import torch
    except ImportError:
        print("02_patchify_solution (torch): SKIP")
    else:
        xt = torch.tensor(x, dtype=torch.float32)
        pt = patchify_torch(xt, 3, 2)
        assert tuple(pt.shape) == (2, 3, 2), tuple(pt.shape)
        torch.testing.assert_close(pt[0], xt[:3])
        torch.testing.assert_close(pt[1], xt[2:5])
        print("02_patchify_solution (torch): PASS")
