"""
213. House Robber II
https://leetcode.com/problems/house-robber-ii/

Same as House Robber, but the houses are arranged in a circle (first and
last houses are adjacent).

Key Intuition:
    Since houses form a circle, you can never rob both the first and last.
    Run House Robber I twice: once on nums[1:] and once on nums[:-1].
    Take the max of the two.

Complexity (Optimal):
    Time:  O(n)
    Space: O(1)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Two passes of House Robber I
# ──────────────────────────────────────────────
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev2, prev1 = 0, 0
            for h in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + h)
            return prev1

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))


# ──────────────────────────────────────────────
# Alternative: DP array version (clearer)
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionArray:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        def rob_range(lo, hi):
            dp = [0] * len(nums)
            dp[lo] = nums[lo]
            dp[lo + 1] = max(nums[lo], nums[lo + 1])
            for i in range(lo + 2, hi + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[hi]

        return max(rob_range(0, len(nums) - 2),
                   rob_range(1, len(nums) - 1))
