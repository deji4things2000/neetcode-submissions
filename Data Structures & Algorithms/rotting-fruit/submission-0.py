class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        fresh = 0
        q = deque()
        m,n = len(grid), len(grid[0])

        #Enqueue the start state
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q and fresh>0:

            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (0<=nr<m and 0<=nc<n and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh-=1
                        q.append((nr,nc))
            
            mins+=1
        
        return mins if fresh==0 else -1
        