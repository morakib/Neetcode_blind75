"""
252. Meeting Rooms (Premium)
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals, determine if a person could
attend all meetings (no two meetings overlap).

Key Intuition:
    Sort by start time. If any meeting starts before the previous one
    ends, there's a conflict.

Complexity (Optimal):
    Time:  O(n log n)
    Space: O(1)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Sort + linear check
# ──────────────────────────────────────────────
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
