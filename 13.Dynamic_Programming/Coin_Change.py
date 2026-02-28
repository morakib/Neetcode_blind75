"""
322. Coin Change
https://leetcode.com/problems/coin-change/

Given coins of different denominations and a total amount, return the
fewest number of coins needed. Return -1 if not possible.

Key Intuition:
    dp[a] = minimum coins to make amount a.
    For each amount from 1 to target, try every coin:
        dp[a] = min(dp[a], dp[a - coin] + 1)
    Base case: dp[0] = 0.

Complexity (Optimal):
    Time:  O(amount × len(coins))
    Space: O(amount)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Bottom‑up DP
# ──────────────────────────────────────────────
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


# ──────────────────────────────────────────────
# Alternative: Top‑down with memoization
# Time O(amount × len(coins)) · Space O(amount)
# ──────────────────────────────────────────────
class SolutionMemo:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            return min((dp(remaining - c) for c in coins), default=float('inf')) + 1

        result = dp(amount)
        return result if result != float('inf') else -1
