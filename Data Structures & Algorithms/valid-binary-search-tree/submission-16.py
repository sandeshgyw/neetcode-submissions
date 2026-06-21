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

        def isValid(node):
            if not node:
                return True

            if node.left and (node.left.val>=node.val or node.left.val >= root.val ):
                return False

            if node.right and (node.right.val<=node.val or node.right.val <=root.val):
                return False

            isLeftValid=isValid(node.left)
            isRightValid=isValid(node.right)

            return isLeftValid and isRightValid

        return isValid(root)