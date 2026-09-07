'''
brute force: O(n^2) T/C, O(1) S/C
    - loop through nums array in 2 nested loops
    - If condition is met, return the two indices 

HM Solution: O(n) T/C, O(n) S/C
    - hash map that tracks num -> index. 
    - loop through nums array.  
        - if target - curr_num is in the hm, return the 2 indices

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_i = {}
        for i, num in enumerate(nums):
            desired = target - num
            if desired in num_to_i:
                return [num_to_i[desired],i]
            num_to_i[num] = i
        