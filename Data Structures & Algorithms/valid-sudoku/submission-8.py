class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS,COLS=9,9

        #if invalid then return False
        # so we check all invalids and if passes then return True

        # row has no repititions

        for i in range(ROWS):
            rowSet=set()
            for j in range(COLS):
                if board[i][j]==".":
                    continue
                if board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])
                


        colSet=set()

        #col has no repititions

        for i in range(ROWS):
            colSet.clear()
            for j in range(COLS):
                if board[j][i]==".":
                    continue 
                if board[j][i] in colSet:
                    return False
                colSet.add(board[j][i])
        
        boxSet=defaultdict(list)

        #sub box has no repititions
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]==".":
                    continue
                
                if board[i][j] in boxSet[i//3,j//3]:
                    return False
                
                boxSet[i//3,j//3].append(board[i][j])
        
        return True



        



                
                


        