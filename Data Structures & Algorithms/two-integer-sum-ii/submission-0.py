class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R: 
            current_sum = numbers[L] + numbers[R]
            if current_sum == target:
                return [L + 1, R + 1]
            elif current_sum > target: # Need smaller number
                R -= 1
            else: # Need bigger number
                L += 1
