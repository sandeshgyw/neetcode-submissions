# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #this function should retrunt the diameter
        # to find diameter we need to find height of the left and right
        # and sum it thats the diameeter
        # but the q is not to find diameter its to find the max so at each node check if
        #thats the max one
        def height(node):
            if not node:
                return 0

            
            leftHeight=height(node.left)
            rightHeight=height(node.right)

            self.diameter=max(self.diameter,leftHeight+rightHeight)



            return 1+max(leftHeight,rightHeight)

        height(root)

        return self.diameter
            
