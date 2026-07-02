class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Implement a two-pointer solution where you have a pointer that starts at the beginning and a pointer that starts at the end. 
        # Stop when:
            # L and R pointers meet OR 
            # L and R are not equal (return false)
        # When L or R isn't alphanumeric, we skip
        # If we reach the end and we have't returned false, return true     
        L, R = 0, len(s) - 1
        while L < R:
            while not s[L].isalnum() and L < R:
                L += 1
            while not s[R].isalnum() and L < R:
                R -= 1
            # Check for equality    
            if s[L].lower() != s[R].lower():
                return False 
            # Move pointers
            L += 1
            R -= 1
        return True