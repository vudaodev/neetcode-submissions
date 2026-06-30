class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Strings cannot be anagrams of each other if they are of different lengths
        if len(s) != len(t):
            return False
        # Use 2 hashmaps. Key = character. Value = character count. 
        # If the hashmap for S and T are the same, then we have a valid anagram.
        S, T = {}, {}
        for _ in s:
            if _ not in S:
                S[_] = 0
            S[_] += 1
        for _ in t:
            if _ not in T:
                T[_] = 0
            T[_] += 1
        return S == T
