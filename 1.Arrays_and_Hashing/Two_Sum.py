"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return the indices
of the two numbers that add up to target.

Key Intuition:
    For each number, its required complement (target − num) is known.
    A hash map lets you check in O(1) whether that complement was seen earlier.

Complexity (Optimal):
    Time:  O(n)
    Space: O(n)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: One‑pass hash map
# ──────────────────────────────────────────────
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i


# ──────────────────────────────────────────────
# Alternative: Brute force
# Time O(n²) · Space O(1)
# ──────────────────────────────────────────────
class SolutionBrute:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
