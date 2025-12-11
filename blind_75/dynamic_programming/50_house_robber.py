"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        # edge cases
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])

        # run through houses and store max money up to i
        dp = [0] * length

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, length):
            # if we rob, don't add dp[i-1]
            rob = nums[i] + dp[i - 2]
            # if we skip then use cash up to dp[i-1]
            skip = dp[i - 1]
            dp[i] = max(rob, skip)

        return dp[-1]
