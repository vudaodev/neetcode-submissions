'''
- Find the sum in array from index 0 to end
  -> This will be our starting rightSum
- Start pointer at index 0, and leftSum at 0
- while pointer < len(nums):
    - Compare leftSum and rightSum
        - if equal, return index
        - if not equal:
            add to leftSum
            remove from rightSum
            move pointer
    [1,7,3,6,5,6]
     ^            leftSum = 0, rightSum = 27
       ^          leftSum += 1 = 1, rightSum -= 7 = 20
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        i, leftSum = 0,0
        while i < len(nums):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            i += 1
        
        return -1