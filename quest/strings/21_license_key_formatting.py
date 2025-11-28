"""
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.
"""

class Solution(object):
    def arrayStyleLicenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        # Get string without dashes
        drop_dashes = []
        for c in s:
            if c != '-':
                drop_dashes.append(c)

        first = len(drop_dashes) % k

        i = 0
        ans = []

        # First block is smaller than k if needed
        if first > 0:
            while len(ans) < first:
                ans.append(drop_dashes[i].upper())
                i += 1
            ans.append('-')

        c = 0
        while i < len(drop_dashes):
            ans.append(drop_dashes[i].upper())
            i += 1
            c += 1
            if c == k:
                ans.append('-')
                c = 0

        if ans:
            ans.pop()

        return "".join(ans)
