"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # approach expects a sorted array
        snums = []
        for i, n in enumerate(nums):
            snums.append([n, i])
        snums.sort()

        # until we find the target
        # try beginning and end
        a = 0
        b = len(nums) - 1
        while a < b:
            s = snums[a][0] + snums[b][0]
            # if sum is too big, reduce right
            if s > target:
                b -= 1
            # if sum too small, increase left
            elif s < target:
                a += 1
            # else we found the target
            else:
                return [snums[a][1], snums[b][1]]

        # return empty array if we didn't find the target
        return []
