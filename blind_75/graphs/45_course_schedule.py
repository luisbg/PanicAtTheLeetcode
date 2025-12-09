"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # build the dependency graph
        graph = defaultdict(list)    # course -> list of dependants (next courses)
        indegree = [0] * numCourses    # indegree[i] = how many dependency courses i has

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # start from all courses with no dependencies
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        # now travel through dependency graph
        taken = 0
        while queue:
            course = queue.popleft()
            taken += 1

            # add to the queue all dependants that now become available
            for dep in graph[course]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    queue.append(dep)

        # did we take all courses?
        return taken == numCourses
