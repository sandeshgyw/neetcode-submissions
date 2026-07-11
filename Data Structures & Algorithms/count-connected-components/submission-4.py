class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList=defaultdict(list)
        components=0

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        
        visited=set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)


        for i in range(n):
            if i not in visited:
                components+=1
                dfs(i)
        return components