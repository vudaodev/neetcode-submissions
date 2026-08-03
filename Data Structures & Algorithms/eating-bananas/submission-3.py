'''
- Cannot eat from more than one pile per hour
- k = rate of eating
- We want to minimise k whilst maximising total eating time (which has to be kept below h)
- Minimum value of k is 1, Maximum value of k is max(piles)
- Strategy: 
1. Find the largest value in piles. k will never be bigger than this value
2. Create an array [1,max(piles)] 
3. Perform binary search on the array that we just created.
    - Keep track of total_time and k, updating k as appropriate
    - If total_time == h: return k
    - If total_time > h: We need to eat quicker, search right
    - If total_time < h: Update k. We may be able to eat slower, search left.
4. return k
T/C: O(n * log m) where n = size of input array and m = max value in array
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
