# [3,2,2,3]
# 2 pointers
# L pointer is next spot where we can place an element
# R pointer traverses array nums
# k = number of elements not equal to val

# traverse the array with R:
    # if element != val: set nums[L] = nums[R], L += 1 
# return k (same as L)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0
        for V in nums:
            if  V != val:
                nums[L] = V
                L += 1
        return L