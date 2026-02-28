"""
323. Number of Connected Components in an Undirected Graph (Premium)
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Given n nodes (0 to n-1) and a list of edges, return the number of
connected components.

Key Intuition:
    Classic Union‑Find: start with n components. For each edge, union
    the two nodes — each successful union reduces the component count by 1.

Complexity (Optimal – Union‑Find):
    Time:  O(E · α(n)) ≈ O(E)
    Space: O(n)
"""

from typing import List
from collections import defaultdict, deque


# ──────────────────────────────────────────────
# Optimal: Union‑Find (Disjoint Set Union)
# ──────────────────────────────────────────────
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        components = n
        for a, b in edges:
            if union(a, b):
                components -= 1
        return components


# ──────────────────────────────────────────────
# Alternative: BFS/DFS
# Time O(V + E) · Space O(V + E)
# ──────────────────────────────────────────────
class SolutionBFS:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        count = 0

        for node in range(n):
            if node not in visited:
                count += 1
                queue = deque([node])
                visited.add(node)
                while queue:
                    cur = queue.popleft()
                    for neighbor in graph[cur]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        return count
