class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid = heights
        m, n = len(grid), len(grid[0])
        pac = set()
        atl = set()

        def dfs(i,j,ocean):
            ocean.add((i,j))
            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            for di, dj in directions:
                ni, nj = di+i, dj+j

                if not (ni < 0 or ni>=m or nj <0 or nj>=n) and (ni,nj) not in ocean and grid[ni][nj] >= grid[i][j]:
                    dfs(ni, nj, ocean)

        #Start from pac edges (top row and top col)
        for i in range(m):
            dfs(i, 0, pac)
        
        for j in range(n):
            dfs(0, j, pac)

        #start from atl edges (bottom row and right col)

        for i in range(m):
            dfs(i, n-1, atl)

        for j in range(n):
            dfs(m-1, j, atl)

        res = []

        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res

        