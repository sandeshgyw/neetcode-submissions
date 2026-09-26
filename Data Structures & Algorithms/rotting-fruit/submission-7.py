class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        EMPTY,FRESH,ROTTEN=0,1,2
        freshCount=0
        queue=deque([])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==FRESH:
                    freshCount+=1
                if grid[i][j]==ROTTEN:
                    queue.append((i,j))
        time=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while freshCount!=0 and queue:
            time+=1
            for _ in range(len(queue)):
                r,c=queue.popleft()

                for dr,dc in directions:
                    nr,nc=r+dr,c+dc

                    if nr<0 or nc<0 or nr>ROWS-1 or nc>COLS-1 or grid[nr][nc]!=FRESH:
                        continue
                    
                    freshCount-=1
                    grid[nr][nc]=ROTTEN
                    queue.append((nr,nc))
        
        if freshCount!=0:
            return -1
        
        return time


                    

        





        