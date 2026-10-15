class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        i,j = 0, n-1
        
        while i<=j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return self.check(s, i, j-1) or self.check(s, i+1, j)
        return True
    
    def check(self, s, i, j):
        while i<=j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True