"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # handle edge case of empty tree
        if not root:
            return []

        ans = []
        traversal = deque()
        traversal.append(root)

        while traversal:
            level_size = len(traversal)
            level_vals = []

            # process each level one at a time
            for _ in range(level_size):
                curr = traversal.popleft()
                level_vals.append(curr.val)

                if curr.left:
                    traversal.append(curr.left)
                if curr.right:
                    traversal.append(curr.right)

            ans.append(level_vals)

        return ans
