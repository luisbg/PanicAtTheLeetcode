class Solution(object):
    def raw_findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ones = 0
        tmp = 0

        for x in nums:
            if x == 1:
                tmp += 1
                if tmp > ones:
                    ones = tmp
            else:
                tmp = 0

        return ones

    def findMaxConsecutiveOnes(self, nums):
        ones = 0
        tmp = 0

        for x in nums:
            if x == 1:
                tmp += 1
                ones = max(ones, tmp)
            else:
                tmp = 0

        return ones
