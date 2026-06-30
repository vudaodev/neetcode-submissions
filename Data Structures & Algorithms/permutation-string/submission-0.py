from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window (fixed length)
        # 2 Hashmaps: 
        # 1 to keep track of frequencies of s1, 1 to keep track of frequencies in substring
        if len(s2) < len(s1):
            return False
        
        L, R = 0, len(s1) - 1
        F1, F2 = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            F1[s1[i]] += 1
        for i in range(len(s1) - 1): # we add the last value in first iteration of while loop
            F2[s2[i]] += 1

        while R < len(s2):
            F2[s2[R]] += 1

            if F1 == F2: 
                return True
            
            F2[s2[L]] -= 1
            if F2[s2[L]] == 0:
                del F2[s2[L]]

            L += 1
            R += 1

        return False