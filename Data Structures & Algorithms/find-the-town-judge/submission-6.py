class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ind = [0] * (n+1) 
        out = [0] * (n+1)
        for ai, bi in trust:
            ind[bi] += 1
            out[ai] += 1

        
        for person in range(1, n+1):
            if ind[person] == (n-1) and out[person] == 0:
                return person

        return -1 

        