class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS=len(heights),len(heights[0])
        pacific_set=set()
        atlantic_set=set()
        
        pacific_visited_set=set()
        atlantic_visited_set=set()

        result=[]
        
  
        
        def dfs(i,j,visited,previousHeight,visited_set):
            if i<0 or i>ROWS-1 or j<0 or j>COLS-1 or (i,j) in visited_set:
                return

            

            if heights[i][j]<previousHeight:
                return
                
            visited.add((i,j))
            
            visited_set.add((i,j))

            dfs(i+1,j,visited,heights[i][j],visited_set)
            dfs(i-1,j,visited,heights[i][j],visited_set)
            dfs(i,j+1,visited,heights[i][j],visited_set)
            dfs(i,j-1,visited,heights[i][j],visited_set)


        #pacific sets
        for i in range(ROWS):
            for j in range(COLS):
                if i==0 or j==0:
                    #pacific touching cells
                    dfs(i,j,pacific_set,heights[i][j],pacific_visited_set)
                    
                if i==ROWS-1 or j==COLS-1:
                    #atlantic touching cells
                    dfs(i,j,atlantic_set,heights[i][j],atlantic_visited_set)
        
        for r,c in pacific_set:
            if (r,c) in atlantic_set:
                result.append([r,c])
        
        return result




            





        