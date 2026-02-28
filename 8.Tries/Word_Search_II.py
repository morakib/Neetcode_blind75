"""
212. Word Search II
https://leetcode.com/problems/word-search-ii/

Given an m × n board and a list of words, return all words that can be
formed by sequentially adjacent cells (no cell reused per word).

Key Intuition:
    Build a Trie from the word list. DFS from every cell; as you walk
    the board, walk the Trie simultaneously. Prune branches where the
    Trie has no continuation. Remove found words to avoid duplicates
    and to prune dead branches.

Complexity (Optimal):
    Time:  O(m · n · 4^L)  — L = max word length (pruning makes it much faster)
    Space: O(W · L)        — W = number of words in the trie
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # stores complete word at leaf


# ──────────────────────────────────────────────
# Optimal: Trie + Backtracking with pruning
# ──────────────────────────────────────────────
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            child = node.children[ch]

            if child.word:
                result.append(child.word)
                child.word = None  # de-duplicate

            # Mark visited
            board[r][c] = '#'
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, child)
            board[r][c] = ch  # restore

            # Prune: remove leaf nodes with no children
            if not child.children:
                del node.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result


# ──────────────────────────────────────────────
# Alternative: Per‑word backtracking (simpler but slower)
# Time O(W · m · n · 4^L) — W words each searched independently
# Not recommended for large inputs.
# ──────────────────────────────────────────────
class SolutionBrute:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        result = []

        def exist(word):
            def dfs(r, c, idx):
                if idx == len(word):
                    return True
                if (r < 0 or r >= rows or c < 0 or c >= cols or
                        board[r][c] != word[idx]):
                    return False
                tmp = board[r][c]
                board[r][c] = '#'
                found = any(dfs(r + dr, c + dc, idx + 1)
                            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)])
                board[r][c] = tmp
                return found

            for r in range(rows):
                for c in range(cols):
                    if dfs(r, c, 0):
                        return True
            return False

        for word in words:
            if exist(word):
                result.append(word)
        return result
