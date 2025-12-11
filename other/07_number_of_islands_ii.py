"""
You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent = [-1] * (m * n)   # -1 means water
        count = 0
        ans = []

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] # path compression
                x = parent[x]
            return x

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return False
            parent[ry] = rx
            return True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r, c in positions:
            idx = r * n + c # 1D index mapping
            if parent[idx] != -1:
                # already land
                ans.append(count)
                continue

            parent[idx] = idx
            count += 1 # assume new land, reduce later if connected

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nidx = nr * n + nc
                    if parent[nidx] != -1: # neighbour is land
                        if union(idx, nidx):
                            count -= 1
            ans.append(count)

        return ans
