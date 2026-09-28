'''
T/C: O(n), S/C: 0(1)
Keep track of max_sum

Use a 2 pointer method with L and R starting at 0.
L = start of subarray, R = end of subarray (inclusive)

Increment R, comparing curr_sum of current subarray to max_sum 
    If curr_sum > max_sum, update max_sum
    If curr_sum < 0, move L and R to R+1

return max_sum
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        L, R, curr_sum = 0, 0, 0

        while R < len(nums):
            curr_sum += nums[R]
            max_sum = max(curr_sum, max_sum)
            # Move L if we have a negative subarray, and reset curr_sum
            if curr_sum < 0:
                L = R + 1
                curr_sum = 0
            # Move R every iteration
            R += 1
        return max_sum
