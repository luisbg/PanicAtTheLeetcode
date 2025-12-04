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
    def heavyReorderList(self, head):
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

    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return  # lists of length 0, 1, 2 are already "reordered"

        # Find the middle (end of first half)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow.next
        slow.next = None  # cut first half from second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # prev is now head of reversed second half
        second = prev
        first = head

        # Merge the two halves
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
