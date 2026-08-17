class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = UnionFind(n)

        if len(edges) != n-1:
            return False

        for a, b in edges:
            if dsu.union(a,b) == False:
                return False
        return True
        



class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

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

        self.parent[ry] = rx
        self.size[rx] += self.size[ry]

        return True

