class Solution(object):
    def bruteForceLargestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        tallest_seen = 0
        for i, h in enumerate(heights):
            count = 1

            # build rectangle to the right
            for j in range(i + 1, len(heights)):
                if h <= heights[j]:
                    count += 1
                else:
                    break

            # build rectangle to the left
            for j in range(i - 1, -1, -1):
                if h <= heights[j]:
                    count += 1
                else:
                    break

            rect = h * count
            if rect > tallest_seen:
                tallest_seen = rect

        return tallest_seen
