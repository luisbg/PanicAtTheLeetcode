"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            if n < 0:
                nums[i] = n * -1

        nums.sort()

        for i, n in enumerate(nums):
            nums[i] = n ** 2

        return nums
