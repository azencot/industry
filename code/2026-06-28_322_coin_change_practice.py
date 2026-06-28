"""
322. Coin Change
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

Example 2:
    Input: coins = [2], amount = 3
    Output: -1

Example 3:
    Input: coins = [1], amount = 0
    Output: 0

Constraints:
    1 <= len(coins) <= 12
    1 <= coins[i] <= 2**31 - 1
    0 <= amount <= 10**4
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = {}
        
        def minCoins(rem):
            if rem == 0:
                return 0

            if rem < 0:
                return -1

            if rem in memo:
                return memo[rem]
        
            best = float("inf")
            for coin in coins:
                sub = minCoins(rem - coin)
                if sub != -1:
                    best = min(best, sub + 1)

            if best == float("inf"):
                memo[rem] = -1
            else:
                memo[rem] = best

            return memo[rem]
    
        return minCoins(amount)


if __name__ == "__main__":
    sol = Solution()

    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1], 0) == 0
    assert sol.coinChange([1], 2) == 2
    assert sol.coinChange([2, 5, 10, 1], 27) == 4
    assert sol.coinChange([186, 419, 83, 408], 6249) == 20

    print("all tests passed")
