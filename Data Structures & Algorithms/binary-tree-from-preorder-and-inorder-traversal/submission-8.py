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
        
        indices_map={}

        for i,val in enumerate(inorder):
            indices_map[val]=i
        
        preIndex=0
    

        def build(leftIndex,rightIndex):
            nonlocal preIndex
            #these are for the inorder
            if leftIndex>rightIndex:
                return
            
            if preIndex>len(preorder)-1:
                return

            root=TreeNode(preorder[preIndex])
            inorderIndex=indices_map[root.val]
            preIndex+=1

            root.left=build(leftIndex,inorderIndex-1)
            root.right=build(inorderIndex+1,rightIndex)

            return root

        return build(0,len(inorder)-1)



        