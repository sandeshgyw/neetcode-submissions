class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        freshFruits=0
        queue=deque([])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    freshFruits+=1
        
        if freshFruits==0:
            return 0
        
        time=0
        
        while queue:
            print(time)
            for _ in range(len(queue)):
                r,c=queue.popleft()

                if r+1<ROWS and grid[r+1][c]==1:#left
                    grid[r+1][c]=2
                    queue.append((r+1,c))
                    freshFruits-=1

                if r-1 >=0 and grid[r-1][c]==1:#rt
                    grid[r-1][c]=2
                    queue.append((r-1,c))
                    freshFruits-=1

                if c+1<COLS and grid[r][c+1]==1:#bot
                    grid[r][c+1]=2
                    queue.append((r,c+1))
                    freshFruits-=1

                if c-1>=0 and grid[r][c-1]==1:#top
                    grid[r][c-1]=2
                    queue.append((r,c-1))
                    freshFruits-=1
            time+=1
       

        if freshFruits!=0:
            return -1
        
        
        return time-1
              




                

        