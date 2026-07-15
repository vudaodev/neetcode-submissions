'''
Brute force solution is O(n^3)
We sort the array O(nlogn), so it's easier to work with.

For each value at i, we use two pointers with j and k to see if we can find two values
that add up to a target: -nums[i]

If nums[j] + nums[k] == target, add to res
If nums[j] + nums[k] > target, decrement k as we need smaller number.
If nums[j] + nums[k] < target, increment k.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)-2):        
            target = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                jk_sum = nums[j] + nums[k]
                if jk_sum == target:
                    triplet = [nums[i],nums[j],nums[k]]
                    # Skipping duplicate values:
                    if triplet not in res:
                        res.append(triplet)
                    else: j += 1
                elif jk_sum > target:
                    k -= 1
                else: 
                    j += 1  
        return res