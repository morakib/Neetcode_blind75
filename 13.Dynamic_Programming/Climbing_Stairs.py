"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You can climb 1 or 2 steps at a time. How many distinct ways to reach
the top (n steps)?

Key Intuition:
    dp[i] = dp[i-1] + dp[i-2] — identical to the Fibonacci sequence.
    You only need two variables, not an array.

Complexity (Optimal):
    Time:  O(n)
    Space: O(1)
"""


# ──────────────────────────────────────────────
# Optimal: Bottom‑up with two variables
# ──────────────────────────────────────────────
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


# ──────────────────────────────────────────────
# Alternative: Top‑down with memoization
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionMemo:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(i):
            if i <= 2:
                return i
            if i in memo:
                return memo[i]
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]

        return dp(n)
