"""
268. Missing Number
https://leetcode.com/problems/missing-number/

Given an array nums containing n distinct numbers in [0, n], return
the one number in the range that is missing.

Key Intuition:
    XOR all indices 0..n with all values in nums. Pairs cancel out;
    the remaining value is the missing number. Alternatively, use
    the Gauss sum formula: n(n+1)/2 − sum(nums).

Complexity (Optimal):
    Time:  O(n)
    Space: O(1)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Gauss summation
# ──────────────────────────────────────────────
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


# ──────────────────────────────────────────────
# Alternative: XOR
# Time O(n) · Space O(1)
# ──────────────────────────────────────────────
class SolutionXOR:
    def missingNumber(self, nums: List[int]) -> int:
        xor = len(nums)
        for i, num in enumerate(nums):
            xor ^= i ^ num
        return xor
