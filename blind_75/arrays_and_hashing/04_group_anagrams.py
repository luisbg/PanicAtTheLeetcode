"""
Given an array of strings strs, group the together. You can return the answer in any order.
"""

class Solution(object):
    def isAnagram(self, a, b):
        # lengths should match
        if len(a) != len(b):
            return False

        # count letters in s in a dictionary
        letters = {}
        for l in a:
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1

        # subtract letters in t from dictionary
        for l in b:
            if l in letters:
                letters[l] -= 1
            else:
                return False

        # all counts should be zero (sum matches subs)
        for k in letters:
            if letters[k] != 0:
                return False

        return True

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        seen = [] # track seen indexes

        # go through all words in array
        for i, a in enumerate(strs):
            if i not in seen:
                group = []
                group.append(a)
                seen.append(i)

                # for each word find its anagrams and add them to seen list
                for j, b in enumerate(strs):
                    if j not in seen and self.isAnagram(a, b):
                        group.append(b)
                        seen.append(j)

                ans.append(group)

        return ans
