# You are given an array prices where prices[i] is the price of a given 
# stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one 
# stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you 
# cannot achieve any profit, return 0.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # general idea: traverse with two pointers i, j
        # i represents buy time, j represents potential sell time
        # if prices[j] < prices[i] -> we lose money, i <- j, and increment j
        # for instance, if prices decrease monotonically, return 0
        # edge case
        if len(prices) == 1:
            return 0

        i, j, maxp = 0, 1, 0
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
            else:
                maxp = max(maxp, prices[j] - prices[i])
            
            j += 1

        return maxp

