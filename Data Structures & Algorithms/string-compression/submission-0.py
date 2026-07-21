'''
Input: chars array

Output:
Directly modify chars array
return k (length of compressed string)

Constraints: 
Only use constant extra space

Approach: 
2 Pointer method 
-> L (write pointer)
-> R (read pointer)
-> Count


["A","A","B"]
 LR             Count of 'A' = 1, Set chars[L] to 'A'
 L    R         Count of 'A' = 2
 L        R     New character. We need to use Left pointer to write "2" then 
                we can proceed.                 
["A","2","B"]
      L   R
'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        L, R = 0, 0
        count = 0

        while R < len(chars):
            chars[L] = chars[R]
            while R < len(chars) and chars[R] == chars[L]: 
                R += 1  
                count += 1
            # R is now pointing at a different value or out of range
            L += 1 # move L to next writable spot so we can start 
                   # appending numbers if needed
            if count > 1:
                count_string = str(count)
                for char in count_string:
                    chars[L] = char
                    L += 1
            count = 0 
            # L is now back at the next writable spot, and we have reset count
            # we can move onto next character if it exists
        return L
