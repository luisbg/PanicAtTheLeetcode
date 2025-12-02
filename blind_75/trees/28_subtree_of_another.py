"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def treesMatch(self, a, b):
        # base both empty
        if not a and not b:
            return True
        # only one is empty
        if not a or not b:
            return False
        # values differ
        if a.val != b.val:
            return False

        return self.treesMatch(a.left, b.left) and self.treesMatch(a.right, b.right)

    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        # early exit if root is none
        if not root:
            return False

        # try all nodes DFS
        # see if any node is the root of a tree that matches root
        if self.treesMatch(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
