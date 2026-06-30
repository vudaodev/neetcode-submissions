class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total, min_len = 0, 0, float('inf')
        for R in range(len(nums)):
            # Move R 
            total += nums[R]
            # Move L
            while total >= target:
                # Update total
                min_len = min(min_len, R-L+1)
                # Move L to try and find a shorter len that meets condition
                total -= nums[L]
                L += 1
        if min_len == float('inf'): return 0
        return min_len