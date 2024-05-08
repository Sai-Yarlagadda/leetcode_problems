class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            sell_price = prices[i]
            if buy_price < sell_price:
                profit = sell_price - buy_price
                if max_profit < profit:
                    max_profit = profit
            else:
                buy_price = sell_price
        return max_profit
        
