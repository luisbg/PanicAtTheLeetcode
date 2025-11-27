"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

class Solution(object):
    def bruteForceDailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        days = len(temperatures)
        ans = [0] * days

        for i, t in enumerate(temperatures):
            wait = 0
            for j in range(i+ 1, days):
                wait += 1
                if temperatures[j] > temperatures[i]:
                    ans[i] = wait
                    break
        
        return ans

    def monotonicStackDailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        days = len(temperatures)
        ans = [0] * days
        stack = []

        # walk from right to left
        for i in range(days - 1, -1, -1):
            count = 0
            temp = temperatures[i]

            # pop days not warmer than today
            while stack and temperatures[stack[-1]] <= temp:
                stack.pop()

            # first warmer day is at the top of the stack
            if stack:
                ans[i] = stack[-1] - i
            else:
                ans[i] = 0

            stack.append(i)

        return ans
