"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
"""

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # turn each interval into two events
        events = []
        for s, e in intervals:
            events.append((s, 1)) # +1 for start time
            events.append((e, -1)) # -1 for end time

        events.sort(key=lambda x: (x[0], x[1]))

        # run through all events tracking current rooms needed
        current_rooms = 0
        max_rooms = 0
        for e in events:
            current_rooms += e[1]
            max_rooms = max(max_rooms, current_rooms)

        return max_rooms
