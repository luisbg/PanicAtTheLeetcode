"""
You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

    let x be the sum of all elements currently in your array.
    choose index i, such that 0 <= i < n and set the value of arr at index i to x.
    You may repeat this procedure as many times as needed.

Return true if it is possible to construct the target array from arr, otherwise, return false.
"""

import heapq

class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        # Single element edge case
        if len(target) == 1:
            return target[0] == 1

        # Use negatives for max-heap
        total = sum(target)
        max_heap = [-n for n in target]
        heapq.heapify(max_heap)

        while True:
            max_val = -heapq.heappop(max_heap) # largest
            rest = total - max_val

            if max_val == 1 or rest == 1:
                return True

            if rest == 0 or max_val < rest:
                return False

            # using modulo to save us from doing `prev = max_val - rest` many many times if max_val is significantly bigger than rest
            prev = max_val % rest
            if prev == 0:
                return False

            total = rest + prev
            heapq.heappush(max_heap, -prev)
