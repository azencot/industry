# There are a total of numCourses courses you have to take, labeled from 0 to 
# numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] 
# indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take 
# course 1.
# Return the ordering of courses you should take to finish all courses. If there are 
# many valid answers, return any of them. If it is impossible to finish all courses, 
# return an empty array.
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ordering = []

        # topological sort
        indeg = [0] * numCourses
        courses = {}
        for (a,b) in prerequisites:
            indeg[a] += 1

            if b not in courses:
                courses[b] = [a]
            else:
                courses[b].append(a)

        queue = []
        for course in range(numCourses):
            if indeg[course] == 0:
                queue.append(course)

        while queue:
            ordering.append(queue.pop())

            if ordering[-1] in courses:
                for item in courses[ordering[-1]]:
                    indeg[item] -= 1
                    if indeg[item] == 0:
                        queue.append(item)

        if len(ordering) == numCourses:
            return ordering
        else:
            return []
