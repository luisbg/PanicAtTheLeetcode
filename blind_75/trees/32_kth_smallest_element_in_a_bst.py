"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        seen = 0
        stack = []
        curr = root

        # traverse in order
        while curr or stack:
            # go left as far as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            seen += 1
            if seen == k:
                return curr.val

            # go right
            curr = curr.right

        # just in case
        return -1
