"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""

class Solution(object):
    def bruteForceSmallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        ans = [0] * n
        for i, x in enumerate(nums):
            for y in nums:
                if x > y:
                    ans[i] += 1
        
        return ans

    def smallerNumbersThanCurrent(self, nums):
        pairs = list(enumerate(nums))
        pairs.sort(key=lambda p: p[1])

        smaller_count = {}
        prev_val = None

        for sorted_index, (orig_index, val) in enumerate(pairs):
            if val not in smaller_count:
                smaller_count[val] = sorted_index

        return [smaller_count[val] for val in nums]
