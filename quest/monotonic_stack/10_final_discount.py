"""
You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.
"""

class Solution(object):
    def bruteForcefinalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        ans = []

        for i, price in enumerate(prices):
            discount = False
            for j in range(i + 1, len(prices)):
                if prices[j] <= price:
                    ans.append(price - prices[j])
                    discount = True
                    break
            
            if not discount:
                ans.append(price)
        
        return ans

    def monotonicStackFinalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        ans = [0] * n
        stack = []

        # walk from right to left
        for i in range(n - 1, -1, -1):
            price = prices[i]

            # remove prices bigger than price
            while stack and stack[-1] > price:
                stack.pop()

            # stack contains nearest price <= price
            if stack:
                discount = stack[-1]
            else:
                discount = 0
            ans[i] = price - discount

            # price is candidate discount for items to the left
            stack.append(price)

        return ans
