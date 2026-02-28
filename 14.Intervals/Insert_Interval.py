"""
57. Insert Interval
https://leetcode.com/problems/insert-interval/

Given a sorted list of non‑overlapping intervals and a new interval,
insert and merge if necessary.

Key Intuition:
    Walk through intervals in three phases:
    1. Add all intervals that end before the new one starts.
    2. Merge all overlapping intervals with the new one.
    3. Add remaining intervals.

Complexity (Optimal):
    Time:  O(n)
    Space: O(n)  — for the output
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Linear scan + merge
# ──────────────────────────────────────────────
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # 1. Add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # 3. Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
