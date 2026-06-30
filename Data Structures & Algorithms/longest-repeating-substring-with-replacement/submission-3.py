from collections import Counter 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        L = 0
        counts = {}

        for R in range(len(s)):
            if s[R] not in counts:
                counts[s[R]] = 0
            counts[s[R]] += 1

            while R - L + 1 > max(counts.values()) + k:
                counts[s[L]] -= 1
                L += 1
    
            longest = max(longest, R - L + 1)

        return longest