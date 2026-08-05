class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n  = len(matrix), len(matrix[0])
        directions = [(-1,0), (1,0), (0, -1), (0, 1)]

        dp = [[0] * n for _ in range(m)]

        def dfs(i,j):
            if dp[i][j] !=0:
                return dp[i][j]
        
            best = 1

            for di, dj in directions:
                ni, nj = i+di, j+dj

                if 0<=ni<m and 0<=nj<n and matrix[ni][nj] > matrix[i][j]:
                    best = max(best, 1+dfs(ni, nj))

            dp[i][j] = best
            return best
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j))
        
        return ans
                

        