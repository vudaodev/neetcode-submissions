'''
Use binary search since we need solution better than O(n)
L = Left index, l = value at L
R = Right index, r = value at R
M = Middle index, m = value at M
[1,2,3,4,5] -> l < r -> return l 
[5,1,2,3,4] -> l > r -> m < r -> search left (inclusive)
[4,5,1,2,3] -> l > r -> m < r -> search left (inclusive)
[3,4,5,1,2] -> l > r -> m > r -> search right
[2,3,4,5,1] -> l > r -> m > r -> search right
[2,1] -> l > r -> m == l -> search right
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            M = (L + R) // 2
            if nums[L] <= nums[R]:
                return nums[L]
            elif nums[L] > nums[R]: 
                if nums[M] < nums[R]: #search left
                    R = M
                elif nums[M] > nums[R]: #search right
                    L = M+1