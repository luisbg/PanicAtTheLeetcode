"""
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
"""

import heapq

class Solution(object):
    def HeavyKSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        heap = []
        for u in nums1:
            for v in nums2:
                heapq.heappush(heap, [u + v, u, v])

        ans = []
        while len(ans) < k:
            tmp = heapq.heappop(heap)
            ans.append([tmp[1], tmp[2]])
        return ans
