"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

class Solution(object):
    def iterativeReverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack = []

        curr = head
        # iterate over the list
        while curr:
            # store values on LIFO stack
            stack.append(curr.val)
            curr = curr.next

        # create new list from stack
        new_head = None
        curr = None
        while stack:
            node = ListNode()
            node.val = stack.pop()
            if curr:
                curr.next = node

            curr = node

            if not new_head:
                new_head = node

        # return new head
        return new_head

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
