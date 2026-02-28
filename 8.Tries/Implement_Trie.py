"""
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith.

Key Intuition:
    Each node is a dictionary of children keyed by character, plus a
    boolean marking end‑of‑word. Traversal follows one character at a
    time — O(L) per operation where L = word length.

Complexity:
    insert:      Time O(L) · Space O(L)
    search:      Time O(L) · Space O(1)
    startsWith:  Time O(L) · Space O(1)
"""


# ──────────────────────────────────────────────
# Optimal: Dict‑of‑dicts Trie
# ──────────────────────────────────────────────
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, prefix: str) -> TrieNode:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


# ──────────────────────────────────────────────
# Alternative: Using defaultdict for auto‑vivification
# Same complexity, slightly more concise
# ──────────────────────────────────────────────
from collections import defaultdict


class TrieDefaultDict:
    def __init__(self):
        # Nested defaultdict factory
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['#'] = True  # end marker

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
