"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        # we need the candidates list to be in order
        candidates.sort()

        # recursive function to track down sequences
        def trackDownDFS(start, remaining, path):
            # if we hit the target exactly, record the combination
            if remaining == 0:
                ans.append(list(path))
                return

            # try all candidates starting at 'start'
            for i in range(start, len(candidates)):
                val = candidates[i]

                # if the candidate is too big, no need to continue
                if val > remaining:
                    break

                # choose this candidate
                path.append(val)
                # recurse with same 'i' because we can reuse the same number
                trackDownDFS(i, remaining - val, path)
                # backtrack
                path.pop()

        trackDownDFS(0, target, [])
        return ans
