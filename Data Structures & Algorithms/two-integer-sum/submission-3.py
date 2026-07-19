'''
Brute force solution: O(n^2), 2 nested loops
Hashmap solution O(n): 
hm[num] = index 
For each num in nums, Check whether target - num is in the HM.
If it is, return the two indices.
Else, Add num to hm. 
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i,num in enumerate(nums):
            desired = target - num
            if desired in hm: 
                return [hm[desired], i]
            hm[num] = i
        