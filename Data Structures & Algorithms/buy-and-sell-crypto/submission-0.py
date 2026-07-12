class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Keep track of maximum profit across all days
        # Keep track of the minimum price across all days
        # T/C: O(n) 
        # S/C: O(1)
        
        max_profit, min_price = 0, prices[0]

        for i in range(1,len(prices)):
            curr_price = prices[i]
            if curr_price < min_price:
                min_price = curr_price
            else:
                profit = curr_price - min_price
                max_profit = max(profit, max_profit) 
            
        return max_profit