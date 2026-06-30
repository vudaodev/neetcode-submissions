class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + "#" + s
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            #We get here when j == #
            length = int(s[i:j])
            ret.append(s[j+1:j+1+length])
            i = j + 1 + length #this puts i at the end of the current string
        return ret
