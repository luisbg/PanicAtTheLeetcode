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
