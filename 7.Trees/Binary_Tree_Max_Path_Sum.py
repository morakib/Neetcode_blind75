"""
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path is any sequence of nodes connected by edges. Find the maximum
path sum (path doesn't need to go through the root).

Key Intuition:
    At each node, compute the max "gain" it can contribute to its parent
    (single branch). Meanwhile, update a global max considering the path
    that *passes through* this node (left gain + node + right gain).
    Gains are clamped to 0 (ignore negative branches).

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
# Optimal: Post‑order DFS
# ──────────────────────────────────────────────
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left_gain = max(dfs(node.left), 0)   # ignore negative
            right_gain = max(dfs(node.right), 0)

            # Path that passes through this node
            self.result = max(self.result, node.val + left_gain + right_gain)

            # Return max gain this node can contribute to its parent
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.result


# ──────────────────────────────────────────────
# Alternative: Same logic, iterative post‑order with stack
# Time O(n) · Space O(n)
# (Rarely needed in interviews — recursive version is cleaner)
# ──────────────────────────────────────────────
class SolutionIterative:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')
        gains = {}   # node -> max single-branch gain

        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                left_gain = max(gains.get(node.left, 0), 0)
                right_gain = max(gains.get(node.right, 0), 0)
                result = max(result, node.val + left_gain + right_gain)
                gains[node] = node.val + max(left_gain, right_gain)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return result
