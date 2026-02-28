"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i]
equals the product of all elements except nums[i], without using division.

Key Intuition:
    For each index, the answer is (product of everything to its left) ×
    (product of everything to its right). Two passes — one forward, one
    backward — build these prefix/suffix products in‑place.

Complexity (Optimal):
    Time:  O(n)
    Space: O(1)  — output array doesn't count as extra space
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Prefix & suffix in a single output array
# ──────────────────────────────────────────────
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Forward pass: answer[i] = product of nums[0..i-1]
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Backward pass: multiply by product of nums[i+1..n-1]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


# ──────────────────────────────────────────────
# Alternative: Separate prefix & suffix arrays (clearer, same time)
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionExplicit:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        return [prefix[i] * suffix[i] for i in range(n)]
