"""
139. Word Break
https://leetcode.com/problems/word-break/

Given a string s and a dictionary wordDict, return true if s can be
segmented into space‑separated dictionary words.

Key Intuition:
    dp[i] = True if s[0:i] can be segmented. For each position i, check
    all dictionary words: if dp[i - len(word)] is True and
    s[i-len(word):i] == word, then dp[i] = True.

Complexity (Optimal):
    Time:  O(n² · m)  — n = len(s), m = avg word length for comparison
    Space: O(n)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Bottom‑up DP
# ──────────────────────────────────────────────
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # empty string

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


# ──────────────────────────────────────────────
# Alternative: Top‑down with memoization
# Time O(n² · m) · Space O(n)
# ──────────────────────────────────────────────
class SolutionMemo:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from functools import lru_cache
        word_set = set(wordDict)

        @lru_cache(maxsize=None)
        def dp(start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set and dp(end):
                    return True
            return False

        return dp(0)
