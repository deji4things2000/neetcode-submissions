class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = set()
        for p, t in trust:
            a.add(t)

        a = list(a)
        
        if len(a) == 1:
            return a[0]
        else:
            return -1