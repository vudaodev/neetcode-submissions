'''
- use a stack to keep track of elements that need to be computed
- If an element isn't an operation '+', '-', '*' or '/': add it to the stack
- When we reach an operation, compute the result in stack[0] and pop stack[1]
    - For example: if our stack is [3,3] and we reach "*", our new stack is [9]
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+","-","*","/"]
        stack = []
        for _ in tokens:
            if _ not in ops:
                stack.append(int(_))
                continue

            if _ == "+":
                res = stack[-2] + stack[-1]
                stack[-2] = res
            elif _ == "-":
                res = stack[-2] - stack[-1]
                stack[-2] = res
            elif _ == "*":
                res = stack[-2] * stack[-1]
                stack[-2] = res
            elif _ == "/":
                res = int(stack[-2] / stack[-1])
                stack[-2] = res
            stack.pop()

        return stack[0]