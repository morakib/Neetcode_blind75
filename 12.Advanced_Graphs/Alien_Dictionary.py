"""
269. Alien Dictionary (Premium)
https://leetcode.com/problems/alien-dictionary/

Given a sorted list of words in an alien language, derive the order
of characters. Return "" if the order is invalid.

Key Intuition:
    Compare adjacent words to extract ordering constraints (edges in a
    directed graph). Then topological sort (BFS — Kahn's) to produce the
    character order. If a cycle exists, the order is invalid.

Complexity (Optimal):
    Time:  O(C)  — C = total characters across all words
    Space: O(1)  — at most 26 nodes/edges (bounded alphabet)
"""

from typing import List
from collections import defaultdict, deque


# ──────────────────────────────────────────────
# Optimal: BFS topological sort
# ──────────────────────────────────────────────
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Initialize graph with all unique characters
        graph = defaultdict(set)
        in_degree = {ch: 0 for word in words for ch in word}

        # Step 2: Build edges from adjacent word comparisons
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Invalid: prefix comes after longer word (e.g. "abc" before "ab")
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break  # only the first difference matters

        # Step 3: Topological sort (Kahn's)
        queue = deque(ch for ch in in_degree if in_degree[ch] == 0)
        result = []

        while queue:
            ch = queue.popleft()
            result.append(ch)
            for neighbor in graph[ch]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If not all characters are in result → cycle
        if len(result) != len(in_degree):
            return ""
        return "".join(result)


# ──────────────────────────────────────────────
# Alternative: DFS topological sort with cycle detection
# Time O(C) · Space O(1)
# ──────────────────────────────────────────────
class SolutionDFS:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        in_degree = {ch: 0 for word in words for ch in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        # DFS-based topological sort
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {ch: WHITE for ch in in_degree}
        order = []

        def dfs(ch):
            color[ch] = GRAY
            for neighbor in graph[ch]:
                if color[neighbor] == GRAY:
                    return False  # cycle
                if color[neighbor] == WHITE and not dfs(neighbor):
                    return False
            color[ch] = BLACK
            order.append(ch)
            return True

        for ch in in_degree:
            if color[ch] == WHITE:
                if not dfs(ch):
                    return ""

        return "".join(reversed(order))
