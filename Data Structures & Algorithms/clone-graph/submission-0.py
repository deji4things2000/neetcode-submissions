"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        hm = {}

        def dfs(cur):
            if cur in hm:
                return hm[cur]

            copy = Node(cur.val)
            hm[cur] = copy


            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))
                
            return copy

        return dfs(node)




        