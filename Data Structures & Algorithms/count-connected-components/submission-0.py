class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList=defaultdict(list)
        visited=set()
        count=0
        
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node,parent):
            if node in visited:
                return
            
            visited.add(node)

            for nei in adjList[node]:
                if nei==parent:
                    continue
                dfs(nei,node)


        
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i,-1)

        return count

