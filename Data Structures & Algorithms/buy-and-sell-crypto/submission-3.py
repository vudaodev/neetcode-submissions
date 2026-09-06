class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
            right += 1
        return max_profit