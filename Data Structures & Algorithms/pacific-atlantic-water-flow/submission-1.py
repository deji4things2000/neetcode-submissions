class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ht = heights
        m, n = len(heights), len(heights[0])
        atl = set()
        pac = set()

        def dfs(i, j, vs, ph):
            if i<0 or i>=m or j<0 or j>=n or ht[i][j] < ph or (i,j) in vs:
                return

            vs.add((i,j))

            dfs(i-1, j, vs, ht[i][j])
            dfs(i+1, j, vs, ht[i][j])
            dfs(i, j-1, vs, ht[i][j])
            dfs(i, j+1, vs, ht[i][j])

            return 

        for j in range(n):
            dfs(0, j, pac, ht[0][j])
            dfs(m-1, j, atl, ht[m-1][j])

        for i in range(m):
            dfs(i, 0, pac, ht[i][0])
            dfs(i, n-1, atl, ht[i][n-1])

        res = []

        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])

        return res

        