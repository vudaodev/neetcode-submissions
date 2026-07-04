class Solution:
    def isValid(self, s: str) -> bool:
        # 1. We need to keep track of which opening and closing brackets 
        # correspond with each other (hm)
        # 2. Keep track of brackets that need to be closed (in a stack)
        # in other words, our stack has to be empty or only contain opening brackets

        # False if: 
            # Odd number of characters
            # Get closing bracket but it does not match opening bracket (top of stack)
            # Get closing bracket, but stack is empty

        if len(s) % 2 != 0:
            return False
        
        hm = {'(': ')', '[': ']', '{': '}' }
        stack = []

        for _ in s:
            if _ in hm: # add to stack if we have opening bracket
                stack.append(_)
            else: # Closing bracket
                if not stack:
                    return False
                if hm[stack[-1]] == _: #closing bracket matches
                    stack.pop()
                else: #closing bracket does not match
                    return False

        if stack:
            return False
        return True
            
