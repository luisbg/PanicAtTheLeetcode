"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
"""

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        # sort all meetings by start time
        intervals.sort()

        # check all meetings finish before the next start time
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True
