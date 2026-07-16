'''
L and R pointers
Calculate M index

If value at index M is the target, return index M
If value < target, search right
If value > target, search left

If we have 1 value left, and its not the target return -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R: 
            M = (L + R) // 2
            if nums[M] == target:
                return M
            elif nums[M] < target:
                L = M + 1
            else:
                R = M - 1
        return -1