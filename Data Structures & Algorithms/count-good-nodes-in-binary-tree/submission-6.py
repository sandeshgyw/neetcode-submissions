# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    good=0
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def dfs(node,pathMax):
            #this function if finds good node adds 1 to result
            if not node:
                return
            if node.val>=pathMax:
                pathMax=node.val
                self.good+=1
            
            leftNodes=dfs(node.left,pathMax)
            rightNodes=dfs(node.right,pathMax)

            

        dfs(root,root.val)
        return self.good

