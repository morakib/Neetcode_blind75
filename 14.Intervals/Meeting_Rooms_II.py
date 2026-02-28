"""
253. Meeting Rooms II (Premium)
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals, find the minimum number of
conference rooms required.

Key Intuition:
    Treat starts and ends as events on a timeline. Sort all start/end
    times. Walk through: +1 room at each start, −1 at each end.
    The peak count is the answer. Alternatively, use a min‑heap of
    end times.

Complexity (Optimal):
    Time:  O(n log n)
    Space: O(n)
"""

from typing import List
import heapq


# ──────────────────────────────────────────────
# Optimal: Min‑heap of end times
# ──────────────────────────────────────────────
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()
        heap = []  # end times of ongoing meetings

        for start, end in intervals:
            # If earliest ending meeting is done before this one starts,
            # reuse that room
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)


# ──────────────────────────────────────────────
# Alternative: Chronological event sweep
# Time O(n log n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionSweep:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        rooms = 0
        end_ptr = 0
        for start in starts:
            if start < ends[end_ptr]:
                rooms += 1
            else:
                end_ptr += 1
        return rooms
