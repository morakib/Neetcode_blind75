"""
54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/

Given an m × n matrix, return all elements in spiral order.

Key Intuition:
    Maintain four boundaries (top, bottom, left, right). Traverse:
    left→right along top, top→bottom along right, right→left along
    bottom, bottom→top along left. Shrink boundaries after each pass.

Complexity (Optimal):
    Time:  O(m · n)
    Space: O(1)  — ignoring output
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Layer‑by‑layer with boundaries
# ──────────────────────────────────────────────
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse right
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # Traverse down
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            # Traverse left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            # Traverse up
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result
