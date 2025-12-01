"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # track lowest_seen
        lowest_seen = prices[0]

        # compare lowest_seen with day's price
        # consider selling everyday based on this diff and save max profit
        max_profit = 0
        for p in prices[1:]: # zero-profit on the first day, skip
            if lowest_seen > p:
                lowest_seen = p

            day_profit = p - lowest_seen
            if max_profit < day_profit:
                max_profit = day_profit

        return max_profit
