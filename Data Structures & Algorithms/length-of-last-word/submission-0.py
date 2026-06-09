class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = s.rstrip()
        n = len(k)
        j = 0

        for i in range(n-1, -1, -1):
            if k[i] == " ":
                break
            j+=1
        return j


        
        