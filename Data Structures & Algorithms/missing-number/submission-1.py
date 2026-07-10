class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Brute force/ naive approach:
            # iterate through all the numbers from 0 to n
                # iterate through all the numbers in nums, until we find missing 
            # T/C: O(n^2), S/C: O(1)
        # Hash Set:
            # Create a HS that contains all numbers in the nums array O(n) T/C op
            # Iterate through all numbers from 0->n and look it up in the HS - O(n) T/C op
                # If the number does not exist in the HS, we return that number 
            # T/C: O(n), S/C: O(n)
            hs = set(nums)
            for num in range(len(nums)+1):
                if num not in hs:
                    return num