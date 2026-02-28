"""
143. Reorder List
https://leetcode.com/problems/reorder-list/

Reorder: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
Do not return anything, modify head in-place.

Key Intuition:
    1. Find the middle using slow/fast pointers.
    2. Reverse the second half.
    3. Merge the two halves by alternating nodes.

Complexity (Optimal):
    Time:  O(n)
    Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ──────────────────────────────────────────────
# Optimal: Split + Reverse + Merge
# ──────────────────────────────────────────────
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find middle (slow ends at start of 2nd half)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        second = slow.next
        slow.next = None  # cut
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        second = prev  # head of reversed 2nd half

        # 3. Merge two halves
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


# ──────────────────────────────────────────────
# Alternative: Deque‑based (uses extra space)
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
from collections import deque


class SolutionDeque:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        nodes = deque()
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        cur = nodes.popleft()
        while nodes:
            cur.next = nodes.pop()
            cur = cur.next
            if nodes:
                cur.next = nodes.popleft()
                cur = cur.next
        cur.next = None
