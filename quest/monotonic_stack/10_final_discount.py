class Solution(object):
    def finalPrices(self, prices):
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
