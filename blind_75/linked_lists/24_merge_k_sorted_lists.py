"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # start a new list
        ans = None
        tail = None

        # run through every list until all are empty
        while True:
            smallest = None
            s_idx = -1

            # check all heads to find the smallest one
            for i, head in enumerate(lists):
                if head and (smallest is None or head.val < smallest):
                    smallest = head.val
                    s_idx = i

            # if we didn' find a non-empty list, we are done
            if s_idx == -1:
                break

            # copy smallest head to answer
            new_node = ListNode(smallest)
            if tail:
                tail.next = new_node
                tail = new_node
            else:
                tail = new_node
                ans = new_node

            # remove smallest head from list
            lists[s_idx] = lists[s_idx].next

        return ans
