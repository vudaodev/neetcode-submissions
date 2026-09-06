class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                total += prices[r] - prices[l]
                l = r
            else:
                l = r
            r += 1
        return total