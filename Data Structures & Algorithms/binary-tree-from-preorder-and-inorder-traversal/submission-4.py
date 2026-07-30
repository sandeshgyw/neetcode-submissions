# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorderIndex=0

        indexMap={}

        for i,val in enumerate(inorder):
            indexMap[val]=i


        def build(left,right):
            #left and right are for the inorder boundary

            if left>right:
                return None
            
            nonlocal preorderIndex



            root=TreeNode(preorder[preorderIndex])

            preorderIndex+=1
            inorderIndex=indexMap[root.val]

            root.left=build(left,inorderIndex-1)
            root.right=build(inorderIndex+1,right)

            return root
        
        return build(0,len(inorder)-1)


        