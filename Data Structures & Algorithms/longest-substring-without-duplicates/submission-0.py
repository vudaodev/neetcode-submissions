'''
Input: string s
Output: length of longest substring without duplicates

Keep track of:
- longest substring seen
- all the values in current substring (Use hashset for O(1) lookup, add, del)

Two pointer technique: L and R
Check if val at R is already in set. 
If not, add to set. update longest substring without duplicates
If R is already in the set, we move L until s[L] matches s[R], then 1 more.
This ensures that all values in the substring are unique. Remove to remove s[L]
from HS as appropriate
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        longest = 0
        hs = set()

        for R in range(len(s)):
            # Add value at R to hashset and update longest
            if s[R] not in hs:
                hs.add(s[R])
                longest = max(len(hs), longest)
            else: # Shrink window to get rid of duplicates
                while s[L] != s[R]:
                    hs.remove(s[L])
                    L += 1
                L += 1

        return longest
            
