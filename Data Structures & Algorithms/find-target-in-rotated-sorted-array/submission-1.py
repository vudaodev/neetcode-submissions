'''
Two pass binary search:

- 1. Find pivot point (lowest value) that splits the rotated sorted array into two
- 2. Find appropriate half
- 3. Perform binary search on the appropriate half of the array

L = Left index, l = value at L
R = Right index, r = value at R
M = Middle index, m = value at M
[1,2,3,4,5] l < r => l is the lowest value
[5,1,2,3,4] l > r, m < r => search left inc
[3,4,5,1,2] l > r, m > r => search right

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find index of lowest value:
        lowest_i = 1000
        L,R = 0, len(nums) - 1
        while L <= R:
            M = (L+R)//2
            if nums[L] <= nums[R]:
                lowest_i = L
                break
            else:
                if nums[M] < nums[R]:
                    R = M
                elif nums[M] > nums[R]:
                    L = M + 1
        # Finding the subarray to search in
        L, R = 0, len(nums) - 1
        if target >= nums[lowest_i] and target <= nums[-1]:
            L = lowest_i
        elif lowest_i > 0 and target >= nums[0] and target<= nums[lowest_i - 1]:
            R = lowest_i - 1
        else:
            return - 1

        # Binary search to find index of target:
        while L <= R:
            M = (L+R)//2
            if nums[M] == target: return M
            elif nums[M] > target:
                R = M - 1
            elif nums[M] < target:
                L = M + 1
        return -1

