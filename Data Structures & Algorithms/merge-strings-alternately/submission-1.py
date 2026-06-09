class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        x=word1
        y=word2

        a = len(word1)
        b = len(word2)
        res = ""

        while l<a or r<b:
            if l<a:
                res+=x[l]
                l+=1
            if r<b:
                res+=y[r]
                r+=1
        return res


