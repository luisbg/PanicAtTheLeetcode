"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""

class Solution(object):
    def heavyProductExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ln = len(nums)
        rtl = [0] * ln
        ltr = [0] * ln

        # get products right to left
        tmp = 1
        for n in range(ln - 1, -1, -1):
            tmp = tmp * nums[n]
            rtl[n] = tmp

        # then add products left to right
        tmp = 1
        for i, n in enumerate(nums):
            tmp = tmp * n
            ltr[i] = tmp

        # multiply products in each side of every index
        # we can assume len(nums) is always >= 2
        ans = [0] * ln
        for i in range(ln):
            if i == 0:
                ans[0] = rtl[1]
            elif i == ln - 1:
                ans[i] = ltr[i - 1]
            else:
                ans[i] = ltr[i - 1] * rtl[i + 1]

        return ans

    # O(1) space complexity
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ln = len(nums)
        ans = [1] * ln

        # First pass: prefix products (left to right)
        prefix = 1
        for i in range(ln):
            ans[i] = prefix
            prefix *= nums[i]

        # Second pass: suffix products (right to left)
        suffix = 1
        for i in range(ln - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
