"""
371. Sum of Two Integers
https://leetcode.com/problems/sum-of-two-integers/

Calculate the sum of two integers a and b without using + or -.

Key Intuition:
    XOR gives the sum without carries. AND + left shift gives the carries.
    Repeat until there are no carries. In Python, integers are arbitrary‑
    precision, so mask to 32 bits to simulate overflow.

Complexity (Optimal):
    Time:  O(1)  — at most 32 iterations
    Space: O(1)
"""


# ──────────────────────────────────────────────
# Optimal: Bit manipulation (32‑bit simulation)
# ──────────────────────────────────────────────
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF   # 32-bit mask
        MAX  = 0x7FFFFFFF   # max positive 32-bit int

        while b & MASK:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # If b is 0 (no more carry), return a masked to 32 bits.
        # Handle negative numbers: if a > MAX, it's negative in 32-bit.
        a = a & MASK
        return a if a <= MAX else ~(a ^ MASK)


# ──────────────────────────────────────────────
# Alternative: Recursive version
# Same logic, recursive form
# ──────────────────────────────────────────────
class SolutionRecursive:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX  = 0x7FFFFFFF

        if b == 0:
            return a if a <= MAX else ~(a ^ MASK)

        return self.getSum((a ^ b) & MASK, ((a & b) << 1) & MASK)
