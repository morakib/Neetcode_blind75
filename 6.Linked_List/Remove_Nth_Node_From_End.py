"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the n‑th node from the end and
return the head.

Key Intuition:
    Use two pointers separated by n nodes. When the fast pointer reaches
    the end, the slow pointer is right before the target node.
    A dummy node elegantly handles the edge case of removing the head.

Complexity (Optimal):
    Time:  O(L)  — L = length of the list
    Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ──────────────────────────────────────────────
# Optimal: One‑pass, two pointers
# ──────────────────────────────────────────────
class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Advance fast n + 1 steps so the gap is n
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next  # delete the target node
        return dummy.next


# ──────────────────────────────────────────────
# Alternative: Two‑pass (compute length first)
# Time O(L) · Space O(1)
# ──────────────────────────────────────────────
class SolutionTwoPass:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        # First pass: get length
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # Edge case: remove the head
        if n == length:
            return head.next

        # Second pass: go to (length - n - 1)‑th node
        cur = head
        for _ in range(length - n - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head
