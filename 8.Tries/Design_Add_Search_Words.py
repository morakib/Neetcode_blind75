"""
211. Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports addWord and search. The search
word can contain '.' which matches any letter.

Key Intuition:
    Build a standard Trie for addWord. For search, when a '.' is
    encountered, branch out and try all children recursively. Only
    one path needs to succeed.

Complexity:
    addWord: Time O(L) · Space O(L)
    search:  Time O(26^L) worst case with all dots · Space O(L) stack
             Typically much faster with real words.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


# ──────────────────────────────────────────────
# Optimal: Trie with DFS wildcard handling
# ──────────────────────────────────────────────
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.is_end

            ch = word[index]
            if ch == '.':
                # Try every child
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(index + 1, node.children[ch])

        return dfs(0, self.root)


# ──────────────────────────────────────────────
# Alternative: Bucket by word length + regex (simpler but slower)
# addWord O(1) · search O(n·L) where n = words of that length
# ──────────────────────────────────────────────
from collections import defaultdict


class WordDictionaryBrute:
    def __init__(self):
        self.words = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.words[len(word)].append(word)

    def search(self, word: str) -> bool:
        for candidate in self.words[len(word)]:
            if all(w == '.' or w == c for w, c in zip(word, candidate)):
                return True
        return False
