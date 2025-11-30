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
        # bruteforce
        # run two two loops trying all permutations
        for x, a in enumerate(nums):
            for y, b in enumerate(nums):
                if x != y and a + b == target:
                    return [x, y]

        return []
