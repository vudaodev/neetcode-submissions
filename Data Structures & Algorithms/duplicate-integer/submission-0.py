class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]: 
                    return True
        return False
    # i = 0, Value at i = 1
        # j = 1, Value at j = 2, 1 != 2  
        # j = 2, Value at j = 3, 1 != 3
        # j = 3, Value at j = 3, 1 != 3 
    # i = 1, Value at i = 2
        # j = 2, Value at j = 3, 2 != 3
        # j = 3, Value at j = 3, 2 != 3
    # i = 2, Value at i = 3
        # j = 3, Value at j = 3, 3 == 3, return True 
