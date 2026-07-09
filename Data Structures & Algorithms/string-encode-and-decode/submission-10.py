class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(f"{len(string)}#{string}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find length of word
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # Append word to res
            start_of_word = j + 1 
            end_of_word = j + 1 + length #exclusive
            word = s[start_of_word:end_of_word]
            res.append(word)
            # Move i:
            i = end_of_word
        return res
    # Process of encoding:
    # In order to decode, we need to know the length of each string.
    # Hello is 5 letters long, World is 5 letters long
    #['Hello','World] => '5#Hello5#World'

    # Process of decoding:
    # Make an empty array to store our words
    #'5#Hello5#World' => ['Hello','World] 
    # First we find the length of a word, Then we add that word to an array
    # We return when we have ran out of words
    
    # Time and space: O(n*m)
    # n = number of strings, m = length of average string