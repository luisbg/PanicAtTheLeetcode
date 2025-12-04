"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # store columns with a zero
        change_cols = set()
        # store rows with a zero
        change_rows = set()

        # find cols and rows with zeroes
        for y in range(num_rows):
            for x in range(num_cols):
                if matrix[y][x] == 0:
                    change_cols.add(x)
                    change_rows.add(y)

        # set columns to zero
        for y in change_rows:
            for x in range(num_cols):
                matrix[y][x] = 0

        # set rows to zero
        for x in change_cols:
            for y in range(num_rows):
                matrix[y][x] = 0
