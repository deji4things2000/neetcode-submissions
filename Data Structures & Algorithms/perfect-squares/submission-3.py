class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n+1] * (n+1)
        dp[0] = 0
        nums = []

        for i in range(1, (n+1)):
            nums.append(i*i)
        
        for i in range(1, n+1):
            for num in nums:
                if i>=num:
                    dp[i] = min(dp[i], dp[i-num] + 1)
        return dp[n]

