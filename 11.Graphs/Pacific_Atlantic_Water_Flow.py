"""
417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/

Given an m × n island height map, return all cells from which water can
flow to both the Pacific and Atlantic oceans.

Key Intuition:
    Instead of flowing *from* every cell (expensive), start from the ocean
    borders and BFS/DFS *inward* (reverse flow: go to cells ≥ current).
    Cells reachable from both oceans are the answer.

Complexity (Optimal):
    Time:  O(m · n)
    Space: O(m · n)
"""

from typing import List
from collections import deque


# ──────────────────────────────────────────────
# Optimal: Reverse BFS from both oceans
# ──────────────────────────────────────────────
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def bfs(starts, reachable):
            queue = deque(starts)
            reachable.update(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                            (nr, nc) not in reachable and
                            heights[nr][nc] >= heights[r][c]):
                        reachable.add((nr, nc))
                        queue.append((nr, nc))

        # Pacific: top row + left col
        pac_starts = ([(0, c) for c in range(cols)] +
                      [(r, 0) for r in range(rows)])
        # Atlantic: bottom row + right col
        atl_starts = ([(rows - 1, c) for c in range(cols)] +
                      [(r, cols - 1) for r in range(rows)])

        bfs(pac_starts, pacific)
        bfs(atl_starts, atlantic)

        return [[r, c] for r, c in pacific & atlantic]


# ──────────────────────────────────────────────
# Alternative: DFS version
# Time O(m · n) · Space O(m · n)
# ──────────────────────────────────────────────
class SolutionDFS:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, reachable, prev_height):
            if ((r, c) in reachable or r < 0 or r >= rows or
                    c < 0 or c >= cols or heights[r][c] < prev_height):
                return
            reachable.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, reachable, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        return [[r, c] for r, c in pacific & atlantic]
