# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
#
# Difficulty: Medium
# Tags: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land)
# and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are
# surrounded by water.
#
# Example 1:
#   Input: grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
#   Output: 1
#
# Example 2:
#   Input: grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
#   ]
#   Output: 3
#
# Constraints:
#   - m == grid.length
#   - n == grid[i].length
#   - 1 <= m, n <= 300
#   - grid[i][j] is '0' or '1'.
#
# --- Timed drill: 2026-06-25 (25 min) ---


# this is standard BFS/DFS; the idea is to iterate over grid, mark visited;  per unvisited cell: BFS to horiz/vert lands; maybe edge cases on boundary
# I can save mem by directly modifying grid, if in-place is allowed

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])

        visited = [[0] * len(row) for row in grid]

        def do_dfs(i, j):
            if i < 0 or i >= m or j<0 or j>=n:
                return
            if visited[i][j] == 1 or grid[i][j] != '1': 
                return

            visited[i][j] = 1

            do_dfs(i-1, j)
            do_dfs(i+1, j)
            do_dfs(i, j-1)
            do_dfs(i, j+1) 

        nrOfIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    do_dfs(i, j)
                    nrOfIslands += 1

        return nrOfIslands


if __name__ == "__main__":
    sol = Solution()

    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert sol.numIslands(grid1) == 1

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert sol.numIslands(grid2) == 3

    assert sol.numIslands([["1"]]) == 1
    assert sol.numIslands([["0"]]) == 0

    print("all tests passed")
