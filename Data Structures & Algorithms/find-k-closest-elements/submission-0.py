class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # L at starting index, R at ending index
        # While window size is greater than k, 
        # We remove L or R (whichever is furthest from x)
        L, R = 0, len(arr) - 1
        while R - L + 1 > k:
            # L is closer
            if abs(arr[L] - x) <= abs(arr[R] - x):
                R -= 1
            else: 
                L += 1
        
        return arr[L:R+1]