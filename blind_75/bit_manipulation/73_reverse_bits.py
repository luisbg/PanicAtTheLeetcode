"""
Reverse bits of a given 32 bits signed integer.
"""

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for _ in range(32):
            # Take the least significant bit of n
            bit = n & 1
            # Shift ans left and add this bit
            ans = (ans << 1) | bit
            # Shift n right to process the next bit
            n >>= 1
        return ans
