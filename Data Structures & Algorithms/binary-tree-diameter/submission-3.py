# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        


        def getHeight(node):
            if not node:
                return 0

            leftHeight=getHeight(node.left)
            rightHeight=getHeight(node.right)

            return 1+max(leftHeight,rightHeight)

        self.diameter=max(self.diameter, getHeight(root.left)+getHeight(root.right))

        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)

        return self.diameter
        
        
        