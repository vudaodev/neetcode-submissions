class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs: 
            res.append(f'{len(string)}#{string}')
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        # List that keeps track of strings
        res = []
        L, R = 0, 0
        # If R reaches the of 's' end our while loop:
        while R < len(s):
            # Increment index R until it reaches a #
            while s[R] != '#':
                R += 1
            # When R reaches #, we know that the length of our string is: s[L:R]
            # s[L:R]. 
            # The corresponding word starts at R+1.
            length = int(s[L:R])
            res.append(s[R+1:R+1+length])
            # After appending the word, we increment L and R to be R + 1 + length
            L = R + 1 + length
            R = R + 1 + length
        return res