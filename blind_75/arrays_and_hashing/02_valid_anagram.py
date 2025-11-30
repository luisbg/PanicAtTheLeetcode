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
        if len(s) == len(t):
            return False

        # count letters in s in a dictionary
        s_dict = {}
        for l in s:
            if l in s_dict:
                s_dict[l] += 1
            else:
                s_dict[l] = 1
        # count letters in t in a dictionary
        t_dict = {}
        for l in t:
            if l in t_dict:
                t_dict[l] += 1
            else:
                t_dict[l] = 1

        # compare dictionaries
        if len(s_dict) != len(t_dict):
            return False

        for k in s_dict:
            if k not in t_dict or s_dict[k] != t_dict[k]:
                return False

        return True
