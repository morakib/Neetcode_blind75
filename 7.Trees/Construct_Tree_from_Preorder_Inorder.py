"""
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given preorder and inorder traversal arrays, reconstruct the tree.

Key Intuition:
    The first element of preorder is the root. Find that root's index
    in inorder — everything to the left is the left subtree, everything
    to the right is the right subtree. Recurse with the appropriate slices.
    Use a hash map for O(1) index lookups in inorder.

Complexity (Optimal):
    Time:  O(n)
    Space: O(n)
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ──────────────────────────────────────────────
# Optimal: Recursive with index map
# ──────────────────────────────────────────────
class Solution:
    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(lo, hi):
            if lo > hi:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = inorder_idx[root_val]
            root.left = build(lo, mid - 1)
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)


# ──────────────────────────────────────────────
# Alternative: Array slicing (cleaner but O(n²) due to slicing)
# Time O(n²) · Space O(n²)
# ──────────────────────────────────────────────
class SolutionSlice:
    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
