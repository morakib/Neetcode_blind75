"""
39. Combination Sum
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target, return all
unique combinations where the chosen numbers sum to target. The same
number may be used unlimited times.

Key Intuition:
    Classic backtracking: at each step, either include the current
    candidate again (unlimited reuse) or move to the next one.
    Pruning: skip when remaining target < 0.

Complexity:
    Time:  O(n^(T/M))  — T = target, M = min candidate
    Space: O(T/M)      — max recursion depth
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: Backtracking
# ──────────────────────────────────────────────
class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        result = []

        def backtrack(start, combo, remaining):
            if remaining == 0:
                result.append(combo[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                # Pass i (not i+1) because we can reuse the same element
                backtrack(i, combo, remaining - candidates[i])
                combo.pop()

        backtrack(0, [], target)
        return result


# ──────────────────────────────────────────────
# Alternative: Backtracking with sorting + early termination
# Same time complexity, but prunes faster in practice.
# ──────────────────────────────────────────────
class SolutionSorted:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, combo, remaining):
            if remaining == 0:
                result.append(combo[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # early termination
                combo.append(candidates[i])
                backtrack(i, combo, remaining - candidates[i])
                combo.pop()

        backtrack(0, [], target)
        return result
