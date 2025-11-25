class Solution(object):
    def raw_shuffle(self, nums, n):
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

    def shuffle(self, nums, n):
        left = nums[:n]      # [x1, x2, ..., xn]
        right = nums[n:]     # [y1, y2, ..., yn]
        ans = []

        for x, y in zip(left, right):
            ans.append(x)
            ans.append(y)

        return ans
