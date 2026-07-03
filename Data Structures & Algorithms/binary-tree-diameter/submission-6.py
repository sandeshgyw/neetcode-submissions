# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0


        def getHeight(node):
            nonlocal diameter
            #this function will return the height of the current node
            #which is max of left or right hegiht
        
            if not node:
                return 0
            
            left=getHeight(node.left)#magic function that gives left ht
            right=getHeight(node.right)#magic that gives right height

            diameter=max(diameter,left+right)

            return 1+max(left,right)
        getHeight(root)
        return diameter
        