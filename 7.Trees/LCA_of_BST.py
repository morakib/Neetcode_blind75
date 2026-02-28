"""
235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a BST, find the lowest common ancestor of two given nodes.

Key Intuition:
    Exploit BST ordering: if both nodes are smaller, go left; if both
    are larger, go right. The first node where they *split* (one on
    each side or one equals current) is the LCA.

Complexity (Optimal):
    Time:  O(h)  — h = height of tree
    Space: O(1)  — iterative
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ──────────────────────────────────────────────
# Optimal: Iterative
# ──────────────────────────────────────────────
class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur


# ──────────────────────────────────────────────
# Alternative: Recursive
# Time O(h) · Space O(h)
# ──────────────────────────────────────────────
class SolutionRecursive:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
