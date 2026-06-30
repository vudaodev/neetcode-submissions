class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = [0]*26
        t_count = [0]*26

        for _ in s:
            s_count[ord(_)-ord('a')] += 1
        
        for _ in t:
            t_count[ord(_)-ord('a')] += 1

        return s_count == t_count