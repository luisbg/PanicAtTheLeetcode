"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
             return node

        # create new node
        # create map of remembered clones
        clones = {}
        clones[node] = Node(node.val)

        stack = []
        stack.append(node)

        # iterate down the graph
        while stack:
            curr = stack.pop()
            for n in curr.neighbors:
                if n not in clones:
                    # add neighbors to visit later
                    stack.append(n)

                    # copy neighbor
                    clones[n] = Node(n.val)
                    # set it as neighbor of new node
                clones[curr].neighbors.append(clones[n])

        return clones[node]
