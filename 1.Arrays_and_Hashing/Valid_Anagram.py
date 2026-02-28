"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s.

Key Intuition:
    Two strings are anagrams iff they share the exact same character
    frequencies. Counter comparison does this in one pass.

Complexity (Optimal):
    Time:  O(n)  — n = len(s) + len(t)
    Space: O(1)  — at most 26 lowercase letters
"""

from collections import Counter


# ──────────────────────────────────────────────
# Optimal: Counter comparison
# ──────────────────────────────────────────────
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# ──────────────────────────────────────────────
# Alternative: Manual frequency array (no imports)
# Time O(n) · Space O(1)
# ──────────────────────────────────────────────
class SolutionManual:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for a, b in zip(s, t):
            count[ord(a) - ord('a')] += 1
            count[ord(b) - ord('a')] -= 1
        return all(c == 0 for c in count)


# ──────────────────────────────────────────────
# Alternative: Sorting
# Time O(n log n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionSort:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
