class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ma = zip(s, t)
        cntS = {}
        cntT = {}

        for c1, c2 in ma:
            if cntS.get(c1, c2) != c2 or cntT.get(c2, c1) != c1:
                return False
 
            cntS[c1] = c2
            cntT[c2] = c1

        return True