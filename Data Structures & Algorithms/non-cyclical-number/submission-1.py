class Solution:
    def isHappy(self, n: int) -> bool:
        hm = {}
        while n != 1:
            if n in hm: # We've encountered n before, therefore cycle
                return False
            # If newN is 1, we have a happy number. Else add to HM
            newN = self.sumSquareDigits(n)
            if newN == 1:
                return True
            hm[n] = newN
            n = newN
        return True

    def sumSquareDigits(self, n: int) -> int:
        ''' Returns the sum of the square of all digits'''
        res = 0
        for digit in str(n):
            res += (int(digit)**2)
        return res

    # Replace integer with sum of its digits squared:
    # 100 -> 1^2 + 0^2 + 0^2 = 0
    # How do we know if we have a loop?
        # We get a number we've gotten already
        # In that case, return False
    # We can use a hashmap to spot whether we've seen a number already
        # Key of hm: the number, Value of hm: sum of the number's digits
    

    