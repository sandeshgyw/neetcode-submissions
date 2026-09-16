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
        
        if not root:
            return False
        
        if not subRoot:
            return True

       
        
        def isSameTree(roo,subRoo):
            if not roo and not subRoo:
                return True
            if not roo:
                return False
            if not subRoo:
                return False
            if roo.val!=subRoo.val:
                return False
            

            return isSameTree(roo.left,subRoo.left) and isSameTree(roo.right,subRoo.right)
        
        if isSameTree(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

            

            
        