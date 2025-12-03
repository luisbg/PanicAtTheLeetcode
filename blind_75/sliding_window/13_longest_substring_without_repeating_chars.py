"""
Given a string s, find the length of the longest without duplicate characters.
"""

class Solution(object):
    def slowLengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # two pointers
        start = 0
        end = 0
        longest = 0

        # run until end of substring is end of string
        while end < len(s):
            # check for duplicates
            sub = s[start:end + 1]
            if len(sub) == len(set(sub)):
                # if no duplicates move end
                end +=1
                longest = max(longest, len(sub))
            else:
                # we have duplicates, move start
                start += 1

            # start always needs to be left or end
            if end <= start:
                end += 1

        return longest

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # two pointers
        start = 0
        end = 0
        longest = 0
        dupes = set()

        # run until end of substring is end of string
        while end < len(s):
            # use set to check for duplicates
            if s[end] not in dupes:
                dupes.add(s[end])
                longest = max(longest, end - start + 1)

                # if no duplicates move end
                end += 1
            else:
                dupes.remove(s[start])
                # we have duplicates, move start
                start += 1

        return longest
