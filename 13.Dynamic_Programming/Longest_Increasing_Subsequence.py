"""
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

Key Intuition (O(n log n)):
    Maintain a "tails" array where tails[i] is the smallest tail
    element for an increasing subsequence of length i+1. For each num,
    binary search to find its position in tails. This gives O(n log n).

Complexity (Optimal):
    Time:  O(n log n)
    Space: O(n)
"""

from typing import List
import bisect


# ──────────────────────────────────────────────
# Optimal: Patience sorting / binary search on tails
# ──────────────────────────────────────────────
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)


# ──────────────────────────────────────────────
# Alternative: Classic DP
# Time O(n²) · Space O(n)
# dp[i] = LIS ending at index i
# ──────────────────────────────────────────────
class SolutionDP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
