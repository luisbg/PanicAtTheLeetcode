"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution(object):
    def slowContainsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                return True

        return False

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # store seen values in hashset
        seen = set()

        # check if value is already in set
        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        # if no clashes, no duplicates
        return False
