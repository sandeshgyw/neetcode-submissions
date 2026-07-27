# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None
        indexMap={}
        
        for i in range(len(inorder)):
            indexMap[inorder[i]]=i
        
        preorderIndex=0
        
        def buildTreee(leftPointer,rightPointer):
            #left and right are for inorder
            #preorder we just incremenet
            nonlocal preorderIndex

            if leftPointer>rightPointer:
                return None
            
            root=TreeNode(preorder[preorderIndex])
            inorderIndex=indexMap[root.val]

            preorderIndex+=1

            root.left=buildTreee(leftPointer,inorderIndex-1)
            root.right=buildTreee(inorderIndex+1,rightPointer)

            return root

        
        return buildTreee(0,len(inorder)-1)


        