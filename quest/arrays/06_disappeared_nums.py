class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        ans = []
        for i in range(1, n + 1):
            found = False
            for v in nums:
                if i == v:
                    found = True
                    break

            if not found:
                ans.append(i)

        return ans
