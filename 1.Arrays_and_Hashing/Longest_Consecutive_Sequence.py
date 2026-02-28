"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence. Must run in O(n) time.

Key Intuition:
    Put all numbers in a set. A number is the *start* of a sequence only
    if (num − 1) is NOT in the set. From each start, count upward.
    Every element is visited at most twice → O(n).

Complexity (Optimal):
    Time:  O(n)
    Space: O(n)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Hash set with smart start detection
# ──────────────────────────────────────────────
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            # Only start counting from the beginning of a sequence
            if n - 1 not in num_set:
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest


# ──────────────────────────────────────────────
# Alternative: Sorting
# Time O(n log n) · Space O(1) or O(n) depending on sort
# ──────────────────────────────────────────────
class SolutionSort:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # skip duplicates
            if nums[i] == nums[i - 1] + 1:
                cur_len += 1
            else:
                cur_len = 1
            longest = max(longest, cur_len)
        return longest
