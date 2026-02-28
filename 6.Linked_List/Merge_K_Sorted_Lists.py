"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists into one sorted linked list.

Key Intuition:
    Use a min‑heap of size k to always pick the smallest current head.
    Push the next node of the chosen list back into the heap.

Complexity (Optimal – Heap):
    Time:  O(N log k)  — N = total nodes, k = number of lists
    Space: O(k)
"""

from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ──────────────────────────────────────────────
# Optimal: Min‑heap
# ──────────────────────────────────────────────
class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        # (value, tie‑breaker index, node)
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# ──────────────────────────────────────────────
# Alternative: Divide and Conquer (merge pairs)
# Time O(N log k) · Space O(log k) — recursion depth
# ──────────────────────────────────────────────
class SolutionDC:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self._merge2(l1, l2))
            lists = merged
        return lists[0]

    def _merge2(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next
