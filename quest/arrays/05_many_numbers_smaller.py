class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
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
