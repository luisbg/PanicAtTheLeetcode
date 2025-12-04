"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # can we use an array to store nodes?
        node_arr = []

        # run through list and add to array
        curr = head
        while curr:
            node_arr.append(curr)
            curr = curr.next

        # run through array from both ends
        start = 0
        end = len(node_arr) - 1
        while start < end:
            # switch links
            tmp = node_arr[start].next
            node_arr[start].next = node_arr[end]

            node_arr[end].next = tmp
            start += 1
            end -=1

        # avoid cycle in the list
        node_arr[start].next = None

        return head
