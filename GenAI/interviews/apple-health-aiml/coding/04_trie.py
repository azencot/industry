"""4. Trie for event / token sequences — PROBLEM.

Implement a trie over sequences of tokens (not characters):

    insert(sequence)
    contains(sequence)     # True only if this exact sequence was inserted
    starts_with(prefix)    # True if some inserted sequence has this prefix

Example:

    insert ["sleep", "wake", "workout"]
    insert ["sleep", "wake", "meal"]
    insert ["sleep", "rest"]
    insert ["workout", "rest"]

    starts_with(["sleep", "wake"]) -> True
    contains(["sleep", "wake"])    -> False
    contains(["sleep", "rest"])    -> True

Complexity: O(L) per op for sequence length L.

Assumptions:
- Tokens are hashable (str / int).
- Empty sequence: insert marks the root as an end; contains([]) is True
  after that; starts_with([]) is always True.

Follow-ups:
1. Top-k next tokens after a prefix.
2. Memory cost.
3. Huge vocabulary.
4. When a flat hash set of tuples is preferable.
5. Difference from a Markov model.

Optional extension (solution file): store counts on nodes for an empirical
next-event distribution.
"""

from __future__ import annotations


class TrieNode:
    def __init__(self):
        raise NotImplementedError


class Trie:
    def __init__(self):
        raise NotImplementedError

    def insert(self, sequence):
        raise NotImplementedError

    def contains(self, sequence):
        raise NotImplementedError

    def starts_with(self, prefix):
        raise NotImplementedError


if __name__ == "__main__":
    t = Trie()
    t.insert(["sleep", "wake", "workout"])
    t.insert(["sleep", "wake", "meal"])
    t.insert(["sleep", "rest"])
    t.insert(["workout", "rest"])

    assert t.starts_with(["sleep", "wake"]) is True
    assert t.contains(["sleep", "wake"]) is False
    assert t.contains(["sleep", "rest"]) is True
    assert t.contains(["workout", "rest"]) is True
    assert t.starts_with(["workout"]) is True
    assert t.starts_with(["meal"]) is False
    assert t.contains(["sleep", "wake", "nap"]) is False
    assert t.starts_with([]) is True
    print("04_trie: PASS")
