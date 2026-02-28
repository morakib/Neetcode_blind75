"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/

A robot on an m × n grid starts at top‑left and can only move right or
down. How many unique paths to the bottom‑right?

Key Intuition:
    dp[r][c] = dp[r-1][c] + dp[r][c-1]. The first row and column are
    all 1's. Can be space‑optimized to a single row.

Complexity (Optimal):
    Time:  O(m · n)
    Space: O(n)
"""


# ──────────────────────────────────────────────
# Optimal: 1D DP (space‑optimized)
# ──────────────────────────────────────────────
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(1, m):
            for c in range(1, n):
                row[c] += row[c - 1]
        return row[-1]


# ──────────────────────────────────────────────
# Alternative: Math — combination formula C(m+n-2, m-1)
# Time O(min(m, n)) · Space O(1)
# ──────────────────────────────────────────────
from math import comb


class SolutionMath:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)
