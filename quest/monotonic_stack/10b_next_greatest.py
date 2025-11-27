"""
Given an array nums of length n, for each index i find the next greater element to its right:
the first nums[j] with j > i and nums[j] > nums[i].
If there is no next greater element, use -1.

Return an array ans where ans[i] is the next greater element of nums[i].

Example:
nums = [2, 1, 2, 4, 3]
ans  = [4, 2, 4, -1, -1]
"""

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [-1] * n
        stack = []  # will store indices

        # Walk from right to left
        for i in range(n - 1, -1, -1):
            # Pop indices whose values are <= current value
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            # If there is something left, it's the next greater
            if stack:
                ans[i] = nums[stack[-1]]  # value, not index

            # Current index becomes a candidate for elements to the left
            stack.append(i)

        return ans
