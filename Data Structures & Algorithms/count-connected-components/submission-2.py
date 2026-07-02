class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList=defaultdict(list)
        visited=set()
        connected=0
        

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node,visited):
            if node in visited:
                return
            
            visited.add(node)

            for nei in adjList[node]:
                dfs(nei,visited)

        
        for i in range(n):
            if i not in visited:
                dfs(i,visited)
                connected+=1
        return connected

            
            

        