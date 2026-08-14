class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS=len(heights),len(heights[0])
        atlantic_set=set()
        pacific_set=set()
        result=[]

        


        def dfs(r,c,prevHeight,visited):
            if r<0 or c<0 or r>ROWS-1 or c>COLS-1 or (r,c) in visited:
                return
            
            if heights[r][c] < prevHeight:
                return
    
            visited.add((r,c))
            dfs(r+1,c,heights[r][c],visited)
            dfs(r-1,c,heights[r][c],visited)
            dfs(r,c-1,heights[r][c],visited)
            dfs(r,c+1,heights[r][c],visited)
        
        for r in range(ROWS):
            for c in range(COLS):
                #pacific
                if r==0 or c==0:
                   dfs(r,c,0,pacific_set)
                if r==ROWS-1 or c==COLS-1:
                    dfs(r,c,0,atlantic_set)
        for r,c in pacific_set:
            if (r,c) in atlantic_set:
                result.append((r,c))
        
        return result
        




        