"""
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a BST and an integer k, return the k‑th smallest value.

Key Intuition:
    In‑order traversal of a BST yields elements in sorted order.
    Just count to k during the traversal.

Complexity (Optimal):
    Time:  O(h + k)
    Space: O(h)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ──────────────────────────────────────────────
# Optimal: Iterative in‑order traversal
# ──────────────────────────────────────────────
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        while cur or stack:
            # Go as far left as possible
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val

            cur = cur.right


# ──────────────────────────────────────────────
# Alternative: Recursive in‑order (collect all, pick k‑th)
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionRecursive:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def inorder(node):
            if not node or len(result) >= k:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result[k - 1]
