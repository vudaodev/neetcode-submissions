'''
Need hashmap to keep track of frequencies in s and t.
Need indices to keep track of substring.
-> l_min, r_min or whatever. starts at 0,0

Minimum substring MUST have a character from t at the start and end of it. 

Everytime we move R pointer to a character that is in t:
    Check for substring
    If substring exists and it's shorter than previous substring, update l_min and r_min.

Condition for moving L: -> check logic again
    Once we've found a substring, we move L till substring is no longer valid.
    Remember to update l_min, r_min as appropriate.
'''
class Solution:

    def minWindow(self, s: str, t: str) -> str:
    
        l_min, r_min = 0, float('inf')
        L = 0
        countT, countS = {}, {}

        for _ in t:
            if _ not in countT:
                countT[_] = 0
            countT[_] += 1
        need, have = len(countT), 0

        for R in range(len(s)):
            r = s[R]
            if r in countT: # r is in T
                if r not in countS:
                    countS[r] = 0
                countS[r] += 1 # update count of r in S

                if countT[r] == countS[r]: #counts of r match for S and T
                    have += 1

            while have == need:
                if R - L < r_min - l_min:
                    r_min, l_min = R, L

                l = s[L]
                if l in countT:
                    if countS[l] == countT[l]:
                        have -= 1
                    countS[l] -= 1
                L += 1

        if r_min == float('inf'): return ""              
        return s[l_min: r_min + 1]
            

            