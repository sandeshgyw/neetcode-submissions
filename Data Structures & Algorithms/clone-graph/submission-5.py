"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adjList={}
        temp=node

        queue=deque([node])

        if not node:
            return
        while queue:
            node=queue.popleft()

            if node in adjList:
                copyNode=adjList[node]
            else:
                copyNode=Node(node.val)
                adjList[node]=copyNode
            
            for nei in node.neighbors:
                if nei in adjList:
                    copyNode.neighbors.append(adjList[nei])
                else:
                    newNode=Node(nei.val)
                    adjList[nei]=newNode
                    copyNode.neighbors.append(newNode)
                    queue.append(nei)
        
        return adjList[temp]

        