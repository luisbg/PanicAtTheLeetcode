"""
Given an array of strings strs, group the together. You can return the answer in any order.
"""

from collections import defaultdict

class Solution(object):
    def slowGroupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        letter_counts = {} # dictionary tracking lettercounts
        seen = set() # set of seen indexes

        # go through all words in array
        # using the word as index store a letter count for all words
        for w in strs:
            lc = {}
            for l in w:
                if l in lc:
                    lc[l] += 1
                else:
                    lc[l] = 1
            letter_counts[w] = lc

        # go through all words
        for i, w in enumerate(strs):
            # if not seen already add to a new group
            if i not in seen:
                group = []
                group.append(w)
                seen.add(i)

                # use lettercounts to find and add anagrams to group
                for j, wb in enumerate(strs):
                    if j not in seen and letter_counts[w] == letter_counts[wb]:
                        group.append(wb)
                        seen.add(j)

                ans.append(group)

        return ans

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)

        # for all words in strs
        for s in strs:
            # count letters
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord('a')] += 1

            # use count as dictionary key with original word as count
            key = tuple(counts)

            # append matching counts
            groups[key].append(s)

        return list(groups.values())
