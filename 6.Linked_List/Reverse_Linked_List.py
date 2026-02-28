"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse and return its head.

Key Intuition:
    Walk through the list, re‑pointing each node's `next` to its
    predecessor. Only three pointers are needed: prev, curr, next_temp.

Complexity (Optimal – Iterative):
    Time:  O(n)
    Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ──────────────────────────────────────────────
# Optimal: Iterative
# ──────────────────────────────────────────────
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev


# ──────────────────────────────────────────────
# Alternative: Recursive
# Time O(n) · Space O(n) — call stack
# ──────────────────────────────────────────────
class SolutionRecursive:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
