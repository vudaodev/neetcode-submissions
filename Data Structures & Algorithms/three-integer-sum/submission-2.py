class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Use 2 pointer to find j and k.
        nums_sorted = sorted(nums)
        res = []
        for i in range(len(nums_sorted)-2):
            target = 0 - nums_sorted[i]
            j, k = i+1, len(nums) - 1
            while j < k: 
                curr_sum = nums_sorted[j] + nums_sorted[k]
                if curr_sum == target:
                    vals = sorted([nums_sorted[i],nums_sorted[j],nums_sorted[k]])
                    if vals not in res:
                        res.append(vals)
                    j += 1
                    k -= 1
                elif curr_sum > target: # need smaller number
                    k -= 1
                else: # need bigger number
                    j += 1
        return res


