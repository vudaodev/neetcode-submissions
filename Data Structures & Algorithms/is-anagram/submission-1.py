class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0]*26
        for _ in s:
            count[ord(_)-ord('a')] += 1
        
        for _ in t:
            count[ord(_)-ord('a')] -= 1

        if count == [0]*26:
            return True
        return False