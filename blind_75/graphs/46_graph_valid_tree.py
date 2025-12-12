"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
"""

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # valid tree is:
        # - no isolated nodes
        # - no separate clusters
        # - no cycles

        # no isolated nodes
        if n - 1 != len(edges):
            return False

        # no separate clusters
        # check via adjacency list
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # traverse starting from 0
        visited = set()
        stack = [0]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for neighbour in adj[node]:
                stack.append(neighbour)

        # did we visit all nodes?
        return len(visited) == n
