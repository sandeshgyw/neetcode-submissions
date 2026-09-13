class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS=len(board),len(board[0])
        o_cells=set()
        border_o_cells=set()
        visited=set()

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='O':
                    o_cells.add((r,c))
                if r==0 or r==ROWS-1 or c==0 or c==COLS-1:
                    border_o_cells.add((r,c))
        

        def dfs(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visited or board[r][c]=="X":
                return
            
            visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for (r,c) in border_o_cells:
            if (r,c) not in visited:
                dfs(r,c)
        
        for (r,c) in o_cells:
            if (r,c) not in visited:
                board[r][c]="X"

        