import numpy as np

def shortestPathBinaryMatrix(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # basically, perform BFS from (0, 0) toward (n-1, n-1)
        # compute shortest path

        n = len(grid)

        dist = -np.ones((n, n))
        queue = [(0, 0)]
        proc = {(0, 0)}
        dist[0, 0] = 1
        while queue:
                # print(queue)
                # print(proc)
                # input()

                i, j = queue.pop()
                if grid[i][j] == 1:
                        continue

                neighs = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]

                for k, l in neighs:
                        if k >= 0 and k<n and l>=0 and l<n:
                                if (k, l) not in proc and grid[k][l] == 0:
                                        queue.append((k, l))
                                        proc.add((k, l))
                                        dist[k, l] = dist[i, j] + 1
        return dist[n-1, n-1]

grid = [[0,1],[1,0]]
grid = [[0,0,0],[1,1,0],[1,1,0]]
grid = [[1,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix(grid))
