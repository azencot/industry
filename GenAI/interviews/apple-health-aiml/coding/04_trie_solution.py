"""4. Trie for event / token sequences — SOLUTION.

Children dict per node; is_end marks a complete inserted sequence.

    insert / contains / starts_with: O(L)
    Memory: O(total unique prefixes)

Optional: node.count for an empirical next-event model after a prefix.

Follow-ups:
1. Top-k next: from the prefix node, rank children by count (heap of
   size k). Deeper "most likely continuation" is a DFS/beam on counts.
2. Memory: one node per distinct prefix. Dense event streams with a
   large vocabulary can be large; share prefixes help.
3. Huge vocab: still a hash map per node. If branching is huge and
   sequences are short, a set of tuples may win.
4. Hash set of tuples: O(1) exact lookup, no prefix query unless you
   also store every prefix. Trie wins when starts_with / next-token
   is the point.
5. Markov(k): P(next | last k tokens) only. Trie conditioned on the
   full prefix can represent variable-order dependencies; it is still
   a count table, not a generalization of unseen prefixes.

This is a simple empirical next-event model, not a learned dynamics
model. Useful as a baseline before an HMM / Transformer over events.
"""

from __future__ import annotations


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, sequence):
        node = self.root
        node.count += 1
        for token in sequence:
            if token not in node.children:
                node.children[token] = TrieNode()
            node = node.children[token]
            node.count += 1
        node.is_end = True

    def _walk(self, sequence):
        node = self.root
        for token in sequence:
            if token not in node.children:
                return None
            node = node.children[token]
        return node

    def contains(self, sequence):
        node = self._walk(sequence)
        return bool(node is not None and node.is_end)

    def starts_with(self, prefix):
        return self._walk(prefix) is not None

    def next_counts(self, prefix):
        """Empirical next-token counts after prefix, or None if missing."""
        node = self._walk(prefix)
        if node is None:
            return None
        return {tok: child.count for tok, child in node.children.items()}


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
    assert t.contains([]) is False

    t.insert([])
    assert t.contains([]) is True

    nxt = t.next_counts(["sleep", "wake"])
    assert nxt == {"workout": 1, "meal": 1}, nxt
    print("04_trie_solution: PASS")
