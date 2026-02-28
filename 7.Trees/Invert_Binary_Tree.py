"""
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert it (mirror) and return the root.

Key Intuition:
    At every node, swap its left and right children, then recurse.
    Base case: null node, just return None.

Complexity (Optimal):
    Time:  O(n)
    Space: O(h)  — h = height (O(n) worst case, O(log n) balanced)
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ──────────────────────────────────────────────
# Optimal: DFS recursive
# ──────────────────────────────────────────────
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# ──────────────────────────────────────────────
# Alternative: BFS iterative
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionBFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
