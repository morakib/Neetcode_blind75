"""
79. Word Search
https://leetcode.com/problems/word-search/

Given an m × n board and a word, return true if the word exists in the
grid by following adjacent cells (no cell reused).

Key Intuition:
    DFS/backtracking from every cell. At each step, mark the cell as
    visited, explore 4 directions, then unmark (backtrack). Match one
    character at a time; return True as soon as the full word is matched.

Complexity:
    Time:  O(m · n · 4^L)  — L = word length
    Space: O(L)             — recursion depth
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Backtracking DFS
# ──────────────────────────────────────────────
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                    board[r][c] != word[idx]):
                return False

            # Mark visited
            tmp = board[r][c]
            board[r][c] = '#'

            found = (dfs(r + 1, c, idx + 1) or
                     dfs(r - 1, c, idx + 1) or
                     dfs(r, c + 1, idx + 1) or
                     dfs(r, c - 1, idx + 1))

            board[r][c] = tmp  # backtrack
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


# ──────────────────────────────────────────────
# Optimization tip: Count character frequencies first.
# If the word's first character is rarer than the last,
# search the reversed word to prune faster.
# ──────────────────────────────────────────────
from collections import Counter


class SolutionOptimized:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)

        # Check if board has enough characters
        for ch, cnt in word_count.items():
            if board_count[ch] < cnt:
                return False

        # Reverse word if first char is more common than last
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                    board[r][c] != word[idx]):
                return False
            tmp = board[r][c]
            board[r][c] = '#'
            found = (dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1) or
                     dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1))
            board[r][c] = tmp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
