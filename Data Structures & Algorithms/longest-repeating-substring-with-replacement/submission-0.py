from collections import Counter 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        L = 0

        for R in range(len(s)):
            while R - L + 1 > Counter(s[L:R+1]).most_common()[0][1] + k:
                L += 1
            longest = max(longest, R - L + 1)

        return longest