"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # run through the list
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length +=1

        # edge case of removing first element
        if length == n:
            return head.next

        # run again and remove length - n
        curr = head
        remove_idx = length - n
        idx = 0
        while curr:
            if idx == remove_idx - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
            idx +=1

        return head
