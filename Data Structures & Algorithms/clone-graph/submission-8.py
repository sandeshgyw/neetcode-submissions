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
        queue=deque([node])
        copyRoot=Node(node.val)

        oldToNew={node:copyRoot}
        

        while queue:
            nod=queue.popleft()

            for nei in nod.neighbors:
                if nei not in oldToNew:
                    copy=Node(nei.val)
                    oldToNew[nei]=copy
                
                    oldToNew[nod].neighbors.append(oldToNew[nei])
                    queue.append(nei)
                else:
                    oldToNew[nod].neighbors.append(oldToNew[nei])
        

        return oldToNew[node]



                
        
        