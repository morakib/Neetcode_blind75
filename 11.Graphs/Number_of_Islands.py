"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m × n 2D grid of '1's (land) and '0's (water), return the
number of islands.

Key Intuition:
    Each connected component of '1's is one island. BFS/DFS from every
    unvisited '1', marking cells as visited (sink them to '0'). Each
    new traversal start = one more island.

Complexity (Optimal):
    Time:  O(m · n)
    Space: O(m · n) worst case for BFS queue / DFS stack
"""

from typing import List
from collections import deque


# ──────────────────────────────────────────────
# Optimal: BFS
# ──────────────────────────────────────────────
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = '0'
            while queue:
                row, col = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    count += 1
        return count


# ──────────────────────────────────────────────
# Alternative: DFS recursive
# Time O(m · n) · Space O(m · n)
# ──────────────────────────────────────────────
class SolutionDFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count
