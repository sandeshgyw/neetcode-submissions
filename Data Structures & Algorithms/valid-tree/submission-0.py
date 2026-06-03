class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjList=defaultdict(list)

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visiting=set()
        visited=set()

        def isValidTree(node,parent):
            # when this function ends we need to have all components visited
            if node in visiting: # visiting=[0,1]
                return False
            
            visiting.add(node)

            for nei in adjList[node]:
                if nei==parent:
                    continue
                
                if not isValidTree(nei,node):
                    return False
            
            visiting.remove(node)
            visited.add(node) # visited=[4]
            
            return True


        
        return isValidTree(0,-1) and len(visited)==n
        # for tree to be valid:
        # all node connnected, so start from one should reach all other
        # no loop, use parent to remove false true




        