"""
377. Combination Sum IV
https://leetcode.com/problems/combination-sum-iv/

Given an array of distinct positive integers nums and a target, return
the number of possible combinations that add up to target.
(Order matters — this is really counting permutations.)

Key Intuition:
    dp[t] = number of ways to reach sum t. For each target from 1..target,
    try every num: dp[t] += dp[t - num].  This is the "unbounded knapsack
    with order" variant.

Complexity (Optimal):
    Time:  O(target × len(nums))
    Space: O(target)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Bottom‑up DP
# ──────────────────────────────────────────────
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for t in range(1, target + 1):
            for num in nums:
                if num <= t:
                    dp[t] += dp[t - num]

        return dp[target]


# ──────────────────────────────────────────────
# Alternative: Top‑down with memoization
# Time O(target × len(nums)) · Space O(target)
# ──────────────────────────────────────────────
class SolutionMemo:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(remaining):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            return sum(dp(remaining - num) for num in nums)

        return dp(target)
