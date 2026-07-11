class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS=len(grid),len(grid[0])
        LAND,WATER,CHEST=2147483647,-1,0
        queue=deque([])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==CHEST:
                    queue.append((i,j))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()

                for dr,dc in directions:
                    nr,nc=r+dr,c+dc

                    if 0<=nr<=ROWS-1 and 0<=nc<=COLS-1 and grid[nr][nc]==LAND:
                        grid[nr][nc]=grid[r][c]+1
                        queue.append((nr,nc))

        
                




        