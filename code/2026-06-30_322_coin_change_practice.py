# LeetCode 322. Coin Change
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins,
# return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
# Example 1:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
#
# Example 3:
# Input: coins = [1], amount = 0
# Output: 0
#
# Constraints:
# 1 <= len(coins) <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
# LeetCode: https://leetcode.com/problems/coin-change/


# this is a classic DP problem; Idea: helper function that computes min coins for the remainder; store pre-computed reminders in hash
# complexity: O(amount * n) time: at most amount distinct states, each tries all coins; O(amount) for memo + recursion depth

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        mem = {}

        def minCoins(rem):
            if rem == 0:
                return 0

            if rem < 0:
                return -1

            if rem in mem:
                return mem[rem]

            min_coins = float('inf')
            for coin in coins:
                tmp_min = minCoins(rem - coin)
                if tmp_min != -1:
                    tmp_min += 1
                    if tmp_min < min_coins:
                        min_coins = tmp_min

            if min_coins == float('inf'):
                min_coins = -1
            mem[rem] = min_coins

            return min_coins


        return minCoins(amount)


if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))  # 3
    print(solution.coinChange([2], 3))  # -1
    print(solution.coinChange([1], 0))  # 0
