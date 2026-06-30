class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        # A set is a Data structure that does not have any duplicates 
        # If a duplicate exists in the nums array, 
        # The set of nums will be a different length. 
        # In this case, we return True.