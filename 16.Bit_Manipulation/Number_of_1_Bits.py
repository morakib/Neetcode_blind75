"""
191. Number of 1 Bits (Hamming Weight)
https://leetcode.com/problems/number-of-1-bits/

Given a positive integer, return the number of set bits (1s) in its
binary representation.

Key Intuition:
    n & (n - 1) clears the lowest set bit. Repeat until n becomes 0;
    the number of iterations equals the number of 1 bits.

Complexity (Optimal):
    Time:  O(k) — k = number of set bits
    Space: O(1)
"""


# ──────────────────────────────────────────────
# Optimal: Brian Kernighan's trick
# ──────────────────────────────────────────────
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


# ──────────────────────────────────────────────
# Alternative: Check each bit
# Time O(32) = O(1) · Space O(1)
# ──────────────────────────────────────────────
class SolutionShift:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


# ──────────────────────────────────────────────
# Pythonic one-liner
# ──────────────────────────────────────────────
class SolutionBuiltin:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
