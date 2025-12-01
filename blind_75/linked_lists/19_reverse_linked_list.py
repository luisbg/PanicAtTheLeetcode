"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

class Solution(object):
    def iterativeReverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head

        # iterate through list
        # switch [prev -> curr.next] [curr -> prev]
        # curr.next becomes None (until next cycle)
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def recursiveReverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # base case is head or next being null
        if head is None or head.next is None:
            return head

        # Recursively reverse all nodes after head
        new_head = self.reverseList(head.next)

        # Make the next node point back to head
        head.next.next = head
        head.next = None  # cut original link

        return new_head
