"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution(object):
    def slowLongestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # add all nums to a set to have O(1) checks
        num_set = set(nums)

        # go through all nums and check if n - 1 is in the set
        # repeat counting sequences
        longest = 0
        for n in nums:
            seq = 1
            i = n
            while i - 1 in num_set:
                i -= 1
                seq += 1

            if seq > longest:
                longest = seq

        return longest
