class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS,COLS=len(board),len(board[0])

        row_map=defaultdict(set)
        col_map=defaultdict(set)
        box_map=defaultdict(set)

        for i in range(ROWS):
            for j in range(COLS):
                val=board[i][j]
                if val==".":
                    continue
                if val in row_map[i] or val in col_map[j] or val in box_map[(i//3,j//3)]:
                    return False
                
                col_map[j].add(val)
                row_map[i].add(val)
                box_map[(i//3,j//3)].add(val)

        return True