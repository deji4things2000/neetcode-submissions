class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        res = []

        while l<len(word1) and r<len(word2):
                res.append(word1[l])
                res.append(word2[r])
                r+=1
                l+=1
        res.append(word1[l:])
        res.append(word2[r:])
        return "".join(res)

