class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        for r, r_price in enumerate(prices):
            l_price = prices[l]
            if l_price > r_price:
                l = r
            profit = r_price - l_price
            max_profit = max(max_profit, profit)
        return max_profit

