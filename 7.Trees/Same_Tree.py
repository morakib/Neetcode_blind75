"""
100. Same Tree
https://leetcode.com/problems/same-tree/

Given the roots of two binary trees, check if they are structurally
identical and have the same node values.

Key Intuition:
    Two trees are the same if their roots match and their left and right
    subtrees are recursively the same. Both being None is the base "equal" case.

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


# ──────────────────────────────────────────────
# Alternative: BFS iterative
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionBFS:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        return True
