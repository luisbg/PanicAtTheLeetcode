class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i * 2] = nums[i]
            ans[i * 2 + 1] = nums[i + n]

        return ans
