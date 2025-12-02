"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = [1] * n
        ans = [base]

        # current patterns to expand
        current = [base]

        while current:
            next_patterns = []

            # for each pattern we have so far
            for pattern in current:
                # look for pairs of adjacent 1s
                for i in range(len(pattern) - 1):
                    if pattern[i] == 1 and pattern[i + 1] == 1:
                        # build a new pattern with that pair replaced by a 2
                        tmp = pattern[:i] + [2] + pattern[i + 2:]

                        # avoid duplicates
                        if tmp not in ans:
                            ans.append(tmp)
                            next_patterns.append(tmp)

            # continue expanding the newly generated patterns
            current = next_patterns

        return len(ans)

    def recursiveWays(self, n):
        # base
        if n == 0:
            return [[1]]

        ans = []
        # we can only get to step n, in two ways
        # one step more from n - 1
        # two step from n - 2

        if n > 0:
            one_step_ways = self.ways(n - 1)
            for s in one_step_ways:
                # add one step
                s.append(1)
                ans.append(s)
        if n > 1:
            two_step_ways = self.ways(n - 2)
            for s in two_step_ways:
                # add two step
                s.append(2)
                ans.append(s)

        return ans

    def recursiveClimbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        return len(self.ways(n))

    def ways(self, known, n):
        # check memoized values
        if n in known:
            return known[n]

        ans = 0
        # we can only get to step n, in two ways
        # one step more from n - 1
        # two step from n - 2
        ans = self.ways(known, n - 1) + self.ways(known, n - 2)
        known[n] = ans

        return ans

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # prefill base
        known = {0: 0, 1: 1, 2: 2}
        return self.ways(known, n)
