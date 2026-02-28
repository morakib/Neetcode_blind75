"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Given n non‑negative integers where each represents a vertical line,
find two lines that together with the x‑axis form a container that
holds the most water.

Key Intuition:
    Start with the widest container (left, right ends). The only way to
    potentially find a larger area is to move the *shorter* line inward,
    because moving the taller one can never increase the limiting height.

Complexity (Optimal):
    Time:  O(n)
    Space: O(1)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Two Pointers (greedy)
# ──────────────────────────────────────────────
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            max_water = max(max_water, w * h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water


# ──────────────────────────────────────────────
# Alternative: Brute force (for reference only — TLE on large inputs)
# Time O(n²) · Space O(1)
# ──────────────────────────────────────────────
class SolutionBrute:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                max_water = max(max_water, (j - i) * min(height[i], height[j]))
        return max_water
