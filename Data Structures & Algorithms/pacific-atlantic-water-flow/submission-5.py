class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result=[]
        #cells where both pacific and atlantic can reach
        ROWS,COLS=len(heights),len(heights[0])

        #pacific cells [0][j] and [i][0]
        #atlantic cells [rows-1][j] and [i][cols-1]
        pacific_set=set()
        atlantic_set=set()

        def dfs(r,c,visited,oldHeight):
            if r<0 or r>ROWS-1 or c<0 or c>COLS-1 or (r,c) in visited or oldHeight>heights[r][c]:
                return
       
            
            visited.add((r,c))

            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])


        for i in range(ROWS):
            for j in range(COLS):
                if i==0 or j==0:
                    dfs(i,j,pacific_set,heights[i][j])    
                if i==ROWS-1 or j==COLS-1:
                    dfs(i,j,atlantic_set,heights[i][j])
        
        for r,c in pacific_set:
            if (r,c) in atlantic_set:
                result.append((r,c))
        
        return result
