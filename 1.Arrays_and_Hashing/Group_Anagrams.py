"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together.

Key Intuition:
    All anagrams share the same sorted‑character signature. Use that
    signature as a hash‑map key to bucket words together in one pass.

Complexity (Optimal):
    Time:  O(n · k log k)  — n strings of avg length k
    Space: O(n · k)
"""

from typing import List
from collections import defaultdict


# ──────────────────────────────────────────────
# Optimal: Sorted‑string key
# ──────────────────────────────────────────────
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            
            # sorted() always returns list( )
            #  s="eat" --> ['a' ,'e','t']

            # using tuple cause we need something Immutable 
            # as the key of list 
            # tuple is unchanged and Immutable 
            # list is mutable 

            groups[key].append(s)
        return list(groups.values()) 

        # group.values() returns only values not keys
        # and as the return type of the function is list
        # so at last converted into list 


# ──────────────────────────────────────────────
# Alternative: Character‑count tuple key (avoids sorting)
# Time O(n · k) · Space O(n · k)  — k bounded by 26 for lowercase
# ──────────────────────────────────────────────
class SolutionCount:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())
