class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList=defaultdict(set)
        count=0
        visited=set()

        for a,b in edges:
            adjList[a].add(b)
            adjList[b].add(a)

        def dfs(i):
            
            if i in visited:
                return
            
            visited.add(i)

            for node in adjList[i]:
                if node not in visited:
                    dfs(node)
        
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)
        
        return count
            
            
