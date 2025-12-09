"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""

        # find shortest string
        shortest = 201
        for s in strs:
            if len(s) < shortest:
                shortest = len(s)

        # compare all strings until there is a difference
        for i in range(0, shortest):
            first = strs[0][i]
            diff = False

            for s in range(1, len(strs)):
                if strs[s][i] != first:
                    diff = True

            # if prefix doesn't match, we are done
            if diff:
                break
            else:
                # if it does match, add it to the answer string
                ans += first

        return ans
