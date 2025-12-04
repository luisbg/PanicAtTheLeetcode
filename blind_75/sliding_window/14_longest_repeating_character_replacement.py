"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # sliding window
        # start with a small window at the left
        start = 0
        end = 1
        longest = 0
        while end < len(s):
            # find most common character and its count
            chars = {}
            for i in range(start, end + 1):
                if s[i] in chars:
                    chars[s[i]] += 1
                else:
                    chars[s[i]] = 1

            most_common = 0
            for c in chars:
                most_common = max(most_common, chars[c])

            window_size = end - start + 1
            if most_common + k >= window_size:
                end += 1
                longest = max(longest, window_size)
            else:
                start += 1

        return longest
