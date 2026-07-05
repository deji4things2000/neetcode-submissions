# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def lca(node, p, q):
            if not node:
                return None

            left = lca(node.left, p, q)
            right = lca(node.right, p, q)

            if p.val <=node.val<=q.val or q.val<=node.val<=p.val:
                return node
            
            return left if left else right
        
        

        return lca(root, p, q)



        