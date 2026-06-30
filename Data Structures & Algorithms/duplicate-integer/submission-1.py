class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Python name - Universal name
        # ----------------------------
        # dictionary = Hash Map
        # set = Hash Set
        # list = Array 

        # Create an empty Hash Set
        hs = set()
        # iterate through nums list
        for num in nums:
            # if value is already in the list, return True
            # add each value of nums list into our Hash Set
            if num in hs:
                return True
            hs.add(num)
        # return False 
        return False
