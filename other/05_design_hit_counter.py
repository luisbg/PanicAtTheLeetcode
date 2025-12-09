"""
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:
    HitCounter() Initializes the object of the hit counter system.
    void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
    int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
"""

class HitCounter(object):
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        # append latest hit
        self.hits.append(timestamp)

        # remove oldest hits if they are too old
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        # start a counter
        count = 0

        # count hits
        for h in self.hits:
            if h <= timestamp and h > timestamp - 300:
                count += 1

        return count
