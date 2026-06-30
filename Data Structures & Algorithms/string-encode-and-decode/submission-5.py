class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for _ in strs:
            res.append(f'{len(_)}#{_}')
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        decoded_res = []
        i = 0
        while i < len(s):
            d_i = i
            while s[d_i] != '#':
                d_i += 1
            length = int(s[i:d_i])
            start_of_string = d_i + 1
            end_of_string = start_of_string + length
            decoded_res.append(s[start_of_string: end_of_string])

            i = end_of_string
        return decoded_res
