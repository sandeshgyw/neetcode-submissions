class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW,COL=9,9

        row_set=defaultdict(set) # makes sure no repitition in a row
        col_set=defaultdict(set)# makes sure no rep in col
        box_set=defaultdict(set)#makes sure no rep in a box

        for r in range(ROW):
            for c in range(COL):
                if board[r][c]==".":
                    continue
                
                if board[r][c] in row_set[r] or board[r][c] in col_set[c] or board[r][c] in box_set[(r//3,c//3)]:
                    return False
                
                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                box_set[(r//3,c//3)].add(board[r][c])
        
        return True



        