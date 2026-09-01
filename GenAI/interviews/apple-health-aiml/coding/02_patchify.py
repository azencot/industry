"""2. Patchify a multivariate time series — PROBLEM.

Given x with shape [T, C], build overlapping patches of length P and stride S.

    N = floor((T - P) / S) + 1
    return shape [N, P, C]

Example:

    x = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]]
    patch_size = 3, stride = 2
    ->
    [
      [[1, 10], [2, 20], [3, 30]],
      [[3, 30], [4, 40], [5, 50]],
    ]

Implement plain Python `patchify`. Optionally implement `patchify_torch`
with torch.Tensor.unfold (x: [T, C] -> [N, P, C]).

Assumptions to state before coding:
- stride > 0, patch_size >= 1.
- If T < P, return an empty list / empty tensor.
- No padding unless asked (follow-up).

After you code, say why patch size is a representation choice: small patches
keep high-frequency detail and explode token count; large patches compress
and can erase transients.

Follow-ups:
1. Pad an incomplete final patch.
2. Mask for padded positions.
3. Channels at different sampling rates.
4. Transformer cost when patch size doubles (stride fixed).
5. Why strided convolution might be preferable to hard patches.
"""

from __future__ import annotations


def patchify(x, patch_size, stride):
    ret = []

    P, T, S = patch_size, len(x), stride

    assert S > 0 and P > 0

    for i in range(0, T, S):
        # check if remaining elements are enough
        if T - i < P:
            # if pad
            ze = [0] * len(x[0])
            ret.append(x[i:] + [ze for _ in range(P - (T - i))])
            break

        ret.append(x[i:i+P])

    return ret


def patchify_torch(x, patch_size, stride):
    """x: torch.Tensor [T, C] -> [N, P, C]. Optional."""
    raise NotImplementedError


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
    print("02_patchify (python): PASS")

    try:
        import torch
    except ImportError:
        print("02_patchify (torch): SKIP")
    else:
        xt = torch.tensor(x, dtype=torch.float32)
        try:
            pt = patchify_torch(xt, 3, 2)
        except NotImplementedError:
            print("02_patchify (torch): not implemented yet")
        else:
            assert tuple(pt.shape) == (2, 3, 2), tuple(pt.shape)
            print("02_patchify (torch): PASS")
