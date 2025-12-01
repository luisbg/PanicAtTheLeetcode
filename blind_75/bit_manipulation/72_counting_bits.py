"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""

class Solution(object):
    def numberOfBits(self, n):
        count = 0
        while n:
            n &= n - 1   # clear the lowest set bit
            count += 1
        return count

    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # start array
        ans = [0]

        # iterate from 1 to n
        for x in range(1, n + 1):
            # add number of 1s for each int
            ans.append(self.numberOfBits(x))

        return ans
