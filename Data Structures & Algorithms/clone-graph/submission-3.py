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
        # this will store nodes we already created
        # as we only need one copy and need a way to access it

        if not node:
            return None

        def clone(node):
            #this function will return the cloned node of a node
            if node in adjList:
                return adjList[node]

            copyNode=Node(node.val)
            adjList[node]=copyNode

            for nei in node.neighbors:
                copyNode.neighbors.append(clone(nei))
            
            return copyNode
        
        clone(node)

        return adjList[node]
        