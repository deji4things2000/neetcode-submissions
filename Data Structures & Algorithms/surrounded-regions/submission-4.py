class Solution:
    def solve(self, board: List[List[str]]) -> None:
        grid = board
        m, n = len(grid), len(grid[0])

        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 'X':
                return

            if grid[i][j] == 'T':
                return

            grid[i][j] = 'T'

            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)


        for i in range(m):
            if grid[i][0] == 'O':
                dfs(i,0)
            if grid[i][n-1] == 'O':
                dfs(i, n-1)

        for j in range(n):
            if grid[0][j] == 'O':
                dfs(0,j)
            if grid[m-1][j] == 'O':
                dfs(m-1,j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
                if grid[i][j] == 'T':
                    grid[i][j] = 'O'

        board = grid

