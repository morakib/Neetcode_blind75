"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

Given a rotated sorted array of distinct integers and a target, return
the index of target or -1 if not found. Must run in O(log n).

Key Intuition:
    At every binary search step, one half is always normally sorted.
    Determine which half is sorted, then check whether the target lies
    within that sorted range to decide which half to search.

Complexity (Optimal):
    Time:  O(log n)
    Space: O(1)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Modified binary search
# ──────────────────────────────────────────────
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


# ──────────────────────────────────────────────
# Alternative: Find pivot first, then standard binary search
# Time O(log n) · Space O(1) — two binary searches
# ──────────────────────────────────────────────
class SolutionTwoPass:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1: find the index of the minimum element (pivot)
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        pivot = lo

        # Step 2: standard binary search on the "unrotated" array
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            real_mid = (mid + pivot) % len(nums)
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
