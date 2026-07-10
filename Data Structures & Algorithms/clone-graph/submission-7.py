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
            return
        oldToNew={}
        

        def cloneNode(nod):
           
            if nod in oldToNew:
                return oldToNew[nod]
            
            
            
            copy=Node(nod.val)
            oldToNew[nod]=copy

            for nei in nod.neighbors:
                copy.neighbors.append(cloneNode(nei))
            
            return copy
        
        return cloneNode(node)
        
        