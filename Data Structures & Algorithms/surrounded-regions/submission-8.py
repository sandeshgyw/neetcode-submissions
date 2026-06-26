class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS,COLS= len(board),len(board[0])
        borders=set()
        visited=set()


        #find all 0s in boundary
        for i in range(ROWS):
            if board[i][0]=='O':
                borders.add((i,0))
            if board[i][COLS-1]=='O':
                borders.add((i,COLS-1))
        
        for j in range(COLS):
            if board[0][j] =='O':
                borders.add((0,j))
            if board[ROWS-1][j]=='O':
                borders.add((ROWS-1,j))
     

        def dfs(r,c):
            
            if r<0 or r>ROWS-1 or c<0 or c>COLS-1 or (r,c) in visited or board[r][c]=='X':
                return
            
            visited.add((r,c))
            
            if board[r][c]=='O':
              
                board[r][c]='T'

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        #the ones connected to those can never be surrounded so mark them say T
        for (r,c) in borders:
            dfs(r,c)

        #loop throguh the grod to find 0s and change them to X
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=='O':
                    board[i][j]="X"

        #rechange Ts to 0s

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=="T":
                    board[i][j]='O'

        
        