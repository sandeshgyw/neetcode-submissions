# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxi=0
    mini=0
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # this will return true if valid and false if invalid
        # if we find only even one condition false we can call return False
        # doing so will end the traversal early and we cant afford false positives

        def isValid(node,low,high):
            #checks if the node is valid
            if not node:
                return True

            if  not low<node.val<high:
                return False

            isLeftValid=isValid(node.left,low,node.val)
            isRightValid=isValid(node.right,node.val,high)

            return isLeftValid and isRightValid

        return isValid(root,float('-inf'),float('+inf'))