class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adjList=defaultdict(list)

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        #O(E)

        #adjList={1:[2,3],2:[1,4],3:[1,4],4:[2,3]}
        visited=set()

        def dfs(node,parent):
            if node in visited:
                return False
            
            visited.add(node)

            for nei in adjList[node]:
                if nei==parent:
                    continue
                
                if not dfs(nei,node):
                    return False
            
            return True
        
        for i in range(len(edges)-1,-1,-1):
            #O(E)
            visited.clear()
            adjList[edges[i][0]].remove(edges[i][1])
            adjList[edges[i][1]].remove(edges[i][0])
            if dfs(1,-1) and len(visited)==len(edges):
                return edges[i]
            adjList[edges[i][0]].append(edges[i][1])
            adjList[edges[i][1]].append(edges[i][0])



                    




      




