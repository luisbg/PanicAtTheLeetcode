class Solution(object):
    def bruteForceSmallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        ans = [0] * n
        for i, x in enumerate(nums):
            for y in nums:
                if x > y:
                    ans[i] += 1
        
        return ans

    def smallerNumbersThanCurrent(self, nums):
        pairs = list(enumerate(nums))
        pairs.sort(key=lambda p: p[1])

        smaller_count = {}
        prev_val = None

        for sorted_index, (orig_index, val) in enumerate(pairs):
            if val not in smaller_count:
                smaller_count[val] = sorted_index

        return [smaller_count[val] for val in nums]
