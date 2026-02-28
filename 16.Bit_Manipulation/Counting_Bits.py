"""
338. Counting Bits
https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans where ans[i] is the number of
1's in the binary representation of i, for 0 ≤ i ≤ n.

Key Intuition:
    dp[i] = dp[i >> 1] + (i & 1). Shifting right drops the last bit,
    which we add back with (i & 1). Each value builds on a previously
    computed one.

Complexity (Optimal):
    Time:  O(n)
    Space: O(n)  — the output
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: DP with bit shift
# ──────────────────────────────────────────────
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


# ──────────────────────────────────────────────
# Alternative: DP using i & (i-1) — strips last set bit
# Time O(n) · Space O(n)
# dp[i] = dp[i & (i-1)] + 1
# ──────────────────────────────────────────────
class SolutionKernighan:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp
