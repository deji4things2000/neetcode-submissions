class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rc = [0] * m
        cc = [0] * n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    rc[r] +=1
                    cc[c] +=1

        total = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (rc[r]>1 or cc[c]>1):
                    total+=1

        return total
            




        