class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = total//2

        if total%2==1:
            return False

        dp = [False] * (n+1)

        dp[0] = True

        for num in nums:
            for s in range(n, num-1, -1):
                dp[s] = dp[s] or dp[s-num]
        return dp[n]
        
        