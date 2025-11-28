"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False

        highest = 0
        idx_h = 0
        for i, a in enumerate(arr):
            if a > highest:
                highest = a
                idx_h = i

        if idx_h == 0:
            return False
        elif idx_h == n - 1:
            return False

        for a in range(1, idx_h + 1):
            if arr[a] <= arr[a - 1]:
                return False

        for a in range(n - 2, idx_h - 1, -1):
            if arr[a] <= arr[a + 1]:
                return False

        return True

    def onePassValidMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False

        i = 0

        # Walk up: strictly increasing
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # Peak can't be first or last
        if i == 0 or i == n - 1:
            return False

        # Walk down: strictly decreasing
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        # Must end exactly at the last index
        return i == n - 1
