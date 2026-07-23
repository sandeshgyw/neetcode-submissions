class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        rottenFruitCount=0
        freshFruitCount=0
        EMPTY,FRESH,ROTTEN=0,1,2
        queue=deque([])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==FRESH:
                    freshFruitCount+=1
                if grid[i][j]==ROTTEN:
                    rottenFruitCount+=1
                    queue.append((i,j))
        
        if freshFruitCount==0:
            return 0
        if rottenFruitCount==0:
            return -1

        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        minutes=0
        
        while queue and freshFruitCount>0:
            minutes+=1
            for _ in range(len(queue)):
                r,c=queue.popleft()

                for dr,dc in directions:
                    nr,nc=r+dr,c+dc

                    if nr<0 or nr>ROWS-1 or nc<0 or nc>COLS-1:
                        continue

                    if grid[nr][nc]==FRESH:
                        grid[nr][nc]=ROTTEN
                        freshFruitCount-=1
                        queue.append((nr,nc))
        
        if freshFruitCount!=0:
            return -1
        
        return minutes
                    

                





        