from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0  # 0 coins to make total 0

        for t in range(1, amount + 1):
            for coin in coins:
                if coin <= t:
                    dp[t] = min(dp[t], 1 + dp[t - coin])
                else:
                    dp[t] = dp[t]

        if dp[amount] != inf:
            return dp[amount] 
        else:
            return -1