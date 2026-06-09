class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        p = picture
        r, c = len(p), len(p[0])
        row = [0] * r
        col = [0] * c

        for i in range(r):
            for j in range(c):
                if picture[i][j] == 'B':
                    row[i] +=1
                    col[j] +=1
        
        ans = 0
        for i in range(r):
            for j in range(c):
                if picture[i][j] == 'B' and row[i] == 1 and col[j] == 1:
                    ans+=1
        return ans




