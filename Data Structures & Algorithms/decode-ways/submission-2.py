class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if not s or s[0] == '0':
            return 0

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            #single digit
            digit1 = int(s[i-1:i])
            if 1<= digit1 <= 9:
                dp[i] += dp[i-1]
            
            #double digit
            digit2 = int(s[i-2:i])
            if 10<= digit2 <=26:
                dp[i] += dp[i-2]
        return dp[n]