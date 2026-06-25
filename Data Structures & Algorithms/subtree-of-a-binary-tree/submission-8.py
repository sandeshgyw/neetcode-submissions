# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p,q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val!=q.val:
                return False
            
            left=isSameTree(p.left,q.left)#is left sub tree same
            right=isSameTree(p.right,q.right) #is right subtree same

            return left and right
            
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        if isSameTree(root,subRoot):
            return True
        
        return isSameTree(root,subRoot) or isSameTree(root.left,subRoot) or isSameTree(root.right,subRoot)
        

        


            


        