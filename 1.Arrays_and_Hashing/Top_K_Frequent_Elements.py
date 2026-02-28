"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent
elements. Answer may be in any order.

Key Intuition:
    Bucket sort by frequency: index = frequency, value = list of numbers
    with that frequency. Walk buckets from high to low to collect top‑k
    in O(n) time — no heap needed.

Complexity (Optimal – Bucket Sort):
    Time:  O(n)
    Space: O(n)
"""

from typing import List
from collections import Counter
import heapq


# ──────────────────────────────────────────────
# Optimal: Bucket sort by frequency
# ──────────────────────────────────────────────
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # bucket[i] holds numbers that appear exactly i times
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        result = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result


# ──────────────────────────────────────────────
# Alternative: Min‑heap of size k
# Time O(n log k) · Space O(n)
# ──────────────────────────────────────────────
class SolutionHeap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
