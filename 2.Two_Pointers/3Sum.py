"""
15. 3Sum
https://leetcode.com/problems/3sum/

Given an integer array nums, return all unique triplets [a, b, c] such
that a + b + c = 0.

Key Intuition:
    Sort the array, fix one element, then use two pointers on the
    remaining subarray to find pairs that sum to its negation.
    Skip duplicates at every level to avoid repeated triplets.

Complexity (Optimal):
    Time:  O(n²)
    Space: O(1)  — ignoring output storage; sort is in‑place
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Sort + Two Pointers
# ──────────────────────────────────────────────
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            # Skip duplicate for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Early termination: smallest triplet already > 0
            if nums[i] > 0:
                break

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    # Skip duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return result


# ──────────────────────────────────────────────
# Alternative: Hash set approach (less common in interviews)
# Time O(n²) · Space O(n)
# ──────────────────────────────────────────────
class SolutionHashSet:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            seen = set()
            j = i + 1
            while j < len(nums):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    result.append([nums[i], complement, nums[j]])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1
        return result
