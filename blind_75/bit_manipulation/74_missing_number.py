"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

# Think about an operation where:
# combining a number with itself “cancels it out”, and
# combining with 0 gives you back the same number.

# That operation is:
# commutative (order doesn’t matter), and
# associative (you can regroup terms however you want).

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for n in range(1, len(nums) + 1):
            ans ^= nums[n - 1]
            ans ^= n

        return ans
