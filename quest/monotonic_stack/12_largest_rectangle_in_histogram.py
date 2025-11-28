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

    def monotonicStackLargestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        stack = []
        ans = [0] * n

        # run right to left
        for i in range(n - 1, -1, -1):
            # keep closest smallest as top of stack
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                ans[i] = heights[i] * (stack[-1] - i)
            else:
                ans[i] = heights[i] * (n - i)

            stack.append(i)

        stack = []
        # run left to right
        for i in range(0, n):
            # keep closest smallest as top of stack
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                ans[i] += heights[i] * (i - stack[-1] - 1)
            else:
                ans[i] += heights[i] * i

            stack.append(i)

        tallest = 0
        for h in ans:
            if h > tallest:
                tallest = h

        return tallest
