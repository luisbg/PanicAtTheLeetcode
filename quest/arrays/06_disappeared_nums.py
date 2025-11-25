class Solution(object):
    def slow_findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        ans = []
        for i in range(1, n + 1):
            found = False
            for v in nums:
                if i == v:
                    found = True
                    break

            if not found:
                ans.append(i)

        return ans

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        seen = set(nums) # set is a hashtable

        ans = []
        for i in range(1, n + 1):
            if i not in seen: # since its a table this is O(1)
                ans.append(i)

        return ans

    def fancyFindDisappearedNumbers(self, nums):
        """
        This solution uses no extra space (except answer array)
        :type nums: List[int]
        :rtype: List[int]
        """

        # First pass: mark seen numbers by making positions negative
        for v in nums:
            idx = abs(v) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Second pass: indices that remain positive were never marked
        ans = []
        for i, v in enumerate(nums):
            if v > 0:
                ans.append(i + 1)

        return ans
