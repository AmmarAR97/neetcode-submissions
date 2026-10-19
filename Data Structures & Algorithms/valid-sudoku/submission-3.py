from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        columns = defaultdict(list)
        boxes = defaultdict(list) #key=r//w,c//3
        for row in range(9):
            for column in range(9):
                val = board[row][column]

                if val == ".":
                    continue
                
                if val in rows[row]:
                    return False
                
                rows[row].append(val)
                
                if val in columns[column]:
                    return False

                columns[column].append(val)

                box_key = row // 3, column // 3
                if val in boxes[box_key]:
                    return False
                
                boxes[box_key].append(val)
        
        return True
