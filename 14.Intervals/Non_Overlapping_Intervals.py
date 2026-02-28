"""
435. Non‑overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals, return the minimum number of intervals
you need to remove to make the rest non‑overlapping.

Key Intuition:
    Sort by end time (greedy "activity selection"). Always keep the
    interval that ends earliest — it leaves the most room for future
    intervals. Count how many you must remove.

Complexity (Optimal):
    Time:  O(n log n)
    Space: O(1)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Greedy — sort by end time
# ──────────────────────────────────────────────
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removals = 0
        prev_end = float('-inf')

        for start, end in intervals:
            if start < prev_end:
                removals += 1     # overlap → remove this one
            else:
                prev_end = end    # no overlap → keep it

        return removals


# ──────────────────────────────────────────────
# Alternative: Sort by start time, track removals differently
# Time O(n log n) · Space O(1)
# ──────────────────────────────────────────────
class SolutionSortByStart:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removals = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                removals += 1
                prev_end = min(prev_end, end)  # keep the one ending earlier
            else:
                prev_end = end

        return removals
