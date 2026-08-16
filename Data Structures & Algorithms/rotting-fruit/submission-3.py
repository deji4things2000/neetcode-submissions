class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    q.append((i,j))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        mins = 0

        while q and fresh>0:
            
            for _ in range(len(q)):
                i, j = q.popleft()

                for di, dj in directions:
                    ni, nj = i+di, j+dj

                    if not (ni<0 or ni>=m or nj<0 or nj>=n) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh-=1
                        q.append((ni, nj))
            mins+=1
        return mins if fresh==0 else -1

            
        

        
        