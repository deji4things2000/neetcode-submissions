class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        dsu = DSU(n)
        for u,v in edges:
            if not dsu.union(u,v):
                return False

        return True


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] !=x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False
        
        self.parent[ry] = rx

        return True

        