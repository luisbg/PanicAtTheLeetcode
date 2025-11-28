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
        for u in range(min(k, len(nums1))):
            for v in range(min(k, len(nums2))):
                heapq.heappush(heap, (nums1[u] + nums2[v], nums1[u], nums2[v]))

        ans = []
        while len(ans) < k:
            tmp = heapq.heappop(heap)
            ans.append([tmp[1], tmp[2]])
        return ans

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k == 0:
            return []

        n1, n2 = len(nums1), len(nums2)
        heap = []
        ans = []

        # Seed heap with (nums1[i], nums2[0]) for i in [0, min(k, n1) )
        for i in range(min(k, n1)):
            # (sum, index in nums1, index in nums2)
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while heap and len(ans) < k:
            s, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])

            # Move to next in nums2 for this i
            if j + 1 < n2:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return ans
