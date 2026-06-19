# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        def lca(parent,p,q):
            if p.val<=parent.val and q.val>=parent.val:
                return parent
            
            if p.val==parent.val and q.val<parent.val:
                return parent
            
            
            
            if p.val<parent.val and q.val<parent.val:
                return lca(parent.left,p,q)
            elif p.val>parent.val and q.val>parent.val:
                return lca(parent.right,p,q)

        return lca(root,p,q)
         
        