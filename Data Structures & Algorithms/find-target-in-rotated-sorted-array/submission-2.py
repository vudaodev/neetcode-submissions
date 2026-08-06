'''
Two pass binary search :
1. Find the minimum point 
2. Find the appropriate half to search
3. Search the appropriate half and return index or -1

[1,2,3,4,5] -> l < r: l is min
[5,1,2,3,4] -> l > r, m < l, search left inc
[4,5,1,2,3] -> l > r, m < l, search left inc
[3,4,5,1,2] -> l > r, m > l, search right
[2,3,4,5,1] -> l > r, m > l, search right
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. Find the minimum point
        l,r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]:
                break
            m = (l+r)//2
            if nums[m] < nums[l]:
                r = m
            else:
                l = m + 1
        lowest_i = l
        # 2. Find the appropriate half to search  
        # one half is index l -> end, other half is index 0 -> l-1
        if lowest_i != 0 and target >= nums[0] and target <= nums[lowest_i - 1]:
            l,r = 0, lowest_i - 1
        else:
            l,r = lowest_i, len(nums) - 1
        # 3.Search the appropriate half
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target: #search left
                r = m - 1
            else:
                l = m + 1
        return -1