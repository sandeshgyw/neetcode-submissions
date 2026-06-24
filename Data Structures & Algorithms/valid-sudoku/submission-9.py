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
        # we have 9 boxes
        # we need a key for these 9 boxes

        # 0,0 1 2    3 4 5     6 7 8
        # 1,0
        # 2,0   
        boxSet=defaultdict(list)
        for i in range(0,9,3): # 0,3,6
            for j in range(0,9,3): # 0,3,6
            #0,0 0,3 0,6. 3,0 3,3 3,6. 6,0 6,3 6,6

            # now in each box we have 9 items to loop thorugh
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l]==".":
                            continue
                        if board[k][l] in boxSet[i,j]:
                            return False
                        boxSet[i,j].append(board[k][l])

        return True
                    
        



                
                


        