"""
Given the root of a binary tree, invert the tree, and return its root.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # base case is empty node
        if not root:
            return

        # flip left and right
        root.left, root.right = root.right, root.left

        # recurse over every node
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
