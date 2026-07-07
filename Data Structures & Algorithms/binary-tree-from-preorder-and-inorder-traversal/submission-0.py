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
        
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def cbt(ps, pe, ins, ine):
            if ps > pe or ins > ine:
                return None

            root_val = preorder[ps]
            root = TreeNode(root_val)

            root_index = inorder_map[root_val]
            left_size = root_index - ins

            root.left = cbt(ps+1, ps+left_size, ins, root_index-1)

            root.right = cbt(ps+left_size+1, pe, root_index+1, ine)

            return root

        return cbt(0, len(preorder)-1, 0, len(inorder)-1)

            
