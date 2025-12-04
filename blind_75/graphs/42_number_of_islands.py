"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

class Solution(object):
    def clearIsland(self, grid, y, x):
        rows = len(grid)
        cols = len(grid[0])

        # validate y and x
        if y < 0 or y >= rows:
            return

        if x < 0 or x >= cols:
            return

        # if position is land change it and recursive over neighbours
        if grid[y][x] == "1":
            grid[y][x] = "0"
            self.clearIsland(grid, y - 1, x)
            self.clearIsland(grid, y + 1, x)
            self.clearIsland(grid, y, x - 1)
            self.clearIsland(grid, y, x + 1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        # iterate over the island
        for y in range(rows):
            for x in range(cols):
                # look for land
                if grid[y][x] == "1":
                    islands += 1
                    # recursively mark all neighbour land as water to not count it twice
                    self.clearIsland(grid, y, x)

        return islands
