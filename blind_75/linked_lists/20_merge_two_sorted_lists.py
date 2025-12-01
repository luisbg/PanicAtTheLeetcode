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
        # current index of both lists
        curr1 = list1
        curr2 = list2

        head = None
        prev = None

        # run through both lists
        while curr1 or curr2:
            # make a new node
            new_curr = ListNode()
            if not head:
                head = new_curr

            # handle ends of lists
            if not curr1:
                new_curr.val = curr2.val
                curr2 = curr2.next
            elif not curr2:
                new_curr.val = curr1.val
                curr1 = curr1.next
            else:
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

        return head
