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

        
        index_map={}
    
        for i in range(len(inorder)):
            value = inorder[i]
            index_map[value] = i
        
        preorder_index=0
        def build(left,right):
            nonlocal preorder_index

            if left>right:
                return None

            root=TreeNode(preorder[preorder_index])
            inorder_index=index_map[root.val]
            preorder_index+=1

            root.left=build(left,inorder_index-1)
            root.right=build(inorder_index+1,right)

            return root
        
        return build(0,len(inorder)-1)
        