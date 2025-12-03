"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution(object):
    def bruteForceMaxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        largest = 0

        # start two pointer: start and end
        # run pointers
        for start in range(len(height) - 1):
            for end in range(1, len(height)):
                if start < end:
                    # track largest container
                    container = (end - start) * min(height[start], height[end])
                    if container > largest:
                        largest = container

        # return largest seen
        return largest
