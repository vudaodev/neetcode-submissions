class Solution:
    def rob(self, nums: List[int]) -> int:
        # NON OPTIMAL SOLUTION: O(n^2) TC/ O(1) SC
        # Change the array so it answers the question: 
        # If we select index i, what is the max that we can earn from index i to end?
        # [6,4,1,3]
        # Start from index -3, and decrement until we reach the start of nums array:
            # For each index, add the largest number possible that isn't it's right adjacent
        # We then return the largest number in the array!
        if len(nums) <= 2:
            return max(nums)
        for i in range(len(nums)-3,-1,-1):
            max_from_rest = 0
            for j in range(i+2,len(nums)):
                max_from_rest = max(nums[j], max_from_rest)
            nums[i] = nums[i] + max_from_rest
        return max(nums)
        


        