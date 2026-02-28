"""
91. Decode Ways
https://leetcode.com/problems/decode-ways/

A message containing letters A-Z is encoded as '1'-'26'. Given a string
of digits s, return the number of ways to decode it.

Key Intuition:
    dp[i] = number of ways to decode s[0:i].
    A single digit (1-9) contributes dp[i-1]; a valid two‑digit number
    (10-26) contributes dp[i-2]. Be careful with '0'.

Complexity (Optimal):
    Time:  O(n)
    Space: O(1)
"""


# ──────────────────────────────────────────────
# Optimal: Bottom‑up DP with two variables
# ──────────────────────────────────────────────
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        prev2 = 1  # dp[i-2], empty string
        prev1 = 1  # dp[i-1], first character

        for i in range(1, len(s)):
            cur = 0
            # Single digit
            if s[i] != '0':
                cur += prev1
            # Two digits
            two_digit = int(s[i - 1:i + 1])
            if 10 <= two_digit <= 26:
                cur += prev2

            prev2, prev1 = prev1, cur

        return prev1


# ──────────────────────────────────────────────
# Alternative: Top‑down with memoization
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionMemo:
    def numDecodings(self, s: str) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            ways = dp(i + 1)
            if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
                ways += dp(i + 2)
            return ways

        return dp(0)
