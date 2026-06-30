class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit == ".": 
                    continue
                
                b = (r // 3) * 3 + (c // 3)

                if digit in rows[r] or digit in cols[c] or digit in boxes[b]:
                    return False # duplicate found
        
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[b].add(digit)

        return True