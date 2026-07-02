class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #replce INF with the closest distance to a chest:0
        #-1 is invalid i.e if we see -1 we dont need to traverse it

        INF=2147483647
        treasures=set()
        queue=deque([])

        #lets first store all the gate indices

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    treasures.add((i,j))
                    queue.append((i,j))

        #treasures has all the chests indices
        level=0

        while queue:
            level+=1
            
            for _ in range(len(queue)):
                r,c=queue.popleft()

                if r+1 <len(grid) and grid[r+1][c]==INF:
                    grid[r+1][c]=level
                    queue.append((r+1,c))
                if r-1>=0 and grid[r-1][c]==INF:
                    grid[r-1][c]=level
                    queue.append((r-1,c))
                if c+1 < len(grid[0]) and grid[r][c+1]==INF:
                    grid[r][c+1]=level
                    queue.append((r,c+1))
                if c-1 >=0 and grid[r][c-1]==INF:
                    grid[r][c-1]=level
                    queue.append((r,c-1))
            

            
                
                    
        
    

        