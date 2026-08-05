class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
        
        if (target+total)%2 != 0:
            return 0
        
        sub_sum = (target+total)//2

        dp = [0] * (sub_sum+1)
        dp[0] = 1
        for num in nums:
            for s in range(sub_sum, num-1, -1):
                dp[s] += dp[s-num]
        return dp[sub_sum]

        
        