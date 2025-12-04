"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32-bit mask (all 1s for lower 32 bits)
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        # work with 32-bit representations of a and b
        a &= MASK
        b &= MASK

        # iterate until there's no carry
        while b != 0:
            # sum without carry
            s = (a ^ b) & MASK
            # carry (shifted left)
            carry = ((a & b) << 1) & MASK

            a, b = s, carry

        # if a is within positive range, return as is
        if a <= MAX_INT:
            return a
        # if a is negative in 32-bit, convert from two's complement
        return ~(a ^ MASK)
