"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None


        queue=deque([node])
        adjList={}

        while queue:
            nod=queue.popleft()

            if nod not in adjList:
                adjList[nod]=Node(nod.val)
            copy=adjList[nod]


            for nei in nod.neighbors:
                if nei not in adjList:
                    copynei=Node(nei.val)
                    adjList[nei]=copynei
                    queue.append(nei)
                
                copy.neighbors.append(adjList[nei])
                
        
        return adjList[node]
                    






                
        
        