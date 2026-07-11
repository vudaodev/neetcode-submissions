class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Make use of a hashset 
        # Loop through the num in nums:
            # If in HS, we return the num
            # If not, add to HS
        # TC: O(n), S/C: O(n)

        hs = set()
        for num in nums:
            if num in hs:
                return num
            hs.add(num)
        

