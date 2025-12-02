"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # create a dictionary
        count = {}

        # track counts of each number in nums
        # in negative since Python's heap is minHeap
        for n in nums:
            if n in count:
                count[n] -= 1
            else:
                count[n] = -1

        # convert dictionary to tuple heap
        h = []
        for key in count:
            heapq.heappush(h, (count[key], key))

        # make a list sized k of top seen elements
        ans = []
        for _ in range(k):
            tmp = heapq.heappop(h)
            ans.append(tmp[1])

        return ans

    # Use a k-sized heap to store less
    def betterMemoryTopKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # create a dictionary
        count = {}

        # track counts of each number in nums
        # in negative since Python's heap is minHeap
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        # convert dictionary to tuple heap
        h = []
        for key in count:
            heapq.heappush(h, (count[key], key))

            # keep heap size at most k
            if len(h) > k:
                heapq.heappop(h) # remove smallest frequency

        # make a list from k sized heap
        ans = []
        for (count, num) in h:
            ans.append(num)

        return ans
