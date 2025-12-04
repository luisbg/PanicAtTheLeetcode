"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Transpose in-place: matrix[i][j] <-> matrix[j][i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 1 2 3      1 4 7
        # 4 5 6  ->  2 5 8
        # 7 8 9      3 6 9

        # Reverse each row in-place
        for i in range(n):
            matrix[i].reverse()

        # 1 4 7      7 4 1
        # 2 5 8  ->  8 5 2
        # 3 6 9      9 6 3
