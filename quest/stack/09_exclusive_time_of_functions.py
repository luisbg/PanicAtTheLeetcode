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
            fid_str, act, time_str = log.split(':')
            time = int(time_str)
            fid = int(fid_str)

            if calls:
                curr = calls[-1]
                times[curr] += time - last_time

            if act == "start":
                calls.append(fid)
                last_time = time
            else:
                times[calls.pop()] += 1 # need increment because time is inclusive
                last_time = time + 1 # also due to inclusive time :(
        
        return times
