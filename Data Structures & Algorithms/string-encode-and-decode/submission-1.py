class Solution:
    # Format: number of characters, separator ±, string
    # 4±neet4±code4±love3±you
    # length = 3, j + 1 + length == j + 4
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "±" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "±": #increment until we find ±
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j + 1 + length
            
        return res