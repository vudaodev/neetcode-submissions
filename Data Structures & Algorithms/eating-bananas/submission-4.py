'''
- Strategy: 
1. Find the highest_value in piles. k will never be bigger than this value 
2. Perform binary search on the range(1,highest_value)
    - Keep track of total_time and k, updating k as appropriate
    - If total_time > h: We need to eat quicker, search right
    - If total_time <= h: Update k. We may be able to eat slower, search left.
3. return k
T/C: O(n * log m) where n = size of input array and m = max value in array
NOTE:
- Memory error: We do NOT have to create an array for the range(1,highest_value+1). Just perform binary search on the actual numbers.
- Even if total_time == h, we may still be able to find a lower number that satisfies the condition
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        highest_rate = max(piles)
        l, r = 1, highest_rate
        k = highest_rate
        while l <= r:
            rate = (l + r)//2
            total_time = 0
            #loop through piles
            for p in piles:
                total_time += math.ceil(p/rate)
            if total_time <= h:
                k = min(rate, k)
                r = rate - 1
            elif total_time > h:
                l = rate + 1
        return k
