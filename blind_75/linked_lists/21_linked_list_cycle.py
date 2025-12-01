"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # run linked list with two pointers
        p1, p2 = head, head

        while True:
            # if we find an empty next there isn't a cycle
            # p1 moves ahead by one
            if p1:
                p1 = p1.next
            else:
                return False

            # p2 moves ahead by two
            if p2 and p2.next:
                p2 = p2.next.next
            else:
                return False

            # if p1 == p2 we have a cycle
            if p1 == p2:
                return True
