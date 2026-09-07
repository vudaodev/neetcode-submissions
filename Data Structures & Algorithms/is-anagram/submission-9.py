'''
- Anagram means: contain same chars with each char appearing same amount of time

- Sorting: O(n log n + m log m) / O(1) -> timsort
    - sort the two strings and see if they match

- Array counting approach: O(n+m) / O(26) - > O(1)
    - Array that is 26 char long full of 0's 
    - index 0 represents 'a' and so on
    - add 1 for character counting in s
    - remove 1 for character counting in t
    - if array is only full of 0's at the end, we return True, else False
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0]*26
        for char in s:
            counts[ord('a') - ord(char)] += 1
        for char in t:
            counts[ord('a') - ord(char)] -= 1
        
        if counts == [0]*26:
            return True
        return False