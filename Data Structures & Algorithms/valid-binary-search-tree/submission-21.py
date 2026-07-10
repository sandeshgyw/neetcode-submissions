# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isValidNode(node,low,high):
            if not node:
                return True
            if node.val<low or node.val>high:
                return False
            
            left=isValidNode(node.left,low,node.val)
            right=isValidNode(node.right,node.val,high)

            if left and right:
                return True
            else:
                return False
        
        return isValidNode(root,float('-inf'),float('+inf'))
        