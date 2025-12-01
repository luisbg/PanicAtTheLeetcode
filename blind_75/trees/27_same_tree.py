"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # base case and edge case
        if not p and not q:
            return True

        # not the same if shape isn't the same
        if p and not q or not p and q:
            return False

        # not the same if values are not the same
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def iterativeIsSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        queue = deque([(p, q)])

        while queue:
            n1, n2 = queue.popleft()

            # Both None: these subtrees match at this position
            if not n1 and not n2:
                continue

            # One is None or values differ: trees differ
            if not n1 or not n2 or n1.val != n2.val:
                return False

            # Enqueue children pairs
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))

        return True
