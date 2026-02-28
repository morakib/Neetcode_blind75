"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Key Intuition:
    A set only stores unique elements — if its size differs from the array's,
    a duplicate exists. Converting to a set gives O(1) lookups.

Complexity (Optimal):
    Time:  O(n)
    Space: O(n)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Hash Set
# ──────────────────────────────────────────────
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# ──────────────────────────────────────────────
# Alternative 1: Early‑exit with a growing set
# Time O(n) · Space O(n) — faster in practice when duplicates are near the start
# ──────────────────────────────────────────────
class SolutionEarlyExit:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


# ──────────────────────────────────────────────
# Alternative 2: Sorting
# Time O(n log n) · Space O(1) if in-place sort allowed
# ──────────────────────────────────────────────
class SolutionSort:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
