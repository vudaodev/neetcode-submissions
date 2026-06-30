class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Strings cannot be anagrams of each other if they are of different lengths
        # Method 1: Sort both strings and check for equality. O(n log n) time/ O(1) space?
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)