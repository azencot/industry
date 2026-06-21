def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    # create a hash table of courses and their dependents
    Adj = [[] for _ in range(numCourses)]

    for prereq in prerequisites:
        a, b = prereq
        Adj[b].append(a)

    # compute in-deg
    indeg = [0] * numCourses
    for u in range(numCourses):
        for v in Adj[u]:
                indeg[v] += 1

    # create a queue with in-deg == 0
    queue = []
    for u in range(numCourses):
        if indeg[u] == 0:
                queue.append(u)
    
    # iterate over queue until it is empty
    while queue:
        u = queue.pop()
        for v in Adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                        queue.append(v)

    if sum(indeg) > 0:
        return False
    else:
        return True


