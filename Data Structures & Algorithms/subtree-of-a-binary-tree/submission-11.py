# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        
        if not subRoot:
            return True
        
        
    

        def isSameTree(p,q):
            if not p and not q :
                return True
            #both are None

            # if it proceeds means at least one is not None
            if not p or not q:
                return False
            
            if p.val!=q.val:
                return False

            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        
        if isSameTree(root,subRoot):
            return True
        
        return isSameTree(root.left,subRoot) or isSameTree(root.right,subRoot)