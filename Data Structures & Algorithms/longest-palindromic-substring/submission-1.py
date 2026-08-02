class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n<=1:
            return s
        dp = [[False] * n for _ in range(n)]
        start = 0
        maxi = 1

        #for single characters
        for i in range(n):
            dp[i][i] = True
            
        #for adjacent characters
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                maxi = 2
        
        #for characters >=3

        for lenght in range(3, n+1):
            for i in range(n-lenght+1):
                j = i+lenght-1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start = i
                    maxi = lenght
        
        return s[start: start + maxi]


        