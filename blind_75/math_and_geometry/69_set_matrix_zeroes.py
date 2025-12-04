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

    def fixedMemSizeSetZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # Check if first row has any zeros
        first_row_zero = False
        for x in range(num_cols):
            if matrix[0][x] == 0:
                first_row_zero = True
                break

        # Check if first column has any zeros
        first_col_zero = False
        for y in range(num_rows):
            if matrix[y][0] == 0:
                first_col_zero = True
                break

        # find cols and rows with zeroes
        # use first row and first column as markers
        for y in range(1, num_rows):
            for x in range(1, num_cols):
                if matrix[y][x] == 0:
                    matrix[y][0] = 0
                    matrix[0][x] = 0

        # Zero out rows based on markers in first column
        for y in range(1, num_rows):
            if matrix[y][0] == 0:
                for x in range(1, num_cols):
                    matrix[y][x] = 0

        # Zero out columns based on markers in first row
        for x in range(1, num_cols):
            if matrix[0][x] == 0:
                for y in range(1, num_rows):
                    matrix[y][x] = 0

        # Finally handle the first row if needed
        if first_row_zero:
            for x in range(num_cols):
                matrix[0][x] = 0

        # Finally handle the first column if needed
        if first_col_zero:
            for y in range(num_rows):
                matrix[y][0] = 0
