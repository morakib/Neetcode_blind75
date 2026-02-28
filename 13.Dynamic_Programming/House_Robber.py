"""
198. House Robber
https://leetcode.com/problems/house-robber/

Given an array of non‑negative integers representing money at each house,
maximize the amount you can rob without robbing adjacent houses.

Key Intuition:
    At each house, choose: rob it (add its value to the answer two houses
    back) or skip it (keep the answer from the previous house).
    dp[i] = max(dp[i-1], dp[i-2] + nums[i]).

Complexity (Optimal):
    Time:  O(n)
    Space: O(1)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Two variables DP
# ──────────────────────────────────────────────
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        return prev1


# ──────────────────────────────────────────────
# Alternative: DP array (clearer)
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionArray:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
