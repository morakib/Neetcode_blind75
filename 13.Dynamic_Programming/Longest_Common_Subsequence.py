"""
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest
common subsequence (LCS).

Key Intuition:
    2D DP: if characters match, dp[i][j] = dp[i-1][j-1] + 1;
    otherwise take the max of skipping either character.
    Can be space‑optimized to one row.

Complexity (Optimal):
    Time:  O(m · n)
    Space: O(min(m, n))  — single row optimization
"""


# ──────────────────────────────────────────────
# Optimal: Bottom‑up DP (space‑optimized)
# ──────────────────────────────────────────────
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Ensure text2 is the shorter string for space optimization
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        prev = [0] * (len(text2) + 1)

        for i in range(1, len(text1) + 1):
            cur = [0] * (len(text2) + 1)
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    cur[j] = prev[j - 1] + 1
                else:
                    cur[j] = max(prev[j], cur[j - 1])
            prev = cur

        return prev[-1]


# ──────────────────────────────────────────────
# Alternative: Full 2D DP table (easier to understand)
# Time O(m · n) · Space O(m · n)
# ──────────────────────────────────────────────
class SolutionFull2D:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
