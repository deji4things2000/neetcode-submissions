class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = UnionFind(n)
        e_acc = {}

        #Link and merge accounts that share same emails
        for i in range(n):
            for email in accounts[i][1:]:
                if email in e_acc:
                    dsu.union(e_acc[email], i)
                else:
                    e_acc[email] = i

        #Group emails by root account
        merged = {}
        for i in range(n):
            root = dsu.find(i)
            if root not in merged:
                merged[root] = []
            
            for email in accounts[i][1:]:
                if email not in merged[root]:
                    merged[root].append(email)

        #format result
        res = []
        for root, emails in merged.items():
            emails.sort()
            name = accounts[root][0]
            res.append([name] + emails)
        return res
    
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

    

        