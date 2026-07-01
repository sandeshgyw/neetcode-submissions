class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        def dfs(i,j):
            if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1 or board[i][j]!='O':
                return
            
            board[i][j]="T"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        

            

            

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[0][j]=='O':
                    dfs(0,j)
                elif board[len(board)-1][j]=='O':
                    dfs(len(board)-1,j)
                elif board[i][0]=='O' :
                    dfs(i,0)
                elif board[i][len(board[0])-1]=='O': 
                    dfs(i,len(board[0])-1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O":
                    board[i][j]="X"
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="T":
                    board[i][j]="O"
        
                    
                    

        