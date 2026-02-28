"""
207. Course Schedule
https://leetcode.com/problems/course-schedule/

There are numCourses courses (0 to numCourses-1) and prerequisites.
Return true if you can finish all courses (no cycle in the DAG).

Key Intuition:
    This is cycle detection in a directed graph. BFS topological sort
    (Kahn's algorithm): start from nodes with in‑degree 0; if you can
    process all nodes, there's no cycle.

Complexity (Optimal):
    Time:  O(V + E)
    Space: O(V + E)
"""

from typing import List
from collections import deque, defaultdict


# ──────────────────────────────────────────────
# Optimal: BFS topological sort (Kahn's algorithm)
# ──────────────────────────────────────────────
class Solution:
    def canFinish(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        visited = 0

        while queue:
            node = queue.popleft()
            visited += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return visited == numCourses


# ──────────────────────────────────────────────
# Alternative: DFS cycle detection
# Time O(V + E) · Space O(V + E)
# ──────────────────────────────────────────────
class SolutionDFS:
    def canFinish(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 0 = unvisited, 1 = in current path, 2 = fully processed
        state = [0] * numCourses

        def has_cycle(node):
            if state[node] == 1:
                return True   # back edge → cycle
            if state[node] == 2:
                return False  # already processed
            state[node] = 1
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            state[node] = 2
            return False

        return not any(has_cycle(i) for i in range(numCourses))
