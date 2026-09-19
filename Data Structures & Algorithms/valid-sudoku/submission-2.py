from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        box = defaultdict(set)  # key (row//3, column//3)

        for row in range(9):
            for column in range(9):
                val = board[row][column]
                if val == ".":
                    continue

                if (
                    val in rows[row]
                    or val in columns[column]
                    or val in box[(row // 3, column // 3)]
                ):
                    return False

                rows[row].add(val)
                columns[column].add(val)
                box[(row // 3, column // 3)].add(val)

        return True
