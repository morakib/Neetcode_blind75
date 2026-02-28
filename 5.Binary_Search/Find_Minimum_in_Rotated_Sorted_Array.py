"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

A sorted array of unique elements is rotated between 1 and n times.
Find the minimum element. Must run in O(log n).

Key Intuition:
    The minimum is at the "inflection point" where the sorted order
    breaks. Binary search: if nums[mid] > nums[right], the min is in
    the right half; otherwise it's in the left half (including mid).

Complexity (Optimal):
    Time:  O(log n)
    Space: O(1)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Modified binary search
# ──────────────────────────────────────────────
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1       # min is in right half
            else:
                r = mid           # min is mid or to the left
        return nums[l]


# ──────────────────────────────────────────────
# Alternative: Linear scan (trivial but O(n))
# Time O(n) · Space O(1)
# ──────────────────────────────────────────────
class SolutionLinear:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
