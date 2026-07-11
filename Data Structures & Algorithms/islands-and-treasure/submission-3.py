class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS=len(grid),len(grid[0])
        LAND,WATER,CHEST=2147483647,-1,0
        queue=deque([])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==CHEST:
                    queue.append((i,j))
        
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()

                #go right
                if r+1<=ROWS-1 and grid[r+1][c]==LAND:
                    grid[r+1][c]=grid[r][c]+1
                    queue.append((r+1,c))
                
                #go left
                if r-1>=0 and grid[r-1][c]==LAND:
                    grid[r-1][c]=grid[r][c]+1
                    queue.append((r-1,c))
                
                #go bot
                if c+1<=COLS-1 and grid[r][c+1]==LAND:
                    grid[r][c+1]=grid[r][c]+1
                    queue.append((r,c+1))
                
                #got top
                if c-1>=0 and grid[r][c-1]==LAND:
                    grid[r][c-1]=grid[r][c]+1
                    queue.append((r,c-1))
        
                




        