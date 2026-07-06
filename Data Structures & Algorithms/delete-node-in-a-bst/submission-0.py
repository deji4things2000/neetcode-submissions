# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def den(node, key):
            if not node:
                return None

            if key < node.val:
                node.left = den(node.left, key)
                return node
            elif key > node.val:
                node.right = den(node.right, key)
                return node

            if not node.left and not node.right:
                return None

            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = node.right
            while temp.left:
                temp = temp.left
            node.val = temp.val
            node.right = den(node.right, temp.val)
            return node

        return den(root, key)

            

        