'''
Fixed sliding Window of length k
Maintain a set that includes all values within a sliding window

L = start of window
R = end of window

Everytime we slide the window:
- Remove the old L value from the set
- Attempt to Add the new R value to the set
    - If R is already in the set, return True

Return False if we get to the end of the window without returning
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        R = min(k, len(nums) - 1) 
        window = set(nums[L:R+1])
        if len(window) != R + 1: return True

        while R < len(nums) - 1:
            # Remove old L
            window.remove(nums[L])
            L += 1
            # Add new R
            R += 1
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False