"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # try to match word[idx:] starting from position (y, x).
        def traverseNeighbours(y, x, idx, visited):
            # ff we've matched all characters, success
            if idx == len(word):
                return True

            # bounds check
            if y < 0 or y >= rows or x < 0 or x >= cols:
                return False

            # already used this cell in current path
            if (y, x) in visited:
                return False

            # current cell must match current character
            if board[y][x] != word[idx]:
                return False

            # mark this cell as visited
            visited.add((y, x))

            # explore 4 neighbors: up, down, left, right
            if (traverseNeighbours(y - 1, x, idx + 1, visited) or
                traverseNeighbours(y + 1, x, idx + 1, visited) or
                traverseNeighbours(y, x - 1, idx + 1, visited) or
                traverseNeighbours(y, x + 1, idx + 1, visited)):
                return True

            # backtrack: unmark this cell
            visited.remove((y, x))
            return False

        # run through board looking for starting points
        rows = len(board)
        cols = len(board[0])

        for y in range(rows):
            for x in range(cols):
                if board[y][x] == word[0]:
                    if traverseNeighbours(y, x, 0, set()):
                        return True

        return False
