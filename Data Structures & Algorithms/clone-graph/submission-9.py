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
        adjList={}

        def clone(nod):
            if nod in adjList:
                return adjList[nod]

            copy=Node(nod.val)
            adjList[nod]=copy

            for nei in nod.neighbors:
                copy.neighbors.append(clone(nei))
            
            
            
            return copy
        
        clone(node)

        return adjList[node]



                
        
        