'''
Edge cases:
target out of range, early False return

1. Perform binary search to find the row
top, middle, bottom
if target < middle[0]: search top
if target > middle[-1]: search bottom
2. if target is in the middle column, perform second binary search (standard L,M,R)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # if target < matrix[0][0] or target > matrix[-1][-1]:
        #     return False
        
        t,b = 0, len(matrix) - 1
        while t <= b:
            m = (t + b)//2
            if target < matrix[m][0]:
                b = m - 1
            elif target > matrix[m][-1]:
                t = m + 1
            else:
                row = matrix[m]
                L, R = 0, len(matrix[0])
                while L <= R:
                    M = (L+R)//2
                    if row[M] == target:
                        return True
                    elif row[M] > target:
                        R = M - 1
                    elif row[M] < target:
                        L = M + 1
                return False
        return False