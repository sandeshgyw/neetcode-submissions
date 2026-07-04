class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS= len(heights),len(heights[0])

        pacific_set=set()
        atlantic_set=set()
        result=[]

        
        def dfs(r,c,visited,prevHeight):
            if r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visited:
                return
            if prevHeight>heights[r][c]:
                return
            visited.add((r,c))
            if prevHeight<=heights[r][c]:
                dfs(r+1,c,visited,heights[r][c])
                dfs(r-1,c,visited,heights[r][c])
                dfs(r,c+1,visited,heights[r][c])
                dfs(r,c-1,visited,heights[r][c])

        for i in range(ROWS):
            for j in range(COLS):
                if i==0 or j==0:
                    dfs(i,j,pacific_set,0)
                if i==ROWS-1 or j==COLS-1:
                    dfs(i,j,atlantic_set,0)

        for r,c in pacific_set:
            if (r,c) in atlantic_set:
                result.append([r,c])

        return result