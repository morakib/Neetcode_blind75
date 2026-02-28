"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Given an array prices where prices[i] is the price on the i‑th day,
maximize profit from one buy and one sell (buy before sell).

Key Intuition:
    Track the minimum price seen so far. At each day, the best profit
    you could make by selling today is (price − min_so_far). Keep the
    running maximum of that profit.

Complexity (Optimal):
    Time:  O(n)
    Space: O(1)
"""

from typing import List


# ──────────────────────────────────────────────
# Optimal: One‑pass, track min price
# ──────────────────────────────────────────────
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


# ──────────────────────────────────────────────
# Alternative: Sliding‑window / two‑pointer view
# Time O(n) · Space O(1)
# Same idea expressed with left (buy) and right (sell) pointers
# ──────────────────────────────────────────────
class SolutionTwoPointer:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r   # found a new minimum
            r += 1
        return max_profit
