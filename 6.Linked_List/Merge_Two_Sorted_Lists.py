"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists into one sorted list made by splicing
together the nodes of the two input lists.

Key Intuition:
    Use a dummy head and a tail pointer. Compare the two current nodes;
    attach the smaller one and advance that list. Append whatever remains.

Complexity (Optimal – Iterative):
    Time:  O(n + m)
    Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ──────────────────────────────────────────────
# Optimal: Iterative with dummy head
# ──────────────────────────────────────────────
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next


# ──────────────────────────────────────────────
# Alternative: Recursive
# Time O(n + m) · Space O(n + m) — call stack
# ──────────────────────────────────────────────
class SolutionRecursive:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
