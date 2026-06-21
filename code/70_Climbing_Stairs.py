# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        visited = {1: 1, 2: 2}

        def calc_way(n):

            if n in visited:
                return visited[n]

            visited[n] = calc_way(n-1) + calc_way(n-2)
            return visited[n]

        return calc_way(n)

        


 