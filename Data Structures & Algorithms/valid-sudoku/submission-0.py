from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set) # Key (row // 3, column // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                if val in rows[r]:
                    return False

                if val in columns[c]:
                    return False
                
                if val in boxes[r//3, c//3]:
                    return False
                
                rows[r].add(val)
                columns[c].add(val)
                boxes[r//3, c//3].add(val)
        
        return True
        