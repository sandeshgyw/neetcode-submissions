# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map={}
        for i,num in enumerate(inorder):
            inorder_map[num]=i
        
        preorderIndex=0

        def build(left,right):
            nonlocal preorderIndex
            #this function builds the tree from the inorder list
            #left and right indicate which values are considered to build the particular node
            if left>right:
                return
            root=TreeNode(preorder[preorderIndex])# we have the root
            preorderIndex+=1
            inorderIndex=inorder_map[root.val]

            root.left=build(left,inorderIndex-1)
            root.right=build(inorderIndex+1,right)

            return root
        
        return build(0,len(inorder)-1)





        