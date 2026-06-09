class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cntS = {}
        cntT = {}

        for c1, c2 in zip(s, t):
            if c1 in cntS and cntS[c1] != c2:
                return False
            if c2 in cntT and cntT[c2] != c1:
                return False
                
            cntS[c1] = c2
            cntT[c2] = c1

        return True


