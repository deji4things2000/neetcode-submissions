class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total:
            return 0

        if (total+target)%2==1:
            return 0


        n = (total+target)//2

        dp = [0] * (n+1)

        dp[0] = 1


        for num in nums:
            for s in range(n, num-1, -1):
                dp[s] +=dp[s-num]

        return dp[n]

        
        