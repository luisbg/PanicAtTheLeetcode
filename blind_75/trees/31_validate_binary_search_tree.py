"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys strictly less than the node's key.
    The right subtree of a node contains only nodes with keys strictly greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def validate(self, node, low, high):
        # empty subtree is valid
        if not node:
            return True

        # node value must be strictly between low and high
        if low is not None and node.val <= low:
            return False
        if high is not None and node.val >= high:
            return False

        # left subtree: values < node.val
        # right subtree: values > node.val
        return (self.validate(node.left, low, node.val) and
                self.validate(node.right, node.val, high))

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.validate(root, None, None)
