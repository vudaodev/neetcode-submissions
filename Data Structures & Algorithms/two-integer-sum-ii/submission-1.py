'''
Two pointer approach: We will treat as 0 based index, then return [L+1, R+1]
L at beginning, R at end

If we have our target: return [L+1, R+1]
If solution is too big, decrement R
If solution is too small, increment L

T/C: O(n), S/C: O(1)
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R:
            total = numbers[L] + numbers[R]
            if total == target:
                return [L+1, R+1]
            elif total > target:
                R -= 1
            else: 
                L += 1