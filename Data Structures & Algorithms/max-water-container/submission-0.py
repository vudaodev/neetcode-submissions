'''
Bruteforce: Consider every possible pair of bars. O(n^2)/ O(1)
Two Pointer: L and R (start and end)
Keep track for max_volume
volume:for L and R, it would be min (L,R) * (R-L)
For each stage:
    Calculate volumn and update max_volume
    Move the pointer with the shorter bar
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        max_vol = 0

        while L < R:
            vol = min(heights[L], heights[R]) * (R-L) # Calc volume
            max_vol = max(max_vol, vol)
            if heights[L] > heights[R]:
                R -= 1
            elif heights[L] < heights[R]:
                L += 1
            else:
                L += 1
        return max_vol



