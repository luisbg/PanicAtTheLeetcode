"""
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person initially at position k (0-indexed) to finish buying tickets.
"""

from collections import deque

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """

        tix_q = deque()
        for idx, val in enumerate(tickets):
            tix_q.append((val, idx))

        seconds = 0
        while tix_q:
            seconds += 1
            t, i = tix_q.popleft()
            t -= 1

            if t > 0:
                tix_q.append((t, i))
            elif i == k:
                return seconds

        return -1
