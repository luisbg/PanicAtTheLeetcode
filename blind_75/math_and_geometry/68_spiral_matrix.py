"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # starting position
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        ans = []
        while top <= bottom and left <= right:
            # move right
            for x in range(left, right + 1):
                ans.append(matrix[top][x])
            # we’ve consumed this top row
            top += 1

            # move down
            for y in range(top, bottom + 1):
                ans.append(matrix[y][right])
            right -= 1

            # move left
            if top <= bottom:
                for x in range(right, left - 1, -1):
                    ans.append(matrix[bottom][x])
                bottom -= 1

            # move up
            if left <= right:
                for y in range(bottom, top - 1, -1):
                    ans.append(matrix[y][left])
                left += 1

        return ans
