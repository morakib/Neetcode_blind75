"""
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given strings s and t, return the minimum window in s that contains
every character of t (including duplicates). Return "" if no such window.

Key Intuition:
    Use a sliding window: expand right to satisfy the requirement, then
    shrink left to minimize the window. Track how many unique characters
    still need to be fulfilled ("need" counter) vs. how many are already
    satisfied ("have" counter).

Complexity (Optimal):
    Time:  O(|s| + |t|)
    Space: O(|s| + |t|)
"""

from collections import Counter


# ──────────────────────────────────────────────
# Optimal: Sliding window with two frequency maps
# ──────────────────────────────────────────────
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count_t = Counter(t)
        required = len(count_t)  # unique chars we need

        window = {}
        have = 0        # how many unique chars meet the required count
        l = 0
        res, res_len = [-1, -1], float('inf')

        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in count_t and window[ch] == count_t[ch]:
                have += 1

            while have == required:
                # Update result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                # Shrink from the left
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]: res[1] + 1] if res_len != float('inf') else ""


# ──────────────────────────────────────────────
# Alternative: Optimized with filtered s (skip irrelevant chars)
# Time O(|s| + |t|) but faster constant when |s| >> |t|
# ──────────────────────────────────────────────
class SolutionFiltered:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count_t = Counter(t)
        required = len(count_t)

        # Only keep characters in s that are in t, with their original indices
        filtered = [(i, ch) for i, ch in enumerate(s) if ch in count_t]

        window = {}
        have = 0
        l = 0
        res, res_len = [-1, -1], float('inf')

        for r in range(len(filtered)):
            ch = filtered[r][1]
            window[ch] = window.get(ch, 0) + 1

            if window[ch] == count_t[ch]:
                have += 1

            while have == required:
                start = filtered[l][0]
                end = filtered[r][0]
                if (end - start + 1) < res_len:
                    res = [start, end]
                    res_len = end - start + 1

                left_ch = filtered[l][1]
                window[left_ch] -= 1
                if window[left_ch] < count_t[left_ch]:
                    have -= 1
                l += 1

        return s[res[0]: res[1] + 1] if res_len != float('inf') else ""
