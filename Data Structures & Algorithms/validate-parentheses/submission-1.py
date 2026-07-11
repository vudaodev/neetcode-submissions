class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False 
        hm = {'(': ')', '[': ']', '{': '}'}
        stack = [] # LIFO
        for bracket in s: # Opening bracket
            if bracket in hm: 
                stack.append(bracket)
            else: # Closing bracket
                if not stack or (bracket != hm[stack[-1]]):
                    return False
                # Closing bracket matches top of stack. Close the bracket and remove. 
                stack.pop()
        if not stack:
            return True
        return False    
    # Edge case: odd length means it is impossible to have only pairs of valid open/close brackets.
        # Return False
    # Use a hashmap to map the pairs of opening and closing brackets (PRE-DETERMINED)
    # Use a stack to keep track of opening brackets that still need to be closed
        # Create an empty stack to start
    # Loop through all brackets within the string S:
        # Opening bracket: 
            # Add it to our stack
        # Closing bracket:
            # 1. Bracket can close the opening bracket on the top of our stack
                # -> Remove the opening bracket on the top of our stack
            # 2. Stack is empty
                # -> Return False
            # 3. Opening bracket at top of stack and our closing bracket do not match
                # -> return False

    # If stack is empty, we return True. Else we return False.

    # T/C: O(n), where n is the length of s
    # S/C: O(n) 