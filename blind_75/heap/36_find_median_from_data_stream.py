"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""

import heapq

class MedianFinder(object):
    def __init__(self):
        # max-heap (as negatives) for lower half
        self.lower = []
        # min-heap for the upper half
        self.upper = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # push into lower (as negative, to make it a max-heap)
        if not self.lower or num <= -self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)

        # rebalance so that:
        # len(lower) == len(upper) or len(lower) == len(upper) + 1
        if len(self.lower) > len(self.upper) + 1:
            # move one from lower to upper
            val = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)
        elif len(self.upper) > len(self.lower):
            # move one from upper to lower
            val = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        total = len(self.lower) + len(self.upper)
        if total == 0:
            return 0.0

        # if odd, lower has one extra element
        if total % 2 == 1:
            return float(-self.lower[0])

        # if even, average of two middles
        return (-self.lower[0] + self.upper[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
