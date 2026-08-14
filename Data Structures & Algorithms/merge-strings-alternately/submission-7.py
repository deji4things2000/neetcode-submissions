class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0
        res = ''

        while i<m and j<n:
            res += word1[i]
            res += word2[j]
            i+=1
            j+=1
        
        if m < n:
            res+=word2[j:]
        elif m > n:
            res+=word1[i:]
        
        return res
            