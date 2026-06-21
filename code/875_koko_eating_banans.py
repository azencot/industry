# class Solution(object):
import math

def minEatingSpeed(self, piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    ones = [1] * len(piles)
    final_sol = max(piles)
    lb, rb = 1, final_sol

    while rb - lb >= 0:
        curr_sol = (rb + lb) // 2
        
        eating_time = []
        for i in range(len(piles)):
            eating_time.append(math.ceil(piles[i] / curr_sol))

        if sum(eating_time) <= h:
            final_sol = curr_sol
            rb = curr_sol - 1
        else:
            lb = curr_sol + 1

    return final_sol

# Input: piles = [3,6,7,11], h = 8
# Output: 4

print(minEatingSpeed(None, [3,6,7,11], 8))

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
print(minEatingSpeed(None, [30,11,23,4,20], 5))

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
print(minEatingSpeed(None, [30,11,23,4,20], 6))

