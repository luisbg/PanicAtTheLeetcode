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
