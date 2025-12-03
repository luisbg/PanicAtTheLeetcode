"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution(object):
    def bruteForceThreeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # add all nums into a set for quick checking
        num_set = set(nums)
        triplet_values = []

        # try every pair
        for ix, x in enumerate(nums):
            for iy, y in enumerate(nums):
                # we need each item to be different index
                if ix != iy:
                    # look for num that would make a triplet
                    t = (x + y) * -1

                    # third is in the list
                    if t in num_set:
                        it = nums.index(t)
                        if it != ix and it != iy:
                            triplet_v = [x,y, t]

                            # avoid duplicate triplets
                            triplet_v.sort()
                            if triplet_v not in triplet_values:
                                triplet_values.append(triplet_v)

        return triplet_values
