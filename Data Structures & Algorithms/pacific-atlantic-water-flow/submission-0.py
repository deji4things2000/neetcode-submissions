class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ht = heights
        m, n = len(ht), len(ht[0])

        pac = set()
        atl = set()

        def dfs(r,c,vst,ph):
            if r<0 or r>=m or c<0 or c>=n or (r,c) in vst or ht[r][c] < ph:
                return

            vst.add((r,c))

            dfs(r+1,c,vst,ht[r][c])
            dfs(r-1,c,vst,ht[r][c])
            dfs(r,c+1,vst,ht[r][c])
            dfs(r,c-1,vst,ht[r][c])

        for c in range(n):
            dfs(0,c,pac,ht[0][c])
            dfs(m-1,c,atl,ht[m-1][c])

        for r in range(m):
            dfs(r,0,pac,ht[r][0])
            dfs(r,n-1,atl,ht[r][n-1])
        

        res = []
        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res








        