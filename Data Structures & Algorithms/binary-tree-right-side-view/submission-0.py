# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def rsv(node, level):
            if not node:
                return

            if len(res) == level:
                res.append(node.val)
            
            rsv(node.right, level+1)
            rsv(node.left, level+1)

        rsv(root, 0)

        return res
        