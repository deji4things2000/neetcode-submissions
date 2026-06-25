class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hmS = {}
        hmT = {}

        for i in range(len(t)):
            hmS[s[i]] = hmS.get(s[i], 0) + 1
            hmT[t[i]] = hmT.get(t[i], 0) + 1
        return hmS==hmT

