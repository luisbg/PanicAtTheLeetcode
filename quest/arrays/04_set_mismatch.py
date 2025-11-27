"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        seen = [0] * n   # seen[0] counts number 1, seen[1] counts number 2, ...
    
        # Count occurrences
        for x in nums:
            seen[x - 1] += 1

        dup = missing = -1

        # Find the one that appears twice and the one that is missing
        for i, count in enumerate(seen):
            if count == 2:
                dup = i + 1
            elif count == 0:
                missing = i + 1

        return [dup, missing]
