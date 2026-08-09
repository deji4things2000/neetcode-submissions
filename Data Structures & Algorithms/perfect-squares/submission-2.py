class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        nums = []
        i = 1
        while i*i<=n:
            nums.append(i*i)
            i+=1
        
        for i in range(1, n+1):
            for num in nums:
                if num > i:
                    break
                else:
                    dp[i] = min(dp[i], dp[i-num] + 1)
        return dp[n]


        