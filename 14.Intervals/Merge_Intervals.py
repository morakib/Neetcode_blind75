"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given an array of intervals, merge all overlapping intervals.

Key Intuition:
    Sort by start time. Walk through intervals: if the current interval
    overlaps with the last merged one, extend its end; otherwise start
    a new merged interval.

Complexity (Optimal):
    Time:  O(n log n)  — sorting dominates
    Space: O(n)        — for the output
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Sort + linear merge
# ──────────────────────────────────────────────
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        return merged
