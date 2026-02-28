"""
48. Rotate Image
https://leetcode.com/problems/rotate-image/

Rotate an n × n 2D matrix 90 degrees clockwise in‑place.

Key Intuition:
    Transpose the matrix (swap rows ↔ columns), then reverse each row.
    Transpose + reverse = 90° clockwise rotation.

Complexity (Optimal):
    Time:  O(n²)
    Space: O(1)  — in‑place
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Transpose + reverse rows
# ──────────────────────────────────────────────
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for row in matrix:
            row.reverse()


# ──────────────────────────────────────────────
# Alternative: Four‑way swap (rotate groups of 4 cells)
# Time O(n²) · Space O(1)
# ──────────────────────────────────────────────
class SolutionFourWay:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                # Save top
                tmp = matrix[i][j]
                # left → top
                matrix[i][j] = matrix[n - 1 - j][i]
                # bottom → left
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                # right → bottom
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                # top → right
                matrix[j][n - 1 - i] = tmp
