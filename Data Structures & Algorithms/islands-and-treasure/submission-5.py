class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        WATER,LAND,TREASURE= -1,2147483647,0
       
        ROWS,COLS=len(grid),len(grid[0])
        queue=deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==TREASURE:
                    queue.append((r,c))
        
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()

                for dr,dc in directions:
                    nr,nc=r+dr,c+dc  

                    if nr<0 or nc<0 or nr>ROWS-1 or nc>COLS-1:
                        continue
                    
                    if grid[nr][nc]==LAND:
                        grid[nr][nc]=grid[r][c]+1
                        queue.append((nr,nc))
        
            






        