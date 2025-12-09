"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

class Solution(object):
    def slowSortedSquares(self, nums):
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

    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # start two pointers
        n = len(nums)
        left = 0
        right = n - 1
        ans = [0] * n
        pos = right

        # run from both ends using the biggest number first
        # update position from the end of the array downward
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans[pos] = nums[left] ** 2
                left += 1
            else:
                ans[pos] = nums[right] ** 2
                right -= 1
            pos -= 1

        return ans
