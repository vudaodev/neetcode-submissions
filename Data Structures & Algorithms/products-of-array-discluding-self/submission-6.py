'''
Pre -> Product of all values before nums[i]
Post -> Product of all values after nums[i]

Start Prefix/Post as arrays of 1's (same length as nums)
nums = [1,2,4,6], pre = [1,1,2,8], post = [1,1,1,1]
Loop through the indices of pre from index 1 -> end
    pre[i] = pre[i-1] * nums[i-1]
    pre[1] = 1, pre[2] = 2*1 = 2, pre[3] = 4*2 = 8
Loop through indices of post from 2nd last index to index 0
    post[i] = post[i+1] * nums[i+1]
    post[2] = post[3] * nums[3] = 6 * 1 = 6 
output = post * pre for every index
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]* len(nums)

        # Prefix:
        prefixProd = 1
        for i in range(0,len(nums)):
            output[i] = prefixProd
            prefixProd *= nums[i]
        # Suffix:
        suffixProd = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= suffixProd
            suffixProd*= nums[i]
        
        return output