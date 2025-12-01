"""
Given a positive integer n, write a function that returns the number of in its binary representation (also known as the Hamming weight).
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        # until the number has no 1 bits
        while n > 0:
            # check if lsb is a 1
            if n % 2 == 1:
                count += 1

            # shift right by 1
            n = n >> 1

        return count
