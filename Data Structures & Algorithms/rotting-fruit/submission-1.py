class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return

        m, n = len(grid), len(grid[0])

        q = deque()
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))
        

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            r,c = q.popleft()
            dist = grid[r][c]

            for dr, dc in directions:
                nr,nc = r+dr, c+dc

                if nr<0 or nr>=m or nc<0 or nc>=n or grid[nr][nc] !=1:
                    continue

                grid[nr][nc] = dist + 1
                q.append((nr,nc))

        maxi = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1

                if grid[r][c] > 0:
                    maxi = max(maxi, grid[r][c])

        return max(0, maxi-2)




        