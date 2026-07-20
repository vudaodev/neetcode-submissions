'''
1. Create a list that contains lists with symbol, value pairs.
2. Create output list for roman numerals (will be joined later)
3. Loop through our list of lists in reverse order:
    - Subtract from 'num' as long as the 'num' > value
    - Append to output list
    - Note: only powers of 10 can be appended consecutively
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [
            ['I',1], ['IV',4], ['V',5], ['IX',9], ['X',10], ['XL',40],
            ['L',50], ['XC',90], ['C',100], ['CD',400],['D',500],
            ['CM',900], ['M',1000]
        ]
        output = []
        for symbol, value in reversed(symList):
            multiple = num // value # e.g. 3749 // 1000 = 3
            num -= (multiple * value) # e.g. 3749 - 3000 = 749
            output.append(multiple*symbol)

        return "".join(output)