# 207. Course Schedule
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where
# prerequisites[i] = [ai, bi] indicates that you must take course bi first if
# you want to take course ai.
#
# For example, the pair [0, 1] indicates that to take course 0 you have to
# first take course 1.
#
# Return True if you can finish all courses. Otherwise, return False.
#
# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: True
# Explanation: There are 2 courses. To take course 1 you should have finished
# course 0. So it is possible.
#
# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: False
# Explanation: There is a cycle.
#
# Constraints:
# - 1 <= numCourses <= 2000
# - 0 <= prerequisites.length <= 5000
# - prerequisites[i].length == 2
# - 0 <= ai, bi < numCourses
# - All pairs prerequisites[i] are unique.
#
# Link: https://leetcode.com/problems/course-schedule/

# approach: maintain two structures: a dict for outgoing edges and a list on in_edges count; the idea is to topo BFS on that structure to identify self-loops
# keep count of learnt courses, can learn all courses with in_edges == 0; after learning them, re-update queue with new in_edges == 0 courses; do that till queue is empty; 
# complexity: O(numCourses + len(prereq)) time + mem

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        courses, in_edges = {}, [0] * numCourses
        for course, prereq in prerequisites:
            courses[prereq] = courses.get(prereq, []) + [course]
            in_edges[course] += 1

        queue = []
        for i in range(numCourses):
            if in_edges[i] == 0:
                queue.append(i)


        count = 0
        while queue:
            course = queue.pop()
            for item in courses.get(course, []):
                in_edges[item] -= 1
                if in_edges[item] == 0:
                    queue.append(item)
            count += 1

        return count == numCourses:


if __name__ == "__main__":
    tests = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (4, [[1, 0], [2, 1], [3, 2]], True),
        (4, [[1, 0], [2, 1], [3, 2], [1, 3]], False),
        (3, [], True),
        (1, [], True),
    ]

    sol = Solution()
    for numCourses, prerequisites, expected in tests:
        result = sol.canFinish(numCourses, prerequisites)
        print(numCourses, prerequisites, result, "PASS" if result == expected else "FAIL")
