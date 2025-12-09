"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:
    FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
    int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
    void add(int value) insert value to the queue.
"""

class FirstUnique(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = deque()
        self.counts = {}

        for n in nums:
            self.add(n)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        for n in self.nums:
            if self.counts[n] == 1:
                return n

        return -1

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value in self.counts:
            self.counts[value] += 1
        else:
            self.nums.append(value)
            self.counts[value] = 1
