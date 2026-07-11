class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
            ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
            ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
            ["M", 1000]
        ]

        output = []

        for symbol, value in reversed(symList):
            count = num // value # 3750//1000 = 3
            output.append(count * symbol)
            remainder = num - value*count
            num = remainder
        
        return ''.join(output)

        # 1. Create a list that contains pairs of symbols and values
        # 2. Create an output list or array(to be converted into list)
        # 3. Loop through all of the symbols and values in symList, 
        # from largest to smallest and build our output
        # 4. Append to our output and subtract from num as appropriate
        # 5. Return our output

        
