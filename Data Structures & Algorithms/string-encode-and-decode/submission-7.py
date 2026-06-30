class Solution:
    #
    def encode(self, strs: List[str]) -> str:
        res = []
        for _ in strs:
            res.append(f'{len(_)}#{_}')
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        decoded_res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start_of_string = j + 1
            end_of_string = start_of_string + length
            decoded_res.append(s[start_of_string: end_of_string])
            i = end_of_string
        return decoded_res
