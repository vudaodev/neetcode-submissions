class Solution:
    # 5#Hello5#World
    def encode(self, strs: List[str]) -> str:
        # Create a list with the strings in this format:
        # length of string + delimiter + string
        strs2 = [f'{len(s)}#{s}' for s in strs]
        # Join into one string and return
        return ''.join(strs2)
    def decode(self, s: str) -> List[str]:
        # Empty list for the strings:
        res = []
        # Two pointer method to get the individual strings
        i,j = 0,0
        while i in range(len(s)):
            # Move j until we hit a Delimiter, to find length of word:
            while s[j] != '#':
                j += 1
            lengthOfWord = int(s[i:j])
            # Add Word to the list:
            i = j + 1
            j = j + 1 + lengthOfWord
            word = s[i:j]
            res.append(word)
            # Move i:
            i = j
        return res