# There are a total of numCourses courses you have to take, labeled from 0 
# to numCourses - 1. You are given an array prerequisites where 
# prerequisites[i] = [ai, bi] indicates that you must take course bi 
# first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have 
# to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # topological sort (BFS): count in-degrees, remove nodes with 0 in-degree, process graph

        # count in-degrees 
        graph = {}
        indeg = [0] * numCourses
        for item in prerequisites:
            if item[1] in graph:
                graph[item[1]].append(item[0])
            else:
                graph[item[1]] = [item[0]]
            indeg[item[0]] += 1

        # add in-deg == 0 to queue
        queue = []
        for course in range(numCourses):
            if indeg[course] == 0:
                queue.append(course)

        # while list not empty: learn courses, add courses with no pre-req
        taken = 0
        while queue:
            course = queue.pop()
            taken += 1

            for nxt in graph.get(course, []):
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    queue.append(nxt)

        # count how many courses are learned, return if it equals numCourses
        return taken == numCourses
