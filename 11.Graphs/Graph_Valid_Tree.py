"""
261. Graph Valid Tree (Premium)
https://leetcode.com/problems/graph-valid-tree/

Given n nodes (0 to n-1) and a list of undirected edges, determine if
these edges form a valid tree.

Key Intuition:
    A valid tree must satisfy two conditions:
    1. Exactly n-1 edges (otherwise cycle or disconnected).
    2. All nodes are connected (single component).
    Union‑Find checks both: n-1 edges + no cycle during unions.

Complexity (Optimal):
    Time:  O(E · α(n)) ≈ O(E)
    Space: O(n)
"""

from typing import List
from collections import defaultdict


# ──────────────────────────────────────────────
# Optimal: Union‑Find
# ──────────────────────────────────────────────
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False  # quick check

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False  # cycle
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        return all(union(a, b) for a, b in edges)


# ──────────────────────────────────────────────
# Alternative: DFS — check connectivity and no cycle
# Time O(V + E) · Space O(V + E)
# ──────────────────────────────────────────────
class SolutionDFS:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)
        return len(visited) == n
