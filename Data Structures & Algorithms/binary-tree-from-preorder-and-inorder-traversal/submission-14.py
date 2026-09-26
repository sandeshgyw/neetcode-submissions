# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index_map={}
        pre_index=0

        for i,num in enumerate(inorder):
            index_map[num]=i
        
        def build(start,end):
            nonlocal pre_index

            if pre_index>len(inorder)-1:
                return
            
            if start>end:
                return
            
            root_val=preorder[pre_index]
            pre_index+=1

            root=TreeNode(root_val)
            index=index_map[root.val]

            root.left=build(start,index-1)
            root.right=build(index+1,end)
            return root
        
        return build(0,len(inorder)-1)


        