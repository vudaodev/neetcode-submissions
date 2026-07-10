class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force solution: nested loops. O(n^2) complexity
        # 1 pass hashmap solution: T/C: O(n), S/C: O(n)
            # key = number, value = index
            # We loop through all i and num in nums: (enumerate)
                # If we have x in the hm such that x = target - currNum: return the two indices
                # Else, add to HM and move onto next num in nums
        hm = {}
        for i,num in enumerate(nums):
            desired = target - num
            if desired in hm:
                return [hm[desired], i]
            hm[num] = i