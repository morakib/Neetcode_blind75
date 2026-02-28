"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/

Given a reference to a node in a connected undirected graph, return a
deep copy (clone) of the graph.

Key Intuition:
    Use a hash map {original_node: cloned_node} to avoid revisiting
    and to handle cycles. BFS or DFS — whenever you encounter a neighbor,
    either clone it (if new) or reuse the existing clone.

Complexity (Optimal):
    Time:  O(V + E)
    Space: O(V)
"""

from typing import Optional
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# ──────────────────────────────────────────────
# Optimal: BFS
# ──────────────────────────────────────────────
class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        clones = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clones[cur].neighbors.append(clones[neighbor])

        return clones[node]


# ──────────────────────────────────────────────
# Alternative: DFS recursive
# Time O(V + E) · Space O(V)
# ──────────────────────────────────────────────
class SolutionDFS:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        clones = {}

        def dfs(cur):
            if cur in clones:
                return clones[cur]
            clone = Node(cur.val)
            clones[cur] = clone
            for neighbor in cur.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)
