"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid BST.

Key Intuition:
    Every node must fall within an allowed range (low, high). Going left
    tightens the upper bound; going right tightens the lower bound.
    Start with (-inf, inf).

Complexity (Optimal):
    Time:  O(n)
    Space: O(h)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ──────────────────────────────────────────────
# Optimal: DFS with valid range
# ──────────────────────────────────────────────
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float('-inf'), float('inf'))


# ──────────────────────────────────────────────
# Alternative: In‑order traversal (should be strictly increasing)
# Time O(n) · Space O(h)
# ──────────────────────────────────────────────
class SolutionInorder:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')

        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)

        return inorder(root)
