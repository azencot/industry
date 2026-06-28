"""
875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/

Koko loves to eat bananas. There are n piles of bananas, the ith pile has
piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses
some pile of bananas and eats k bananas from that pile. If the pile has fewer
than k bananas, she eats all of them instead and will not eat any more bananas
during this hour.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
    Input: piles = [3,6,7,11], h = 8
    Output: 4

Example 2:
    Input: piles = [30,11,23,4,20], h = 5
    Output: 30

Example 3:
    Input: piles = [30,11,23,4,20], h = 6
    Output: 23

Constraints:
    1 <= len(piles) <= 10**4
    len(piles) <= h <= 10**9
    1 <= piles[i] <= 10**9
"""

import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = (lo + hi) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            if hours <= h:
                hi = mid
            else:
                lo = mid + 1

        return lo



if __name__ == "__main__":
    sol = Solution()

    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    assert sol.minEatingSpeed([1], 1) == 1
    assert sol.minEatingSpeed([312884470], 312884469) == 2

    print("all tests passed")
