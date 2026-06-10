class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r = 0,0
        s = ''

        if len(word1)<len(word2):
            n = len(word1)
        else:
            n = len(word2)

        while l<n:
            s+=word1[l]
            s+=word2[r]
            l+=1
            r+=1
        
        if len(word1)>len(word2):
            s+=word1[l:]
        else:
            s+=word2[r:]
        
        return s


        