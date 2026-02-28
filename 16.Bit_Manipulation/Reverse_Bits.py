"""
190. Reverse Bits
https://leetcode.com/problems/reverse-bits/

Reverse the bits of a 32‑bit unsigned integer.

Key Intuition:
    Extract the last bit of n, place it at the correct position in the
    result, shift n right. Repeat 32 times.

Complexity (Optimal):
    Time:  O(1)  — always 32 iterations
    Space: O(1)
"""


# ──────────────────────────────────────────────
# Optimal: Bit‑by‑bit reversal
# ──────────────────────────────────────────────
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result


# ──────────────────────────────────────────────
# Alternative: Divide and conquer (swap halves recursively)
# Time O(1) · Space O(1) — 5 operations on 32-bit word
# ──────────────────────────────────────────────
class SolutionDivideConquer:
    def reverseBits(self, n: int) -> int:
        n = ((n & 0xFFFF0000) >> 16) | ((n & 0x0000FFFF) << 16)
        n = ((n & 0xFF00FF00) >> 8)  | ((n & 0x00FF00FF) << 8)
        n = ((n & 0xF0F0F0F0) >> 4)  | ((n & 0x0F0F0F0F) << 4)
        n = ((n & 0xCCCCCCCC) >> 2)  | ((n & 0x33333333) << 2)
        n = ((n & 0xAAAAAAAA) >> 1)  | ((n & 0x55555555) << 1)
        return n


# ──────────────────────────────────────────────
# Pythonic
# ──────────────────────────────────────────────
class SolutionPythonic:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)
