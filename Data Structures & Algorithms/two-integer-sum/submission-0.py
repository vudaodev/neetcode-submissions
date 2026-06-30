class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap: 
        # key = number
        # value = index of number

        # for each index:
            # if target - nums[index] is in the hashmap,
            # return the two indices
            # if not, add the num to our hashmap
        hm = {}

        for i in range(len(nums)):
            desired_num = target - nums[i]
            if desired_num in hm:
                return [hm[desired_num],i]
            hm[nums[i]] = i