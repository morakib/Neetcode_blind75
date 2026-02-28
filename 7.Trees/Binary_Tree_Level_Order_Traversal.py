"""
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root, return the level order traversal (values grouped by level).

Key Intuition:
    BFS with a queue. Process nodes level‑by‑level: at each level,
    drain the current queue size and collect all values for that level.

Complexity (Optimal):
    Time:  O(n)
    Space: O(n)
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ──────────────────────────────────────────────
# Optimal: BFS with queue
# ──────────────────────────────────────────────
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result


# ──────────────────────────────────────────────
# Alternative: DFS recursive (track depth)
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionDFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(result):
                result.append([])
            result[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return result
