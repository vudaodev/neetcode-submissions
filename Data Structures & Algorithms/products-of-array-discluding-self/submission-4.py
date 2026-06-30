class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialise output array with 1's
        n = len(nums)
        output = [1]*n

        # Calculate products of elements strictly to the left
        prefix_product = 1
        for i in range(0,n):
            output[i] = prefix_product
            prefix_product *= nums[i]
        
        # Calculate products of elements strictly to the right
        # and multiply existing left product
        suffix_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix_product
            suffix_product *= nums[i]

        return output
        
            