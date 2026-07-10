class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm = {}
        for i in range(len(s)):
            if s[i] in hm:
                if hm[s[i]] != t[i]:
                    return False
            else:
                if t[i] in hm.values():
                    return False
                hm[s[i]] = t[i]
        return True
        # hm mapping from s to t
        # Loop through the indices in s and t
            # s[i] is in the hm
                # hm[s[i]] != t[i] -> early return False
                # hm[s[i]] == t[i] -> continue
            # s[i] != in the hm
                # t[i] is in values -> early return False 
                # t[i] is not in values -> hm[s[i]] = t[i]
        # Return True 
    # T/C: O(n), where n is the length of s and t
    # S/C: O(128) -> O(1)
    # s = abc , t = dee <- cannot do this 