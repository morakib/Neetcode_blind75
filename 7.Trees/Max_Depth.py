"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth (longest
root‑to‑leaf path in number of nodes).

Key Intuition:
    The depth of a tree is 1 + max(depth of left, depth of right).
    Base case: empty tree has depth 0.

Complexity (Optimal):
    Time:  O(n)
    Space: O(h)
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ──────────────────────────────────────────────
# Alternative: BFS level‑order (count levels)
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionBFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        queue = deque([root])
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


# ──────────────────────────────────────────────
# Alternative: Iterative DFS with stack
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionIterDFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_d = 0
        while stack:
            node, depth = stack.pop()
            max_d = max(max_d, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_d
