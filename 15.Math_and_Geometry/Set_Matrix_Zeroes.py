"""
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/

Given an m × n matrix, if an element is 0, set its entire row and column
to 0. Do it in‑place.

Key Intuition:
    Use the first row and first column as markers. If matrix[i][j] == 0,
    set matrix[i][0] = 0 and matrix[0][j] = 0. Then make a second pass
    to zero out marked rows/columns. Handle the first row/col separately
    with boolean flags.

Complexity (Optimal):
    Time:  O(m · n)
    Space: O(1)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Use first row/col as markers
# ──────────────────────────────────────────────
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Mark zeros in first row/col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Handle first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


# ──────────────────────────────────────────────
# Alternative: Record zero positions with sets
# Time O(m · n) · Space O(m + n)
# ──────────────────────────────────────────────
class SolutionSets:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
