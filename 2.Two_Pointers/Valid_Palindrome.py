"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Given a string s, return true if it is a palindrome after converting to
lowercase and removing non‑alphanumeric characters.

Key Intuition:
    Use two pointers from the outside inward, skipping non‑alphanumeric
    characters and comparing case‑insensitively. No need to build a
    cleaned string first.

Complexity (Optimal):
    Time:  O(n)
    Space: O(1)
"""


# ──────────────────────────────────────────────
# Optimal: Two pointers, in‑place
# ──────────────────────────────────────────────
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


# ──────────────────────────────────────────────
# Alternative: Pythonic one‑liner (builds cleaned string)
# Time O(n) · Space O(n)
# ──────────────────────────────────────────────
class SolutionPythonic:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]
