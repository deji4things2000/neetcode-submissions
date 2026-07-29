class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip(' ')
        res = 0
        n = len(s)

        for i in range(n-1, -1, -1):
            if s[i] != ' ':
                res+=1
            else:
                break
        return res
