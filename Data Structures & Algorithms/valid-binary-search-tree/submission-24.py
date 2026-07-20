# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #as false cases are more makes sense to return falses first
        if not root:
            return True

        #left subtree is less than parent


        #rtsubtree is more than parent

        #both are bST - hence recursion

        def valid(node,low,high):
            if not node:
                return True
            if node.val<=low or node.val>=high:
                return False

            return valid(node.left,low,node.val)  and valid(node.right,node.val,high)
        

        return valid(root,float('-inf'),float('+inf'))
        