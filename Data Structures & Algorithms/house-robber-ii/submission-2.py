class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]

        if n==2:
            return max(nums[0], nums[1])

        def lin(start, end):
            dp = [0] * (end-start+1)
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start+1])
            for i in range(2, (end-start+1)):
                dp[i] = max(dp[i-1], (nums[start+i] + dp[i-2]))
            return dp[-1]
        
        scen = lin(0, n-2)
        scen1 = lin(1, n-1)


        return max(scen, scen1)
        