class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        components = n
        for u,v in edges:
            if dsu.union(u,v):
                components-=1

        return components
        



class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n


    def find(self, x):
        if self.parents[x]!=x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x,y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx

        self.parents[ry] = rx
        self.size[rx] += self.size[ry]
        return True


