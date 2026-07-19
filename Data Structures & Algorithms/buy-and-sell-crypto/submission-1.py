'''
Keep track of:
    maxProfit = 0
    minPrice = prices[0]

for each day:
    Calculate max_profit of selling on said day 
    Update maxProfit
    Update minPrice

return maxProfit
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, minPrice = 0, prices[0]

        for price in prices:
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
            minPrice = min(minPrice, price)

        return maxProfit