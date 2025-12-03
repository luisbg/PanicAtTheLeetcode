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

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # add all nums into a set for quick checking
        num_set = set(nums)
        triplet_values = []

        # add all values to a tuple list (value, index)
        # and sort it
        num_idx = []
        for i, n in enumerate(nums):
            num_idx.append((n, i))
        num_idx.sort()

        # set every num as target
        for target in num_idx:
            start = 0
            end = len(nums) - 1

            while start < end:
                res = -num_idx[start][0] - num_idx[end][0]
                if res == target[0]:
                    if (target[1] != num_idx[start][1] and
                        target[1] != num_idx[end][1]):
                        # found one
                        triplet_v = [target[0], num_idx[start][0], num_idx[end][0]]

                        # avoid duplicate triplets
                        triplet_v.sort()
                        if triplet_v not in triplet_values:
                            triplet_values.append(triplet_v)

                    start += 1
                    end -= 1
                elif res > target[0]:
                    start += 1
                else:
                    end -= 1

        return triplet_values

    def cleanerThreeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # If this is the same as the previous value, skip to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                s = nums[left] + nums[right]

                if s == target:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates on the left
                    left_val = nums[left]
                    while left < right and nums[left] == left_val:
                        left += 1

                    # Skip duplicates on the right
                    right_val = nums[right]
                    while left < right and nums[right] == right_val:
                        right -= 1

                elif s < target:
                    left += 1
                else:
                    right -= 1

        return res
