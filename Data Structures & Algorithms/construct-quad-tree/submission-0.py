"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isuniform(n,r,c):
            val =grid[r][c]
            for i in range(r, r+n):
                for j in range(c, c+n):
                    if grid[i][j] != val:
                        return False
            return True

        def build(n,r,c):
            if isuniform(n,r,c):
                return Node(grid[r][c], True, None, None, None, None)

            half = n//2
            topLeft = build(half, r,c)
            topRight = build(half, r, c+half)
            bottomLeft = build(half, r+half,c)
            bottomRight = build(half, r+half, c+half)

            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        return build(len(grid), 0, 0)


        