# There is an m x n binary grid matrix with all the values set 0 initially. Design an algorithm to randomly pick an index (i, j) 
# where matrix[i][j] == 0 and flips it to 1. All the indices (i, j) where matrix[i][j] == 0 should be equally likely to be returned.

# Optimize your algorithm to minimize the number of calls made to the built-in random function of your language and optimize the time and 
# space complexity.

# Implement the Solution class:

# Solution(int m, int n) Initializes the object with the size of the binary matrix m and n.

# int[] flip() Returns a random index [i, j] of the matrix where matrix[i][j] == 0 and flips it to 1.

# void reset() Resets all the values of the matrix to be 0.

import random

# lazy Fisher-Yates shuffle with a hashmap.
class Solution(object):

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.m = m
        self.n = n

        self.map = {}
        self.remain = self.m * self.n
        

    def flip(self):
        """
        :rtype: List[int]
        """
        i = random.randint(0, self.remain - 1)

        val = self.map.get(i, i)

        self.remain -= 1
        self.map[i] = self.map.get(self.remain, self.remain)

        return [val // self.n, val % self.n]

    def reset(self):
        """
        :rtype: None
        """
        self.map = {}
        self.remain = self.m * self.n