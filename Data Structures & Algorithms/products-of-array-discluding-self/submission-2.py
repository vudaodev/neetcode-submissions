class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialise output array with 1's
        n = len(nums)
        output = [20]*n

        # Calculate products of elements strictly to the left
        prefix = 1
        for i in range(0,n):
            output[i] = prefix
            prefix*= nums[i]
        
        # Calculate products of elements strictly to the right
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
        
            