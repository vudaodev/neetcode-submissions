from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window (fixed length)
        # 2 Hashmaps that maintains frequencies (for s1 and s2 substring respectively)
        if len(s2) < len(s1): # Edgecase: We cannot have a permutation! 
            return False
        
        F1, F2 = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            F1[s1[i]] += 1
        
        L = 0
        for R in range(len(s2)):
            F2[s2[R]] += 1

            if R - L + 1 > len(s1):
                F2[s2[L]] -= 1
                if F2[s2[L]] == 0:
                    del F2[s2[L]]
                L += 1
            
            if F1 == F2: 
                return True


        return False 

