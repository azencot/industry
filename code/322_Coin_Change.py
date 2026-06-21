# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        amount_hash = {0: 0}

        def cc(amount):

            if amount in amount_hash:
                return amount_hash[amount]

            if amount < 0:
                return -1

            min_coins_nr = float('inf')
            for coin in coins:
                if coin <= amount:
                    tmp_coins_nr = cc(amount - coin)

                    if tmp_coins_nr != -1:
                        min_coins_nr = min(min_coins_nr, 1 + tmp_coins_nr)
            
            min_coins_nr = min_coins_nr if min_coins_nr != float('inf') else -1
            amount_hash[amount] = min_coins_nr
            
            return min_coins_nr

        return cc(amount)