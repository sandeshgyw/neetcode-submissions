class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS=9
        COLS=9

        row_set=defaultdict(list)
        col_set=defaultdict(list)
        box_set=defaultdict(list)
        #reps in any ==false

        #only if all fail pass then we get true
        #so to try and end it as quickly as possoble we try erasing the falses

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]==".":
                    continue
                if board[i][j] in row_set[i] or board[i][j] in col_set[j] or board[i][j] in box_set[(i//3,j//3)]:
                    return False
                row_set[i].append(board[i][j])
                col_set[j].append(board[i][j])
                box_set[(i//3,j//3)].append(board[i][j])
        return True


        