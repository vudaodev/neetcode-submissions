class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force: T/C O(n^2) / S/C: O(1)
        # HashMap: T/C O(n), S/C: O(n)
            # Key: number 
            # Value: indice
        # Loop through the nums array.
            # Check to see whether we have x where x = target - currentNumber inside of 
            # the Hashmap. If we do, we return both indices. Else, we add the currentNumber
            # and indice to the hashmap.
        hm = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in hm:
                return [hm[x], i]
            hm[num] = i
        
        