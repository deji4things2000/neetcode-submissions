# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None  # keeps track of the previous node in in-order traversal

        def inorder(node):
            nonlocal prev
            if not node:
                return True
            
            # Traverse left subtree
            if not inorder(node.left):
                return False
            
            # Check current node: in-order must be strictly increasing
            if prev is not None and node.val <= prev:
                return False
            
            prev = node.val  # update previous
            
            # Traverse right subtree
            return inorder(node.right)
        
        return inorder(root)
