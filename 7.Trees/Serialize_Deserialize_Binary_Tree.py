"""
297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Design an algorithm to serialize a binary tree to a string and
deserialize it back.

Key Intuition:
    Use pre‑order DFS. Represent null nodes with a sentinel (e.g. "N").
    On deserialization, consume tokens in the same pre‑order sequence,
    using nulls to know when a subtree is complete.

Complexity:
    Time:  O(n)  — both serialize & deserialize
    Space: O(n)
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ──────────────────────────────────────────────
# Optimal: Pre‑order DFS
# ──────────────────────────────────────────────
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split(","))

        def dfs():
            val = next(tokens)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# ──────────────────────────────────────────────
# Alternative: BFS (level‑order) serialization
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class CodecBFS:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("N")
        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        tokens = data.split(",")
        root = TreeNode(int(tokens[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if tokens[i] != "N":
                node.left = TreeNode(int(tokens[i]))
                queue.append(node.left)
            i += 1
            if tokens[i] != "N":
                node.right = TreeNode(int(tokens[i]))
                queue.append(node.right)
            i += 1
        return root
