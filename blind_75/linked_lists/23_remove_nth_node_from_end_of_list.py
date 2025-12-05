"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def onePassRemoveNthFromEnd(self, head, n):
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

    def twoPassRemoveNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # run through the list with two pointers
        # faster runs from the beginning
        # slower runs n behind
        faster = head
        slower = head

        # move faster n steps ahead
        for _ in range(n):
            faster = faster.next

        # if faster is None, we are removing the head
        if not faster:
            return head.next

        # move both until faster is at the last node
        while faster.next:
            faster = faster.next
            slower = slower.next

        # now slower is at the place to remove
        slower.next = slower.next.next

        return head
