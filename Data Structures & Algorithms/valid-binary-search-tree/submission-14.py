# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # this will return true if valid and false if invalid
        # if we find only even one condition false we can call return False
        # doing so will end the traversal early and we cant afford false positives

        if not root:
            return True
        
        #check1: left node is always less
        if root.left and root.left.val>root.val:
            return False
        #check2 right is always false
        if root.right and root.right.val<root.val:
            return False

        isLeftValid=self.isValidBST(root.left)
        isRightValid=self.isValidBST(root.right)

        return isLeftValid and isRightValid