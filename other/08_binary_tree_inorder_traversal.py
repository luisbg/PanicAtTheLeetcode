"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []

        # recurse in order
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)
        return ans
