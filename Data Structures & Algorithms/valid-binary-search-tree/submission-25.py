# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we return true for valid bst and fasle for not valid
        # what makes it invalid?
        # left subtree has key grater than parent
        # right subtree has key less than parent
        # both left and right are not valid BST
        # in this case we can return False

        # we need to do this for each node the same reptitive task so we need a recursion function so that we can go thorugh the nodes till we reach None
        if not root:
            return True

        def isValid(node,left,right):
            # contract: this function returns false if this node is not validBST
            # to be valid it should be in range of > than the parent node for right and < paretn for left

            if not node:
                return True
            
            if node.val<=left or node.val>=right:
                return False
            
            return isValid(node.left,left,node.val) and isValid(node.right,node.val,right)
        
        return isValid(root,float('-inf'),float('+inf'))
            
            
        

        