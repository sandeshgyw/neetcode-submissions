class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #from borders O start dfs and makr them as say T
        #then reloop and turn all Os to X
        #then turn all Ts to O

        ROWS,COLS=len(board),len(board[0])

        def dfs(r,c):
            if r<0 or r>ROWS-1 or c<0 or c>COLS-1 or board[r][c]!="O":
                return
            
            board[r][c]="T"

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if i==0 or i==ROWS-1:
                    if board[i][j]=='O':
                        dfs(i,j)
                
                if j==0 or j==COLS-1:
                    if board[i][j]=='O':
                        dfs(i,j)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=='O':
                    board[i][j]="X"
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=="T":
                    board[i][j]="O"


        