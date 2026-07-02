class Solution:
    def validPalindrome(self, s: str) -> bool:


        n = len(s)
        i, j = 0, n-1

        while i<=j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return self.check(i+1, j, s) or self.check(i, j-1, s)
        return True
        
    def check(self, i, j, s):
        while i<=j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
            

    
        
        