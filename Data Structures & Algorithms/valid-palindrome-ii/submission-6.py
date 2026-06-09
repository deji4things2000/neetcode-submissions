class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n-1

        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return self.check(s, l+1, r) or self.check(s, l, r-1)
        return True

    def check(self,s,  l, r):
        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True

