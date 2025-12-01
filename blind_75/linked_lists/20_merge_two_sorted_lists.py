"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1 = list1
        curr2 = list2

        head = None
        prev = None
        # run through both lists while both have nodes
        while curr1 and curr2:
            # make a new node
            new_curr = ListNode()
            if not head:
                head = new_curr

            # pick lowest current node
            # set it at new node and move pointer
            if curr1.val <= curr2.val:
                new_curr.val = curr1.val
                curr1 = curr1.next
            else:
                new_curr.val = curr2.val
                curr2 = curr2.next

            if prev:
                prev.next = new_curr
            prev = new_curr

        # handle end of lists
        if prev:
            prev.next = curr1 if curr1 else curr2
        else:
            head = curr1 if curr1 else curr2

        return head

    def useExistingMergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()      # dummy head to simplify edge cases
        tail = dummy            # tail always points to last node in merged list

        p1, p2 = list1, list2

        # Walk both lists while they both have nodes
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next

        # At most one of p1, p2 is non-null now; append the remainder
        tail.next = p1 if p1 else p2

        return dummy.next
