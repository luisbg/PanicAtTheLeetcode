"""
Given two strings s and t, return true if t is an of s, and false otherwise.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # early exit if lenghts don't match
        if len(s) != len(t):
            return False

        # count letters in s in a dictionary
        letters = {}
        for l in s:
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1

        # subtract letters in t
        for l in t:
            if l in letters:
                letters[l] -= 1
            else:
                return False

        # all counts should be zero (sum matches subs)
        for k in letters:
            if letters[k] != 0:
                return False

        return True
