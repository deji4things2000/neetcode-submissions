class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        n
        ind = [0] * (n+1)
        out = [0] * (n+1)

        for tt, t in trust:
            ind[t] += 1
            out[tt] +=1

        for i in range(1, n+1):
            if ind[i] == (n-1) and out[i] ==0:
                return i

        return -1
        
        