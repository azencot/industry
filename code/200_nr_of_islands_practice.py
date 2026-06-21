# Given an m x n 2D binary grid grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent 
# lands horizontally or vertically. You may assume all four edges of the 
# grid are all surrounded by water.
class Solution(object):
    def numIslands(self, grid):

        # idea: BFS from grid[1, 1] over inner grid cells; 
        # BFS expands only on grid[i, j] = 1 cells
        # mark visited cells; 
        # many edge cases
        m, n = len(grid), len(grid[0])

        visited = set()
        nrOfIslands = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == "0" or (i, j) in visited:
                    continue

                nrOfIslands += 1

                queue = [(i, j)]
                visited.add((k, l))

                # DFS from (i, j)
                while queue:
                    (k, l) = queue.pop()

                    if k-1 >= 0 and grid[k-1][l] == "1" and (k-1, l) not in visited:
                        queue.append((k-1, l))
                        visited.add((k - 1, l))

                    if k+1 < m and grid[k+1][l] == "1" and (k+1, l) not in visited:
                        queue.append((k+1, l))
                        visited.add((k + 1, l))

                    if l-1 >= 0 and grid[k][l-1] == "1" and (k, l-1) not in visited:
                        queue.append((k, l-1))
                        visited.add((k, l-1))

                    if l+1 < n and grid[k][l+1] == "1" and (k, l+1) not in visited:
                        queue.append((k, l+1))
                        visited.add((k, l + 1))

        return nrOfIslands