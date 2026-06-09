class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmS = {}
        hmT = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hmS[s[i]] = hmS.get(s[i], 0) + 1
            hmT[t[i]] = hmT.get(t[i], 0) + 1

        return hmS == hmT
        