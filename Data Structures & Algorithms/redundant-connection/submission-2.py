class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = UnionFind(n+1)

        for parent, child in edges:
            if dsu.union(parent, child) == False:
                return [parent, child]

class UnionFind:
    def __init__(self, n):
        self.size = [1] * n
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False
            
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        
        self.parent[rx] = ry
        self.size[rx] += self.size[ry]
        return True