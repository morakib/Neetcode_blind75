"""
271. Encode and Decode Strings (LeetCode Premium / LintCode 659)
https://leetcode.com/problems/encode-and-decode-strings/

Design an algorithm to encode a list of strings to a single string and
decode it back to the original list.

Key Intuition:
    Prefix each string with its length and a delimiter (e.g. "4#word").
    This avoids any escaping issues because the length tells you exactly
    how many characters to consume.

Complexity:
    Time:  O(n) for both encode and decode — n = total chars across all strings
    Space: O(n)
"""

from typing import List


class Codec:
    # ──────────────────────────────────────────
    # Optimal: Length‑prefixed encoding
    # ──────────────────────────────────────────
    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = s.index('#', i)          # find delimiter
            length = int(s[i:j])          # parse length
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return result


# ──────────────────────────────────────────────
# Alternative: Escaping‑based approach
# Use a special separator (e.g. "/;") and escape any "/" in the
# original strings with "//". Decode by splitting and un‑escaping.
# More error‑prone; length‑prefix is preferred in interviews.
# ──────────────────────────────────────────────
class CodecEscape:
    def encode(self, strs: List[str]) -> str:
        return '/;'.join(s.replace('/', '//') for s in strs)

    def decode(self, s: str) -> List[str]:
        # This simplified version has edge‑case issues —
        # length‑prefix is strictly better.
        parts = s.split('/;')
        return [p.replace('//', '/') for p in parts]
