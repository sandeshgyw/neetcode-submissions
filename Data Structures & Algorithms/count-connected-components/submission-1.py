class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList=defaultdict(list)
        connectedCount=0
        visited=set()

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(i,parent):
            #0,1,2
            #visits all components connected to this node
            if i in visited:
                return
            #visited=0,1,2
            visited.add(i)

            for nei in adjList[i]:
                #1
                if parent==nei:
                    continue
                dfs(nei,i)
            
            return
            

        
        for i in range(n):
            if i not in visited:
                #if it enters here means it is a new unconnected node
                connectedCount+=1
                dfs(i,-1)
        
        return connectedCount

        