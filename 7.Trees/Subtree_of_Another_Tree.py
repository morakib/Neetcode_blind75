"""
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/

Given roots of trees root and subRoot, return true if subRoot is a
subtree of root.

Key Intuition:
    At every node in root, check whether the subtree rooted there is
    identical to subRoot (using isSameTree). One match is enough.

Complexity (Optimal):
    Time:  O(m · n)  — m = nodes in root, n = nodes in subRoot
    Space: O(h)      — recursion depth
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ──────────────────────────────────────────────
# Optimal: Recursive check at every node
# ──────────────────────────────────────────────
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self._isSame(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def _isSame(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t:
            return True
        if not s or not t or s.val != t.val:
            return False
        return self._isSame(s.left, t.left) and self._isSame(s.right, t.right)


# ──────────────────────────────────────────────
# Alternative: Serialize both trees and use string matching
# Time O(m + n) with KMP — but O(m · n) with naive find
# Space O(m + n)
# ──────────────────────────────────────────────
class SolutionSerialize:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "#"
            # Use delimiters to avoid false substring matches
            return f",{node.val},{serialize(node.left)},{serialize(node.right)}"

        return serialize(subRoot) in serialize(root)
