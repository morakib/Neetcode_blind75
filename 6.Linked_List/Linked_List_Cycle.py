"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Given head, determine if the linked list has a cycle.

Key Intuition:
    Floyd's Tortoise and Hare: slow moves 1 step, fast moves 2 steps.
    If there's a cycle they will eventually meet; if not, fast reaches
    the end.

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
# Optimal: Floyd's cycle detection
# ──────────────────────────────────────────────
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


# ──────────────────────────────────────────────
# Alternative: Hash set of visited nodes
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionHash:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        cur = head
        while cur:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        return False
