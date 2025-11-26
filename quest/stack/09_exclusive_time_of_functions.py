class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """

        times = [0] * n
        calls = []
        last_time = 0
        for log in logs:
            fid, act, time = log.split(':')

            if calls:
                curr = calls[-1]
                times[curr] += int(time) - last_time

            last_time = int(time)

            if act == "start":
                calls.append(int(fid))
            else:
                times[calls.pop()] += 1 # need increment because time is inclusive
                last_time += 1 # also due to inclusive time :(
        
        return times
