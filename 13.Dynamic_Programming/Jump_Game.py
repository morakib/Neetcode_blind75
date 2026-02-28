"""
55. Jump Game
https://leetcode.com/problems/jump-game/

Given an array nums where nums[i] is the max jump length from position i,
determine if you can reach the last index.

Key Intuition:
    Track the farthest index reachable so far. Walk left to right; if
    you can reach position i (i ≤ farthest), update farthest. If
    farthest ≥ last index at any point, return True.

Complexity (Optimal):
    Time:  O(n)
    Space: O(1)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Greedy — track farthest reachable
# ──────────────────────────────────────────────
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        return True


# ──────────────────────────────────────────────
# Alternative: Work backwards — track last good position
# Time O(n) · Space O(1)
# ──────────────────────────────────────────────
class SolutionBackward:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
