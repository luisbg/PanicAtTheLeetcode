"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # get needle length
        nl = len(needle)

        # iterate from start to end - need length in haystack
        for i in range(len(haystack) - nl + 1):
            # looking for needle
            if haystack[i:i+nl] == needle:
                return i

        return -1
