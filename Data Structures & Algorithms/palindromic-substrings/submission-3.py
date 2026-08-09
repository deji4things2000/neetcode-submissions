class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n==1:
            return 1

        dp = [[False] * n for _ in range(n)]
        count = 0

        #for single characters:
        for i in range(n):
            dp[i][i] = True
            count+=1
        #for adjacent characters with lenght == 2:
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count+=1
        
        #For 3 characters and above
        for lenght in range(3, n+1):
            for i in range(n-lenght+1):
                j = i+lenght-1
                if s[i] == s[j] and dp[i+1][j-1] == True:
                    dp[i][j] = True
                    count+=1

        return count        