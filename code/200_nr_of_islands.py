def nrOfIslands(grid):

	# BFS directly on grid
	m, n = len(grid), len(grid[0])

	processed = {}
	nrOfIslands = 0
	for i in range(m):
		for j in range(n):

			if grid[i][j] == "0" or (i, j) in processed:
				continue

			nrOfIslands += 1

			queue = [(i, j)]
			processed[(i, j)] = 1
			while queue:
				(ii, jj) = queue.pop()

				if ii-1 >= 0 and grid[ii-1][jj] == "1":
					if (ii-1, jj) not in processed:
						queue.append((ii-1, jj))
						processed[(ii-1, jj)] = 1

				if ii+1 < m and grid[ii+1][jj] == "1":
					if (ii+1, jj) not in processed:
						queue.append((ii+1, jj))
						processed[(ii+1, jj)] = 1

				if jj-1 >= 0 and grid[ii][jj-1] == "1":
					if (ii, jj-1) not in processed:
						queue.append((ii, jj-1))
						processed[(ii, jj-1)] = 1

				if jj+1 < n and grid[ii][jj+1] == "1":
					if (ii, jj+1) not in processed:
						queue.append((ii, jj+1))
						processed[(ii, jj+1)] = 1

	return nrOfIslands





# # number of islands
# def tup2lin(tup, n):
# 	return tup[0]*n + tup[1]

# def lin2tup(lin, n):
# 	i = lin // n
# 	j = lin % n
# 	return (i, j)

# def nrOfIslands(grid):
# 	# grid[i][j] = 0/1 = water/land
# 	m, n = len(grid), len(grid[0])

# 	# construct tree (Adj)  	O(m * n)
# 	Adj = [[] for _ in range(m*n)]
# 	queue = {}

# 	# O(m * n)
# 	for ij in range(m * n):
# 		i, j = lin2tup(ij, n)

# 		# ignore boundry
# 		if i == 0 or i == m-1 or j == 0 or j == n-1:
# 			continue

# 		# continue if no land
# 		if grid[i][j] == "0":
# 			continue

# 		# ij is a land (init to not processed)
# 		queue[ij] = 0

# 		if grid[i-1][j] == "1":
# 			Adj[ij].append(tup2lin((i-1, j), n))

# 		if grid[i+1][j] == "1":
# 			Adj[ij].append(tup2lin((i+1, j), n))

# 		if grid[i][j-1] == "1":
# 			Adj[ij].append(tup2lin((i, j-1), n))

# 		if grid[i][j+1] == "1":
# 			Adj[ij].append(tup2lin((i, j+1),n))

# 	# perform BFS; track processed vertices;
# 	islandsNum = 0

# 	for ij in queue:
# 		# print(queue)
# 		if queue[ij] == 0:
# 			islandsNum += 1
# 			queue[ij] = 1

# 		for v in Adj[ij]:
# 			queue[v] = 1

# 	# return the number of distinct islands
# 	return islandsNum

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(nrOfIslands(grid))
