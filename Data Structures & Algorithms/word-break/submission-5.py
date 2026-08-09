class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = set(wordDict)
        n = len(s)

        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if s[j:i] in seen and dp[j] == True:
                    dp[i] = True
                    break
        return dp[n]