"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without
repeating characters.

Key Intuition:
    Expand a sliding window to the right. When a duplicate is found,
    shrink from the left until all characters in the window are unique.
    A set tracks the current window's characters.

Complexity (Optimal):
    Time:  O(n)
    Space: O(min(n, m))  — m = size of the character set
"""


# ──────────────────────────────────────────────
# Optimal: Sliding window with a set
# ──────────────────────────────────────────────
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest = max(longest, r - l + 1)
        return longest


# ──────────────────────────────────────────────
# Alternative: Sliding window with last‑seen index map (jump left pointer)
# Time O(n) · Space O(min(n, m))
# Slightly faster because left pointer can jump instead of sliding.
# ──────────────────────────────────────────────
class SolutionMap:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = 0
        longest = 0
        for r, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= l:
                l = last_seen[ch] + 1
            last_seen[ch] = r
            longest = max(longest, r - l + 1)
        return longest
