"""
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

Given a string s and an integer k, you can replace at most k characters.
Return the length of the longest substring containing the same letter.

Key Intuition:
    In any valid window, (window_length − count_of_most_frequent_char) ≤ k.
    Expand right; when the condition breaks, shrink left. You don't need
    to decrement max_freq when shrinking because only a *larger* max_freq
    can ever produce a longer answer.

Complexity (Optimal):
    Time:  O(n)
    Space: O(1)  — at most 26 letter counts
"""


# ──────────────────────────────────────────────
# Optimal: Sliding window
# ──────────────────────────────────────────────
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        max_freq = 0
        result = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])

            # Window is invalid: more replacements needed than k
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result


# ──────────────────────────────────────────────
# Alternative: Binary search on answer length + sliding window check
# Time O(n log n) · Space O(1)
# For each candidate length, slide a window and check feasibility.
# ──────────────────────────────────────────────
class SolutionBinarySearch:
    def characterReplacement(self, s: str, k: int) -> int:
        def can_make(length: int) -> bool:
            count = {}
            for r in range(len(s)):
                count[s[r]] = count.get(s[r], 0) + 1
                if r >= length:
                    count[s[r - length]] -= 1
                    if count[s[r - length]] == 0:
                        del count[s[r - length]]
                if r >= length - 1:
                    if length - max(count.values()) <= k:
                        return True
            return False

        lo, hi, ans = 1, len(s), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_make(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
