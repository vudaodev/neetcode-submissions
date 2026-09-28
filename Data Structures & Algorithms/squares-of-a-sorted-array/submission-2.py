'''
1. Square all of the numbers
2. 2 pointer approach going from S and E to lowest point. put into res.
3. return res.

'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for _ in range(len(nums)):
            nums[_] = nums[_]**2
        S, E = 0, len(nums) - 1
        res = [-1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[S] > nums[E]:
                res[i] = nums[S]
                S += 1
            else: 
                res[i] = nums[E]
                E -= 1
        # while S < E:
        #     if nums[S] > nums[E]:
        #         res[r] = nums[S]
        #         S += 1
        #     else: 
        #         res[r] = nums[E]
        #         E -= 1
        #     r -= 1
        # res[0] = nums[S]
        return res


