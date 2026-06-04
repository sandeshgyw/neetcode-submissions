class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent={}
        rank={}

        for i in range(len(edges)):
            parent[i+1]=i+1
            rank[i+1]=i

        def find(node):
            #cool finds path
            #but isnt it better if we update even id we find answer of what we did not need
            if parent[node]==node:
                return parent[node]
            
            return find(parent[node])



        def union(node1,node2):
            root1=find(node1)
            root2=find(node2)

            if root1==root2:
                return False
            
            if rank[root1]<rank[root2]:
                parent[root1]=root2
            elif rank[root1]>rank[root2]:
                parent[root2]=root1
            else:
                parent[root2]=root1
                rank[root1]+=1
            
            return True

            





        for a,b in edges:
            if not union(a,b):
                return [a,b]
            
        return []

        


                    




      




