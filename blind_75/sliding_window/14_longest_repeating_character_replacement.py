"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

class Solution(object):
    def slowerCharacterReplacement(self, s, k):
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

            # increase window if most common + k is smaller than window
            # shrink if not
            window_size = end - start + 1
            if most_common + k >= window_size:
                end += 1
                longest = max(longest, window_size)
            else:
                start += 1

        return longest

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)  # char -> frequency in current window
        most_common = 0              # frequency of the most common char in window
        start = 0
        longest = 0

        for end in range(len(s)):
            # include s[end] in the window
            c = s[end]
            count[c] += 1
            most_common = max(most_common, count[c])

            window_size = end - start + 1

            # if we need more than k replacements, shrink from the left
            # changes needed = window_size - max_freq
            if window_size - most_common > k:
                count[s[start]] -= 1
                start += 1
                window_size = end - start + 1  # updated size after shrinking

            # window is valid here
            longest = max(longest, window_size)

        return longest
