"""
295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

Design a data structure that supports addNum and findMedian.

Key Intuition:
    Maintain two heaps: a max‑heap for the smaller half and a min‑heap
    for the larger half. Keep them balanced (sizes differ by at most 1).
    The median is the top of the larger heap — or the average of both tops.

Complexity:
    addNum:     Time O(log n)
    findMedian: Time O(1)
    Space: O(n)
"""

import heapq


# ──────────────────────────────────────────────
# Optimal: Two heaps (max‑heap + min‑heap)
# ──────────────────────────────────────────────
class MedianFinder:
    def __init__(self):
        # max‑heap (invert values) for smaller half
        self.lo = []   # max-heap (negate values)
        # min‑heap for larger half
        self.hi = []   # min-heap

    def addNum(self, num: int) -> None:
        # Always add to max‑heap first
        heapq.heappush(self.lo, -num)
        # Move top of lo to hi to maintain ordering
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        # Balance: lo should have >= hi elements
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2.0


# ──────────────────────────────────────────────
# Alternative: SortedList (from sortedcontainers)
# addNum O(log n) · findMedian O(1)
# Requires: pip install sortedcontainers
# ──────────────────────────────────────────────
# from sortedcontainers import SortedList
#
# class MedianFinderSorted:
#     def __init__(self):
#         self.data = SortedList()
#
#     def addNum(self, num: int) -> None:
#         self.data.add(num)
#
#     def findMedian(self) -> float:
#         n = len(self.data)
#         if n % 2 == 1:
#             return self.data[n // 2]
#         return (self.data[n // 2 - 1] + self.data[n // 2]) / 2.0
