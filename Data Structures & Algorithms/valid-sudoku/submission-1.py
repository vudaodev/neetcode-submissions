'''
Input: board = [[row1], 
                [row2],
                ...
                [row9]]
Ouput: True if board is valid, False otherwise

Each row cannot have duplicates -> 1 set for every row (9 total)
Each col cannot have duplicates -> 1 set for every col (9 total)
Each Box cannot have duplicates -> 1 set for every box (9 total)

Go through every
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.': continue
                #need condition for b!
                b = 3*(r//3) + (c//3)
                if val in rows[r] or val in cols[c] or val in boxes[b]:
                    return False
                rows[r].add(val), cols[c].add(val), boxes[b].add(val)
        
        return True