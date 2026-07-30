"""
input: array of temps
output: result, where result[i] is the number of days after ith day before a warmer 
temp appears

Edge case: If no warmer temp exists, answer is 0
Use a stack to keep track of temp/indice pairs that we need an answer for

Loop through the numbers in temp:
    while curr_temp > top of stack:
        - pop top of stack
        - edit output array (result)
    After stack is empty or there are no more smaller values, add curr_temp 
Return results

T/C/: O(n), S/C: O(n)
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0]*len(temperatures)
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                top_i, top_v = stack.pop()
                results[top_i] = i - top_i
            stack.append([i,v])
        return results